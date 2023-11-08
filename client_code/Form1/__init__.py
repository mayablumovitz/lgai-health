from ._anvil_designer import Form1Template
from anvil import *
import anvil.server

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    alert('This is the app I just built')
    # Any code you write here will run before the form opens.

  def Deidentify_clicked(self, **event_args):
    """This method is called when this radio button is selected"""
    pass
