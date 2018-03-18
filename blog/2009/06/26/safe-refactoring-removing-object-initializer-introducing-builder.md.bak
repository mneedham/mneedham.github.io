+++
draft = false
date="2009-06-26 00:02:45"
title="Safe refactoring: Removing object initializer, introducing builder"
tag=['coding', 'refactoring', 'safe']
category=['Coding', 'Incremental Refactoring']
+++

I previously wrote about <a href="http://www.markhneedham.com/blog/2009/05/26/refactoring-removing-duplication-more-safely/">an approach we took to safely remove some duplication</a> and I recently followed a similar mantra to replace an <a href="http://www.markhneedham.com/blog/2009/02/16/c-object-initializer-and-the-horse-shoe/">object initializer</a> call which had around 40 properties being setup with a builder to try and make the code a bit easier to understand.

We did have tests checking the values being setup by the object initializer so I was already able to refactor with some degree of safety - it would probably have been possible to just create the builder and build the object from that and then delete the old code and replace it with the new but I've caused myself too many problems from doing that before that I decided to try a more incremental approach.

The idea was to have the builder and the object initializer both creating the object at the same time and as I built a property from the builder I would set it in the object initializer until eventually all of the   properties were being set directly from the builder's object and then I could just return that instead - this approach feels quite similar to what Kent Beck describes as having parallel implementations in <a href="http://www.infoq.com/presentations/responsive-design">his recent presentation on Responsive Design</a>.

The code I started with was something like this:


~~~csharp

public Foo CreateMeAFoo() 
{
	return new Foo
	{
		Bar = "someValue",
		OtherBar = "someOtherValue",
		UltraBar = "aValue",
		...
		AnotherArgumentWayDownHere = 1
		...
		AndSoOn = "yes"

	}
}
~~~

I worked together with one of the business analysts on our team who pointed out that there were actually some clear groupings in what I had just been considering 'data' and we were able to put those explicit domain concepts into the code as part of the builder.

My first step however was to remove the object initializer to avoid making any silly mistakes - an example of one I have made when using object initializers is to set a property using 'Int16.Parse' and then passing in a string with a value of "53700" which causes the method to throw an exception and the stack trace just directs you to the first line of the object initializer, making it quite difficult to work out which line has failed.

Having worked the code into a sequence of setters I gradually added methods to the builder to create the policy:


~~~csharp

public Foo CreateMeAFoo() 
{
	var fooBuilder = new FooBuilder().AddBars("someValue", "someOtherValue", "aValue);
	var newFoo = fooBuilder.Build();

	var foo = new Foo();
	foo.Bar = newFoo.Bar;
	foo.OtherBar = newFoo.OtherBar;
	foo.UltraBar = newFoo.UltraBar;
	...
	foo.AnotherArgumentWayDownHere = 1

	return foo;
}
~~~


~~~csharp

public class FooBuilder  
{
	private string bar;
	private string otherBar;
	private string ultraBar;

	public FooBuilder AddBars(string bar, string otherBar, string ultraBar)
	{
		this.bar = bar;
		this.otherBar = otherBar;
		this.ultraBar = ultraBar;
		return this;
	}

	public Foo Build()
	{
		var foo = new Foo();
		foo.Bar = bar;
		foo.OtherBar = otherBar;
		foo.UltraBar = ultraBar;
		return foo;
	}
}
~~~

I created some duplication by doing this - I am now creating the 'Foo' twice - but I didn't check any of the code into the main branch until I had totally replaced the original Foo creation with the builder.

I did about two of three properties at a time and then ran the tests which I thought might be too small a step but actually saved me on a couple of occasions so it probably actually saved me time.

Eventually when I had all the tests passing I got rid of the original Foo and replaced it with the one from the builder:


~~~csharp

public Foo CreateMeAFoo() 
{
	var fooBuilder = new FooBuilder().AddBars("someValue", "someOtherValue", "aValue);
	return fooBuilder.Build();
}
~~~

This code is still in a state of transition - it is still possible to create an object with half the fields not set by passing in nulls to the builder for example - and I'm trying to work out what the best step is to fix that. 

I generally prefer to have everything setup in the constructor and then you know that the object is in a good state as soon as you create it, but in this case moving everything straight into the constructor will probably make the object even more difficult to deal with.

My current thinking is to maybe check the pre conditions for creating the object inside the builder and then refactor out value objects so that there are not so many properties overall but I'm open to other ideas.
