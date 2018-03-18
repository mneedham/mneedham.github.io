+++
draft = false
date="2009-07-04 10:17:31"
title="Domain Driven Design: Conformist"
tag=['domain-driven-design']
category=['Domain Driven Design']
+++

Something which constantly surprises me about <a href="http://domaindrivendesign.org/">Domain Driven Design</a> is how there is a pattern described in the book for just about every possible situation you find yourself in when coding on projects.

A lot of these patterns appear in the 'Strategic Design' section of the book and one which is very relevant for the project I'm currently working on is the 'Conformist' pattern which is described like so:

<blockquote>
When two development teams have an upstream/downstream relationship in which the upstream has no motivation to provide for the downstream team's needs, the downstream team is helpless. Altruism may motivate upstream developers to make promises, but they are unlikely to be fulfilled. Belief in those good intentions leads the downstream team to make plans based on features that will never be available. The downstream project will be delayed until the team ultimately learns to live with what it is given. An interface tailored to the needs of the downstream team is not in the cards.
</blockquote>

We are working on the front end of an application which interacts with some services to get and save the data from the website.

We realised that we had a situation similar to this originally but didn't know that it was the conformist pattern and our original approach was to rely completely on the model in the service layer to the extent that we were mapping directly from SOAP calls to WCF message objects and then passing these around the code - I originally described this as being an <a href="http://www.markhneedham.com/blog/2008/12/28/internalexternal-domain-models/">externally defined domain model</a>.

This led to quite a lot of pain as whenever there was a change in the service layer model our code base broke all over the place and we then ended up spending most of the day fire fighting - we were too tightly coupled to an external system.

At this stage we were reading Domain Driven Design in our <a href="http://www.markhneedham.com/blog/2009/01/25/learning-alone-or-learning-together/">Technical Book Club</a> and I was fairly convinced that what we really needed to do was have our own model and create an anti corruption layer to translate between the service layer model and the new model that we would create.

We changed our code to follow this approach and created <a href="http://www.markhneedham.com/blog/2009/03/10/ddd-repository-not-only-for-databases/">repositories</a> and mappers which were the main places in our code base where we cared about this external dependency and although the isolation of the end point has worked much better we never really ended up with a rich domain model that really represented the business domain.

We had something in between the service layer model and the real business model which didn't really help anyone and meant we ended up spending a lot of time trying to translate between the different definitions that were floating around. 

Writing the code for the anti corruption layer also takes a lot of time, <a href="http://www.markhneedham.com/blog/2009/04/02/tdd-testing-mapping-code/">is quite frustrating/tedious</a> and it was hard to see the value we were getting from doing so.

We've now reached the stage where we know this is the case and that it probably makes much more sense to just accept it and to not spend any more time trying to create our own model but instead just adapt what we have to more closely match the model we get from the services layer.

We will still keep a thin mapping layer as this gives us some protection against changes that may happen in the service layer.

I think a key thing for me here is that it's really easy <a href="http://www.markhneedham.com/blog/2009/03/30/ddd-recognising-relationships-between-bounded-contexts/">to be in denial</a> about what is actually happening since what you really want is to be in control of your own domain model and design it so that it closely matches the business so that they would be able to read and understand your code if they wanted to. Sometimes that isn't the case.

Chatting with Dave about this he suggested that a lesson for us here is that it's important to <strong>know which pattern you are following</strong> which <a href="http://twitter.com/AndyPalmer/statuses/2434721277">Andy Palmer also pointed out on twitter</a>.  
