+++
draft = false
date="2015-07-28 20:05:47"
title="Python: Difference between two datetimes in milliseconds"
tag=['python']
category=['Python']
+++

<p>
I've been doing a bit of adhoc measurement of some cypher queries executed via <a href="http://py2neo.org/2.0/">py2neo</a> and wanted to work out how many milliseconds each query was taking end to end.
<p>

<p>
I thought there'd be an obvious way of doing this but if there is it's evaded me so far and I ended up <a href="http://stackoverflow.com/questions/1345827/how-do-i-find-the-time-difference-between-two-datetime-objects-in-python">calculating the different between two <em>datetime</em> objects</a> which gave me the following timedelta object:
</p>



~~~python

>>> import datetime
>>> start = datetime.datetime.now()
>>> end = datetime.datetime.now()

>>> end - start
datetime.timedelta(0, 3, 519319)
~~~

<p>
The 3 parts of this object are 'days', 'seconds' and 'microseconds' which I found quite strange!
</p>


<p>
These are the methods/attributes we have available to us:
</p>



~~~python

>>> dir(end - start)
['__abs__', '__add__', '__class__', '__delattr__', '__div__', '__doc__', '__eq__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__mul__', '__ne__', '__neg__', '__new__', '__nonzero__', '__pos__', '__radd__', '__rdiv__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rmul__', '__rsub__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', 'days', 'max', 'microseconds', 'min', 'resolution', 'seconds', 'total_seconds']
~~~

<p>
There's no 'milliseconds' on there so we'll have to calculate it from what we do have:
</p>



~~~python

>>> diff = end - start
>>> elapsed_ms = (diff.days * 86400000) + (diff.seconds * 1000) + (diff.microseconds / 1000)

>>> elapsed_ms
3519
~~~

<p>
Or we could do the following slightly simpler calculation:
</p>



~~~python

>>> diff.total_seconds() * 1000
3519.319
~~~

<p>And now back to the query profiling!</p>

