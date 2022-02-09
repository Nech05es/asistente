import os
class Clear:
  """this class allows you to clean the console """
  def __init__(self,system):
    if system == None:
      os.system('cls')
    elif system == 'unix':
      os.system('clear')
#clear = Clear('unix')