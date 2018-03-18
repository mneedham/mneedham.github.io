+++
draft = false
date="2015-01-10 01:22:56"
title="Python NLTK/Neo4j: Analysing the transcripts of How I Met Your Mother"
tag=['neo4j', 'python']
category=['neo4j', 'Python']
+++

<p>
After reading <a href="https://twitter.com/emileifrem">Emil's</a> <a href="http://dataconomy.com/discovering-the-power-of-dark-data/">blog post about dark data</a> a few weeks ago I became intrigued about trying to find some structure in free text data and I thought How I met your mother's transcripts would be a good place to start.
</p>


<p>I found a website which has the <a href="http://transcripts.foreverdreaming.org/viewforum.php?f=177">transcripts for all the episodes</a> and then having manually downloaded the two pages which listed all the episodes, wrote a script to grab each of the transcripts so I could use them on my machine.
</p>


<p>I wanted to learn a bit of Python and my colleague <a href="https://twitter.com/technige">Nigel</a> pointed me towards the <a href="http://docs.python-requests.org/en/latest/">requests</a> and <a href="http://www.crummy.com/software/BeautifulSoup/bs4/doc/">BeautifulSoup</a> libraries to help me with my task. The script to grab the transcripts looks like this:</p>



~~~python

import requests
from bs4 import BeautifulSoup
from soupselect import select

episodes = {}
for i in range(1,3):
    page = open("data/transcripts/page-" + str(i) + ".html", 'r')
    soup = BeautifulSoup(page.read())

    for row in select(soup, "td.topic-titles a"):
        parts = row.text.split(" - ")
        episodes[parts[0]] = {"title": parts[1], "link": row.get("href")}

for key, value in episodes.iteritems():
    parts = key.split("x")
    season = int(parts[0])
    episode = int(parts[1])
    filename = "data/transcripts/S%d-Ep%d" %(season, episode)
    print filename

    with open(filename, 'wb') as handle:
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        response = requests.get("http://transcripts.foreverdreaming.org" + value["link"], headers = headers)
        if response.ok:
            for block in response.iter_content(1024):
                if not block:
                    break

                handle.write(block)
~~~

<p>
<em>the files containing the lists of episodes are named 'page-1' and 'page-2'</em>
</p>


<p>The code is reasonably simple - we find all the links inside the table, put them in a dictionary and then iterate through the dictionary and download the files to disk. The code to save the file is a bit of a monstrosity but there didn't seem to be a 'save' method that I could use.</p>


<p>
Having downloaded the files, I thought through all sorts of clever things I could do, including generating a bag of words model for each episode or performing sentiment analysis on each sentence which I'd <a href="https://www.kaggle.com/c/word2vec-nlp-tutorial">learnt about from a Kaggle tutorial</a>.
</p>


<p>
In the end I decided to start simple and extract all the words from the transcripts and count many times a word occurred in a given episode.
</p>


<p>
I ended up with the following script which created a dictionary of (episode -> words + occurrences):
</p>



~~~python

import csv
import nltk
import re

from bs4 import BeautifulSoup
from soupselect import select
from nltk.corpus import stopwords
from collections import Counter
from nltk.tokenize import word_tokenize

def count_words(words):
    tally=Counter()
    for elem in words:
        tally[elem] += 1
    return tally

episodes_dict = {}
with open('data/import/episodes.csv', 'r') as episodes:
    reader = csv.reader(episodes, delimiter=',')
    reader.next()

    for row in reader:
        print row
        transcript = open("data/transcripts/S%s-Ep%s" %(row[3], row[1])).read()
        soup = BeautifulSoup(transcript)
        rows = select(soup, "table.tablebg tr td.post-body div.postbody")

        raw_text = rows[0]
        [ad.extract() for ad in select(raw_text, "div.ads-topic")]
        [ad.extract() for ad in select(raw_text, "div.t-foot-links")]

        text = re.sub("[^a-zA-Z]", " ", raw_text.text.strip())
        words = [w for w in nltk.word_tokenize(text) if not w.lower() in stopwords.words("english")]

        episodes_dict[row[0]] = count_words(words)
~~~

<p>

</p>


<p>
Next I wanted to explore the data a bit to see which words occurred across episodes or which word occurred most frequently and realised that this would be a much easier task if I stored the data somewhere.
</p>


<p>s/somewhere/in Neo4j</p>


<p>
Neo4j's query language, Cypher, has a really nice ETL-esque tool called 'LOAD CSV' for loading in CSV files (as the name suggests!) so I added some code to save my words to disk:
</p>



~~~python

with open("data/import/words.csv", "w") as words:
    writer = csv.writer(words, delimiter=",")
    writer.writerow(["EpisodeId", "Word", "Occurrences"])
    for episode_id, words in episodes_dict.iteritems():
        for word in words:
            writer.writerow([episode_id, word, words[word]])
~~~

<p>This is what the CSV file contents look like:</p>



~~~bash

$ head -n 10 data/import/words.csv
EpisodeId,Word,Occurrences
165,secondly,1
165,focus,1
165,baby,1
165,spiders,1
165,go,4
165,apartment,1
165,buddy,1
165,Exactly,1
165,young,1
~~~

<p>
Now we need to write some Cypher to get the data into Neo4j:
</p>



