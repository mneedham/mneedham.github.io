+++
draft = false
date="2010-01-25 22:06:23"
title="TDD: Rewriting/refactoring tests"
tag=['tdd']
category=['Testing']
+++

I've read several times about the dangers of <a href="http://chadfowler.com/2006/12/27/the-big-rewrite">the</a> <a href="http://blog.objectmentor.com/articles/2009/01/09/the-big-redesign-in-the-sky">big</a> <a href="http://www.magpiebrain.com/2010/01/10/the-great-rewrite/">rewrite</a> when it comes to production code but I've recently been wondering whether or not we should apply the same rules when it comes to test code or not.

I worked with <a href="http://raphscallion.com/blog/">Raphael Speyer</a> for a few weeks last year and on the code base we were working on he often spent some time rewriting tests originally written using <a href="http://rmock.sourceforge.net/">rMock</a> to use <a href="http://mockito.org/">mockito</a> which was the framework we were driving towards. 

One of the benefits that he was able to get from doing this was that he had to understand the test in order to change it which enabled him to increase his understanding of how the code was supposed to work and identify anything that didn't seem quite right.

I quite liked this idea at the time and while spending some time recently working with some tests which required quite a lot of setup and were testing several different things in the same test. 

Unfortunately a few of them were failing and it was quite difficult to work out why that was.

My initial approach was to try and work my way through the tests inlining all the test code to start with and then <a href="http://www.markhneedham.com/blog/2010/01/24/tdd-removing-the-clutter/">extracting out irrelevant details</a> to make the tests easier to understand. 

Despite those attempts I was unable to work out why the test was failing so I worked out what the main things the test was trying to verify and then wrote tests from scratch for each of those cases.

I was able to write tests covering everything the original test did in several smaller tests in less time than I had spent trying to debug the original one and with a fair degree of confidence that I'm testing exactly the same thing.

As I see it the big danger of rewriting is that we're always playing catch up with the current system which is still being worked on in production and we never quite catch up.

I'm not so sure this logic applies in this case because we're only rewriting small bits of code which means that we can replace the original test very quickly. 

My main driver when working with tests is to ensure that they're <strong>easy to understand</strong> and make it <strong>easy to reason about the code</strong> so if I have to rewrite some tests to make that happen then I think it's a fair trade off.

My initial approach would nearly always be to refactor the tests that are already there. Rewriting is something I'd look to do if I was really struggling to refactor effectively.
