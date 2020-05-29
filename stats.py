# Simple stats from Mornington Crescent dataset.

import json
import pandas as pd

games_file = open('mornington-crescent-game-archive/games.json')
games_json = (games_file.read())
games_file.close()
games = json.loads(s=games_json)

########
# Shortest and longest games.
########
game_lengths = sorted(list(map(lambda game: len(game['moves']), games)))
print('Shortest game: {} moves.'.format(game_lengths[0]))
print('Longest game: {} moves.'.format(game_lengths[-1]))

########
# Which stations are most often visited before final move to MC?
########
frequencies = {}                                    # Key=station, value=count of times it is the penultimate station.
for each_game in games:
    penultimate = each_game['moves'][-2]['move']    # Two moves before end of game is the penultimate station.

    if penultimate in frequencies:
        frequencies[penultimate] += 1
    else:
        frequencies[penultimate] = 1

# Make a pair of lists out of the dictionary keys and values.
stations, freq = [], []
for each_station in sorted(frequencies, reverse=True):
    stations.append(each_station)
    freq.append(frequencies[each_station])

# Load the lists into a DataFrame.
df = pd.DataFrame({'station': stations, 'frequency': freq}).sort_values(by='frequency', ascending=False)
print('\nPenultimate stations.')
print(df.head().to_string(index=False))
print('...')
print(df.tail().to_string(index=False))
