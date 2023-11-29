from ._anvil_designer import ReDeIdentifyTemplate
from anvil import *
import anvil.server

class ReDeIdentify(ReDeIdentifyTemplate):
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
      result_text = result['generated_text'].split('FINAL REPORT', 2)[2].strip()
    else:
      print("running deidentify")
      result = anvil.server.call('deidentify', str(content))
      result_text = result['generated_text'].split('replaced with underscores:')[-1]
      print(result_text)
    result_text = result_text.replace('\\n', '\n')
    self.Output.text = 'FINAL REPORT\n' + result_text

  def Uploader_change(self, file, **event_args):
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
    