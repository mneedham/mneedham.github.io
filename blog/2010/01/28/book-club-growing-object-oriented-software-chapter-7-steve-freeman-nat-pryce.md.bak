+++
draft = false
date="2010-01-28 19:13:22"
title="Book Club: Growing Object Oriented Software - Chapter 7 (Steve Freeman & Nat Pryce)"
tag=['book-club']
category=['Book Club']
+++

My colleague <a href="http://ilovemartinfowler.com/">David Santoro</a> has started up a technical book club at the client we're working at in Wales and the book choice for the first session was Chapter 7 - Achieving Object Oriented Design - of <a href="http://www.amazon.com/gp/product/0321503627?ie=UTF8&tag=marneesblo-20&linkCode=as2&camp=1789&creative=390957&creativeASIN=0321503627">Growing Object Oriented Software</a>, guided by tests written by Steve Freeman and Nat Pryce.

In this chapter they cover various approaches for driving towards object oriented code including techniques to find new objects and a detailed description of TDD and how we can approach this in a way that allows us to drive out new behaviour effectively.

These are some of my thoughts and our discussion of the chapter:

<ul>
<li>I quite liked the quote that the authors open the chapter with:

<blockquote>
In matters of style, swim with the current; in matters of principle, stand like a rock. 
—Thomas Jefferson
</blockquote>
I think we often end up spending a lot of time <a href="http://www.markhneedham.com/blog/2009/11/04/consistency-in-the-code-base/">arguing about style</a> when a lot of the time keeping to core principles is more important if we're to keep our state in a maintainable state. I suppose it's a bit of an abstract quote but it seems a useful one to keep in mind.
</li>
<li>One suggestion that the authors make is to organise our code into layers - an <strong>implementation layer</strong> where have our different objects (which Martin Fowler refers to as the push button API) and then a <strong>declarative layer</strong> on top of that i.e. a <a href="http://martinfowler.com/dslwip/">domain specific language</a>.

On the projects I've worked on I don't recall us doing this except for in test code where we would often end up writing DSLish code to describe how the application was supposed to work. I suppose this is just a logical next step.
</li>
<li>Somewhat related to this the authors point out that following a TDD approach ensures that we have to specify the 'what' of what we want to achieve before we specify the 'how'. In this case the test describes what we want to achieve and the production code is the implementation of that.

They also emphasise the importance of ensuring our tests are understandable by limiting their scope. From my experience we can often get away with using <a href="http://www.markhneedham.com/blog/2010/01/24/tdd-removing-the-clutter/">very minimal test data</a> in most of our unit tests and if we need to write a lot of setup code for each test then we've probably done something wrong somewhere.

Anwar pointed out that if we're finding it difficult to test what we want to from one level then it can make sense to try and test that from further up the stack. While this is certainly true I think we need to be careful to ensure that we're not just doing that because we don't want to work out how to make our code easier to test further down.</li>

<li>I first realised how useful value objects could be after seeing a <a href="http://www.markhneedham.com/blog/2009/03/15/qcon-london-2009-the-power-of-value-power-use-of-value-objects-in-domain-driven-design-dan-bergh-johnsson/">talk by Dan Bergh Johnsson at QCon in London</a> last year and the authors describe several ways that we can try and get more of these types of objects in our code.



<ul>
<li><strong>Breaking out</strong> - if code's becoming too complicated we might split the responsibility of a large object into several smaller ones. I find that the key here is to focus on making incremental improvements to this type of code. It can often be a big job to get the design of these types of objects as we want them and since we might not get the time to do that, just making the smallest improvement we can think of repeatedly can be quite useful. Having said that I still find it quite difficult to do.</li>
<li><strong>Budding off</strong> - to mark a domain concept in the code we might create an object that wraps a field or has no fields at all. I find this approach is the hardest to introduce as people often see it as adding pointless code when we could just use a primitive instead. This is the area of <a href="http://www.markhneedham.com/blog/2009/03/10/oo-micro-types/">micro types</a> and I think there's probably a measure of judgement required here to determine in which situations we get benefit from taking this approach.</li>
<li><strong>Bundling up</strong> - if we see a group of values being used together then we might bundle them together into a type. I find that it's easier to do this when it's groups of primitives that you're bringing together. I don't find it as easy to spot when groups of objects are being used together and a concept is probably missing.</li>
</ul>
</li>
<li>While I've been doing TDD for a few years now I don't think I've yet totally grasped the idea of pulling interfaces into existence to the extent that the authors describe while writing tests:

<blockquote>
We think of this as “on-demand” design: we “pull” interfaces and their imple- mentations into existence from the needs of the client, rather than “pushing” out the features that we think a class should provide. 
</blockquote>

Liz Keogh refers to this as <a href="http://lizkeogh.com/2009/07/01/pixie-driven-development/">Pixie Driven Development</a> and I think following this approach would help us to end up with meaningful interfaces containing groups of functionality rather than seemingly random groups of methods which seem somewhat related.

It's certainly an area I need to spend more time practicing on.</li>
</ul>
