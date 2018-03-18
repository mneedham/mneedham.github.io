+++
draft = false
date="2010-01-24 01:13:57"
title="TDD: Removing the clutter"
tag=['tdd']
category=['Testing']
+++

I got the chance to work with <a href="http://fragmental.tw/">Phil</a> for a couple of weeks last year and one of the most interesting things that he started teaching me was the importance of reducing the clutter in our tests and ensuring that we take some time to refactor them as well as the code as part of the 'red-green-refactor' cycle.

I'm still trying to work out the best way to do this but I came across a really <a href="http://blog.thecodewhisperer.com/post/333781027/what-your-tests-dont-need-to-know-will-hurt-you">interesting post by J.B. Rainsberger where he describes how he removes irrelevant details from his tests</a>.

Since I worked with Phil I've started noticing some of the ways that we can simplify tests so that they are more useful as documentation of how our system works.

<h3>Wrapping methods around irrelevant test builders</h3>

One thing I've noticed in tests recently is that generally most of the setup code for a test is irrelevant and is just there to get the test to actually run. There's very little that's actually interesting and more often than not it ends up getting hidden amongst the other irrelevant stuff.

The <a href="http://www.markhneedham.com/blog/2009/01/21/c-builder-pattern-still-useful-for-test-data/">test builder pattern</a> is a really useful one for allowing us to easily setup test data but I feel that if we're not careful it contributes to the clutter.

To describe a contrived example:

~~~csharp

[Test]
public void SomeTest() 
{
	var bar = BarBuilder.Build.WithBaz("baz").BuildBar();
	var foo = FooBuilder.Build.Bar(bar).BuildFoo();

	var someObject = new SomeObject();
	var result = someObject.SomeMethod(foo);

	Assert.That(result.Baz, Is.EqualTo("baz");
}
~~~

In this example 'Foo' is actually not important at all. What we're really interested in is Baz which happens to be accessed via Foo.

I've started refactoring tests like that into the following style:


~~~csharp

[Test]
public void SomeTest() 
{
	var bar = BarBuilder.Build.WithBaz("baz").BuildBar();

	var someObject = new SomeObject();
	var result = someObject.SomeMethod(FooWith(bar));

	Assert.That(result.Baz, Is.EqualTo("baz");
}

private Foo FooWith(Bar bar)
{
	return FooBuilder.Build.Bar(bar).BuildFoo();
}
~~~

In this example it doesn't make much different in terms of readability but when there's more dependencies it works quite well for driving the test into a state where all we see are the important details that form part of the 'Arrange - Act - Assert' pattern.

<h3>New up object under test inline</h3>

Object initialisation is often not worthy of a variable in our test since it doesn't really add anything to our understanding of the test. 

I only really break this rule when we need to call one method on the object under test and then need to call another method to verify whether or not the expected behaviour happened. 

More often than not this is only the case when dealing with framework code. It's much easier to avoid this in our own code.

In the example that I started with we can inline the creation of 'SomeObject' without losing any of the intent of the test:


~~~csharp

[Test]
public void SomeTest() 
{
	var bar = BarBuilder.Build.WithBaz("baz").BuildBar();

	var result = new SomeObject().SomeMethod(FooWith(bar));

	Assert.That(result.Baz, Is.EqualTo("baz");
}
~~~

The only time I don't do this is when the constructor takes in a lot of dependencies and keeping it all inlined would take the code off the right side of the screen.

In any case it's a sign that something's gone wrong and the object probably has too many dependencies so we need to try and fix that.

<h3>Pull up static dependencies into fields</h3>
Another technique I've been trying is pulling static dependencies i.e. ones whose values are not mutated in the test up into fields and initialising them there.

A typical example would be in <a href="http://www.markhneedham.com/blog/2010/01/15/tdd-thoughts-on-using-a-clock-in-tests/">tests that have a clock</a>.


~~~csharp

[Test]
public void ShouldShowFoosOlderThanToday()
{
	var clock = new ControlledClock(new DateTime(2010,1,16));
	var fooService = MockRepository.GenerateStub<IFooService>();
 
	var fooFromYesterday = new Foo { Date = 1.DayBefore(clock) });
	var aCollectionOfFoos = new List<Foo> { fooFromYesterday };
	fooService.Stub(f => f.GetFoos()).Return(aCollectionOfFoos);
 
	var oldFoos = new FooFinder(clock, fooService).GetFoosFromEarlierThanToday();
 
	Assert.That(oldFoos.Count, Is.EqualTo(1));
	// and so on
}
~~~

I would pull the clock variable up to be a field since the value we want to return for it is going to be the same for the whole test fixture.


~~~csharp

[TestFixture]
public class TheTestFixture
{
	private readonly IClock Clock = new ControlledClock(new DateTime(2010,1,16));

	[Test]
	public void ShouldShowFoosOlderThanToday()
	{
		var fooService = MockRepository.GenerateStub<IFooService>();
 
		var fooFromYesterday = new Foo { Date = 1.DayBefore(clock) });
		var aCollectionOfFoos = new List<Foo> { fooFromYesterday };
		fooService.Stub(f => f.GetFoos()).Return(aCollectionOfFoos);
 
		var oldFoos = new FooFinder(Clock, fooService).GetFoosFromEarlierThanToday();
 
		Assert.That(oldFoos.Count, Is.EqualTo(1));
		// and so on
	}
}
~~~

I'm less certain what I would do with 'fooService'. I've run into problems previously by pulling these types of dependencies up into a setup method if we've also moved the corresponding 'Stub' or 'Mock' call as well. With that setup the intent of the test is now in two places which makes it more difficult to understand.

<h3>In Summary</h3>
It's really interesting to read about the way that others are trying to write better tests and <a href="http://www.exampler.com/blog/2010/01/13/mocks-the-removal-of-test-detail-and-dynamically-typed-languages/">Brian Marick also has a post where he describes how he is able to create even more intention revealing tests in a dynamic language</a>. 

It'd be cool to here some more ideas around this.

