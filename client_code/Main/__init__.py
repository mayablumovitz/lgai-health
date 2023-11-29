from ._anvil_designer import MainTemplate
from anvil import *
import anvil.server

class Main(MainTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.scoring_1.visible = False

  def ReDeIdentify_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.scoring_1.visible = False
    self.re_de_identify_1.visible = True
    self.ReDeIdentify.role = "selected-navbar"
    self.Scoring.role = "default"

  def Scoring_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.scoring_1.visible = True
    self.re_de_identify_1.visible = False
    self.ReDeIdentify.role = "default"
    self.Scoring.role = "selected-navbar"
