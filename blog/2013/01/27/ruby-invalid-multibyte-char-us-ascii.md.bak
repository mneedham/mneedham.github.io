+++
draft = false
date="2013-01-27 15:14:01"
title="Ruby: invalid multibyte char (US-ASCII)"
tag=['ruby']
category=['Ruby']
+++

<p>I've used Ruby on and off for the last few years but somehow had never come across the following error which we got last week while attempting to print out a currency value:</p>


<cite>blah.ruby</cite>

~~~ruby

amount = "£10.00"
puts amount
~~~


~~~text

$ ruby blah.ruby 
blah.ruby:1: invalid multibyte char (US-ASCII)
blah.ruby:1: invalid multibyte char (US-ASCII)
~~~

<p>Luckily my pair <a href="http://www.linkedin.com/profile/view?id=13286237">Jae</a> had come across this before and showed me <a href="http://blog.grayproductions.net/articles/ruby_19s_three_default_encodings">a blog post which explains what's going on and how to sort it out</a>.</p>


<p>It turns out that since Ruby 1.9 we need to explicitly specify which encoding we want to use for strings otherwise it will default to US-ASCII in my case at least.</p>


<p>We can get around this by explicitly telling the interpreter that we want to use UTF-8 encoding by including the following comment at the top of our file:</p>



~~~ruby

# encoding: UTF-8
amount = "£10.00"
puts amount
~~~

<p>Then when we interpret the file this time:</p>



~~~text

$ ruby blah.ruby 
£10.00
~~~

<p>Since we were only editing one file it made sense to just set the comment manually but if we need to do that in a more widespread way then we'd want to use the <a href="https://github.com/m-ryan/magic_encoding">magic_encoding gem</a>.</p>


<p>Yehuda Katz also wrote a post a few years ago <a href="http://yehudakatz.com/2010/05/05/ruby-1-9-encodings-a-primer-and-the-solution-for-rails/">explaining all things encoding in more detail</a>.</p>

