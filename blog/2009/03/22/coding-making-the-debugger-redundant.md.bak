+++
draft = false
date="2009-03-22 19:52:31"
title="Coding: Making the debugger redundant"
tag=['coding', 'tdd', 'debugging', 'erlang']
category=['Coding']
+++

I recently wrote my <a href="http://www.markhneedham.com/blog/2009/03/20/coding-reassessing-what-the-debugger-is-for/">dislike of the debugger</a> and related to this, I spent some time last year watching some videos from JAOO 2007 on <a href="http://channel9.msdn.com/posts/Charles/">MSDN's Channel 9</a>. One of my favourites is an <a href="http://channel9.msdn.com/posts/Charles/JAOO-2007-Joe-Armstrong-On-Erlang-OO-Concurrency-Shared-State-and-the-Future-Part-2/">interview featuring Joe Armstrong and Eric Meijer</a> where Joe Armstrong points out  that when coding Erlang he never has to use a debugger because state is immutable.

In Erlang, once you set the value of a variable 'x' it cannot be changed. Therefore if the value of 'x' is incorrect at some point in your program you only need to look in one place to see why that has happened. 

With imperative languages like Java and C# variables can be set as many times as you like assuming they've not been declared as readonly for example.

It got me thinking about how the way that we can reduce the need to use the Debugger when writing code in imperative languages. Debugging is so boring and takes so long that spending large amounts of doing it both crushes the spirits and slows you down considerably.

<h3>Test Driven Development</h3>

Before I learnt TDD if I had a problem with my code the only way I could really find out more about that problem was to turn to the debugger.

One of the aims of writing code test first is to remove the need to debug. As Pat Kua points out in his blog, when you use a TDD approach to writing code, a nice side effect is that <a href="http://www.thekua.com/atwork/2007/10/test-driven-development-requires-less-debugging/">you tend to stop using the debugger so much</a>.

Doing TDD is not enough though, we want to look to <a href="http://www.markhneedham.com/blog/2009/01/28/tdd-design-tests-for-failure/">design our tests for failure</a> so that they do fail we have a useful error message that helps us work out why something failed rather than having to get out the debugger to work it out. Hamcrest matchers are really useful for this, particularly when it comes to analysing test case failures from a continuous integration tool's console.

Writing our tests in a <a href="http://blog.jayfields.com/2008/11/ubiquitous-assertion-syntax.html">consistent style</a> also helps especially when it comes to setting up mocks and stubs from my experience. If we know how and where these have been setup then we don't need to resort to the debugger to work out why one was or wasn't called - it should be obvious just from reading the test.

<h3>Immutability</h3>

This is an idea which I touched on in a post I wrote around how writing clean OO code can help <a href="http://www.markhneedham.com/blog/2009/03/12/oo-reducing-the-cost-oflots-of-stuff/">reduce the cost of change</a> in our applications, the suffering that having too much mutable state can cause you becoming abundantly clear to me after a coding dojo session where we did <a href="http://www.markhneedham.com/blog/2009/01/30/coding-dojo-8-isola/">just</a> <a href="http://www.markhneedham.com/blog/2009/02/12/coding-dojo-9-refactoring-isola/">that</a>.

Even using the debugger was difficult because we were trying to remember what the state was meant to be compared to how it actually was.

Greg Young has an <a href="http://vimeo.com/3171910">interesting presentation which he gave at a Europe Virtual Alt.NET meeting in February</a> (there is also a <a href="http://www.infoq.com/interviews/greg-young-ddd">similar interview on InfoQ</a>) where he talks about how we can model state transitions explicitly by using command objects rather than implicitly by having domain objects keep track of a lot of internal state. 

He also describes the use of getters/setters as a domain anti-pattern which I would certainly agree with as it results in behaviour being defined away from the data, usually resulting in unexpected state changes in our objects which we can't figure out without getting out the debugger.

<h3>Minimise dependencies</h3>

Ensuring that our classes don't have too many dependencies is another useful approach - <a href="http://codebetter.com/blogs/ian_cooper/archive/2008/12/03/the-fat-controller.aspx">an anti-pattern</a> which tends to happen quite frequently in the controller of the MVC pattern.

When too much is happening in classes they become difficult to understand and by virtue difficult to test, resulting in increased debugger usage because we've probably missed out some paths through the code inadvertently.

When this happens we want to try and pull some of the similar operations out into another controller to make our life easier.

<h3>In Summary</h3>
These are some of the ways that I have noticed help reduce our need to rely on the debugger.

Using TDD as an approach to coding helped me cut down my debugger usage a lot and it is no longer my first choice of tool when there is a problem with code.

I'm sure there are other ways to reduce the need to debug, I just haven't discovered them yet!
