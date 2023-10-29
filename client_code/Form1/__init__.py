from ._anvil_designer import Form1Template

from anvil import *
import anvil.server

class Form1(Form1Template):

  def __init__(self, **properties):

    # Set Form properties and Data Bindings.

    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def label_1_show(self, **event_args):
    """This method is called when the Label is shown on the screen"""
    pass

  def process_button_click(self, **event_args):
    res = anvil.server.call('output', "SOS")
    if res:
      self.data_view.text = res
    else:
      self.data_view = "Error in fetching"
    
  def file_loader_1_change(self, file, **event_args):
      result = anvil.server.call('my_image_classifier', file)
    

    

