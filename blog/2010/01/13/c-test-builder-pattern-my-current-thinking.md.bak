+++
draft = false
date="2010-01-13 01:37:15"
title="C# Test Builder Pattern: My current thinking"
tag=['coding', 'c']
category=['Coding']
+++

I've written previously about the <a href="http://www.markhneedham.com/blog/2009/01/21/c-builder-pattern-still-useful-for-test-data/">test builder pattern in C#</a> and having noticed some different implementations of this pattern I thought it'd be interesting to post my current thinking on how to use it.

One thing I've noticed is that we often end up just creating methods which effectively act as setters rather than easing the construction of an object.

This seems to happen most commonly when the value we want to set is a boolean value. The following is quite typical:


~~~csharp

public CarBuilder WithSomething(boolean value)
{
	this.something = value;
	return this;
}
~~~

The usage would be like so:


~~~csharp

new CarBuilder().WithSomething(true).Build();
~~~

It doesn't read too badly but it seems to be unnecessary typing for the user of the API. If we're going to use the fluent interface approach then I would prefer to have two methods, defined like so:


~~~csharp

public CarBuilder WithSomething()
{
	this.something = true;
	return this;
}

public CarBuilder WithoutSomething()
{
	this.something = false;
	return this;
}
~~~

We could then use this like so:


~~~csharp

new CarBuilder().WithSomething().Build();
...
new CarBuilder().WithoutSomething().Build();
~~~

That requires more code but I think it's a bit more expressive and makes life easier for the user of the API.

An alternative approach which my colleague Lu Ning showed me and which I think is actually better is to <a href="http://www.markhneedham.com/blog/2009/08/15/builders-hanging-off-class-vs-builders-in-same-namespace/">make use of the object initializer syntax if all we have are setter methods on a builder</a>.

We might therefore end up with something like this:


~~~csharp

public class FooBuilder 
{
	public string Something = "DefaultSomething";
	public boolean SomethingElse = false;

	public Foo Build()
	{
		return new Foo(Something, SomethingElse);
	}
}
~~~


~~~csharp

new FooBuilder { SomethingElse = true }.Build();
~~~

With this approach we end up writing less code and although we use public fields on the builder I don't think it's a big deal since it allows us to achieve our goal more quickly. If we need other methods that take out the complexity of construction then we can easily just add those as well.

Another thing to note when using this pattern is that <strong>we don't need to override all the object's attributes on every single test</strong>. We only need to override those ones which we are using in our test. The rest of the values can just be defaulted.


~~~csharp

[Test]
public void ShouldDoSomething()
{
	var foo = new FooBuilder { Bar = "myBar", Baz = "myBaz", SomethingElse = "mySE", AndAgain = "..." }.Build();


	// and then further on we only check the value of Bar for example

	Assert.That(someValue, Is.EqualTo("myBar"); 
}
~~~

We don't need to specifically set any of the values except 'Bar' because they are irrelevant and create a clutter in the test which means it takes longer to understand what's going on. 

This would be preferable:


~~~csharp

[Test]
public void ShouldDoSomething()
{
	var foo = new FooBuilder { Bar = "myBar" }.Build();


	// and then further on we only check the value of Bar for example

	Assert.That(someValue, Is.EqualTo("myBar"); 
}
~~~

Something which I've been wondering about recently is understanding the best way to describe the case where we don't want to define a specific value i.e. we want it as null.

I'd normally just set it to null like so:


~~~csharp

new FooBuilder { Bar = null }.Build();
~~~

But we could make the API have a specific method and I haven't really decided whether there's much value to doing so yet:


~~~csharp

new FooBuilder().WithNoBar().Build();
~~~
