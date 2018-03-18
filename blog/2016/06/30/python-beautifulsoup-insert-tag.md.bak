+++
draft = false
date="2016-06-30 21:28:35"
title="Python: BeautifulSoup - Insert tag"
tag=['python']
category=['Python']
+++

<p>
I've been scraping the Game of Thrones wiki in preparation <a href="http://www.meetup.com/Women-Who-Code-London/events/231014802/">for a meetup at Women Who Code next week</a> and while attempting to extract character allegiances I wanted to insert missing line breaks to separate different allegiances.
</p>


<p>
I initially tried <a href="http://stackoverflow.com/questions/14652706/python-beautifulsoup-add-tags-around-found-keyword">creating a line break</a> like this:
</p>



~~~python

>>> from bs4 import BeautifulSoup
>>> tag = BeautifulSoup("<br />", "html.parser")
>>> tag
<br/>
~~~

<p>
It looks like it should work but later on in my script I check the 'name' attribute to work out whether I've got a line break and it doesn't return the value I expected it to:
</p>



~~~python

>>> tag.name
u'[document]'
~~~

<p>
My script assumes it's going to return the string 'br' so I needed another way of creating the tag. The following does the trick:
</p>



~~~python

>>> from bs4 import Tag
>>> tag = Tag(name = "br")
>>> tag
<br></br>
~~~


~~~python

>>> tag.name
'br'
~~~

<p>
That's all for now, back to scraping for me!
</p>

