from ._anvil_designer import Form1Template
from anvil import *
import anvil.server

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    openai_api_key = self.text_box_1.text
    channel_url = self.text_box_2.text
    text = anvil.server.call('get_text_from_url',channel_url)
    self.rich_text_2.content = anvil.server.call('get_summary',openai_api_key,text)
    Notification(f"Generated summary for url : {channel_url}!!").show()
    pass

