from ._anvil_designer import ContactUsFormTemplate
from anvil import *
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..server_modules import verify_token

@verify_token
class ContactUsForm(ContactUsFormTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def form_show(self, **event_args):
    """This method is called when the form is shown on the page"""
    self.layout.reset_links()
    self.layout.contact_us_link.role = 'selected'
    
