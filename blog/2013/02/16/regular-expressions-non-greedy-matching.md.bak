+++
draft = false
date="2013-02-16 12:17:49"
title="Regular Expressions: Non greedy matching"
tag=['regular-expressions']
category=['Software Development']
+++

<p>I was playing around with some football data earlier in the week and I wanted to try and extract just the name 'Rooney' from the following bit of text:</p>



~~~text

Rooney 8′, 27′
~~~

<p>My initial regular expression was the following which annoyingly captures the time of the first goal:</p>



~~~ruby

> "Rooney 8′, 27′".match(/(.*)\s\d(.*)/)[1]
=> "Rooney 8,"
~~~

<p>It works fine if the player has only scored one goal…</p>



~~~ruby

> "Rooney 8′".match(/(.*)\s\d(.*)/)[1]
=> "Rooney"
~~~

<p>...but since the second part of the regex ("\s\d(.*)") appears twice only the last instance of it is matched and the rest of the text gets captured by the first part of the regex.</p>


<p>One way around this is to make the first part of the regex <a href="http://robertpyke.blogspot.co.uk/2009/02/ruby-regex-non-greedy-operator-using_05.html">non greedy/lazy</a> so that it will make as little as possible rather than as much as possible.</p>


<p>We can do that by using the lazy version of '*' which is '*?':</p>



~~~ruby

> "Rooney 8′, 27′".match(/(.*?)\s\d(.*)/)[1]
=> "Rooney"
~~~

<p>Of course you could also argue that I'm being very lazy by using ".*" in the first place and you probably have a point! The following more explicit regular expression achieves the same thing:</p>



~~~ruby

> "Rooney 8′, 27′".match(/([A-Za-z\s-]+)\s\d(.*)/)[1]
=> "Rooney"
~~~

<p>As a side note I find that when I'm playing around with regular expressions it really makes sense to have a bunch of test cases that I can run after each change to make sure I haven't inadvertently broken everything.</p>


<p><a href="http://www.regexper.com/">regexper.com</a> is also really helpful for visualising what the regular expression is actually doing!</p>

