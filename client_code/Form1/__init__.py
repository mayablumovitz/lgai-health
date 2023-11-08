from ._anvil_designer import Form1Template
from anvil import *
import anvil.server

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.reorde = "de"
    self.txt = ""

  def Deidentify_clicked(self, **event_args):
    """This method is called when this radio button is selected"""
    self.reorde = "de"

  def Reidentify_clicked(self, **event_args):
    """This method is called when this radio button is selected"""
    self.reorde = "re"

  def Submit_click(self, **event_args):
    """This method is called when the button is clicked"""
    # re-or-de = radioGroup1.
    print(self.reorde)
    # colab = anvil.server.call('LGAI_project')

  def file_loader_1_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    try:
        if file.name.endswith('.txt'):
            file_content = file.read().decode('utf-8')
            self.txt = file_content
        else:
            raise ValueError("Invalid file format. Please load a .txt file.")
    except Exception as e:
        return f"Error: {str(e)}"
