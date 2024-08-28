import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.secrets
import anvil.users
import anvil.server
import anvil.tables as tables
from anvil.tables import app_tables
import anvil.tables.query as q
import bcrypt
import jwt
import datetime
from functools import wraps
import base64
import os
from dotenv import load_dotenv

load_dotenv()

# Constants
JWT_SECRET = os.getenv('JWT_SECRET')  # Replace with a secure key
JWT_ALGORITHM = os.getenv('JWT_ALGORITHM')
JWT_EXP_DELTA_SECONDS = int(os.getenv('JWT_EXP_DELTA_SECONDS')) # 1 hour

# Create a JWT token
def create_jwt(user):
  payload = {
    'user_id': user.get_id(),
    'email': user['email'],
    'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=JWT_EXP_DELTA_SECONDS)
  }
  token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
  return token

# Decorator to verify JWT token
def verify_token(func):
  @wraps(func)
  def wrapper(*args, **kwargs):
    token = kwargs.get('token', None)
    if not token:
      return {"success": False, "message": "Token is missing."}

    # Check if the token is still in the session (not logged out)
    session_token = anvil.server.session.get('jwt_token')
    if session_token != token:
      return {"success": False, "message": "Invalid or expired session."}

    try:
      payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
      kwargs['user_id'] = payload['user_id']
      kwargs['email'] = payload['email']
    except jwt.ExpiredSignatureError:
      return {"success": False, "message": "Token expired."}
    except jwt.InvalidTokenError:
      return {"success": False, "message": "Invalid token."}

    return func(*args, **kwargs)
  return wrapper

# Register a new user
@anvil.server.callable
def register_user(first_name, last_name, email, password):
  existing_user = app_tables.users.get(email=email)
  if existing_user:
    return {'success': False, 'message': 'User already exists'}
  hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
  hashed_password_str = base64.b64encode(hashed_password).decode('utf-8')
  try:
    app_tables.users.add_row(first_name=first_name, last_name=last_name, email=email, password_hash=hashed_password_str)
    return {"success": True, "message": "User registered successfully."}
  except Exception as e:
    return {"success": False, "message": f"Registration failed: {str(e)}"}

# Login a user
@anvil.server.callable
def login_user(email, password):
  user = app_tables.users.get(email=email)
  if user:
    hashed_password = base64.b64decode(user['password_hash'].encode('utf-8'))
    if bcrypt.checkpw(password.encode('utf-8'), hashed_password):
      token = create_jwt(user)
      anvil.users.force_login(user)  # Login the user and store the session
      # anvil.server.session['jwt_token'] = token
      return {"success": True, "token": token}
    return {"success": False, "message": "Invalid email or password."}

# Logout function
@anvil.server.callable
def logout():
  anvil.users.logout()  # Clear the user's session
  # if 'jwt_token' in anvil.server.session:
  #   del anvil.server.session['jwt_token']
  return {"success": True, "message": "Logged out successfully."}

# Get user data (protected route)
@anvil.server.callable
@verify_token
def get_user_data():
  user = anvil.users.get_user()
  if user:
    return {
      "success": True,
      "email": user['email']
    }
  return {"success": False, "message": "User not found or not logged in."}
