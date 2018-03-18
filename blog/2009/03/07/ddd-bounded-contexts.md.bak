+++
draft = false
date="2009-03-07 10:03:38"
title="DDD: Bounded Contexts"
tag=['domain-driven-design']
category=['Domain Driven Design']
+++

I've been reading Casey Charlton's <a href="http://dddstepbystep.com/">excellent series of posts on Domain Driven Design</a> recently and today came across his thoughts about <a href="http://devlicio.us/blogs/casey/archive/2009/02/18/ddd-what-kind-of-applications-is-it-suited-to.aspx">which types of applications Domain Driven Design is suited to</a>.

Towards the end of the post he talks about the fact that there is a lot of excellent ideas in Domain Driven Design even if you don't have the chance to use all of them.

<blockquote>
...there is a wealth of wisdom and experience encapsulated in Domain Driven Design – use what you think applies to your situation, and you will find your software becoming more flexible, more reactive to your audience, and easier to understand – just don’t expect miracles, and beware of over complicating your code for the sake of it – sometimes simpler really is better.
</blockquote>

A pattern which I think is applicable in the majority of systems is <a href="http://devlicio.us/blogs/casey/archive/2009/02/11/ddd-bounded-contexts.aspx">bounded context</a> - if I remember correctly this isn't mentioned in <a href="http://www.infoq.com/minibooks/domain-driven-design-quickly">InfoQ's Domain Driven Quickly book</a> but is extensively covered in the <a href="http://www.amazon.com/Domain-Driven-Design-Tackling-Complexity-Software/dp/0321125215">big blue book</a>.

To quote the book with regards to what a <a href="http://domaindrivendesign.org/discussion/messageboardarchive/BoundedContext.html">bounded context</a> is:

<blockquote>
The delimited applicability of a particular model. BOUNDING CONTEXTS gives team members a clear and shared understanding of what has to be consistent and what can develop independently.
</blockquote>

This means that a given model which we define is only valid in a specific part of our system. We would then have a layer of mapping between this bounded context and other parts of the system.

I've found this to be a really useful pattern to help reduce complexity where our application has integration end points. It makes it significantly easier to understand the code as you don't need to keep all the context of what terms mean in other systems.

One thing that we discussed in our Domain Driven Design book club last week is that there are actually <strong>bounded contexts within the application itself as well as within the system</strong> as a whole.

For example if our application has a back-end database then that represents a relational model of the data in our system - that representation doesn't make sense in other parts of the system and would typically be encapsulated from our code with the help of an ORM - the ORM effectively acting as an <a href="http://www.joeydotnet.com/blog/archive/2007/09/10/building-the-often-needed-anti-corruption-layer.aspx">anti corruption layer</a> between the database and our domain model. 

I think we can also apply this with regards to the model we use on our user interfaces - often the model we display to our users differs from the one that makes sense to the business.

The only disadvantage of creating all these different bounded contexts is that we need to create mapping code between each of them, a job which can be pretty tedious at times. 

On the other hand I think the advantages we get from having clearly defined areas where our various models are valid easily outweigh this in most cases.
