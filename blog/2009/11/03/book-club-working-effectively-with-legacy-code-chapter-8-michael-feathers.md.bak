+++
draft = false
date="2009-11-03 00:16:32"
title="Book Club: Working Effectively With Legacy Code - Chapter 8 (Michael Feathers)"
tag=['book-club']
category=['Book Club']
+++

In our latest technical book club we discussed chapter 8 - 'How do I add a feature?' - of Michael Feather's '<a href="http://www.amazon.co.uk/Working-Effectively-Legacy-Robert-Martin/dp/0131177052/ref=sr_1_1?ie=UTF8&s=books&qid=1257168892&sr=8-1">Working Effectively With Legacy Code</a>'.

This chapter covers Test Driven Development and a technique I hadn't come across before called <a href="http://www.springerlink.com/content/f87155k53852761j/">Programming By Difference</a>.

These are some of my thoughts and our discussion of the chapter:

<ul>
<li>In the section on TDD Feathers mentions the <a href="http://www.markhneedham.com/blog/2009/10/31/coding-copypaste-then-refactor/">copy/paste/refactor pattern</a> which I wrote about a few days ago. <a href="http://camswords.wordpress.com/">Cam</a> pointed out that this technique allows us to get to the green bar more quickly after which we can decide how to clean up the code. It seems like perhaps this could be added to Kent Beck's 'Green Bar Patterns' that he describes in '<a href="http://www.markhneedham.com/blog/2008/10/07/test-driven-development-by-example-book-review/">Test Driven Development by Example</a>'.

I've noticed a few times recently that delaying our desire to remove duplication until we can properly see where the duplication lies might be a better strategy than prematurely removing duplication and creating a meaningless abstraction which can be difficult to remove.</li>
<li>From the examples in the book, <strong>programming by difference</strong> is used to describe an approach where we create a sub class and override some aspect of the super class. It allows us to quickly add new features although it does increase the complexity of the system since we have to add a new class to achieve this.  

The next step after this is to refactor the code into a state where the new class' behaviour is moved elsewhere or the new class is shaped into something that makes more sense.

Feathers also points out that while programming by difference may initially lead to our code being in worse shape it can also allow us to see new abstractions which we can then work towards. </li>
<li>I like the term '<strong>normalised hierarchy</strong>' with respect to the way that we create inheritance hierarchies. Feathers suggests that we should look to create a hierarchy where no class has more than one implementation of a method. i.e. <a href="http://www.markhneedham.com/blog/2009/05/06/c-using-virtual-leads-to-confusion/">if a class has a concrete implementation of a method then that shouldn't be overriden</a>.</li>
<li>Towards the end of the chapter Feathers asks whether it is overkill to create a particular class which is just acting like a properties collection at the time. We discussed this and Cam pointed out that we seem to either end up with 'complex interactions and simple objects' or 'more complicated objects and simple interactions'.

From my observations it seems that <a href="http://www.markhneedham.com/blog/2009/10/23/coding-the-primitive-obsession/">we err on the side of not creating enough objects</a> but <a href="http://blogs.agilefaqs.com/2009/10/26/goodbye-simplicity-im-object-obsessed/">as Naresh Jain points out it is possible to go too far the other way and end up creating objects just for the sake of it</a>. </li>
</ul>

Michael Feathers recently linked to a paper titled '<a href="http://bit.ly/1gFXr6">Testable Java</a>' that he's currently working on which covers some of the ideas from the book but with examples in Java. Worth a look.
