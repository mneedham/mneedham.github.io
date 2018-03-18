+++
draft = false
date="2010-01-17 19:09:35"
title="Coding: Missing abstractions and LINQ"
tag=['coding', 'c']
category=['Coding']
+++

Something which I've noticed quite a lot on the projects that I've worked on since C# 3.0 was released is that lists seem to be passed around code much more and have LINQ style filters and transformations performed on them while failing to describe the underlying abstraction explcitly in the code.

As a result of this we quite frequently we end up with this code being in multiple places and since it's usually not very much code the repetition goes unnoticed more than other types of duplication might do.

A typical example of this might be the following:


~~~csharp

public class SomeFooHolder
{
	public List<Foo> Foos { get; set }
}
~~~ 

An example of how this might be used is like so:


~~~csharp

var someFooHolder = new FooHolder(...);
someFooHolder.Foos.Select(f => f.Completed);
~~~

That code would typically be repeated in other places in the code where we want to get all the completed foos.

Although it's a simple change, as a first step I prefer to make that concept more explicit by putting 'CompletedFoos' on 'SomeFooHolder':


~~~csharp

public class SomeFooHolder
{
	public List<Foo> Foos { get; set; }
	public List<Foo> CompletedFoos 
	{ 
		get { return Foos.Select(f => f.Completed); }
	}
}
~~~

Perhaps an even better solution would be to create an object 'Foos' to encapsulate that logic further:


~~~csharp

public class Foos
{
	private readonly List<Foo> foos;

	public Foos(List<Foo> foos)
	{
		this.foos = new List<Foo>(foos.AsReadOnly());
	}

	public Foos Completed
	{
		get { return new Foos(foos.Select(f => f.Completed)); }
	}
}
~~~

As I've written about previously <a href="http://www.markhneedham.com/blog/2009/07/24/wrapping-collections-inheritance-vs-composition/">I prefer to wrap the list rather than extend it</a> as the API of 'Foos' is more expressive since we don't have all the list operations available to any potential users of the class. 