~~~cypher

// words
LOAD CSV WITH HEADERS FROM "file:/Users/markneedham/projects/neo4j-himym/data/import/words.csv" AS row
MERGE (word:Word {value: row.Word})
~~~


~~~cypher

// episodes
LOAD CSV WITH HEADERS FROM "file:/Users/markneedham/projects/neo4j-himym/data/import/words.csv" AS row
MERGE (episode:Episode {id: TOINT(row.EpisodeId)})
~~~


~~~cypher

// words to episodes
LOAD CSV WITH HEADERS FROM "file:/Users/markneedham/projects/neo4j-himym/data/import/words.csv" AS row
MATCH (word:Word {value: row.Word})
MATCH (episode:Episode {id: TOINT(row.EpisodeId)})
MERGE (word)-[:USED_IN_EPISODE {times: TOINT(row.Occurrences) }]->(episode);
~~~

<p>
Having done that we can write some simple queries to explore the words used in How I met your mother:
</p>



~~~cypher

MATCH (word:Word)-[r:USED_IN_EPISODE]->(episode) 
RETURN word.value, COUNT(episode) AS episodes, SUM(r.times) AS occurrences
ORDER BY occurrences DESC
LIMIT 10

==> +-------------------------------------+
==> | word.value | episodes | occurrences |
==> +-------------------------------------+
==> | "Ted"      | 207      | 11437       |
==> | "Barney"   | 208      | 8052        |
==> | "Marshall" | 208      | 7236        |
==> | "Robin"    | 205      | 6626        |
==> | "Lily"     | 207      | 6330        |
==> | "m"        | 208      | 4777        |
==> | "re"       | 208      | 4097        |
==> | "know"     | 208      | 3489        |
==> | "Oh"       | 197      | 3448        |
==> | "like"     | 208      | 2498        |
==> +-------------------------------------+
==> 10 rows
~~~

<p>
The main 5 characters occupy the top 5 positions which is probably what you'd expect. I'm not sure why 'm' and 're' are in the next two position s - I expect that might be scraping gone wrong! 
</p>


<p>
Our next query might focus around checking which character is referred to the post in each episode:
</p>



~~~cypher

WITH ["Ted", "Barney", "Robin", "Lily", "Marshall"] as mainCharacters
MATCH (word:Word) WHERE word.value IN mainCharacters
MATCH (episode:Episode)<-[r:USED_IN_EPISODE]-(word)
WITH episode, word, r
ORDER BY episode.id, r.times DESC
WITH episode, COLLECT({word: word.value, times: r.times})[0] AS topWord
RETURN episode.id, topWord.word AS word, topWord.times AS occurrences
LIMIT 10

==> +---------------------------------------+
==> | episode.id | word       | occurrences |
==> +---------------------------------------+
==> | 72         | "Barney"   | 75          |
==> | 143        | "Ted"      | 16          |
==> | 43         | "Lily"     | 74          |
==> | 156        | "Ted"      | 12          |
==> | 206        | "Barney"   | 23          |
==> | 50         | "Marshall" | 51          |
==> | 113        | "Ted"      | 76          |
==> | 178        | "Barney"   | 21          |
==> | 182        | "Barney"   | 22          |
==> | 67         | "Ted"      | 84          |
==> +---------------------------------------+
==> 10 rows
~~~

<p>
If we dig into it further there's actually quite a bit of variety in the number of times the top character in each episode is mentioned which again probably says something about the data:
</p>



~~~cypher

WITH ["Ted", "Barney", "Robin", "Lily", "Marshall"] as mainCharacters
MATCH (word:Word) WHERE word.value IN mainCharacters
MATCH (episode:Episode)<-[r:USED_IN_EPISODE]-(word)
WITH episode, word, r
ORDER BY episode.id, r.times DESC
WITH episode, COLLECT({word: word.value, times: r.times})[0] AS topWord
RETURN MIN(topWord.times), MAX(topWord.times), AVG(topWord.times), STDEV(topWord.times)

==> +-------------------------------------------------------------------------------------+
==> | MIN(topWord.times) | MAX(topWord.times) | AVG(topWord.times) | STDEV(topWord.times) |
==> +-------------------------------------------------------------------------------------+
==> | 3                  | 259                | 63.90865384615385  | 42.36255207691068    |
==> +-------------------------------------------------------------------------------------+
==> 1 row
~~~

<p>
Obviously this is a very simple way of deriving structure from text, here are some of the things I want to try out next:
</p>


<ul>

<li>
Detecting common phrases/memes/phrases used in the show (e.g. the yellow umbrella) - this should be possible by creating different length n-grams and then searching for those phrases across the corpus.
</li>
<li>
Pull out scenes - some of the transcripts use the keyword 'scene' to denote this although some of them don't. Depending how many transcripts contain scene demarkations perhaps we could train a classifier to detect where scenes should be in the transcripts which don't have scenes.
</li>
<li>
Analyse who talks to each other or who talks about each other most frequently
</li>
<li>Create a graph of conversations as my colleagues <a href="http://maxdemarzi.com/2012/08/10/summarize-opinions-with-a-graph-part-1/">Max</a> and <a href="http://jexp.github.io/blog/html/simple_nlp_with_graphs.html">Michael</a> have previously blogged about.</li>
</ul>
