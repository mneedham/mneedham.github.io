+++
draft = false
date="2008-12-19 20:57:23"
title="TDD: Mock expectations in Setup"
tag=['tdd', 'testing', 'mocking']
category=['Testing']
+++

One of the ideas that I mentioned in a recent post about what I consider to be a <a href="http://www.markhneedham.com/blog/2008/12/04/what-make-a-good-unit-test/">good unit test</a> was the ideas that we shouldn't necessarily consider the <a href="http://en.wikipedia.org/wiki/Don%27t_repeat_yourself">DRY</a> (Don't Repeat Yourself) principle to be our number one driver.

I consider putting mock expectations in the setup methods of our tests to be one of those occasions where we shouldn't obey this principle and I thought this would be fairly unanimously agreed upon but <a href="http://twitter.com/markhneedham/status/1050794791">putting the question to the Twittersphere</a> led to <a href="http://twitter.com/the_chrismo/status/1050828782">mixed</a> <a href="http://twitter.com/tirsen/status/1050872945">opinions</a>.

<h3>The case for expectations in setup</h3>
The argument for putting expectations in the setup method is that it helps <strong>remove duplication and helps us to fail more quickly</strong>.

This would certainly be the case if, for example, we instantiated our object under test in the setup method and there were some expectations on its dependencies on creation.

<h3>The case against expectations in setup</h3>
The reason I'm so against putting expectations in setup methods derives from the pain of trying to debug <a href="http://www.nmock.org/">NMock</a> error messages when we put expectations and stubs in the setup method on a project I worked on about a year ago.

The number of times we were caught out by a failure which seemed 'impossible' from looking at the failing test was ridiculous.

After that experience we made sure that it was always obvious which expectations  belonged to which test by inlining them and taking the duplication hit.

I believe a lot of the value of tests comes from the way that they fail, and if we can write tests in a way that the <strong>failure message and subsequent fix are really obvious</strong> then we are going the right way.

<h3>My current approach</h3>
My current approach to try and get the best of both worlds is to follow the approach <a href="http://fragmental.tw">Phil</a> describes in his post on <a href="http://fragmental.tw/2008/07/02/domain-driven-tests/">Domain Driven Tests</a>.

If we have repeated expectations across different tests then I now try to extract those into an appropriately named methods which can be called from each test.


~~~csharp


[Test]
public void ShouldDoSomething() 
{
	ExpectServiceToReturnSomeValue();
	
	// rest
	// of
	// test
}

private void ExpectServiceToReturnSomeValue() 
{
	// code describing expectations
}
~~~

This creates a little bit of duplication in that we have to call this method individually in each test which uses it but I think it makes the test more readable and easier to debug.

I'm still not sure what I consider the best way to name these types of methods - Phil uses a combination of a comment and method name to create readable tests but I'm keen to try and have the intent completely described by a method name if possible.
