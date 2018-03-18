+++
draft = false
date="2009-11-24 23:31:25"
title="Book Club: Working Effectively With Legacy Code - Chapter 10 (Michael Feathers)"
tag=['book-club']
category=['Book Club']
+++

In our latest technical book club we discussed chapter 10 - 'I Can't Run This Method in a Test Harness' - of Michael Feather's '<a href="http://www.amazon.com/gp/product/0131177052?ie=UTF8&tag=marneesblo-20&linkCode=as2&camp=1789&creative=390957&creativeASIN=0131177052">Working Effectively With Legacy Code</a>'.

In this chapter Feathers outlines some of the problems we might have getting methods under test and then suggests some ways to get around those problems.

These are some of my thoughts and our discussion of the chapter:

<ul>
<li>I quite like the idea of pragmatic refactoring that Feathers suggests early on in the chapter:

<blockquote>Ideally, it would be great to break it down into smaller classes, but we have to carefully consider whether we want to do that much refactoring right now. It would be great to do it, but whether we can depends on where we are in our release cycle, how much time we have, and all the associated risks.</blockquote>
I think it's important to understand when hacking code in is going to hurt us and quite often I think the side effects of taking this approach are underestimated.

<a href="http://watchitlater.com/blog/">Tom</a> spoke of '<strong>value fetishism</strong>' whereby we get so caught up trying to add 'business value' that we forget to keep the code in good stead for future work.

I quite like the analogy that Alistair Cockburn uses of <a href="http://alistair.cockburn.us/Software+development+as+a+cooperative+game">software development as a series of cooperative gamem</a> and I think it's sometimes easy to forget in the rush to get some code out for a release that we have to make sure that we don't make our lives impossible for the next game/release by rushing code in without paying due attention.</li>
<li>Feathers spends some time suggesting how we can <strong>test private methods</strong> - one way is to <a href="http://www.markhneedham.com/blog/2009/11/10/legacy-code-sensing/">change the method to be public</a>. There are a couple of reasons why we might not want to do that: <ul>
<li>The method is just a utility and isn't something that clients would care about. We have therefore made our API more noisy</li>
<li>If a client calls the method then it could have an adverse affect on the results of other methods in the class</li></ul>
The cleanest solution for that second point is to move those methods out into their own class where we could test against them directly. A smaller step to take is to make the method protected and then create a test version of the class from which we can call the protected method directly.

Feathers also talks about the danger of using reflection to allow us to test this kind of code - it might allow us to get tests around the code but we're not making the code any better and we may not notice quite how bad the code has got. We are just delaying the inevitable.

There's a tool in .NET land called <a href="http://learn.typemock.com/">TypeMock</a> which allows you to test pretty much anything but I wonder whether we would run into the same problems that Feathers describes above.</li>
<li>I quite liked the <a href="http://svengrand.blogspot.com/2008/05/new-xunit-test-pattern.html">skin and wrap the API pattern</a> whereby we create our own interface for a tricky dependency. We then refer to the interface in our code instead of the concrete dependency and have a class which just delegates to the real dependency. We did this when trying to <a href="http://www.markhneedham.com/blog/2008/09/17/testing-file-system-operations/">test file operations</a> on a project I worked on a couple of years ago.</li>
</ul>
