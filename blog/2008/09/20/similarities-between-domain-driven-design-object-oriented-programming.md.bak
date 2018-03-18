+++
draft = false
date="2008-09-20 13:12:25"
title="Similarities between Domain Driven Design & Object Oriented Programming"
tag=['oop', 'altnetuk', 'ddd', 'eric-evans']
category=['Domain Driven Design', 'OOP']
+++

At the <a href="http://altnetuk.com/">Alt.NET UK Conference</a> which I <a href="http://www.markhneedham.com/blog/2008/09/14/altnet-uk-conference-20/">attended</a> over the weekend it occurred to me while listening to some of the discussions on <a href="http://domaindrivendesign.org/books/">Domain Driven Design</a> that a lot of the ideas in DDD are actually very similar to those being practiced in <a href="http://en.wikipedia.org/wiki/Object-oriented_programming">Object Oriented Programming</a> and related best practices.

<h3>The similarities</h3>
<h4>Anaemic Domain Model/Law of Demeter</h4>

There was quite a bit of discussion in the  session about <a href="http://www.martinfowler.com/bliki/AnemicDomainModel.html">anaemic domain models</a>.

An anaemic domain model is one where a lot of the objects are merely data holders and do not actually have any behaviour inside them. While it has a fancy name, in OO terms this problem materialises due to our failure to adhere to the <a href="http://en.wikipedia.org/wiki/Law_of_Demeter">Law of Demeter</a>. 

My colleague Dan Manges has a <a href="http://www.dcmanges.com/blog/37">brilliant post</a> describing this principle but a tell tale sign is that if you see code like the following in your code base then you're probably breaking it.


~~~csharp

object.GetSomething().GetSomethingElse().GetSomethingElse()
~~~

This is often referred to as train wreck code and comes from breaking the idea of <a href="http://www.pragmaticprogrammer.com/articles/tell-dont-ask">Tell Don't Ask</a>. In essence we should not be asking an object for its data and then performing operations on that data, we should be telling the object what we want it to do.

<h4>Side Effect Free Functions/Command Query Separation</h4>

DDD talks about <a href="http://domaindrivendesign.org/discussion/messageboardarchive/SideEffectFreeFunctions.html">side effect free functions</a> which are described as follows:

<blockquote>
An operation that computes and returns a result without observable side effects
...
The developer calling an operation must understand its implementation and the implementation of all its delegations in order to anticipate the result.
</blockquote>

My colleague <a href="http://blog.kriskemper.com/2008/08/06/another-best-practice-command-query-separation/">Kris Kemper talks about</a> a very similar OOP best practice called <a href="http://www.martinfowler.com/bliki/CommandQuerySeparation.html">command query separation</a>. From <a href="http://www.martinfowler.com/bliki/CommandQuerySeparation.html">Martin Fowler's</a> description:

<blockquote>
The really valuable idea in this principle is that it's extremely handy if you can clearly separate methods that change state from those that don't. This is because you can use queries in many situations with much more confidence, introducing them anywhere, changing their order. 
</blockquote>

It's not exactly the same but they have a shared intention - helping to make the code read more intuitively so that we can understand what it does without having to read all of the implementation details.

<h4>Intention Revealing Interfaces/Meaningful Naming</h4>

<a href="http://domaindrivendesign.org/discussion/messageboardarchive/IntentionRevealingInterfaces.html">Intention Revealing Interfaces</a> describe a similar concept to Side Effect Free Functions although they address it slightly differently:

<blockquote>
A design in which the names of classes, methods, and other elements convey both the original developer's purpose in creating them and their value to a client developer.
...
If a developer must consider the implementation of a component in order to use it, the value of encapsulation is lost.
</blockquote>

In OOP this would be described as using meaningful names as detailed in Uncle Bob's <a href="http://www.amazon.co.uk/Clean-Code-Handbook-Software-Craftsmanship/dp/0132350882/ref=sr_1_1?ie=UTF8&s=books&qid=1221745437&sr=8-1">Clean Code</a> (<a href="http://www.markhneedham.com/blog/2008/09/05/the-productive-programmer-book-review/">my review</a>). 

<h4>Bounded Context/Clean Boundaries</h4>

