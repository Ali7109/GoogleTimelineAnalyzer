from ._anvil_designer import Form1Template

from anvil import *
import anvil.server

class Form1(Form1Template):

  def __init__(self, **properties):
    self.init_components(**properties)


  def process_button_click(self, **event_args):
    res = anvil.server.call('show_travel_data')
    if res:
      self.data_view.text = res
    else:
      self.data_view = "Error in fetching"
    
  def file_loader_1_change(self, file, **event_args):
    anvil.server.call('process_file', file)

  def to_input_copy_pressed_enter(self, **event_args):
    pass

    

    

