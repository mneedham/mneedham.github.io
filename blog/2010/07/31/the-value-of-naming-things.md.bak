+++
draft = false
date="2010-07-31 07:05:52"
title="The value of naming things"
tag=['software-development']
category=['Software Development']
+++

<a href="http://twitter.com/hyfather">Nikhil</a> and I were discussing some of the ideas around Test Driven Development earlier in the week and at one stage I pointed out that I quite liked Bryan Liles' idea of '<a href="http://aac2009.confreaks.com/07-feb-2009-13-30-tatft-the-laymans-guide-bryan-liles.html">make it pass or change the message</a>'.

Bryan suggests that when we have a failing test our next step should be to make that test pass or at least write some code which results in us getting a different error message and hopefully one step closer to making the test pass.

As I described this to Nikhil he pointed out that this is probably what most people are doing anyway and now the technique just has a name.

I think this is probably a fair assessment but then again I find it very useful when people give a name to common techniques/patterns as it <strong>makes them much easier to talk about</strong> without having to fill in a whole load of context.

For example <a href="http://www.markhneedham.com/blog/2010/07/05/the-limited-red-society-joshua-kerievsky/">Joshua Kerievsky has come up with some names to describe incremental refactoring techniques</a> such as parallel change and narrowed change.

Parallel change describes a technique where we want to change a method signature but don't want to break all the clients of that method by directly changing it.

Instead we create the new method alongside the current one and gradually move the clients to call the new one instead. When they've all moved we can delete the original method.

Narrowed change describes a technique where we try to reduce the number of places where we have to make the change we want to make.

It's much easier to use the vocabulary that Kerievsky has come up with than to have to describe the techniques each time!

However I do think it is possible to go too far with naming things to the point that there are actually so many names that it's incredibly difficult to remember them all.

<a href="http://xunitpatterns.com/">xUnit Patterns</a> seems like an example of this to me.

There are an incredible number of patterns described in that book and while they do all describe slightly different scenarios I'm not necessarily convinced that having this many different patterns makes our discussions easier.

Overall though I think having names for common patterns in software development is a good thing and it does add value even though it seems like we've just 'given something a name'.
