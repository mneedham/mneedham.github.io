+++
draft = false
date="2009-12-31 16:08:25"
title="OOP: Behavioural and Structural constraints"
tag=['oop']
category=['OOP']
+++

A few months ago I wrote a post describing how we should <a href="http://www.markhneedham.com/blog/2009/09/02/tdd-test-the-behaviour-rather-than-implementation/">test the behaviour of code rather than the implementation</a> whereby we would write tests against the public API of an object rather than exposing other internal data of the object and testing against that directly.

While I still think this is a useful way of testing code I didn't really have a good definition for what makes that a test of an object's behaviour.

I've been reading through James Odell's '<a href="http://www.amazon.com/gp/product/052164819X?ie=UTF8&tag=marneesblo-20&linkCode=as2&camp=1789&creative=390957&creativeASIN=052164819X">Advanced Object-Oriented Analysis and Design Using UML</a>' and he describes it like so:

<blockquote>
Behavioural constraints limit the way object state changes may occur
</blockquote>

In <a href="http://www.markhneedham.com/blog/2009/12/01/fundamentals-of-object-oriented-design-in-uml-book-review/">Meilir Page-Jones language</a> I think this would describe informative and imperative messages:

<ul>
<li>Informative – a message telling an object about something that happened in the past.</li>
<li>Imperative – a message telling an object to take some action on itself.</li>
</ul>

Both of these types of messages change the state of the object so in C# or Java these would be the public methods on an object that clients interact with.

That seems to describe the way that we would test the object. These would be the methods that we'd call in our test.

Odell goes on to describe structural constraints:

<blockquote>
Structural constraints limit the way objects associate with each other, that is, they restrict object state.
</blockquote>

This seems close to an interrogative message:

<ul>
<li>Interrogative – a message asking an object to reveal something about itself.</li>
</ul>

This would seem closer to the way that we would verify whether the object's state changed as expected. We're querying the object through the structural constraints that have been setup.

I can think of two main reasons why this approach is more effective than just testing directly against the internals of an object:

<ul>
<li>It ensures we're testing something useful otherwise we might be writing tests on our code for a scenario that will never happen.</li>
<li>We have a better idea of when we've finished writing our tests since we know when we've tested all the behaviour.</li>
