+++
draft = false
date="2010-03-24 06:53:55"
title="TDD: Consistent test structure"
tag=['tdd', 'testing']
category=['Testing']
+++

While pairing with <a href="http://foldingair.blogspot.com/">Damian</a> we came across the fairly common situation where we'd written two different tests - one to handle the positive case and one the negative case.

While tidying up the tests after we'd got them passing we noticed that the test structure wasn't exactly the same. The two tests looked a bit like this:


~~~csharp

[Test]
public void ShouldSetSomethingIfWeHaveAFoo()
{
	var aFoo = FooBuilder.Build.WithBar("bar").WithBaz("baz").AFoo();

	// some random setup
	// some stubs/expectations

	var result = new Controller(...).Submit(aFoo);

	Assert.That(result.HasFoo, Is.True);
}
~~~


~~~csharp

[Test]
public void ShouldNotSetSomethingIfWeDoNotHaveAFoo()
{
	// some random setup
	// some stubs/expectations

	var result = new Controller(...).Submit(null);

	Assert.That(result.HasFoo, Is.False);
}
~~~

There isn't a great deal of difference between these two bits of code but the structure of the test isn't the same because I inlined the 'aFoo' variable in the second test.

Damian pointed out that if we were just glancing at the tests in the future it would be much easier for us if the structure was exactly the same. This would mean that we would immediately be able to identify what the test was supposed to be doing and why.

In this contrived example we would just need to pull out the 'null' into a descriptive variable:


~~~csharp

[Test]
public void ShouldNotSetSomethingIfWeDoNotHaveAFoo()
{
	var noFoo = null;

	// some random setup
	// some stubs/expectations

	var result = new Controller(...).Submit(noFoo);

	Assert.That(result.HasFoo, Is.False);
}
~~~

Although this is a simple example I've been trying to follow this guideline wherever possible and my tests now tend to have the following structure:


~~~csharp

[Test]
public void ShouldShowTheStructureOfMarksTests()
{
	// The test data that's important for the test
	
	// Less important test data

	// Expectation/Stub setup

	// Call to object under test

	// Assertions
}
~~~

As a neat side effect I've also noticed that it seems to be easier to spot duplication that we can possibly extract with this approach as well.
