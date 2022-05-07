from game import Game
from common_words import common_words
import numpy as np
from ai import simulate

p_wins = []
for (i, word) in enumerate(common_words):
    print(f'simulating word {word}')
    p_wins.append(simulate(trials=1000, starting_word=word))

np_wins = np.array(p_wins)
npcw = np.array(common_words)
order = np.argsort(np_wins)[::-1]
print(np_wins[order][:50])
print(npcw[order][:50])
