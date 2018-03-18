+++
draft = false
date="2017-12-01 15:26:36"
title="Python: Learning about defaultdict's handling of missing keys"
tag=['collections', 'python', 'scikit-learn']
category=['Python']
+++

<p>
While reading the scikit-learn code I came across a bit of code that I didn't understand for a while but in retrospect is quite neat.
</p>


<p>
This is the code snippet that intrigued me:
</p>



~~~python

vocabulary = defaultdict()
vocabulary.default_factory = vocabulary.__len__
~~~

<p>
Let's quickly see how it works by adapting an example from scikit-learn:
</p>



~~~python

>>> from collections import defaultdict
>>> vocabulary = defaultdict()
>>> vocabulary.default_factory = vocabulary.__len__

>>> vocabulary["foo"]
0
>>> vocabulary.items()
dict_items([('foo', 0)])

>>> vocabulary["bar"]
1
>>> vocabulary.items()
dict_items([('foo', 0), ('bar', 1)])
~~~

<p>
What seems to happen is that when we try to find a key that doesn't exist in the dictionary an entry gets created with a value equal to the number of items in the dictionary.
</p>


<p>
Let's check if that assumption is correct by explicitly adding a key and then trying to find one that doesn't exist:
</p>



~~~python

>>> vocabulary["baz"] = "Mark
>>> vocabulary["baz"]
'Mark'
>>> vocabulary["python"]
3
~~~

<p>
Now let's see what the dictionary contains:
</p>



~~~python

>>> vocabulary.items()
dict_items([('foo', 0), ('bar', 1), ('baz', 'Mark'), ('python', 3)])
~~~

<p>
All makes sense so far. If we look at <a href="https://github.com/python/cpython/blob/master/Modules/_collectionsmodule.c#L1973">the source code</a> we can see that this is exactly what's going on: 
</p>



~~~python

"""
__missing__(key) # Called by __getitem__ for missing key; pseudo-code:
  if self.default_factory is None: raise KeyError((key,))
  self[key] = value = self.default_factory()
  return value
"""
pass
~~~

<p>
scikit-learn uses this code to store a mapping of features to their column position in a matrix, which is a perfect use case.
</p>


<p>All in all, very neat!</p>

