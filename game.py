import random as random
from common_words import common_words
input = open('data/CSW19-5.txt')

class Game:
  __all_words = [line.strip().lower() for line in input]
  def __init__(self, word = None, max_guesses = 6):
    self.__max_guesses = max_guesses
    self.__guesses = 0
    self.__status = 'in progress'
    if not word:
      self.__word = self.__choose_random_start()
    else:
      if word.lower() not in self.__all_words:
        print('Word must be in dictionary')
        return
      self.__word = word

  def __choose_random_start(self):
    return common_words[random.randint(0, len(common_words)-1)].lower()

  def get_status(self):
    return self.__status

  def get_guesses(self):
    return self.__guesses

  def get_word(self):
    return self.__word

  def evaluate_guess(self, guess):
    lower_guess = guess.lower()
    if self.__status != 'in progress':
      return { 'outcome': 'fail', 'reason': 'Game is over'}
    if lower_guess not in self.__all_words:
      return { 'outcome': 'fail', 'reason': 'Word is not in dictionary'}
    self.__guesses += 1

    answer_array = list(self.__word)
    guess_array = list(lower_guess)
    # start with all gray
    feedback = [(letter, 'gray') for letter in guess_array]

    # check for greens
    for idx, letter in enumerate(guess_array):
      if self.__word[idx] == letter: # add green
        feedback[idx] = (letter, 'green')
        answer_array[idx] = None # remove from answer array
        guess_array[idx] = '-' # Don't evaluate this one again
    
    # check for yellows
    for idx, letter in enumerate(guess_array):
      if letter in answer_array:
        feedback[idx] = (letter, 'yellow')
        answer_array[idx] = None # remove from answer array
        guess_array[idx] = '-' # remove from answer array

    # win
    if [outcome for (letter, outcome) in feedback] == ['green', 'green', 'green', 'green', 'green']:
      self.__status = 'win'
    elif self.__guesses >= self.__max_guesses: # lost
      self.__status = 'loss'
    return { 'outcome': 'success', 'status': self.__status, 'feedback': feedback }