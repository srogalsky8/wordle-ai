from game import Game
from common_words import common_words
import string
import pandas as pd

def filter_words(eligible_words, feedback):
    eligible = eligible_words
    # filter words with green matches
    for (position, letter_feedback) in enumerate(feedback):
        (letter, color) = letter_feedback
        if(color == 'green'):
            eligible = { word: [None if i == position else l for i, l in enumerate(letters)] for (word, letters) in eligible.items() if letters[position] == letter}

    # filter based on yellows
    for (position, letter_feedback) in enumerate(feedback):
        (letter, color) = letter_feedback
        if(color == 'yellow'):
            eligible = {
                word: [None if i == position else l for i, l in enumerate(letters)]
                for (word, letters) in eligible.items()
                if letter in letters and letters[position] != letter
            }

    # filter based on yellows
    for (position, letter_feedback) in enumerate(feedback):
        (letter, color) = letter_feedback
        if(color == 'gray'):
            eligible = { word: letters for (word, letters) in eligible.items() if letter not in letters}
    return eligible

def get_top_word(potential_words):
    letter_counts = {}
    for word in potential_words:
        for letter in list(word):
            letter_counts[letter] = letter_counts.get(letter, 0)+1
    print(letter_counts)
    return 'trace'

# Turn 2
game = Game(word='taste')
# TODO: start with all_words and prioritize common words in guess
potential_words = {word: list(word) for word in common_words}
guesses = []
guess = 'oiled'
last_turn = None

while game.get_status() == 'in progress':
    print(f'DOING TURN {game.get_guesses()+1}')
    potential_words = {word: list(word) for word in potential_words.keys()} # reset
    if last_turn and last_turn['feedback']:
        # TODO: sort by words which have no repeated letters
        potential_words = filter_words(potential_words, last_turn['feedback'])
        guess = get_top_word(list(potential_words.keys()))
        guess = list(potential_words.keys())[0]
    print(f'Guessing {guess}')
    last_turn = game.evaluate_guess(guess)
    if last_turn['outcome'] == 'success':
        guesses.append(last_turn['feedback'])
    else: 
        # try again with another word
        print(last_turn['reason'])
        guess = potential_words[0]

if game.get_status() == 'win':
    print(f'Woohoo, \U0001F973 we won in {game.get_guesses()} turns with word {guess}')
elif game.get_status() == 'loss':
    print(f'Noooo \U0001F616 we lost after {game.get_guesses()} turns')
else:
    print(f'\U0001F450 I don\'t know what happened')