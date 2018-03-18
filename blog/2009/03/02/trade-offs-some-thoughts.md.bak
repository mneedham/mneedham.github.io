+++
draft = false
date="2009-03-02 23:01:11"
title="Trade Offs: Some Thoughts"
tag=['software-development', 'domain-driven-design', 'trade-offs', 'mapping']
category=['Software Development']
+++

As we know with software development with pretty much every decision we make or technology we choose there is a trade off that goes with making this choice as compared with choosing an alternative.

I first learnt this when working with <a href="http://www.oshineye.com/">Ade</a> a couple of years ago and while I know it to be true, I had come to believe that some practices are just non-negotiable and we should look to apply them judiciously wherever possible.

Various conversations have made me come to the realisation that not everyone believes this and that there are trade offs being made by following or not following these practices.

<h3>Domain Driven Design Ubiquitous Language</h3>
I consider this approach to writing software to be absolutely key to ensuring that the code base is easy to navigate around for newcomers  and indeed to anyone who has to read the code after we have written it.

The trade off we are making here is that sometimes we will end up writing more code in designing our code around the language of the business rather than choosing a solution which may be technically easier to implement but less expressive.

To take a simple example of this in action, consider <a href="http://www.norwichunion.com/car-insurance/">car insurance</a>. 

As a customer I would provide the insurer with details about my car, where I live and so on. This information would lead to me being provided with a <strong>Quote</strong>. Should I then decide to buy that Quote it would become a <strong>Policy</strong>. There is clearly quite an important difference between the two terms but in terms of data, maybe 75% is the same across both concepts. 

If we decide to implement the language of the business in our code then we may end up creating a new object and copying a lot of data across from the old one. 

The benefit we get from doing this is that the code is more expressive and describes the business process more accurately.

<h3>Interacting with other systems</h3>

My thoughts when it comes to using data from other systems is that we should look to keep interaction with the other system in one place - inside the <a href="http://moffdub.wordpress.com/2008/09/21/anatomy-of-an-anti-corruption-layer-part-1/">anti corruption layer</a>.

The benefit of doing this is that we keep control over our model and similar (but not exactly the same) concepts from other systems don't creep into our application and lead to confusion around our domain model.

The disadvantage is that we may end up writing a lot of mapping code depending on how closely the other systems' models are to our own. This code tends to be extremely tedious to write and difficult to test in a way that doesn't involved re-creating most of the production code logic in our tests to create our expectations.

<h3>Object Oriented Programming</h3>
I have had the opportunity recently to work <a href="http://pilchardfriendly.blogspot.com/">with</a> <a href="http://twitter.com/davcamer">several</a> <a href="http://blog.m.artins.net/">people</a> who really know how to write code in this way and I've found it to be the most effective way to manage complexity in code that I've come across so far.

I've a long way to go before I've mastered OOP, but I try to follow the <a href="http://www.lostechies.com/blogs/chad_myers/archive/2008/03/07/pablo-s-topic-of-the-month-march-solid-principles.aspx">SOLID principles</a> as much as possible - keeping classes small, behaviour with data and so on. - and I think it helps to make code much easier to understand and indeed change.

Now the trade off is that it is much harder to write code in this way than to just write procedural code and create <a href="http://martinfowler.com/bliki/AnemicDomainModel.html">anaemic objects</a> which just have getters and setters on them. It also requires much more thinking - we have to think where to put behaviour, how to name new classes and so on.

Therefore I could easily see an argument that it's quicker to write code procedurally than in an object oriented way. If we take this approach though we have to be prepared for the time we lose later on when it comes to trying to change the code that we were able to write so quickly before - it will probably take much longer now.

<h3>In Summary</h3>
I still believe that there is a lot of value in these approaches but it's always good to know what alternative approach is being discarded by choosing a particular approach.

That way we can make more informed decisions.
