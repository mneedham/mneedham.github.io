+++
draft = false
date="2009-01-30 11:16:27"
title="TDD: Test DRYness"
tag=['tdd', 'testing']
category=['Testing']
+++

I had a discussion recently with <a href="http://fabiopereira.me/blog/">Fabio</a> about <a href="http://c2.com/cgi/wiki?DontRepeatYourself">DRY</a>ness in our tests and how we don't tend to adhere to this principal as often in test code as in production code. 

I think certainly some of the reason for this is that we don't take as much care of our test code as we do production code but for me at least some of it is down to the fact that if we make our tests <a href="http://dannorth.net/2008/06/let-your-examples-flow">too DRY then they become very difficult to read</a> and perhaps more importantly, very difficult to <a href="http://www.markhneedham.com/blog/2009/01/28/tdd-design-tests-for-failure/">debug when there is a failure</a>.

There seem to be different types of DRYness that weave themselves into our test code which result in our code becoming more difficult to read.

<h3>Suboptimal DRYness</h3>

<h4>Setup method</h4>
Putting code into a setup method is the most common way to reduce duplication in our tests but I don't think this is necessarily the best way to do it.

The problem is that we end up increasing the context required to understand what a test does such that the reader needs to read/scroll around the test class a lot more to work out what is going on. This problem becomes especially obvious when we put mock expectations into our setup method. 

One of those expectations becomes unnecessary in one of our tests and not only is it not obvious why the test has failed but we also have a bit of a refactoring job to move the expectations out and only into the tests that rely on them.

<h4>Helper methods with more than one responsibility</h4>
Extracting repeated code into helper methods is good practice but going too far and putting too much code into these methods defeats the purpose.

One of the most common ways that this is violated is when we have methods which <strong>create the object under test but also define some expectations on that object's dependencies in the same method</strong>.

This violates the idea of having intention revealing method names as well as making it difficult to identify the reason for test failures when they happen.

<h4>Assertions</h4>
I tend to follow the  <a href="http://www.lostechies.com/blogs/jimmy_bogard/archive/2008/07/24/arrange-act-assert-and-bdd-specifications.aspx">Arrange, Act, Assert</a> approach to designing tests whereby the last section of the test asserts whether or not the code under test acted as expected.

I'm not yet convinced that following the DRY approach is beneficial here because it means that you need to do more work to understand why a test is failing. 

On the other hand if assertions are pulled out into an intention revealing method then the gain in readability might level out the extra time it takes to click through to a failing assertion.

My favourite approach to test assertions is to use behavioral style assertions

e.g. 

~~~csharp

stringValue.ShouldEqual("someString") 
~~~

...and I don't think applying the DRY principle here, if we have a lot of similar assertions, adds a lot of value.

<h3>DRY and expressive</h3>

I'm not against DRYness in tests, I think it's a good thing as long as we go about it in a way that still keeps the code expressive.

<h4>Test data setup</h4>
The setup and use of test data is certainly an area where we don't gain an awful lot by having duplication in our tests. If anything having duplication merely leads to clutter and doesn't make the tests any easier to read.

I have found the <a href="http://www.markhneedham.com/blog/2009/01/21/c-builder-pattern-still-useful-for-test-data/">builder pattern</a> to be very useful for creating clutter free test data where you only specifically define the data that you care about for your test and default the rest.

<h4>Single responsibility helper methods</h4>

If we decide that extracting code into a helper method increases the readability of a test then the key for is to ensure that these helper methods only do one thing otherwise it becomes much more difficult to understand what's going on.

My current thinking is that we should aim for having only one statement per method where possible so that we can skim through these helper methods quickly without having to spend too much time working out what's going on.

An idea Dan North talks about (and which is nicely illustrated in <a href="http://www.lindsaar.net/2008/6/24/tip-24-being-clever-in-specs-is-for-dummies">this blog post</a>) is putting these helper methods just before the test which makes use of them. I haven't tried this out yet but it seems like a neat way of making the code more DRY and more readable.

<h3>In Summary</h3>

I've noticed recently that I don't tend to read test names as often as I used to so I'm looking to the test code to be expressive enough that I can quickly understand what is going on just from scanning the test.

Keeping the code as simple as possible, extracting method when it makes sense and removing clutter are some useful steps on the way to achieving this.
