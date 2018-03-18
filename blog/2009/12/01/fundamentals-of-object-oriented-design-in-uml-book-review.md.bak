+++
draft = false
date="2009-12-01 23:26:38"
title="Fundamentals of Object-Oriented Design in UML: Book Review"
tag=['books', 'object-orientation']
category=['Books']
+++

One of my favourite recent blog posts is one written by <a href="http://www.codeodor.com/index.cfm/2009/6/17/Strive-for-low-coupling-and-high-cohesion-What-does-that-even-mean/2902">Sammy Larbi on coupling and cohesion</a> and while discussing it with <a href="http://fragmental.tw/">Phil</a> he suggested that I would probably like this book and in particular <a href="http://www.markhneedham.com/blog/2009/10/28/coding-connascence-some-examples/">the chapter on connascence which I've previously written about</a>.

<h3>The Book</h3>

<a href="http://www.amazon.com/gp/product/020169946X?ie=UTF8&tag=marneesblo-20&linkCode=as2&camp=1789&creative=390957&creativeASIN=020169946X">Fundamentals of Object-Oriented Design in UML</a> by Meilir Page-Jones

<h3>The Review</h3>

I really enjoyed reading this book and I think it's one that I could come back and read again to gain something else from in the future.

Nearly all the mistakes that I've made and seen made with respect to the design of object oriented code are outlined in one form or the other in this book.

The book is split into three sections. The first discusses some fairly basic object oriented concepts, the second covers UML as a notation for describing our designs and the final section goes more deeply into the principles of object-oriented design. 

<h4>What did I learn?</h4>

<ul>
<li>Although we don't seem to use UML much these days I was coming to the conclusion while reading those chapters that perhaps UML is useful as a design tool but the aim shouldn't be to come up with a UML diagram, but rather to drive a design in code. 

This is something which <a href="http://blog.objectmentor.com/articles/2009/10/08/tdd-triage">Uncle Bob also touched on recently</a>:

<blockquote>
Is TDD a replacement for design?

No. You still need all your design skills. You still need to know design principles, and design patterns. You should know UML. And, yes, you should create lightweight models of your proposed software designs.
</blockquote>

We actually found on a project I worked on recently that everyone had a different way of diagramming a design and it would have been useful to have a common notation between us. UML is surely the tool to solve that problem.</li>
<li>I quite like the way that Page-Jones describes the <strong>different types of messages</strong> that objects can receive:

<ul><li>Informative - a message telling an object about something that happened in the past.</li>
<li>Interrogative - a message asking an object to reveal something about itself.</li>
<li>Imperative - a message telling an object to take some action on itself.</li>
</ul>

An interrogative message is effectively a getter whereas the other two are commands being sent to the object. I've not seen the distinction between events which happened in the past and those which are going to happen in the immediate future.</li>
<li>I've frequently come across the idea of information hiding when it comes to designing objects but Page-Jones introduces the idea of <strong>implementation hiding</strong> which I think is really neat. 

The idea is that while some information about our object will be viewable to other objects e.g. through attributes/getters, we can still hide the implementation of that information internally so that if we we want to change it in the future then we won't have to change all its clients too.</li>
<li>I found the concept of the <strong>rings of operation</strong> really interesting.  The idea is that there are some methods on our objects which just make use of other methods on the same object. Those methods wouldn't touch any of the fields of an object directly but would rely on those methods in the inner rings to do so.

For example if we have a getter on an object to access a field then if other methods on that object want to access that field they should go via the getter instead of accessing the field directly. 

I often find myself avoiding using getters with the hope that if don't increase their usage then it will be easier to get rid of them in the future. This approach would discourage doing that.</li>
<li>I like the idea of <a href="http://www.markhneedham.com/blog/2009/11/19/two-controllers-type-conformance-and-the-liskov-substitution-principle/">type conformance</a> when it comes to inheritance - we should try to ensure that any sub types adhere to the contract of their parent. 

The other part of this chapter describes '<strong>closed behaviour</strong>' - all the operations on any class that we inherit from should obey our class' invariant. 

I think this can be where we go wrong when <a href="http://www.markhneedham.com/blog/2009/07/24/wrapping-collections-inheritance-vs-composition/">we write classes which extend a List for example</a>. The API of a List will typically have 'Add' and ''Remove' operations but on a lot of the application I work on we only want the 'Add' functionality and not the 'Remove' option. Page Jones suggests that if we want to use inheritance in this situation then we should override methods on the super class to make 'Remove' do nothing. </li>
<li>I now find that I prefer Page Jones definition of cohesion:

<blockquote>
Class cohesion is the measure of interrelatedness of the features (the attributes and operations) located in the external interface of a class</blockquote>

I'm inclined to believe that we might be able to tell how related the features are by looking at the clients of the class and seeing whether they are all using the class in similar ways.

He then outlines three signs that we have cohesion problems with a class:

<ul>
<li>Mixed instance cohesion - a class has some features that are undefined for some objects of the class. I find that this typically happens when we try to make a generic data type to cover everything and then try to jam any variations on the type into the same definition. It is typically solved by pulling out another class. This is the worst type of cohesion.</li>
<li>Mixed domain cohesion - a class contains an element that directly couples the class with another class that is unrelated domain wise. This typically happens when we mix infrastructure code into our domain code.</li>
<li>Mixed role cohesion - a class contains an element that couples it with an unrelated class in the same domain. I think this is the most typical type of cohesion that I've seen and the main problem is that we end up with classes which have multiple roles which makes them difficult to change.</li>
</ul>
</ul>

<h3>In Summary</h3>
There's way more in this book than I could ever hope to cover here but these are some of the interesting bits that stood out from this reading of it. I'm pretty sure that I'll come back to this one in the future.

While reading the book I had the feeling that some of the ideas are quite similar to those in Domain Driven Design and since this book was published it contributes to my belief that <a href="http://www.markhneedham.com/blog/2008/09/20/similarities-between-domain-driven-design-object-oriented-programming/">a lot of DDD is covered by just doing OOP well</a>.

Overall this is a really good book, worth reading.
