from game import Game
from common_words import common_words
import pandas as pd
import json

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

# based on frequency of remaining letters
def get_word_by_letter_freq(potential_words, past_guesses):
    letter_counts = {}
    for word in potential_words:
        for letter in word:
            letter_counts[letter] = letter_counts.get(letter, 0)+1
    # get letters we've guessed already
    guessed_letters = []
    for guess in past_guesses:
        for (letter, color) in guess:
            guessed_letters.append(letter)
    guessed_letters = list(set(guessed_letters))
    # remove letters we've already guessed
    for letter in guessed_letters:
        if letter in letter_counts:
            del letter_counts[letter]

    # for each potential word, get a freq score
    scores = { word: sum([letter_counts.get(letter, 0) for letter in set(list(word))]) for word in potential_words }
    (word, count) = sorted(scores.items(), key=lambda x: x[1], reverse=True)[0]
    return word

with open('./data/freq_map.json') as json_file:
    data = json.load(json_file)
df = pd.read_csv("./data/Wordle letter frequencies.txt", sep = '\t')
# based on frequency in english dictionary
def get_word_by_freq(potential_words):
    better_words = {word: data[word] for word in potential_words}
    better_words = sorted(better_words.items(), key=lambda x: x[1], reverse=True)
    (guess, frequencies) = better_words[0]
    return guess


input = open('data/CSW19-5.txt')
all_words = [line.strip().lower() for line in input]

def play_game(show_output = False):
    game = Game()
    # TODO: start with all_words and prioritize common words in guess
    potential_words = {word: list(word) for word in all_words}
    guesses = []
    last_turn = None
    # guess = 'salet'
    while game.get_status() == 'in progress':
        show_output and print(f'DOING TURN {game.get_guesses()+1}')
        potential_words = {word: list(word) for word in potential_words.keys()} # reset
        if last_turn and last_turn['feedback']:
            potential_words = filter_words(potential_words, last_turn['feedback'])
        guess = get_word_by_freq(list(potential_words.keys()))
        # guess = get_word_by_letter_freq(list(potential_words.keys()), guesses)
        # guess = list(potential_words.keys())[0] # naive choice
        show_output and print(f'Guessing {guess}')
        last_turn = game.evaluate_guess(guess)
        if last_turn['outcome'] == 'success':
            guesses.append(last_turn['feedback'])
        else: 
            # try again with another word
            show_output and print(last_turn['reason'])
            guess = potential_words[0]

    if(show_output):
        if game.get_status() == 'win':
            print(f'Woohoo, \U0001F973 we won in {game.get_guesses()} turns with word {guess}')
        elif game.get_status() == 'loss':
            print(f'Noooo \U0001F616 we lost after {game.get_guesses()} turns')
            print(f'The word was {game.get_word()}')
        else:
            print(f'\U0001F450 I don\'t know what happened')

    if(game.get_status() == 'loss'):
        print(f'lost {game.get_word()}')
        print(guesses)
    return game.get_status()

results = []
trials = 100
for i in range(0,trials):
    results.append(play_game(show_output = False))

print(f'Won {(results.count("win")/trials)*100}% of {trials} games')


# #get most freq letter on each turn
# turn=['1','2','3','4','5']
# most_freq=[]
# for i in range(5):
#     sort=sorted(df[turn[i]].values, reverse=True)[:5]
#     letter=[df['Letter'][df[turn[i]].values==sort[j]].values for j in range(5)]
#     letters=[letter[j][0] for j in range(5)]
#     most_freq.append(letters)
# #['S', 'C', 'B', 'T', 'P'] - first turn
# #get list of potential words from the common list based on most freq letters

# potential_guess=[i for i in common_words if i in most_freq[0]]


# #function to suggest starting characters before guessing words
# def suggest_chars_turn_zero():
#     best_chars = []
#     df_letters_original = df.set_index('Letter')
#     print("Consider the following letters:")
#     first_word_freq = df_letters_original['Overall'].nlargest(5)
#     for letter in first_word_freq.index:
#         best_chars.append(letter)
#     print(best_chars)
# # turn zero
# suggest_chars_turn_zero()