DDD's <a href="http://domaindrivendesign.org/discussion/messageboardarchive/BoundedContext.html">bounded context</a> describes "The delimited applicability of a particular model" i.e. the context in which is is held valid.

This is quite closely related to the idea of clean boundaries in Clean Code where Uncle Bob states:

<blockquote>
Code at the boundaries needs clear separation and tests that define expectations
</blockquote>

In both cases we are creating an explicit separation of 'our code' from the outside world so to speak. We want to clearly define where 'our world' ends by defining the interfaces with which we interact with the outside world.

<h4>Anti Corruption Layer/Wrappers</h4>

The <a href="http://domaindrivendesign.org/discussion/messageboardarchive/AnticorruptionLayer.html">anti corruption layer</a> in DDD is  "an isolating layer to provide clients with functionality in terms of their own domain model." 

It is used to create a boundary for our bounded context so that the models of other systems we interact with doesn't creep into our system.

This is implemented in OO using one of the <a href="http://en.wikipedia.org/wiki/Wrapper_pattern">wrapper patterns</a>. Examples of these are the <a href="http://en.wikipedia.org/wiki/Facade_pattern">Facade</a>, <a href="http://en.wikipedia.org/wiki/Adapter_pattern">Adapter</a>, or <a href="http://martinfowler.com/eaaCatalog/gateway.html">Gateway</a> pattern which all solve the problem in slightly different ways. 

The intention in all cases is to have one area of our code which calls 3rd party libraries and shields the rest of the code from them. 

<h3>Domain Driven Design = Object Oriented Programming + Ubiquitous Language?</h3>

While talking through some of these ideas I started to come to the conclusion that maybe the ideas that DDD describe are in fact very similar to those that OOP originally set out to describe.

The bit that DDD gives us which has perhaps been forgotten in OOP over time is describing the interactions in our systems in terms of the business problem which we are trying to solve i.e. the <a href="http://domaindrivendesign.org/discussion/messageboardarchive/UbiquitousLanguage.html">Ubiquitous Language</a>.

From Wikipedia's Object Oriented Programming entry:

<blockquote>
OOP can be used to translate from real-world phenomena to program elements (and vice versa). OOP was even invented for the purpose of physical modeling in the Simula-67 programming language.
</blockquote>

The second idea of physical modeling  seems to have got lost somewhere along the way and we often end up with code that describes a problem at a very low level. Instead of describing a business process we describe the technical solution to it. You can be writing OO code and still not have your objects representing the terms that the business uses.

There are some things that DDD has certainly made clearer than OOP has managed. Certainly the first part of the book which talks about building a business driven Domain Model is something which we don't pay enough attention to when using OOP. 

For me personally before I read the concepts of DDD I would derive a model that I thought worked and then rarely go back and re-look at it to see if it was actually accurate. Reading DDD has made me aware that this is vital otherwise you eventually end up translating between what the code says and what the business says.

Ideas around maintaining model integrity are also an area I don't think would necessarily be covered in OOP although some of the implementations use OOP ideas so they are not that dissimilar.

<h3>Why the dismissal of DDD?</h3>

The reason I decided to explore the similarities between these two concepts wasn't to dismiss Domain Driven Design - I think the framework it has given us for describing good software design is very useful. 

Clearly I have not mapped every single DDD concept to an equivalent in OOP. I think DDD has given a name or term to some things that we may just take for granted in OOP. Certainly the DDD ideas expressed around the design of our model are all good OOP techniques that may not be explicitly stated anywhere.

I wanted to point out these similarities as I feel it can help to reduce the fear of adopting a new concept if we know it has some things in common with what we already know - if a developer knows how to write OO code and knows design concepts very well then the likelihood is that the leap to DDD will not actually be that great. 

It would be really good if we could get to the stage where when we teach the concepts of OOP we can do so in a way that emphasises that the objects we create should be closely linked to the business domain and are not just arbitrary choices made by the developers on the team.

Maybe the greatest thing about DDD is that it has brought all these ideas together in one place and made them more visible to practitioners.

I am very interested in how different things overlap, what we can learn from these intersections and what things they have in common. It's not about the name of the concept for me, but learning what the best way to deliver software and then to maintain that software after it has been delivered.
