+++
draft = false
date="2009-12-10 22:14:26"
title="TDD: Big leaps and small steps"
tag=['tdd']
category=['Testing']
+++

About a month ago or so <a href="http://blog.extracheese.org/2009/11/how_i_started_tdd.html">Gary Bernhardt wrote a post showing how to get started with TDD</a> and while the post is quite interesting, several comments on the post pointed out that he had jumped from iteratively solving the problem straight to the solution with his final step.

Something which I've noticed while solving algorithmic problems in couple of different functional programming languages is that the test driven approach doesn't work so well for these types of problems.

Dan North points out something similar in an <a href="http://vimeo.com/7722342">OreDev presentation where he talks about writing a BDD framework in Clojure</a>. 

To paraphrase:

<blockquote>
If you can't explain to me where this approach breaks down then you don't know it well enough. You're trying to sell a silver bullet.

The classic failure mode for iterative development is the big algorithm case. That's about dancing with the code and massaging it until all the test cases pass.
</blockquote>

<a href="http://blog.objectmentor.com/articles/2009/10/08/tdd-triage">Uncle Bob also points this out</a> while referring to the way we develop code around the UI:

<blockquote>
There is a lot of coding that goes into a Velocity template. But to use TDD for those templates would be absurd. The problem is that I’m not at all sure what I want a page to look like. I need the freedom to fiddle around with the formatting and the structure until everything is just the way I want it. Trying to do that fiddling with TDD is futile. Once I have the page the way I like it, then I’ll write some tests that make sure the templates work as written.
</blockquote>

I think the common theme is that TDD works pretty well when we have a rough idea of where we intend to go with the code but we just don't know the exact path yet. We can take <strong>small steps</strong> and incrementally work out exactly how we're going to get there.

When we don't really know how to solve the problem - which more often than not seems to be the case with algorithmic type problems - then at some stage we will take a <strong>big leap</strong> from being nowhere near a working solution to the working solution.

In those cases I think it still makes sense to have some automated tests both to act as regression to ensure we don't break the code and to tell us when we've written the algorithm correctly.

An example of a problem where TDD doesn't work that well is solving the <a href="http://www.markhneedham.com/blog/2009/07/04/coding-dojo-19-groovy-traveling-salesman-variation/">traveling salesman problem</a>.

In this case the solution to the problem is the implementation of an algorithm and it's pretty difficult to get there unless you actually know the algorithm.

During that dojo <a href="http://blog.rufiao.com/">Julio</a> actually spent some time working on the problem a different way - by implementing the algorithm directly - and he managed to get much further than we did.

It seems to me that perhaps this explains why although TDD is a useful design technique it's not the only one that we should look to use.

When we have worked out where we are driving a design then TDD can be quite a useful tool for working incrementally towards that but it's no substitute for taking the time to think about what exactly we're trying to solve.
