+++
draft = false
date="2015-03-22 01:51:52"
title="Python: Simplifying the creation of a stop word list with defaultdict"
tag=['python']
category=['Python']
+++

<p>
I've been playing around with topics models again and recently read a <a href="http://www.perseus.tufts.edu/publications/02-jocch-mimno.pdf">paper by David Mimno</a> which suggested the following heuristic for working out which words should go onto the stop list:
</p>


<blockquote>
A good heuristic for identifying such words is to remove those that occur in more than 5-10% of documents (most common) and those that occur fewer than 5-10 times in the entire corpus (least common).
</blockquote>

<p>
I decided to try this out on the <a href="https://github.com/mneedham/neo4j-himym/blob/master/data/import/sentences.csv">HIMYM dataset</a> that I've been working on over the last couple of months. 
</p>


<p>I started out with the following code to build a dictionary of words, their total occurrences and the episodes they'd been used in:</p>



~~~python

import csv
from sklearn.feature_extraction.text import CountVectorizer
from collections import defaultdict

episodes = defaultdict(str)
with open("sentences.csv", "r") as file:
    reader = csv.reader(file, delimiter = ",")
    reader.next()
    for row in reader:
        episodes[row[1]] += row[4]

vectorizer = CountVectorizer(analyzer='word', min_df = 0, stop_words = 'english')
matrix = vectorizer.fit_transform(episodes.values())
features = vectorizer.get_feature_names()

words = {}
for doc_id, doc in enumerate(matrix.todense()):
    for word_id, score in enumerate(doc.tolist()[0]):
        word = features[word_id]
        if not words.get(word):
            words[word] = {}

        if not words[word].get("score"):
            words[word]["score"] = 0
        words[word]["score"] += score

        if not words[word].get("episodes"):
            words[word]["episodes"] = set()

        if score > 0:
            words[word]["episodes"].add(doc_id)
~~~

<p>
This works fine but the code inside the last for block is ugly and most of it is handling the case when parts of a dictionary aren't yet initialised which is defaultdict territory. You'll notice I am using defaultdict in the first part of the code but not yet the second as I'd struggled to get it working.
</p>


<p>
This was my first attempt to make the 'words' variable based on it:
</p>



~~~python

>>> words = defaultdict({})
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: first argument must be callable
~~~

<p>
We can see why this doesn't work if we try to evaluate '{}' as a function which is what defaultdict does internally:
</p>



~~~python

>>> {}()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'dict' object is not callable
~~~

<p>Instead what we need is to pass in 'dict':</p>



~~~python

>>> dict()
{}

>>> words = defaultdict(dict)

>>> words
defaultdict(<type 'dict'>, {})
~~~

<p>
That simplifies the first bit of the loop:
</p>



~~~python

words = defaultdict(dict)
for doc_id, doc in enumerate(matrix.todense()):
    for word_id, score in enumerate(doc.tolist()[0]):
        word = features[word_id]
        if not words[word].get("score"):
            words[word]["score"] = 0
        words[word]["score"] += score

        if not words[word].get("episodes"):
            words[word]["episodes"] = set()

        if score > 0:
            words[word]["episodes"].add(doc_id)
~~~

<p>We've still got a couple of other places to simplify though which we can do by defining a <a href="http://pymotw.com/2/collections/defaultdict.html">custom function</a> and passing that into defaultdict:</p>



~~~python

def default_dict_function():
   return {"score": 0, "episodes": set()}

>>> words = defaultdict(default_dict_function)

>>> words
defaultdict(<function default_dict_function at 0x10963fcf8>, {})
~~~

<p>
And here's the final product:
</p>



~~~python

def default_dict_function():
   return {"score": 0, "episodes": set()}
words = defaultdict(default_dict_function)

for doc_id, doc in enumerate(matrix.todense()):
    for word_id, score in enumerate(doc.tolist()[0]):
        word = features[word_id]
        words[word]["score"] += score
        if score > 0:
            words[word]["episodes"].add(doc_id)
~~~

<p>After this we can write out the words to our stop list:</p>



~~~python

with open("stop_words.txt", "w") as file:
    writer = csv.writer(file, delimiter = ",")
    for word, value in words.iteritems():
        # appears in > 10% of episodes
        if len(value["episodes"]) > int(len(episodes) / 10):
            writer.writerow([word.encode('utf-8')])

        # less than 10 occurences
        if value["score"] < 10:
            writer.writerow([word.encode('utf-8')])
~~~
