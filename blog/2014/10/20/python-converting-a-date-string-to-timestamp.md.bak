+++
draft = false
date="2014-10-20 15:53:51"
title="Python: Converting a date string to timestamp"
tag=['python']
category=['Python']
+++

<p>I've been playing around with Python over the last few days while cleaning up a data set and one thing I wanted to do was translate date strings into a timestamp.</p>


<p>I started with a date in this format:</p>



~~~python

date_text = "13SEP2014"
~~~

<p>So the first step is to translate that into a Python date - the <a href="https://docs.python.org/2/library/datetime.html#strftime-strptime-behavior">strftime section of the documentation</a> is useful for figuring out which format code is needed:</p>



~~~python

import datetime

date_text = "13SEP2014"
date = datetime.datetime.strptime(date_text, "%d%b%Y")

print(date)
~~~


~~~bash

$ python dates.py
2014-09-13 00:00:00
~~~

<p>The next step was to translate that to a UNIX timestamp. I thought there might be a method or property on the Date object that I could access but I couldn't find one and so ended up using <a href="https://docs.python.org/2/library/calendar.html#calendar.timegm">calendar</a> to do the transformation:</p>



~~~python

import datetime
import calendar

date_text = "13SEP2014"
date = datetime.datetime.strptime(date_text, "%d%b%Y")

print(date)
print(calendar.timegm(date.utctimetuple()))
~~~


~~~text

$ python dates.py
2014-09-13 00:00:00
1410566400
~~~

<p>It's not too tricky so hopefully I shall remember next time.</p>

