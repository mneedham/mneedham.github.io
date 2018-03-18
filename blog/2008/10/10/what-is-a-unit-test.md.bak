+++
draft = false
date="2008-10-10 23:21:43"
title="What is a unit test?"
tag=['tdd', 'unit-test']
category=['Testing']
+++

One of the questions which came up during the <a href="http://www.markhneedham.com/blog/2008/10/01/altnet-sydney-user-group-meeting-1/">Sydney Alt.NET User Group</a> meeting at the start of October was around what a unit test actually is.

I suppose the somewhat naive or simplistic definition is that it is just any test written using an xUnit framework such as <a href="http://www.nunit.org/index.php">NUnit</a> or <a href="http://www.junit.org/">JUnit</a>. However, integration or acceptance tests are often written using these frameworks so this definition doesn't hold.

While discussing this last week a colleague came up with what I considered to be a very clear yet precise definition. To paraphrase: '<strong>A unit test has no dependencies</strong>'.

This means that if the class that we are testing does have dependencies then we need we need to remove these from our test either by using a <a href="http://en.wikipedia.org/wiki/Mock_Object">mocking</a> framework or by stubbing them out.

Dependencies might include calls to a database, web services, 3rd party APIs - we don't want our unit tests to rely on these being available in order to execute our test.

<h3>Why should I care?</h3>

If we depend on things outside of our control then we are making our tests fragile and unrepeatable - if a test fails because a dependency outside our control is unreliable we cannot fix it easily. 

There is definitely room for integration tests in a system but we can gain much more benefit from them when this integration is not mixed in with testing the functionality of a single unit.

The goal with a unit test is that we should be able to start up our IDE and run the test - there should be nothing else to setup to make this happen.

<h3>The grey area</h3>

The grey area that I have noticed is around file system interactions in unit tests.

I wrote previously about a way that I have seen using for <a href="http://www.markhneedham.com/blog/2008/09/17/testing-file-system-operations/">testing file system operations</a> but I have often written tests which load test data from an XML file before loading it into the test.

Doing that creates a dependency on the file system although it makes the test a lot cleaner than having a huge string containing all the data. If the file is included as part of the project then I think it doesn't necessarily have to be a problem.

<h3>What makes a good unit test?</h3>
A well written unit test in my book should be simple to understand and run quickly. This is especially helpful when we are practicing TDD as it allows us to keep the cycles between writing code and tests very small.

My colleague <a href="http://fragmental.tw/2008/07/02/domain-driven-tests/">Phillip Calcado has a post </a>about an approach to make the former happen but the final word goes to Uncle Bob who suggests the F.I.R.S.T acronym in <a href="http://www.markhneedham.com/blog/2008/09/15/clean-code-book-review/">Clean Code</a> to describe what well written (clean) unit tests should look like:

<ul>
<li><strong>F</strong>ast - they should ruin quickly. This encourages you to run them often.</li>
<li><strong>I</strong>ndependent - they should not depend on each other. It should be possible to run the tests in any order.</li>
<li><strong>R</strong>epeatable - it should be possible to run them in any environment. They should be environment independent.</li>
<li><strong>S</strong>elf-Validating - they should either pass or fail.</li>
<li><strong>T</strong>imely - they should be written in a timely manner i.e. just before the production code is written.</li>
</ul>




