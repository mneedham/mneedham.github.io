+++
draft = false
date="2009-05-23 15:37:34"
title="Coding: Setters reduce trust"
tag=['coding', 'setters']
category=['Coding']
+++

I've written previously about my dislike of the way the <a href="http://www.markhneedham.com/blog/2009/02/16/c-object-initializer-and-the-horse-shoe/">object initialiser is misused in C# 3.0</a> and although I've also written about my preference for <a href="http://www.markhneedham.com/blog/2009/02/28/coding-implicit-vs-explicit-modeling/">explicit modeling</a> and the need for <a href="http://www.markhneedham.com/blog/2009/03/04/coding-good-citizens/">objects to act as good citizens </a>I've never quite been able to articulate what it is I dislike so much about having setter methods on objects. 

I've learnt from experience that it leads to a world of pain in our code by having the ability to setup an object after construction using setters and in a conversation with a colleague about this last week he suggested that the reason it's such a bad practice to follow is that <strong>it makes us lose our trust in not only that object but in all the other objects in the application</strong>.

The thinking here is that if we get caught out (usually by a null pointer exception) when using an object which wasn't completely set up at construction then we are likely to have a seed of doubt in our mind when we come across another object as to whether the same pattern has been followed with that one - we've lost a little bit of our belief that we can just use this object and it will work the way we expect it to.

As a result of that loss of trust we end up spending more time looking at more implementation details of an object just to check how it has been designed to ensure that we don't get caught out.

I don't think this is a particularly useful way to spend our time and it also adds another thing that we have to keep in our mind when looking at code, further dragging us away from the task that we originally intended to do.

Apart from when we're creating <a href="http://www.martinfowler.com/bliki/FluentInterface.html">fluent interface</a> style DSLs I've always felt more pain from using setters than I've gained from that so when I don't see a good reason for them - sometimes Java frameworks might need them (thanks <a href="http://dahliabock.wordpress.com/">Dahlia</a>!) - to exist I pretty much follow <a href="http://groups.google.com/group/software_craftsmanship/browse_thread/thread/da5e9c019b559062?pli=1">the boy scout rule</a> and try and get rid of them.
