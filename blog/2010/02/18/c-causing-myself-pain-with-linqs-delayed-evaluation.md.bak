+++
draft = false
date="2010-02-18 22:28:12"
title="C#: Causing myself pain with LINQ's delayed evaluation"
tag=['c']
category=['.NET']
+++

I recently came across some code was imperatively looping through a collection and then mapping each value to go to something else by using an injected dependency to do that.

I thought I'd try to make use of functional collection parameters to try and simplify the code a bit but actually ended up breaking one of the tests.

About a month ago I wrote about how I'd written a <a href="http://www.markhneedham.com/blog/2010/01/25/tdd-simplifying-a-test-with-a-hand-rolled-stub/">hand rolled stub to simplify a test</a> and this was actually where I caused myself the problem!

The hand rolled stub was defined like this:


~~~csharp

public class AValueOnFirstCallThenAnotherValueService : IService
{
	private int numberOfCalls = 0;
 
	public string SomeMethod(string parameter)
	{
		if(numberOfCalls == 0)
		{
			numberOfCalls++;
			return "aValue";
		}
		else
		{
			numberOfCalls++;
			return "differentValue";
		}
	}
}
~~~

The test was something like this:


~~~csharp

[Test]
public void SomeTest()
{
	var fooOne = new Foo { Bar = "barOne" };
	var fooTwo = new Foo { Bar = "barTwo" }; 
	var aCollectionOfFoos = new List<Foo> { fooOne, fooTwo };

	var service = new AValueOnFirstCallThenAnotherValueService();

	var someObject = new SomeObject(service);

	var fooBars = someObject.Method(aCollectionOfFoos);

	Assert.That(fooBars[0].Other, Is.EqualTo("aValue"));
	// and so on
}
~~~

The object under test looked something like this:


~~~csharp

public class SomeObject 
{
	private IService service;

	public SomeObject(IService service)
	{
		this.service = service;
	}

	public IEnumerable<FooBar> Method(List<Foo> foos)
	{
		var fooBars = new List<FooBar();
		foreach(var foo in foos)
		{
			fooBars.Add(new FooBar { Bar = foo.Bar, Other = service.SomeMethod(foo.Bar) }; 
		}

		// a bit further down

		var sortedFooBars = fooBars.OrderBy(f => f.Other);

		return fooBars;
	}
}
~~~

I decided to try and incrementally refactor the code like so:


~~~csharp

public class SomeObject 
{
	...

	public IEnumerable<FooBar> Method(List<Foo> foos)
	{
		var fooBars = foos.Select(f => new FooBar { Bar = f.Bar, Other = service.SomeMethod(f.Bar) };

		// a bit further down

		var sortedFooBars = fooBars.OrderBy(f => f.Other);

		return fooBars;
	}
}
~~~

I ran the tests after doing this and the test I described above failed - it was expecting a return value for 'Other' of 'aValue' but was actually returning 'differentValue'.

I was a bit confused about what was going on until I started watching what the test was doing through the debugger and realised that on the 'OrderBy' call on line 10 the 'Select' call on line 7 was being reevaluated which meant that the value returned by 'service.SomeMethod' would be 'differentValue' since it was being called for the 3rd and 4th time and it's set up to return 'aValue' only on the 1st time.

The way to get around this problem was to force the evaluation of 'fooBars' to happen immediately by calling 'ToList()':


~~~csharp

public class SomeObject 
{
	...

	public IEnumerable<FooBar> Method(List<Foo> foos)
	{
		var fooBars = foos.Select(f => new FooBar { Bar = f.Bar, Other = service.SomeMethod(f.Bar) }.ToList();

		...
	}
}
~~~

In this case it was fairly easy to identify the problem but I've written similar code before which has ended up reordering collections with thousands of items in because it's been lazy evaluated every time the collection is needed.

In <a href="http://msdn.microsoft.com/en-us/magazine/ee309512.aspx">Jeremy Miller's article about functional C#</a> he suggests the idea of memoization as an optimisation technique to stop expensive calls being made more times than they need to be so perhaps this would be another way to solve the problem although I haven't tried that approach before.
