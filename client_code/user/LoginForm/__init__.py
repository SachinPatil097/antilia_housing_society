from ._anvil_designer import LoginFormTemplate
from anvil import *


class LoginForm(LoginFormTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def submit_registration_click(self, **event_args):
    """This method is called when the button is clicked"""
    email = self.email_input.text
    password = self.password_input.text
    result = anvil.server.call('register_user', email, password)
    if result['success']:
        alert(result['message'])
        self.open_form('LoginForm')
    else:
        alert(result['message'])
