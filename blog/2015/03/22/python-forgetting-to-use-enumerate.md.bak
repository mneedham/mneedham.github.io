+++
draft = false
date="2015-03-22 01:28:33"
title="Python: Forgetting to use enumerate"
tag=['python']
category=['Python']
+++

<p>
Earlier this evening I found myself writing the equivalent of the following Python code while building a stop list for a topic model...
</p>



~~~python

words = ["mark", "neo4j", "michael"]
word_position = 0
for word in words:
   print word_position, word
   word_position +=1
~~~

<p>
...which is very foolish given that there's <a href="https://docs.python.org/2/library/functions.html#enumerate">already a function</a> that makes it really easy to grab the position of an item in a list:</p>



~~~python

for word_position, word in enumerate(words):
   print word_position, word
~~~

<p>Python does make things extremely easy at times - you're welcome future Mark!</p>

