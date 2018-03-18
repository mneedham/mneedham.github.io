+++
draft = false
date="2015-05-24 23:51:25"
title="Python: Joining multiple generators/iterators"
tag=['python']
category=['Python']
+++

<p>

In my previous blog post I described how I'd <a href="http://www.markhneedham.com/blog/2015/05/23/python-refactoring-to-iterator/">refactored some scraping code I've been working on to use iterators</a> and ended up with a function which returned a generator containing all the events for one BBC live text match:

</p>



~~~python

match_id = "32683310"
events = extract_events("data/raw/%s" % (match_id))

>>> print type(events)
<type 'generator'>
~~~

<p>
The next thing I wanted to do is get the events for multiple matches which meant I needed to glue together multiple generators into one big generator. 
</p>


<p>
itertools' <cite><a href="https://docs.python.org/2/library/itertools.html#itertools.chain">chain</a></cite> function <a href="http://stackoverflow.com/questions/3211041/how-to-join-two-generators-in-python">does exactly what we want</a>:
</p>


<blockquote>
itertools.chain(*iterables)


Make an iterator that returns elements from the first iterable until it is exhausted, then proceeds to the next iterable, until all of the iterables are exhausted. Used for treating consecutive sequences as a single sequence.
</blockquote>

<p>First let's try it out on a collection of range generators:</p>



~~~python

import itertools
gens = [(n*2 for n in range(0, 3)), (n*2 for n in range(4,7))]
>>> gens
[<generator object <genexpr> at 0x10ff3b140>, <generator object <genexpr> at 0x10ff7d870>]

output = itertools.chain()
for gen in gens:
  output = itertools.chain(output, gen)
~~~

<p>Now if we iterate through 'output' we'd expect to see the multiples of 2 up to and including 12:</p>



~~~python

>>> for item in output:
...   print item
...
0
2
4
8
10
12
~~~

<p>Exactly as we expected! Our scraping code looks like this once we plug the chaining in:
</p>



~~~python

matches = ["32683310", "32683303", "32384894", "31816155"]

raw_events = itertools.chain()
for match_id in matches:
    raw_events = itertools.chain(raw_events, extract_events("data/raw/%s" % (match_id)))
~~~

<p>
'raw_events' now contains a single generator that we can iterate through and process the events for all matches.
</p>

