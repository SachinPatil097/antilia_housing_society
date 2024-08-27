from ._anvil_designer import RegistrationFormTemplate
from .BaseForm import BaseForm
from anvil import *


class RegistrationForm(BaseForm):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    super().__init__(**properties)

    # Any code you write here will run before the form opens.
