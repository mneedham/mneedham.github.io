+++
draft = false
date="2009-12-19 00:55:19"
title="Coding: An outside in observation"
tag=['coding']
category=['Coding']
+++

I've been reading <a href="http://cacm.acm.org/magazines/2009/5/24646-api-design-matters">Michl Henning's post on API design</a> and one thing which he points out is that it's important to drive the design of an API based on the way that it will be used by its clients:

<blockquote>
A great way to get usable APIs is to let the customer (namely, the caller) write the function signature, and to give that signature to a programmer to implement. This step alone eliminates at least half of poor APIs: too often, the implementers of APIs never use their own creations, with disastrous consequences for usability
</blockquote>

This is similar to <a href="http://butunclebob.com/ArticleS.MichaelFeathers.TheGoldenRuleOfApiDesign">Michael Feathers' Golden Rule of API Design</a>:

<blockquote>
It's not enough to write tests for an API you develop, you have to write unit tests for code that uses your API.

When you do, you learn first-hand the hurdles that your users will have to overcome when they try to test their code independently
</blockquote>

When we don't do this we start guessing how we think things might be used and we end up with generic solutions which solve many potential use cases in an average to poor way and none of them in a good way.

Henning goes on to say:

<blockquote>
There are many ways to "pass the buck" when designing an API. A favorite way is to be afraid of setting policy: "Well, the caller might want to do this or that, and I can't be sure which, so I'll make it configurable." The typical outcome of this approach is functions that take five or 10 parameters. Because the designer does not have the spine to set policy and be clear about what the API should and should not do, the API ends up with far more complexity than necessary.
</blockquote>

What I found interesting while thinking about this is that the underlying idea is to <strong>drive the design from the outside in</strong> which is quite a popular approach in several different areas of software development.

<h4>Consumer Driven Contracts</h4>

My colleague Ian Robinson came up with the idea of <a href="http://martinfowler.com/articles/consumerDrivenContracts.html">consumer driven contracts</a> for describing an effective way for service providers and consumers to work together. 

The idea here is that since the consumer is going to be using the service they should have more say on its design i.e. the contract is designed with the end use in sight rather than the provider just coming up with something and throwing it over the fence to its consumers who then have to deal with whatever they've been given.

<h4>Test Driven Development/Behaviour Driven Development</h4>

While not the only way that we can drive design from the outside in, test driven development is quite a useful way of achieving this when we do it well.

We might typically start out by writing a functional test to describe the functionality that we're about to create and then move down to smaller more targeted unit tests to drive out the functionality.

This approach helps ensure that we only write the code that we need to write to satisfy the bit of functionality being added and from my experience the APIs tend to be more usable than when we just write code without considering how it will be used.

This is similar to what Liz Keogh describes in her '<a href="http://lizkeogh.com/2009/07/01/pixie-driven-development/">Pixie driven development</a>' post where she describes how to use a behaviour driven approach to implement functionality.

<h4>Functional Programming</h4>
I've been playing around with a couple of functional languages for about a year now and I nearly always find that I start out with the high level function and then work out which other functions I need to help me solve the problem at hand.

I can't think of a better way to write functional code than this. On a few occasions I've started writing functions without keeping the end in sight and whenever I do this I seem to end up throwing away the functions because they don't contribute to the overall problem I'm trying to solve.
