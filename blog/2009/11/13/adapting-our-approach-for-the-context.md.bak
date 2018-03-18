+++
draft = false
date="2009-11-13 06:34:00"
title="Adapting our approach for the context"
tag=['software-development']
category=['Software Development']
+++

Amongst the many posts written recently about unit testing one which I quite liked was <a href="http://fallenrogue.com/post/234250827/re-its-ok-not-to-unit-test-or-what-you-do-on-your">written by fallenrogue</a> where he describes how in different contexts/cultures a different approach is favoured which means a technique like TDD might not work so well.

cashto, the guy who wrote <a href="http://blogs.msdn.com/cashto/archive/2009/03/31/it-s-ok-not-to-write-unit-tests.aspx">the original post</a>, agrees with this in the comments on that post:

<blockquote>
Absolutely right. I write apps on mobile devices in C++. What works for me may not work well for someone who designs websites with RoR, and vice versa. Context definitely matters -- it was one of the points I was trying to get across.
</blockquote>

Recently I've started noticing that it's quite beneficial to <a href="http://www.markhneedham.com/blog/2009/10/05/my-software-development-journey-year-3-4/">consider the context</a> that we're working in for all sorts of approaches we might want to take.

<h3>Immutability</h3>

When I was first playing around with <a href="http://www.markhneedham.com/blog/category/dotnet/f-dotnet/">F#</a> I liked the idea of having everything in the code being immutable and I decided that it would be interesting to try and apply that idea to the code I wrote in C# on the project I was working on.

Unfortunately it didn't work out as well as I'd hoped because it requires more code to do that, it's not really idiomatic C# so it was confusing to my colleagues and we ended up having objects hanging around which weren't updated with the latest state changes because I'd forgotten to re-assign the variable to the new instance.

I still think that we could probably make more use of <a href="http://www.markhneedham.com/blog/2009/03/15/qcon-london-2009-the-power-of-value-power-use-of-value-objects-in-domain-driven-design-dan-bergh-johnsson/">value objects</a> in our code but I'm not convinced that aiming for immutability everywhere when using C# is the way to go.

If it was a different context such as a problem we were trying to solve in Haskell or to a lesser extent F# then it would make perfect sense.

<h3>Confidence changing code</h3>

Another example of this is the confidence that we can have in making changes to the code base.

I've worked on projects where there's been a lot of test coverage across the board and also ones where there wasn't.

With the latter we'd have to put some time in to get tests around that code before thinking about making big changes.

If we don't have the time to do that then we need to be quite careful when changing code since we don't have a quick feedback mechanism to let us know whether we've broken anything or not.

<h3>Final thoughts</h3>

<a href="http://programmingtour.blogspot.com/2009/10/on-term-pragmatic.html">Corey Haines wrote a post on pragmatism</a> about a month ago where he suggested the following:

<blockquote>
Often times, people use the term 'pragmatic' as a way to hide a lack of skill and experience. Or, sometimes, it is used in ignorance: someone doesn't realize that they don't understand something well enough. Usually, though, it is brought to play when someone is justifying cutting corners on something.
</blockquote>

I think this applies when deciding that an approach isn't useful in our context. We need to be careful that we're not just making excuses for our lack of skill in that area.

When I first started working professionally in software development I was fairly convinced that there would be an optimal approach to take in every situation that I just didn't know about yet.

A few years later I've come across a lot of really good approaches to solving problems but no approach that is applicable across the board.
