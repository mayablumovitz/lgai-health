import anvil.server
import anvil.media 
# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#
@anvil.server.callable()
def get_media_txt(output_text):
  txt_media = anvil.BlobMedia('text/plain', output_text.encode(), name='output.txt')
  return txt_media