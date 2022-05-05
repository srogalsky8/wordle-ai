from game import Game
from common_words import common_words
import string
import pandas as pd

df = pd.read_csv("./data/Wordle letter frequencies.txt", sep = '\t')

df_letters = df.set_index('Letter')
first_word_freq = df_letters['Overall'].nlargest(5)

print(first_word_freq)

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


#get most freq letter on each turn
turn=['1','2','3','4','5']
most_freq=[]
for i in range(5):
    sort=sorted(df[turn[i]].values, reverse=True)[:5]
    letter=[df['Letter'][df[turn[i]].values==sort[j]].values for j in range(5)]
    letters=[letter[j][0] for j in range(5)]
    most_freq.append(letters)
#['S', 'C', 'B', 'T', 'P'] - first turn
#get list of potential words from the common list based on most freq letters

potential_guess=[i for i in common_words if i in most_freq[0]]