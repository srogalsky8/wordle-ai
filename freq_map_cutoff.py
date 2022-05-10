
import json
import pandas as pd

with open('./data/freq_map.json') as json_file:
    data = json.load(json_file)

sorted_data = sorted(data.items(), key=lambda x: x[1], reverse=True)

# method 1: hard cutoff
percentile = 0.45
quantile = int(percentile*len(sorted_data))
freq_data = {word: 1 for (word, freq) in sorted_data[:quantile]}
reduced = {word: 0.2 for (word, freq) in sorted_data[quantile:]}
freq_data.update(reduced)

# method 2: scaled
scaled_data = {word: (len(sorted_data) - index)/len(sorted_data) for (index, (word, freq)) in enumerate(sorted_data)}