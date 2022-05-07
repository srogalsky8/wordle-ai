
import json
import pandas as pd

with open('./data/freq_map.json') as json_file:
    data = json.load(json_file)

sorted_data = sorted(data.items(), key=lambda x: x[1], reverse=True)
percentile = 0.1

quantile = int(percentile*len(sorted_data))

freq_data = {word: (len(sorted_data) - index)/len(sorted_data) for (index, (word, freq)) in enumerate(sorted_data)}
# freq_data = {word: 1 for (word, freq) in sorted_data[:quantile]}
# scaled_data = {word: 0.1 for (word, freq) in sorted_data[quantile:]}
# freq_data.update(scaled_data)

