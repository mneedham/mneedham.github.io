+++
draft = false
date="2013-01-27 02:30:05"
title="Python: (Conceptually) removing an item from a tuple"
tag=['python']
category=['Python']
+++

<p>As part of some code I've been playing around I wanted to remove an item from a tuple which wasn't particularly easy because  Python's tuple data structure is immutable.</p>


<p>I therefore needed to create a new tuple excluding the value which I wanted to remove.</p>


<p>I ended up writing the following function to do this but I imagine there might be an easier way because it's quite verbose:</p>



~~~python

def tuple_without(original_tuple, element_to_remove):
    new_tuple = []
    for s in list(original_tuple):
        if not s == element_to_remove:
            new_tuple.append(s)
    return tuple(new_tuple)  
~~~

<p>Which can be used like so:</p>



~~~python

>>> tuple_without((1,2,3,4), 1)
(2, 3, 4)
~~~


~~~python

>>> tuple_without((1,2,3,4), 0)
(1, 2, 3, 4)
~~~

<p>The easiest approach seemed to be to build up a list containing all the values and then convert it to a tuple by using the <cite><a href="http://docs.python.org/2/library/functions.html#tuple">tuple</a></cite> function.</p>


<p>It'd be cool if there was a way to transform a tuple like this but I couldn't find such a function in my travels.</p>

