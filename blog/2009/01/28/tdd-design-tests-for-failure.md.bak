+++
draft = false
date="2009-01-28 00:48:16"
title="TDD: Design tests for failure"
tag=['tdd', 'testing']
category=['Testing']
+++

As with most code, tests are read many more times than they are written and as the majority of the time the reason for reading them is to identify a test failure I think it makes sense that we should be designing our tests with failure in mind.

Several ideas come to mind when thinking about ways to write/design our tests so that when we do have to read them our task is made easier.

<h3>Keep tests data independent</h3>

The worst failures for me are the ones where a test fails and when we investigate the cause it turns out that it only failed because some data it relied on changed.

This tends to be the case particularly when we are writing boundary tests against external services where the data is prone to change.

In this situations we need to try and keep our tests <strong>general enough that they don't give us these false failures, but also specific enough that they aren't completely worthless</strong>.

As an example, when testing XML based services it makes more sense to check that certain elements exist in the document rather than checking that these elements have certain values. The latter approach leads to brittle, difficult to maintain tests while the former leads to tests that are more independent and whose failures are actually a cause for concern.

<h3>Consistent Structure</h3>
Jay Fields touched on this in a post he wrote a couple of months ago about having a <a href="http://blog.jayfields.com/2008/11/ubiquitous-assertion-syntax.html">ubiquitous assertion syntax</a> for every test.

That way when we look at a failing test we know what to expect and we can get down to fixing the test rather than trying to work out how exactly it failed.

We have used the <a href="http://www.lostechies.com/blogs/jimmy_bogard/archive/2008/07/24/arrange-act-assert-and-bdd-specifications.aspx">Arrange, Act, Assert</a> approach on the last couple of projects I've worked on which has worked quite well for dividing the tests into their three main parts. We typically leave empty lines between the different sections or add a comment explaining what each section is.

The nice thing about this approach when you get it right is that you don't even have to read the test name - the test reads like a specification and explains for itself what it going on.

My personal preference for the Assert step is that I should be able to work out why the test is failing from within the test method without having to click through to another method in the test class. There is a debate about whether or not that approach is <a href="http://c2.com/cgi/wiki?DontRepeatYourself">DRY</a>, but that's a discussion for another post!

<h3>Avoid false failures</h3>
Failing because of test reliance on data is one example of a false failure but there are other ways that a test failure can be quite misleading as to the actual reason that it failed.

Null Reference or Null Pointer Exceptions are the chief culprits when it comes to this - a test will seemingly randomly start throwing one of these exceptions either on an assertion or in the actual code.

With the former we should shore the test up by testing something more general further up the test, so that we get a more meaningful failure the next time.

With the latter this usually happens because we added in some code without changing the tests first. I always get bitten when I disrespect Uncle Bob's Three Laws.

<ul>
<li>Write no production code except to pass a failing test.</li>
<li>Write only enough of a test to demonstrate a failure</li>
<li>Write only enough production code to pass the test</li>
</ul>

Sometimes we get false failures due to not having enough data set up on our objects. Depending on the situation we might have a look at the test to see whether it is testing too much and the class has taken on more responsibility.

If it turns out all is fine then the <a href="http://www.markhneedham.com/blog/2009/01/21/c-builder-pattern-still-useful-for-test-data/">builder pattern</a> is a really good way for ensuring we don't run into this problem again.
