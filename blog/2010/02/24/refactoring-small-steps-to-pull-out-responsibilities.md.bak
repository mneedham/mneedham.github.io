+++
draft = false
date="2010-02-24 00:45:38"
title="Refactoring: Small steps to pull out responsibilities"
tag=['coding', 'refactoring']
category=['Coding', 'Incremental Refactoring']
+++

I wrote previously about how I've been <a href="http://www.markhneedham.com/blog/2010/02/23/coding-effect-sketches-and-the-mikado-method/">using effect sketches to identify responsibilities in objects</a> so that I can pull them out into other objects and once I've done this I often find that I can't see a small next step to take.

At this stage in the past I've often then stopped and left the refactoring until I have more time to complete it but this hasn't really worked and a lot of the time I end up only seeing the code change in my mind and not in the actual code.

I came across this problem again last week in an object which had 8 dependencies when I came across it.

Having drawn the effect sketch I realised that 3 of those could be pulled out into a new object which could then be injected into the original object and help to encapsulate those other 3 dependencies.

The code that I wanted to change was something like this:


~~~csharp

public class TheObject 
{
	private readonly DependencyA;
	private readonly DependencyB;
	private readonly DependencyB;
	...	

	public Foo FooCreation()
	{
		var dependencyAValue = dependencyA.GetSomething();
		var dependencyBValue = dependencyB.GetSomething();
		var dependencyCValue = dependencyC.GetSomething();

		return new Foo(dependencyAValue, dependencyBValue, dependencyCValue);
	}

	...
}
~~~

I wanted to pull the 'FooCreation' method out into another object and then change all the places that were calling 'TheObject'FooCreation' to just call this new object directly.

The first step was to create a 'FooFactory' and just have that delegated to internally:


~~~csharp

public class FooFactory 
{
	private readonly DependencyA;
	private readonly DependencyB;
	private readonly DependencyB;
	...	

	public Foo Create()
	{
		var dependencyAValue = dependencyA.GetSomething();
		var dependencyBValue = dependencyB.GetSomething();
		var dependencyCValue = dependencyC.GetSomething();

		return new Foo(dependencyAValue, dependencyBValue, dependencyCValue);
	}

}
~~~


~~~csharp

public class TheObject 
{
	...	

	public Foo FooCreation()
	{
		return new FooFactory(dependencyA, dependencyB, dependencyC).Create();
	}

	...
}
~~~

I ran out of time at this stage to finish off the refactoring but it was obvious where the refactoring was going so the next time I got the chance I injected the 'FooFactory' into 'TheObject':


~~~csharp

public interface IFooFactory 
{
	Foo Create();
}
~~~


~~~csharp

public class TheObject 
{
	private readonly IFooFactory;
	...	
	public TheObject(IFooFactory fooFactory) 
	{
		this.fooFactory = fooFactory;
	}

	public Foo FooCreation()
	{
		return fooFactory.Create();
	}

	...
}
~~~

To do this I had to go and change the tests on 'TheObject' and move some of them to go directly against 'FooFactory'.

The third stage of the refactoring was to change all the places which called 'TheObject.FooCreation()' to just call 'FooFactory.Create()' directly.	
Some of those places were also using other methods on 'TheObject' so those objects now have an extra dependency although I think at least the code is more intention revealing than it was previously.

I'm sure there are some other patterns for this type of small step refactoring but this is just one that I've noticed so far.
