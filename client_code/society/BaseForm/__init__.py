from ._anvil_designer import BaseFormTemplate
from anvil import *
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class BaseForm(BaseFormTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def home_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('society.DashboardForm')

  def about_us_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('society.AboutUsForm')

  def contact_us_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('society.ContactUsForm')

  def reset_links(self, **event_args):
    self.home_link.role = ''
    self.about_us_link.role = ''
    self.contact_us_link.role = ''