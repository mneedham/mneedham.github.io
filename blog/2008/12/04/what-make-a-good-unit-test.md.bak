+++
draft = false
date="2008-12-04 00:31:29"
title="What makes a good unit test?"
tag=['tdd', 'testing', 'unit-test']
category=['Testing']
+++

Following on from my post around the <a href="http://www.markhneedham.com/blog/2008/10/10/what-is-a-unit-test/">definition of a unit test</a>, a recent discussion on the <a href="http://www.nabble.com/Test-Driven-Development-f17142.html">Test Driven Development mailing list</a> led me to question what my own approach is for writing unit tests.

To self quote from my previous post:

<blockquote>
A well written unit test in my book should be simple to understand and run quickly. 
</blockquote>

Quite simple in theory but as I have learnt (and am still learning) the hard way, much harder to do in practice. Breaking that down further what does it actually mean?

<h3>Intention revealing name</h3>
There was some discussion a few months ago with regards to whether test names were actual valuable, but as the majority of my work has been in Java or C# I think it is very important.

I favour <a href="http://www.markhneedham.com/blog/2008/10/10/what-is-a-unit-test/">BDD style test names</a> which describe the behaviour of what we are testing rather than the implementation details. For me naming the tests in this way allows people who look at the test in future to question whether it is a valid test as well as whether it is actually doing what it claims to be doing.

<h3>No clutter</h3>
If we can keep tests short and to the point they are much easier for the next person to read.

To achieve this we need to ensure that we keep the code in the test method to the minimum, including putting object setup code into another method so that it doesn't clutter the test and only setting the expectations that we care about if we are using a mocking framework. 

This is made much easier by the <a href="http://ayende.com/Blog/archive/2008/05/16/Rhino-Mocks--Arrange-Act-Assert-Syntax.aspx">Arrange-Act-Assert</a> approach being followed by mocking frameworks nowadays. I think this approach maps quite nicely to the Given-When-Then BDD syntax as a nice way of defining our tests or examples in BDD land.

<h3>Don't remove all duplication</h3>
While removing duplication from code is generally a good thing I don't think we should apply the DRY principle too judiciously on test code.

As <a href="http://fragmental.tw/2008/07/02/domain-driven-tests/">Phil points out</a> this can make tests very difficult to read and understand. I tend to favour test expressiveness over removing all duplication.

<h3>One behaviour per test</h3>
I used to try and follow the idea of having only one assertion per test but Sczcepan's idea of <a href="http://monkeyisland.pl/2008/01/31/10rules/">testing one behaviour per class</a> is much better.

This is one part of writing tests where we should stick to the <a href="http://en.wikipedia.org/wiki/Single_responsibility_principle">Single Responsibility Principle</a> in as far as not overloading the test with assertions which then make it more difficult to work out where the code failed if a test fails.

<h3>Expressive failure messages</h3>
When using JUnit or NUnit for assertions in the IDE the assertion failure messages don't really make much difference because we have the code fresh in our mind and it's only one click to get to the failure.

If an assertion with either of these frameworks fails on the build on the other hand it's much harder at a glance to tell exactly why it failed. This is why I favour <a href="http://code.google.com/p/hamcrest/">Hamcrest</a> which tells you precisely why your test failed.

<h3>In Summary</h3>
For me the key with unit tests is to make sure that other people in the team can read and understand them easily.

No doubt there are other ways of ensuring our unit tests are well written but these are the ways that I consider the most important at the moment.
