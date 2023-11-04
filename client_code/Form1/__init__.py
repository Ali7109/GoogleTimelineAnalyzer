from ._anvil_designer import Form1Template

from anvil import *
import anvil.server

class Form1(Form1Template):

  def __init__(self, **properties):
    self.init_components(**properties)


  def number_of_travels_click(self, **event_args):
    from_text = self.from_input.text
    to_text = self.to_input.text
    
    self.from_input.text = ""
    self.to_input.text = ""
    
    if not from_text or not to_text:
      return alert("Please enter valid from and to locations")
    
    res = anvil.server.call('calculate_travels', from_text, to_text)
    
    if res or res == 0:
      self.output_title.visible = True
      self.output_label_showcase.visible = True
      self.output_label_showcase.text = "#Travels from " + from_text + " to " + to_text + " = " + str(res)
    else:
      alert("Data not ready, please reupload file")

  def entries_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    to_location = self.entries_input.text
    self.entries_input.text = ""

    if not to_location:
      return alert("Please entervalid entry location")

    res = anvil.server.call('calculate_entries', to_location)
    if res or res == 0:
      self.output_title.visible = True
      self.output_label_showcase.visible = True
      self.output_label_showcase.text = "Number of Entries to " + to_location + " = " + str(res)
    else:
      alert("Data not ready, please reupload file")
   

  
  def file_loader_1_change(self, file, **event_args):

    if not file:
      self.output_card.visible = False
    
    process_result = anvil.server.call('process_file', file)
    if process_result:
      self.output_card.visible = True
    else:
      alert("Error occured please try again")





    

    

