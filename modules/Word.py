class Words:
  """this allows you to go through a sentence and separate each word and enter them in a list that i then go through to search for phrases for the artificial intelligence"""
  def __init__(self,string = None):
    self.string = string
    self.word = ''
    self.words = []
    if self.string != None:
      if len(self.string) >= 1:
        for char in self.string:
          if char != ' ' and char != ',' and char != '.':
            self.word += char
          else:
            self.words.append(self.word) 
            self.word = ''
      else:
        print('no se ingreso nada')
        self.words.remove()
    print(self.words)

#w = Words('yo quiero ser fullstack y software enginer.')