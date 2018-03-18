+++
draft = false
date="2010-01-15 21:56:48"
title="TDD: Thoughts on using a clock in tests"
tag=['tdd', 'stubs']
category=['Testing']
+++

A few months ago <a href="http://blog.objectmentor.com/articles/2009/10/28/manual-mocking-resisting-the-invasion-of-dots-and-parentheses">Uncle Bob wrote a post about TDD where he suggested that he preferred to use hand created stubs in his tests</a> wherever possible and only resorted to using a Mockito created stub as a last resort.

I <a href="http://www.markhneedham.com/blog/2010/01/15/tdd-hand-written-stubs-vs-framework-generated-stubs/">wrote previously about my thoughts of where to use each of the two approaches</a> and one example of where hand written stubs seems to make sense is the clock.

I wonder if this ties in with <a href="http://blog.thecodewhisperer.com/post/333781027/what-your-tests-dont-need-to-know-will-hurt-you">J.B. Rainsberger's theory of irrelevant details</a> in the tests which make use of it.

We would typically define an interface and stub version of the clock like so:


~~~csharp

public interface IClock
{
	DateTime Now();
}
~~~


~~~csharp

public class ControlledClock : IClock
{
	private readonly DateTime dateTime;

	public ControlledClock(DateTime dateTime)
	{
		this.dateTime = dateTime;
	}

	public DateTime Now() 
	{ 
		return dateTime; 
	}
}
~~~

I forgot about it to start with and was stubbing it out using Rhino Mocks but I realised that every single test needed something similar to the following code:


~~~csharp

var theCurrentTime = new DateTime(2010, 1, 16);
var clock = MockRepository.GenerateStub<IClock>();
clock.Stub(c => c.Now()).Return(theCurrentTime);
~~~

We can extract out the creation of the first two lines into fields but the third line remains and typically that might end up being pushed into a setup method which is run before each test.

With a clock it's maybe not such a big deal but with other dependencies from my experience it can become very difficult to follow where exactly the various return values are being setup.

When we use a hand written stub we only have to write the following code and then the date is controlled everywhere that calls 'Now()':


~~~csharp

private readonly IClock clock = new ControlledClock(new DateTime(2010,1,16));
~~~

Following on from that my colleague <a href="http://twitter.com/mikewagg">Mike Wagg</a> suggested the idea of creating extension methods on integers to allow us to fluently define values relative to the clock.


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

The extension method on integer would be like this:


~~~csharp

public static class IntegerExtensions
{
	public static DateTime DayBefore(this int value, IClock clock)
	{
		return clock.Now.Subtract(TimeSpan.FromDays(value));
	}
}
~~~

It reads pretty well and seems more intention revealing than any other approaches I've tried out so I think I'll be continuing to use this approach.
