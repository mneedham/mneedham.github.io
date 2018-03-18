+++
draft = false
date="2009-12-03 16:27:29"
title="Book Club: Working Effectively With Legacy Code - Chapter 11 (Michael Feathers)"
tag=['book-club']
category=['Book Club']
+++

In our latest technical book club we discussed chapter 11 - 'I Need to Make a Change. What Methods Should I Test?' - of Michael Feathers' '<a href="http://www.amazon.com/gp/product/0131177052?ie=UTF8&tag=marneesblo-20&linkCode=as2&camp=1789&creative=390957&creativeASIN=0131177052">Working Effectively With Legacy Code</a>'.

In this chapter Feathers covers some techniques which allow us to work out which parts of the code we need to write tests around when we make changes.

These are some of my thoughts and our discussion of the chapter:

<ul>
<li>Feathers starts off the chapter by introducing the idea of <strong>effect sketching</strong> which I've been trying out recently both on the projects I've been working on and with the <a href="http://www.markhneedham.com/blog/2009/11/04/reading-code-unity/">Unity dependency injection container</a>. 

The idea is that we create a diagram which shows the effect that changing different fields and methods will have on the rest of the class and then based on this we can see where we need to create a safety net of tests for any given change.

It seems like this type of diagram would also be quite useful for identifying when a class has more than one responsibility because you would end up with several mini unconnected effect sketches within the main one.</li>
<li>Feathers suggests that we should look to write <strong>characterisation tests</strong> around legacy code. These are written a little differently to TDD's tests because we make the assertion match what the code is currently doing. The idea is to document what the system is doing now. We might come across 'bugs' while doing this but we wouldn't necessarily change the tests to verify how the code 'should' be until we find out what the effect of doing that would be.

We want to write enough of these tests that we feel confident that we have a good enough safety net to allow us to change the code.</li>
<li>There are some interesting ideas about encapsulation towards the end of the chapter where Feathers considers the <strong>trade off between ensuring test coverage and encapsulation</strong>.

<blockquote>Breaking encapsulation can make reasoning about our code harder, but it can make it easier if we end up with good explanatory tests afterward.

...

Encapsulation and test coverage aren't always at odds, but when they are, I bias towards test coverage. Often it can help me get more encapsulation later.

Encapsulation isn't an end in itself; it is a tool for understanding.</blockquote>
I find this is sometimes quite a big barrier to break down because people are often reluctant to change code to make it more testable. That's sometimes a valid concern but with legacy code not so much.</li>
</ul>
