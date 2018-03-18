+++
draft = false
date="2010-04-25 22:48:37"
title="Small step refactoring: Overload constructor"
tag=['refactoring']
category=['Coding', 'Incremental Refactoring']
+++

I've previously written about some approaches that I've been taught with respect to <a href="http://www.markhneedham.com/blog/2010/02/24/refactoring-small-steps-to-pull-out-responsibilities/">taking small steps</a> <a href="http://www.markhneedham.com/blog/2009/05/26/refactoring-removing-duplication-more-safely/">when refactoring code</a> and another approach which a couple of colleagues have been using recently is the idea of <strong>overloading the constructor</strong> when refactoring objects.

On a couple of occasions we've been trying to completely change the way an object was designed and changing the current constructor would mean that we'd have to change all the tests against that object before checking if the new design was actually going to work or not.

Given a simple example where we want to change the following object to take in a completely different type and not use 'field1' or 'field2' anymore:


~~~csharp

public class Foo
{
	public Foo(string field1, int field2)
	{
		// and so on
	}
}
~~~

One approach would be to change that constructor to take in the extra parameter and then gradually phase out the other parameters: 


~~~csharp

public class Foo
{
	public Foo(string field1, int field2, Bar bar)
	{
		// and so on
	}
}
~~~

An alternative is to create another constructor and leave the old one as it is before changing the tests one by one to make use of the new approach.


~~~csharp

public class Foo
{
	public Foo(string field1, int field2)
	{
		// we gradually phase this one out
	}

	public(Bar bar)
	{
		// the new constructor
	}
}
~~~

Even if we want to still use 'field1' and 'field2' we can still make use of this approach and just default the extra value until we've migrated our tests across.


~~~csharp

public class Foo
{
	public Foo(string field1, int field2, Bar bar)
	{
		// and so on
	}

	public Foo(string field1, int field2) : this(field1, field2, new Bar())
	{
	}
}
~~~

I quite like this approach as it allows us to keep the code compiling while we're making changes to it to improve the design. 

The main thing to remember with this approach is not to keep the old approach around for too long and to make sure we move our code across to use the new approach as quickly as possible otherwise it can become very confusing for other pairs which come across the code in this half way state.
