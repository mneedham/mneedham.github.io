+++
draft = false
date="2009-03-20 21:39:56"
title="Coding: Reassessing what the debugger is for"
tag=['coding']
category=['Coding']
+++

When I first started programming in a 'proper' IDE one of the things that I thought was really cool was the ability to debug through my code whenever something wasn't working quite the way I expected it to.

Now the debugger is not a completely pointless tool - indeed there is sometimes no other easy way to work out what's going wrong - but I think it now becomes the default problem solver whenever a bit of code is not working as we expect it to.

Admittedly the name '<a href="http://www.answers.com/debugger">debugger</a>' doesn't really help us here as the name describes a tool that "helps in locating and correcting programming errors" which is all well and good but I think <strong>it should be one of the last tools that we turn to rather than one of the first</strong>.

<h3>Why?</h3>

From my experience I have found the debugger to be a <strong>very slow</strong> way of diagnosing, fixing and then ensuring that bugs don't come back into my code again.

No doubt some people are experts at setting up the breakpoints and getting the debugger to step to exactly the right place and locating the problem, but even when we've done that we don't have a way of ensuring it doesn't reoccur unless we go and write an example/test that exposes it.

Another problem I have come across when debugging through code is that the code can sometimes act differently when we slow down its speed of execution, meaning that the bug we  see without the debugger is <strong>not necessarily repeatable</strong> with it.


<h3>When using the debugger is reasonable</h3>

Despite my dislike of the debugger there are certainly occasions where it is very useful and superior to alternative approaches.

<strong>Tracing problems in framework or 3rd party code</strong> is one of those occasions. For example we were recently getting an error a few levels inside the ASP.NET MVC code and didn't have a good idea of why it was happening.

Going through the code for 20 minutes or so with the debugger turned out to be a very useful exercise and we were able to find the problem and then change what we were doing so it didn't reoccur.

Another time when it is useful is when we have <strong>code on another server</strong> that isn't working - hooking in a remote debugger is very useful for discovering problems which may or may not be related to the fact that the environment the code is running under there is slightly different to our local one.

<h3>Alternatives</h3>

One of the most ironic cases I have seen of what I consider debugger misuse is using it to debug through a test failure as soon as it fails!

A key benefit of writing tests is that it should stop the need to use the debugger so something has gone a bit wrong if we're using the debugger in this case.

The typical situation is when there has been a null pointer exception somewhere and we want to work out why that's happened. The debugger is rarely the best choice for doing that.

It is usually quite easy to work out just from reading the error message we get from our testing framework where the problem is, and if it's not then we should look at writing our tests in a way that is <a href="http://www.markhneedham.com/blog/2009/01/28/tdd-design-tests-for-failure/">more conducive for solving these types of problems</a>.

An approach I recently learnt for <strong>narrowing down test failures</strong> is to use the <a href="http://www.markhneedham.com/blog/2008/11/21/saff-squeeze-first-thoughts/">Saff Squeeze</a>. By using this approach we look to reduce the areas in our code where the failure is happening until we find the exact location. We can then put a test around this to ensure it doesn't happen again.

It's definitely more difficult to do this than to just get out the debugger but I think we get greater insight into areas of our code that aren't well tested and we can also tighten up our tests while doing so.  

Another approach while I have certainly overlooked in the past is <strong>looking at the logs</strong> to see what's going on. If we are using logging effectively then it should have recorded the information needed to help us diagnose the problem quickly. 

<h3>In Summary</h3>
Of course these approaches may not work out for us sometimes in which case I have no problem with getting out the debugger.

Taking time to think whether we actually need to do so or if another approach might be better is certainly a valuable thing to do though.
