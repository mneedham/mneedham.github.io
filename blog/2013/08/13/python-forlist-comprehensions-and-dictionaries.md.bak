+++
draft = false
date="2013-08-13 22:59:52"
title="Python: for/list comprehensions and dictionaries"
tag=['python']
category=['Python']
+++

<p>I've been working through Coursera's <a href="https://class.coursera.org/matrix-001/class/index">Linear Algebra course</a> and since all of the exercises are in Python I've been playing around with it again.</p>


<p>One interesting thing I learnt is that you can construct dictionaries using a <a href="http://www.secnetix.de/olli/Python/list_comprehensions.hawk">list comprehension</a> type syntax.</p>


<p>For example, if we start with the following dictionaries:</p>



~~~python

>>> x = { "a": 1, "b":2 } 
>>> y = {1: "mark", 2: "will"}
>>> x
{'a': 1, 'b': 2}
>>> y
{1: 'mark', 2: 'will'}
~~~

<p>We might want to create a new dictionary which links from the keys in x to the values in y. In this case we work out the mapping by finding the key in y which corresponds with each value in x.</p>


<p>So the map we want to see at the end should look like this:</p>



~~~text

{"a": 'mark', "b": 'will'}
~~~

<p>We can iterate over the keys/values of a dictionary by calling <cite>Dictionary#iteritems</cite> like so:</p>



~~~python

>>> for key, value in x.iteritems():
...   print (key, value)
... 
('a', 1)
('b', 2)
~~~

<p>I thought I might be able to construct my new dictionary by converting this into a for comprehension:</p>



~~~python

>>> [key:value for key, value in x.iteritems()]
  File "<stdin>", line 1
    [key:value for key, value in x.iteritems()]
        ^
SyntaxError: invalid syntax
~~~

<p>Unfortunately that didn't work but I came across <a href="http://stackoverflow.com/questions/3294889/iterating-over-dictionaries-for-loops-in-python">an interesting post</a> from which I learned that using curly brackets might do the trick.</p>



~~~python

>>> {key:value for key, value in x.iteritems()}
{'a': 1, 'b': 2}
>>> type({key:value for key, value in x.iteritems()})
<type 'dict'>
~~~

<p>I wanted to make the final dictionary take a lookup into account which we can do like this:</p>



~~~python

>>> {key:y[value] for key, value in x.iteritems()}
{'a': 'mark', 'b': 'will'}
~~~

<p>Apparently this is known as a <a href="http://www.python.org/dev/peps/pep-0274/">dictionary comprehension</a> and has <a href="http://stackoverflow.com/questions/7276511/are-there-dictionary-comprehensions-in-python-problem-with-function-returning">been in the language since version 2.7</a>.</p>


<p>I'm sure this is old news to seasoned Python developers but I'd not come across it before so to me it's pretty neat!</p>

