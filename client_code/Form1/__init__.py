from ._anvil_designer import Form1Template
from anvil import *
import anvil.server

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
    print(str(content))
    if (self.Reidentify.selected):
      print("running reidentify")
      result = anvil.server.call('reidentify', str(content))
    else:
      print("running deidentify")
      result = anvil.server.call('deidentify', str(content))
    self.Output.text = 'FINAL REPORT\n' + result['generated_text'].split('FINAL REPORT', 2)[2].strip()
    print(result)

  def Uploader_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    print("uploaded")

  def Reidentify_clicked(self, **event_args):
    """This method is called when this radio button is selected"""
    pass

  def Deidentify_clicked(self, **event_args):
    """This method is called when this radio button is selected"""
    pass
