+++
draft = false
date="2014-06-08 01:34:03"
title="Ruby: Regex - Matching the Trademark ™ character"
tag=['ruby']
category=['Ruby']
+++

<p>I've been <a href="http://gist.neo4j.org/?6e24a3bb09766e62b0b1">playing around with some World Cup data</a> and while cleaning up the data I wanted to strip out the year and host country for a world cup.</p>


<p>I started with a string like this which I was reading from a file:</p>



~~~text

1930 FIFA World Cup Uruguay ™
~~~

<p>And I wanted to be able to extract just the 'Uruguay' bit without getting the trademark or the space preceding it. I initially tried the following to match all parts of the line and extract my bit:</p>



~~~ruby

p text.match(/\d{4} FIFA World Cup (.*?) ™/)[1]
~~~

<p>Unfortunately that doesn't actually compile:</p>



~~~text

tm.rb:4: syntax error, unexpected $end, expecting ')'
p text.match(/\d{4} FIFA World Cup (.*?) ™/)[1]
                                           ^
~~~

<p>I was initially able to work around the problem by <a href="http://books.google.co.uk/books?id=0Msuh5Vq-uYC&pg=PT102&lpg=PT102&dq=ruby+regex+trademark+character&source=bl&ots=fIXwQaJOaK&sig=hH8mmjxhHGe8iyvXT0CakRv8Ods&hl=en&sa=X&ei=_1aTU_aGGcWcyAScuYCYDQ&ved=0CCYQ6AEwAA#v=onepage&q=ruby%20regex%20trademark%20character&f=false">matching the unicode code point</a> instead:</p>



~~~text

p text.match(/\d{4} FIFA World Cup (.*?) \u2122/)[1]
~~~

<p>While working on this blog post I also remembered that you can <a href="http://stackoverflow.com/questions/1739836/invalid-multibyte-char-us-ascii-with-rails-and-ruby-1-9">specify the character set of your Ruby file</a> and by default it's ASCII which would explain why it doesn't like the ™ character.</p>
 

<p>If we add the following line at the top of the file then we can happily use the ™ character in our regex:</p>



~~~ruby

# encoding: utf-8
# ...
p text.match(/\d{4} FIFA World Cup (.*?) ™/)[1]
# returns "Uruguay"
~~~

<p>This post therefore ends up being more of a reminder for future Mark when he comes across this problem again having forgotten about Ruby character sets!</p>

