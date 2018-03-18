+++
draft = false
date="2015-01-25 12:47:01"
title="Python: Find the highest value in a group"
tag=['python', 'pandas']
category=['Python']
+++

<p>
In my continued playing around with a How I met your mother data set I needed to find out the last episode that happened in a season so that I could use it in a chart I wanted to plot.
</p>


<p>
I had this CSV file containing each of the episodes:
</p>



~~~bash

$ head -n 10 data/import/episodes.csv
NumberOverall,NumberInSeason,Episode,Season,DateAired,Timestamp
1,1,/wiki/Pilot,1,"September 19, 2005",1127084400
2,2,/wiki/Purple_Giraffe,1,"September 26, 2005",1127689200
3,3,/wiki/Sweet_Taste_of_Liberty,1,"October 3, 2005",1128294000
4,4,/wiki/Return_of_the_Shirt,1,"October 10, 2005",1128898800
5,5,/wiki/Okay_Awesome,1,"October 17, 2005",1129503600
6,6,/wiki/Slutty_Pumpkin,1,"October 24, 2005",1130108400
7,7,/wiki/Matchmaker,1,"November 7, 2005",1131321600
8,8,/wiki/The_Duel,1,"November 14, 2005",1131926400
9,9,/wiki/Belly_Full_of_Turkey,1,"November 21, 2005",1132531200
~~~

<p>
I started out by parsing the CSV file into a dictionary of (seasons -> episode ids):
</p>



~~~python

import csv
from collections import defaultdict

seasons = defaultdict(list)
with open("data/import/episodes.csv", "r") as episodesfile:
    reader = csv.reader(episodesfile, delimiter = ",")
    reader.next()
    for row in reader:
        seasons[int(row[3])].append(int(row[0]))

print seasons
~~~

<p>which outputs the following:</p>



~~~bash

$ python blog.py
defaultdict(<type 'list'>, {
  1: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22], 
  2: [23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44], 
  3: [45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64], 
  4: [65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88], 
  5: [89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112], 
  6: [113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136], 
  7: [137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160], 
  8: [161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184], 
  9: [185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208]})
~~~

<p>
It's reasonably easy to transform that into a dictionary of (season -> max episode id) with the following couple of lines:
</p>



~~~python

for season, episode_ids in seasons.iteritems():
    seasons[season] = max(episode_ids)

>>> print seasons
defaultdict(<type 'list'>, {1: 22, 2: 44, 3: 64, 4: 88, 5: 112, 6: 136, 7: 160, 8: 184, 9: 208})
~~~

<p>
This works fine but it felt very much like a <a href="https://github.com/hadley/dplyr">dplyr</a> problem to me so I wanted to see whether I could write something cleaner using <a href="http://pandas.pydata.org/">pandas</a>.
</p>


<p>
I started out by capturing the seasons and episode ids in separate lists and then building up a DataFrame:
</p>



~~~python

import pandas as pd
from pandas import DataFrame

seasons, episode_ids = [], []
with open("data/import/episodes.csv", "r") as episodesfile:
    reader = csv.reader(episodesfile, delimiter = ",")
    reader.next()
    for row in reader:
        seasons.append(int(row[3]))
        episode_ids.append(int(row[0]))

df = DataFrame.from_items([('Season', seasons), ('EpisodeId', episode_ids)])

>>> print df.groupby("Season").max()["EpisodeId"]
Season
1          22
2          44
3          64
4          88
5         112
6         136
7         160
8         184
9         208
~~~

<p>
Or we can simplify that and read the CSV file directly into a DataFrame:
</p>



~~~python

df = pd.read_csv('data/import/episodes.csv', index_col=False, header=0)

>>> print df.groupby("Season").max()["NumberOverall"]
Season
1          22
2          44
3          64
4          88
5         112
6         136
7         160
8         184
9         208
~~~

<p>
Pretty neat. I need to get more into pandas.
</p>

