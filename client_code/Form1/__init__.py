from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import anvil.media

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  def Submit_click(self, **event_args):
    """This method is called when the button is clicked"""
    if (self.Uploader.file is None):
      alert("Upload your file to run.")
      raise ValueError("No file was uploaded.")
    content = self.Uploader.file.get_bytes()
    if (self.Reidentify.selected):
      print("running reidentify")
      result = anvil.server.call('reidentify', str(content))
    else:
      print("running deidentify")
      result = anvil.server.call('deidentify', str(content))

    result_text = result['generated_text'].split('FINAL REPORT', 2)[2].strip()
    result_text = result_text.replace('\\n', '\n')
    self.Output.text = 'FINAL REPORT\n' + result_text

    if(self.Uploader_gold.file is not None):
      gold_content = self.Uploader_gold.file.get_bytes()
      score = anvil.server.call('score', str(gold_content), str(content))
      print(score.split("Score: ")[-1])
      self.gold_score.text = "Gold Standard Score: " + score['generated_text']

  def Uploader_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    print("uploaded")

  def Uploader_gold_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    print("uploaded")
    
  def Reidentify_clicked(self, **event_args):
    """This method is called when this radio button is selected"""
    pass

  def Deidentify_clicked(self, **event_args):
    """This method is called when this radio button is selected"""
    pass

  def Download_click(self, **event_args):
    """This method is called when the button is clicked"""
    txt_media = anvil.server.call('get_media_txt', self.Output.text)
    anvil.media.download(txt_media)
