+++
draft = false
date="2015-07-15 06:20:07"
title="Python: UnicodeDecodeError: 'ascii' codec can't decode byte 0xe2 in position 0: ordinal not in range(128)"
tag=['python']
category=['Python']
+++

<p>
I was recently doing some text scrubbing and had difficulty working out how to remove the '†' character from strings.
</p>


<p>e.g. I had a string like this:</p>



~~~python

>>> u'foo †'
u'foo \u2020'
~~~

<p>I wanted to get rid of the '†' character and then strip any trailing spaces so I'd end up with the string 'foo'. I tried to do this in one call to 'replace':</p>



~~~python

>>> u'foo †'.replace(" †", "")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
UnicodeDecodeError: 'ascii' codec can't decode byte 0xe2 in position 1: ordinal not in range(128)
~~~

<p>
It took me a while to work out that "† " was being treated as ASCII rather than UTF-8. Let's fix that:
</p>



~~~python

>>> u'foo †'.replace(u' †', "")
u'foo'
~~~

<p>
I think the following call to <cite>unicode</cite>, which I've <a href="http://www.markhneedham.com/blog/2015/05/21/python-unicodeencodeerror-ascii-codec-cant-encode-character-uxfc-in-position-11-ordinal-not-in-range128/">written about before</a>, is equivalent:
</p>



~~~python

>>> u'foo †'.replace(unicode(' †', "utf-8"), "")
u'foo'
~~~

<p>
Now back to the scrubbing!
</p>

