import random as random
input = open('data/CSW19-5.txt')

class Game:
  __all_words = [line.strip() for line in input]
  def __init__(self, word = None, max_guesses = 6):
    self.__max_guesses = max_guesses
    self.__guesses = 0
    if not word:
      self.__word = self.__choose_random_start()
      print('chose random word ' + self.word)
    else:
      self.__word = word

  def __choose_random_start(self):
    return self.__all_words[random.randint(0, len(self.__all_words)-1)]

  def __evaluate_letter(self, letter, position):
    if (self.__word[position] == letter):
      return 'green'
    if (letter in self.__word):
      return 'yellow'
    return 'gray'

  def evaluate_guess(self, guess):
    if guess not in self.__all_words:
      return { 'outcome': 'retry', 'reason': 'Must enter exactly 5 letters'}
    if len(guess != 5):
      return { 'outcome': 'retry', 'reason': 'Must enter exactly 5 letters'}
    self.__guesses += 1
    feedback = {letter: self.__evaluate_letter(letter, pos) for pos, letter in enumerate(guess)}
    if(feedback.values
    return {
      'outcome': 'win',
      'feedback': feedback
    }

Game()
Game.evaluate_guess('g')