from ._anvil_designer import LoginFormTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class LoginForm(LoginFormTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def registration_form_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('user.RegistrationForm')

  def registration_form_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('user.RegistrationForm')
