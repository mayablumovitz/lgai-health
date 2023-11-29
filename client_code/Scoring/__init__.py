from ._anvil_designer import ScoringTemplate
from anvil import *
import anvil.server

class Scoring(ScoringTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  def Uploader_gold_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    print("uploaded gold standard")

  def Uploader_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    print("uploaded report")

  def Submit_click(self, **event_args):
    """This method is called when the button is clicked"""
    if(self.Uploader_gold.file is not None and self.Uploader.file is not None):
      gold_content = self.Uploader_gold.file.get_bytes()
      content = self.Uploader.file.get_bytes()
      score = anvil.server.call('score', str(gold_content), str(content))
      self.gold_score.text = "Gold Standard Score: " + score['generated_text'].split("Score: ")[-1][0]
    else:
      alert("Upload your files to run.")
      raise ValueError("No files were uploaded.")
      