+++
draft = false
date="2010-06-28 08:39:10"
title="Intuition and 'quit thinking and look'"
tag=['software-development']
category=['Software Development']
+++

Something which <a href="http://twitter.com/dermotkilroy">Dermot</a>, <a href="http://twitter.com/christianralph">Christian</a> and I noticed last week is that on our project we've reached the stage where we intuitively know what the underlying problem is for any given error message in the application we're working on.

We're pretty much at the stage where we're effectively pattern matching what's going on without needing to think that much anymore.

This is a good thing because it saves a lot of time analysing every single message to try and work out what's going on - I think this means that we've reached a higher level of the <a href="http://www.markhneedham.com/blog/2009/08/10/dreyfus-model-more-thoughts/">Dreyfus model</a> when it comes to this particular situation.

The problem with getting too used to this approach is that eventually we'll come across a problem that we haven't come across before and if we don't recognise that this is the case we'll end up getting very frustrated.

I had the chance to work with <a href="http://www.oshineye.com/">Ade Oshineye</a> a few years ago and he always encouraged me to "<strong>quit thinking and look</strong>" when it came to problem solving.

This idea is derived from a book titled '<a href="http://www.amazon.com/exec/obidos/ASIN/0814474578/debuggingrule-20">9 indispensable rules of debugging</a>' and the thinking behind it is that we often go straight to the solution for a problem without spending the time to understand what the problem actually is.

We actually came across a situation like this recently while investigating a problem in production.

We were getting an exception which looked pretty similar to other problems that we'd seen previously so we immediately tried that solution without any further investigation.

It had no impact at all so we had to go back and actually look at the error message we were receiving before trying something else.

As it turned out the time we wasted picking the wrong solution was less than 30 seconds but I think we had got to the point where a bit of <strong>complacency had crept in</strong> and we believed that there weren't any ways the application could go wrong that we hadn't seen before.

Talking further about this with Dermot he pointed out that this situation was akin to discovering an unknown unknown i.e. we came across a problem that we didn't know we didn't know about since we thought we knew about all of them!

Errol Morris wrote <a href="http://opinionator.blogs.nytimes.com/2010/06/20/the-anosognosics-dilemma-1/?hp">an interesting article about this recently in the New York Times</a> in which  referenced Dunning and Kruger's paper '<a href="http://en.wikipedia.org/wiki/Dunning%E2%80%93Kruger_effect">Unskilled and Unaware of It: How Difficulties of Recognizing One’s Own Incompetence Lead to Inflated Self-assessments</a>'.

The learning for me from this is that while intuition is very useful it's also important to at least be aware that we probably don't know everything and that we may well come across new situations and will have to approach them as a novice again.
