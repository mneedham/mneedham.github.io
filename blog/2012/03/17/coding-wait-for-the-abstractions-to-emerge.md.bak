+++
draft = false
date="2012-03-17 11:19:11"
title="Coding: Wait for the abstractions to emerge"
tag=['software-development']
category=['Software Development']
+++

One of the things that I've learnt while developing code in an incremental way is that the way the code should be designed isn't going to be obvious straight away so we need to be patience and wait for it to emerge.

There's often a tendency to pull out classes or methods but more recently I've been trying to follow an approach where I leave the code in one class/method and play around with/study it until I see a good abstraction to make.

More often than not it takes a few times over multiple days before anything reveals itself. 

I recently watched <a href="https://twitter.com/#!/venkat_s">Venkat Subramaniam's</a> Agile India presentation '<a href="http://www.youtube.com/watch?v=iGsPeR-SYYo&feature=youtu.be">How to Approach Refactoring</a>' in which amongst other bits of advice he suggests that we '<strong>make it work then make it evolve</strong>' which sounds like it's covering the same type of ground.

Sometimes in the rush to abstract code to make it easier to test or to reduce the size of a class we end up creating an abstraction which doesn't really make sense in the business domain.

Having big methods of inline code goes against what we've learnt but putting all the code together makes it much easier to see the real abstractions in the code than if some premature abstractions have been made and we have to remember those as well.

It's still useful to be driven by the goal of pulling out small classes of behaviour/data that are easy to test but <strong>spending a bit more time understanding the domain before doing so seems to work better</strong>.

We recently had some unwieldy code which we couldn't quite work out how to abstract so we left the logic inline until we knew better even though it looked quite messy.

Eventually when talking to one of the subject matter experts they mentioned a term that they used which actually combined two things together which we'd originally thought were independent.

A simple rule of thumb is that if there is no name in the domain for what you're abstracting then it might not make sense to do so. 

It doesn't always work but at least gets your thinking about whether you're improving the code with the abstraction you're about to make!
