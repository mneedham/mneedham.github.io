+++
draft = false
date="2009-09-20 12:06:04"
title="TDD: Keeping test intent when using test builders"
tag=['tdd', 'test-builder']
category=['Testing']
+++

While the <a href="http://www.markhneedham.com/blog/2009/01/21/c-builder-pattern-still-useful-for-test-data/">test data builder</a> pattern is quite a useful one for simplifying the creation of test data in our tests I think we need to be quite careful when using it that we don't lose the intent of the test that we're writing.

The main advantage that I see with this pattern is that by using it we can provide default values for properties of our objects which aren't important for the bit of functionality that we're currently testing but which need to be provided otherwise the test can't actually be run.

In order for our tests to express their intent clearly it is still important to explicitly set the values that we care about for the current test otherwise it will become quite difficult to work out why a test is failing when it does.

For example I recently came across a failing test similar to this:


~~~csharp

[Test]
public void ShouldTestSomeCoolStuff()
{
	var foo = new FooBuilder().Build();

	var yetAnotherObject = someOtherObject.ThatTakesIn(foo);

	Assert.AreEqual("DEFAULTBAR", yetAnotherObject.Bar);
	Assert.AreEqual("DEFAULTBAZ", yetAnotherObject.Baz)	
}
~~~

It was failing because the actual values being returned were 'defaultBar' and 'defaultBaz' which initially made us wonder if there was some capitalisation going wrong in one of our objects.

As it turned out the values being returned were just the default ones from the 'FooBuilder' and we were asserting the wrong thing:


~~~csharp

public class FooBuilder
{
	private string bar = "defaultBar";
	private string baz = "defaultBaz";

	public FooBuilder Bar(string value)
	{
		bar = value;
		return this;
	}

	public FooBuilder Baz(string value)
	{
		baz = value;
		return this;
	}

	public Foo Build()
	{
		return new Foo(bar, baz);
	}
}
~~~

While it didn't take us too long to get to the cause of the problem I think it would have made our lives easier if we'd been able to tell why it was failing just from looking at the test instead of having to look in a couple of different classes to figure it out.

A test written more like this would help us to achieve that:


~~~csharp

[Test]
public void ShouldTestSomeCoolStuff()
{
	var foo = new FooBuilder().Bar("myBar").Baz("myBaz").Build();

	var yetAnotherObject = someOtherObject.ThatTakesIn(foo);

	Assert.AreEqual("myBar", yetAnotherObject.Bar);
	Assert.AreEqual("myBaz", yetAnotherObject.Baz)	
}
~~~

Then if we want to remove duplication we can just put the expected values into more descriptive variables:


~~~csharp

[Test]
public void ShouldTestSomeCoolStuff()
{
	var expectedBar = "myBar";
	var expectedBaz = "myBaz";
	var foo = new FooBuilder().Bar(expectedBar).Baz(expectedBaz).Build();

	var yetAnotherObject = someOtherObject.ThatTakesIn(foo);

	Assert.AreEqual(expectedBar, yetAnotherObject.Bar);
	Assert.AreEqual(expectedBaz, yetAnotherObject.Baz)	
}
~~~

There's a bit more test code than in the first example but if the test fails again we should be able to work out why more quickly than before because we are now more explicit about which values are actually important for this test.
