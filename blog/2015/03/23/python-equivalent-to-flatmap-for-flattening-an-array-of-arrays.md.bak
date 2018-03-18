+++
draft = false
date="2015-03-23 00:45:00"
title="Python: Equivalent to flatMap for flattening an array of arrays"
tag=['python']
category=['Python']
+++

<p>I found myself wanting to flatten an array of arrays while writing some Python code earlier this afternoon and being lazy my first attempt involved building the flattened array manually:</p>



~~~python

episodes = [
    {"id": 1, "topics": [1,2,3]},
    {"id": 2, "topics": [4,5,6]}
]

flattened_episodes = []
for episode in episodes:
    for topic in episode["topics"]:
        flattened_episodes.append({"id": episode["id"], "topic": topic})

for episode in flattened_episodes:
    print episode
~~~

<p>If we run that we'll see this output:</p>



~~~bash

$ python flatten.py

{'topic': 1, 'id': 1}
{'topic': 2, 'id': 1}
{'topic': 3, 'id': 1}
{'topic': 4, 'id': 2}
{'topic': 5, 'id': 2}
{'topic': 6, 'id': 2}
~~~

<p>
What I was really looking for was the Python equivalent to the <a href="http://www.markhneedham.com/blog/2011/07/03/clojure-equivalent-to-scalas-flatmapcs-selectmany/">flatmap function</a> which I learnt can be achieved in Python <a href="http://stackoverflow.com/questions/1077015/python-list-comprehensions-compressing-a-list-of-lists">with a list comprehension</a> like so:
</p>



~~~python

flattened_episodes = [{"id": episode["id"], "topic": topic}
                      for episode in episodes
                      for topic in episode["topics"]]

for episode in flattened_episodes:
    print episode
~~~

<p>
We could also choose to <a href="http://naiquevin.github.io/a-look-at-some-of-pythons-useful-itertools.html">use itertools</a> in which case we'd have the following code:
</p>



~~~python

from itertools import chain, imap
flattened_episodes = chain.from_iterable(
                        imap(lambda episode: [{"id": episode["id"], "topic": topic}
                                             for topic in episode["topics"]],
                             episodes))
for episode in flattened_episodes:
    print episode
~~~

<p>
We can then simplify this approach a little by wrapping it up in a 'flatmap' function:
</p>



~~~python

def flatmap(f, items):
        return chain.from_iterable(imap(f, items))

flattened_episodes = flatmap(
    lambda episode: [{"id": episode["id"], "topic": topic} for topic in episode["topics"]], episodes)

for episode in flattened_episodes:
    print episode
~~~

<p>I think the list comprehensions approach still works but I need to look into itertools more - it looks like it could work  well for other list operations.</p>

