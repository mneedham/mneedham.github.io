+++
draft = false
date="2009-05-21 19:05:26"
title="Coding Dojo #15: Smalltalk"
tag=['coding-dojo', 'smalltalk']
category=['Coding Dojo']
+++

We decided to play around with Smalltalk a bit in our latest coding dojo.

A lot of the ideas that I value the most in terms of writing software effectively seem to have originally come from the Smalltalk community and a colleague of mine has been reading Kent Beck's <a href="http://www.markhneedham.com/blog/2008/10/07/test-driven-development-by-example-book-review/">TDD by Example book</a> and was really keen to try out the language to see where Kent's original ideas came from.

<h3>The Format</h3>

We only had 2/3 people for the dojo this week so we all spent a bit of time at the keyboard getting familiar with the way things worked. We  projected to a wide screen television	 so the other guys could track what was doing on.

<h3>What We Learnt</h3>

<ul>
<li>One interesting thing for me was that the <strong>Smalltalk syntax reminded me a little bit of Ruby</strong>. We spent a little bit of time with irb open as well as the Smalltalk environment and compared what the code would look like for a few simple expressions in the different languages. Ruby seemed a little bit easier to understand for some of the expressions but I guess it has probably been influenced syntax wise by Smalltalk.

To give a simple example that we tried out, this is how you'd print the values 1-10 to the screen:

In Smalltalk:

~~~smalltalk

1 to: 10 do: [:i | Transcript cr; show: (i printString)].
~~~

In Ruby:

~~~ruby

(1..10).each { |i| puts i }
~~~

</li>

<li>We were following a <a href="http://objectsroot.com/squeak/squeak_tutorial-2.html#ss2.2">simple introduction to Squeak</a>, an open source implementation of Smalltalk. We were actually using <a href="http://www.cincomsmalltalk.com/scripts/DownloadInstaller.ssp">Visual Works/Cincom Smalltalk</a> which seems to differ a little bit. For example there was no 'asString' method on integer when we tried to execute the following bit of code:


~~~smalltalk

Transcript show: (1 asString)
~~~

It leads to the error:


~~~text

Unhandled exception: Message not understood: #asString
~~~

Instead we needed to use 'printString like this:


~~~smalltalk

Transcript show: (1 printString)
~~~
I'm sure there are probably some other differences but we only tried a few examples at the dojo.
</li>
<li>The idea of the <strong>development environment being the same as the environment where the code runs</strong> was quite strange for me but we saw some benefits of it even in the small amount of code we wrote. On making one of our many syntax errors the IDE popped up with a message asking whether we wanted to debug that piece of code on the fly. Pretty cool if we'd understood the stack trace that followed a bit better!
<li>I haven't looked into the type systems of other languages that closely but I was quite surprised that looking the type of the value '1' was 'SmallInteger' - it was <strong>much more strongly typed than I had expected</strong>. The ability to delve into the code of objects within the environment is really cool and we came across quite a bit of code which intrigued us to want to learn more.</li>
<li>
The intention for this session wasn't actually to learn Smalltalk the language, as I don't think dojos are great for doing that, but rather to try and <strong>understand the concepts behind all expressions being about sending a message to an object</strong> which for me is what object orientation is all about.

Chatting with <a href="http://twitter.com/davcamer">Dave</a> about object oriented design he spoke highly of Smalltalk as being the language where he learnt a lot about this and a couple of colleagues have said the same thing as well.</li>
</ul>

<h3>For next time</h3>

<ul>
<li>We just about got started with writing a little bit of Smalltalk code this week but next week I'd quite like to see if we can write a little application using Smalltalk. We're particularly keen on working out how unit testing fits into the picture and it'd be quite cool to play around with <a href="http://www.seaside.st/">seaside</a> a bit as well.</li>
<li>Smalltalk is quite renowned for its <a href="http://www.refactory.com/RefactoringBrowser/">refactoring browser</a> so we're quite keen to play around with that a bit and see what its like compared to some of the features available in IDEs nowadays</li>
</ul>
