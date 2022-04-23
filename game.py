import random as random
input = open('data/CSW19-5.txt')

class Game:
  __all_words = [line.strip() for line in input]
  def __init__(self, word = None, max_guesses = 6):
    # TODO: supplied word must be in dictionary
    self.__max_guesses = max_guesses
    self.__guesses = 0
    self.__status = 'in progress'
    if not word:
      self.__word = self.__choose_random_start()
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

  def get_status():
    return self.__status

  def get_guesses():
    return self.__guesses

  def evaluate_guess(self, guess):
    if self.__status != 'in progress': 
      return { 'outcome': 'fail', 'reason': 'Game is over'}
    if guess.upper() not in self.__all_words:
      return { 'outcome': 'fail', 'reason': 'Word is not in dictionary'}
    self.__guesses += 1
    feedback = [(letter, self.__evaluate_letter(letter, pos)) for pos, letter in enumerate(guess)]
    # win
    if [outcome for (letter, outcome) in feedback] == ['green', 'green', 'green', 'green', 'green']:
      self.__status = 'win'
    # lost
    if self.__guesses >= 6:
      self.__status = 'loss'
    return { 'outcome': 'success', 'status': self.__status, 'feedback': feedback }

# game = Game('trace')
# turn = game.evaluate_guess('track')