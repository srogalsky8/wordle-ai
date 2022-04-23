from game import Game
from common_words import common_words
import string

game = Game()
guesses = []
# potential_letters = string.ascii_lowercase # start with all letters
print('random word: ' + game.get_word())

# Turn 1
turn = game.evaluate_guess('trace')
if turn['outcome'] == 'success':
    guesses.append(turn['feedback'])

# Turn 2
# figure out the next guess
potential_words = common_words
for guess in guesses:
    for (position, letter_feedback) in enumerate(guess):
        (letter, color) = letter_feedback
        if(color == 'green'):
            potential_words = [word for word in potential_word if word[position] == letter]
        elif(color == 'yellow'):
            potential_words = [word for word in potential_word if letter in word]
        elif(color == 'gray'):
            # TODO: if letter is repeated in the guess and it's green or yellow
            potential_words = [word for word in potential_word if letter not in word]

# { t, e, a, r, s}
# { b: 1, e: 2, r: 1, s: 1}

# yeare
# eerie




# target: tears
# guess: beers