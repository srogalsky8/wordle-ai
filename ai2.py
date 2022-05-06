from game import Game

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

# maximize word
def get_top_word(potential_words, past_guesses):
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


input = open('data/CSW19-5.txt')
all_words = [line.strip().lower() for line in input]

def play_game(show_output = False):
    game = Game()
    # TODO: start with all_words and prioritize common words in guess
    potential_words = {word: list(word) for word in all_words}
    guesses = []
    guess = 'trace'
    last_turn = None

    while game.get_status() == 'in progress':
        show_output and print(f'DOING TURN {game.get_guesses()+1}')
        potential_words = {word: list(word) for word in potential_words.keys()} # reset
        if last_turn and last_turn['feedback']:
            # TODO: sort by words which have no repeated letters
            potential_words = filter_words(potential_words, last_turn['feedback'])
            # based on frequency of remaining letters
            guess = get_top_word(list(potential_words.keys()), guesses)
            # naive choice
            # guess = list(potential_words.keys())[0]
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
    return game.get_status()

results = []
trials = 1000
for i in range(0,trials):
    results.append(play_game(show_output = False))

print(f'Won {(results.count("win")/trials)*100}% of {trials} games')