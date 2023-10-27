from ._anvil_designer import Form1Template

from anvil import *



class Form1(Form1Template):

  def __init__(self, **properties):

    # Set Form properties and Data Bindings.

    self.init_components(**properties)



    # Any code you write here will run before the form opens.

  def label_1_show(self, **event_args):
    """This method is called when the Label is shown on the screen"""
    pass

