+++
draft = false
date="2015-03-15 22:43:17"
title="Python: Transforming Twitter datetime string to timestamp (z' is a bad directive in format)"
tag=['python']
category=['Python']
+++

<p>
I've been playing around with importing Twitter data into Neo4j and since Neo4j can't store dates natively just yet I needed to convert a date string to timestamp.
</p>


<p>I started with the following which unfortunately throws an exception:</p>



~~~python

from datetime import datetime
date = "Sat Mar 14 18:43:19 +0000 2015"

>>> datetime.strptime(date, "%a %b %d %H:%M:%S %z %Y")

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/_strptime.py", line 317, in _strptime
    (bad_directive, format))
ValueError: 'z' is a bad directive in format '%a %b %d %H:%M:%S %z %Y'
~~~

<p>
<a href="https://docs.python.org/2/library/datetime.html#strftime-strptime-behavior">%z is actually a valid option</a> used to extract the timezone but my googling suggests it not working is one of the idiosyncrasies of strptime. 
</p>


<p>
I eventually came across the <cite>python-dateutil</cite> library, as <a href="http://stackoverflow.com/questions/3305413/python-strptime-and-timezones">recommended by Joe Shaw on StackOverflow</a>.
</p>


<p>Using that library the problem is suddenly much simpler:</p>



~~~bash

$ pip install python-dateutil
~~~


~~~python

from dateutil import parser
parsed_date = parser.parse(date)

>>> parsed_date
datetime.datetime(2015, 3, 14, 18, 43, 19, tzinfo=tzutc())
~~~

<p>
To get to a timestamp we can use calendar as I've <a href="http://www.markhneedham.com/blog/2014/10/20/python-converting-a-date-string-to-timestamp/">described before</a>:
</p>



~~~python

import calendar
timestamp = calendar.timegm(parser.parse(date).timetuple())

>>> timestamp
1426358599
~~~
