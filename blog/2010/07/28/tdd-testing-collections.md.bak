+++
draft = false
date="2010-07-28 06:05:25"
title="TDD: Testing collections"
tag=['tdd']
category=['Testing']
+++

I've been watching <a href="http://www.pragprog.com/screencasts/v-kbtdd/test-driven-development">Kent Beck's TDD screencasts</a> and in the 3rd episode he reminded me of a mistake I used to make when I was first learning how to test drive code.

The mistake happens when testing collections and I would write a test which would pass even if the collection had nothing in it.

The code would look something like this:


~~~csharp

[Test]
public void SomeTestOfACollection()
{
	var someObject = new Object();
	var aCollection = someObject.Collection;

	for(var anItem : aCollection)
	{
		Assert.That(anItem.Value, Is.EqualTo(...));
	}
}
~~~

If the collection returned by someObject is empty then the test will still pass because there is no assertion to deal with that situation coming up.

In Kent's example he is using an iterator rather than a collection so he creates a local 'count' variable which he increments inside the for loop and then writes an assertion outside the loop that the 'count' variable has a certain value.

In my example we can just check that the length of the collection is non zero before we iterate through it.


~~~csharp

[Test]
public void SomeTestOfACollection()
{
	var someObject = new Object();
	var aCollection = someObject.Collection;

	Assert.That(aCollection.Count(), Is.GreaterThan(0));
	for(var anItem : aCollection)
	{
		Assert.That(anItem.Value, Is.EqualTo(...));
	}
}
~~~

It's a relatively simple problem to fix but it's certainly one that's caught me out before!
