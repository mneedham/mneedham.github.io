+++
draft = false
date="2012-03-29 06:45:59"
title="Readability/Performance"
tag=['software-development']
category=['Software Development']
+++

I recently read the <a href="http://www.aosabook.org/en/graphite.html">Graphite chapter</a> of <a href="http://www.aosabook.org/en/index.html">The Architecture of Open Source Applications</a> book which mostly tells the story of how Chris Davis incrementally built out <a href="http://graphite.wikidot.com/">Graphite</a> - a pretty cool tool that can be used to do real time graphing of metrics.

The whole chapter is a very good read but I found the design reflections especially interesting:

<blockquote>
One of Graphite's greatest strengths and greatest weaknesses is the fact that very little of it was actually "designed" in the traditional sense. [It] evolved gradually, hurdle by hurdle, as problems arose. Many times the hurdles were foreseeable and various pre-emptive solutions seemed natural. However <strong>it can be useful to avoid solving problems you do not actually have yet, even if it seems likely that you soon will</strong>.
</blockquote>

One of the main success criteria of the application that I'm currently working on is its performance - it doesn't have millisecond-ish latency requirements but it does need to do a lot of calculations and return within a reasonable amount of time.

Several times we've been working on a bit of code and have written something which is <strong>easy to read but runs in quadratic time</strong> because we have a nested iteration over a collection.

Having this performance requirement in mind has made us think twice about whether we should be looking for a better way of writing that code but that would seem to be a premature optimisation since we don't actually know that this bit of code is going to be the bottleneck.

Instead we've started to put a performance testing infrastructure in place so that we can actually <a href="https://github.com/codahale/metrics">gather some data</a> that tells us where the problems in the code are.

Davis goes on to state the following in his article:

<blockquote>
The reason is that you can learn much more from closely studying actual failures than from theorizing about superior strategies. Problem solving is driven by both the empirical data we have at hand and our own knowledge and intuition. I've found that doubting your own wisdom sufficiently can force you to look at your empirical data more thoroughly.
</blockquote>

As I <a href="http://www.markhneedham.com/blog/2012/03/28/testing-trying-not-to-overdo-it/">mentioned in my last post</a> the main logic in our application involves loading a bunch of data from Oracle and then processing various calculations on it.

At the moment we're getting sub second responses from most requests and where that isn't the case the bottleneck has been in one of our database queries rather than in the code.

Maybe eventually we'll want to optimise those bits of code which have quadratic running time and the good thing is that we've abstracted those bits of code so we could optimise that code with minimal impact to the rest of the code base.

I've been working through <a href="http://www.algo-class.org">Algo Class</a> and one of the things that I've learnt is that you only really see problems with algorithms of quadratic running time if you are iterating through really big collections - otherwise it's barely noticeable.

In our case the collections will probably be small so we unlikely to see that problem. 

On the other hand we are likely to be repeating the same calculations multiple times so we will probably look to add some caching if that starts to become a problem.

Of course when we do that we'll need to check our performance tests before and after the change to ensure that we've actually addressed a real problem rather than theorised about it!

For now though we're continuing to write our code in the way that is most readable/easy to understand and waiting for our performance tests to force us to change that approach.

-----

I've not worked closely on anything which had proprietary trading style latency requirements so if your experience is different please let me know in the comments.
