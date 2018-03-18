+++
draft = false
date="2009-11-18 17:25:32"
title="Book Club: Working Effectively With Legacy Code - Chapter 9 (Michael Feathers)"
tag=['book-club', 'working-effectively-with-legacy-code']
category=['Book Club']
+++

In our latest technical book club we discussed chapter 9 - 'I Can't Get This Class Into A Test Harness' - of Michael Feather's '<a href="http://www.amazon.com/gp/product/0131177052?ie=UTF8&tag=marneesblo-20&linkCode=as2&camp=1789&creative=390957&creativeASIN=0131177052">Working Effectively With Legacy Code</a>'.

This chapter goes through various problems that we might have getting a class under test and then suggests different techniques to get around those problems.

These are some of my thoughts and our discussion of the chapter:

<ul>
<li>One approach that Feathers describes when dealing with constructors which take in a lot of values is to just <strong>pass in nulls for the parameters that we don't care about</strong>.

While I think this is a useful strategy it's useful to keep in mind that the need to do this is often an indication that the class is doing too much and we probably need to look at breaking that class out into two smaller ones.

Another useful bit of advice Feathers gives is to try and get the code under test instead of discussing all the reasons why we won't be able to do so:

<blockquote>
The best way to see if you will have trouble instantiating a class in a test harness is to just try to do it. Write a test case and attempt to create an object in it. The compiler will tell you what you need to make it really work.
</blockquote>
I think this advice is applicable to most aspects of software development. A lot of time is spent debating approaches when it would be far better just to try something out and see what happens.</li>
<li>Several patterns are described for dealing with singletons in our code and Matt also pointed out the <a href="http://stackoverflow.com/questions/887317/monostate-vs-singleton">mono state pattern</a> which <a href="http://www.objectmentor.com/resources/articles/SingletonAndMonostate.pdf">Uncle Bob outlined</a> as being a step on the way to getting rid of them.</li>
<li>The <a href="http://grabbagoft.blogspot.com/2007/08/legacy-code-testing-techniques-subclass.html">sub class and override pattern</a> is described for handling several of the problems we might encounter. The idea here is to get the code into a position where the code which is making it difficult to test a class is all in one protected method which we can then override in a sub class and replace with a fake/stub version of the method.

I've previously fallen into the trap of thinking that this is a pattern we should be aiming for when designing code from scratch. In particular it seems to happen a lot in ASP.NET MVC controllers when working out how to test code in 'OnActionExecuting' and similar methods.

I now believe it is another indicator that we are too highly coupled to a concrete implementation which has side effects and we might be better off looking for an abstraction that allows us to break that.</li>
<li>Feathers makes another really telling comment towards the end of the chapter when discussing how we use language features to try and enforce certain things in our code:

<blockquote>
In the end, it all comes down to responsible design and coding
</blockquote>
This reminded me of his '<a href="http://www.markhneedham.com/blog/2009/09/30/book-club-design-sense-michael-feathers/">Design Sense</a>' presentation where he covers similar ground and it's very true. No matter what language features we have it's down to us to use them sensibly in the systems we write.
</ul>

