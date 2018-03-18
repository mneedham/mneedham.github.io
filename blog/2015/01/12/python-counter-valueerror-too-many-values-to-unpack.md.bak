+++
draft = false
date="2015-01-12 23:16:58"
title="Python: Counter - ValueError: too many values to unpack"
tag=['python']
category=['Python']
+++

<p>
I recently came across <a href="https://docs.python.org/2/library/collections.html#collections.Counter">Python's Counter tool</a> which makes it really easy to count the number of occurrences of items in a list.
</p>


<p>
In my case I was trying to work out how many times words occurred in a corpus so I had something like the following:
</p>



~~~python

>> from collections import Counter
>> counter = Counter(["word1", "word2", "word3", "word1"])
>> print counter
Counter({'word1': 2, 'word3': 1, 'word2': 1})
~~~

<p>
I wanted to write a for loop to iterate over the counter and print the (key, value) pairs and started with the following:
</p>



~~~python

>>> for key, value in counter:
...   print key, value
...
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: too many values to unpack
~~~

<p>
I'm not sure why I expected this to work but in fact since Counter is a sub class of dict we need to call <a href="https://docs.python.org/2/library/stdtypes.html#dict.iteritems">iteritems</a> to get an iterator of pairs rather than just keys.
</p>


<p>The following does the job:</p>



~~~python

>>> for key, value in counter.iteritems():
...   print key, value
...
word1 2
word3 1
word2 1
~~~

<p>Hopefully future Mark will remember this!</p>

