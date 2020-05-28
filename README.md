# Mornington Crescent Analysis
Simple analysis of Morning Crescent dataset.
Finds,
* Number of moves in the shortest (and longest) games.
* Stations which are most (and least) often the last station visited before MC.
#### Running the stats
```
git submodule add https://github.com/pete-rai/mornington-crescent-game-archive.git
pip install pandas
python stats.py
```
... produces,
```
Shortest game: 3 moves.
Longest game: 31 moves.

Penultimate stations.
       station  frequency
   Hammersmith        138
  Edgware Road        126
      Elm Park         84
    Wood Green         81
 Rickmansworth         81
...
    station  frequency
  Southwark         29
 Bermondsey         29
 East India         26
 Cutty Sark         22
  Greenwich         21
```