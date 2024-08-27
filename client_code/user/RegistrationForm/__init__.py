from ._anvil_designer import RegistrationFormTemplate
from anvil import *
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server


class RegistrationForm(RegistrationFormTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def login_form_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('user.LoginForm')

  def registration_submit_click(self, **event_args):
    """This method is called when the button is clicked"""
    first_name = self.first_name_input.text
    last_name = self.last_name_input.text
    email = self.email_input.text
    password = self.password_input.text
    result = anvil.server.call('register_user',first_name, last_name, email, password)
    if result['success']:
        alert(result['message'])
        open_form('user.LoginForm')
    else:
        alert(result['message'])
