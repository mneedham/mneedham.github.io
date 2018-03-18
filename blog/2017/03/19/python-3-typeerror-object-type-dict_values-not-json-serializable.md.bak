+++
draft = false
date="2017-03-19 16:40:03"
title="Python 3: TypeError: Object of type 'dict_values' is not JSON serializable"
tag=['python']
category=['Python']
+++

<p>
I've recently upgraded to Python 3 (I know, took me a while!) and realised that one of my scripts that writes JSON to a file no longer works!
</p>


<p>
This is a simplified version of what I'm doing:
</p>



~~~python

>>> import json
>>> x = {"mark": {"name": "Mark"}, "michael": {"name": "Michael"}  } 
>>> json.dumps(x.values())
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/local/Cellar/python3/3.6.0/Frameworks/Python.framework/Versions/3.6/lib/python3.6/json/__init__.py", line 231, in dumps
    return _default_encoder.encode(obj)
  File "/usr/local/Cellar/python3/3.6.0/Frameworks/Python.framework/Versions/3.6/lib/python3.6/json/encoder.py", line 199, in encode
    chunks = self.iterencode(o, _one_shot=True)
  File "/usr/local/Cellar/python3/3.6.0/Frameworks/Python.framework/Versions/3.6/lib/python3.6/json/encoder.py", line 257, in iterencode
    return _iterencode(o, 0)
  File "/usr/local/Cellar/python3/3.6.0/Frameworks/Python.framework/Versions/3.6/lib/python3.6/json/encoder.py", line 180, in default
    o.__class__.__name__)
TypeError: Object of type 'dict_values' is not JSON serializable
~~~

<p>
Python 2.7 would be perfectly happy:
</p>



~~~python

>>> json.dumps(x.values())
'[{"name": "Michael"}, {"name": "Mark"}]'
~~~

<p>
The difference is in the results returned by the <cite>values</cite> method:
</p>



~~~python

# Python 2.7.10
>>> x.values()
[{'name': 'Michael'}, {'name': 'Mark'}]

# Python 3.6.0
>>> x.values()
dict_values([{'name': 'Mark'}, {'name': 'Michael'}])
>>> 
~~~

<p>
Python 3 no longer returns an array, instead we have a <cite>dict_values</cite> wrapper around the data. 
</p>


<p>
Luckily this is easy to resolve - we just need to <a href="http://stackoverflow.com/questions/16228248/python-simplest-way-to-get-list-of-values-from-dict">wrap the call to <cite>values</cite> with a call to <cite>list</cite></a>:
</p>



~~~python

>>> json.dumps(list(x.values()))
'[{"name": "Mark"}, {"name": "Michael"}]'
~~~

<p>
This versions works with Python 2.7 as well so if I accidentally run the script with an old version the world isn't going to explode.
</p>

