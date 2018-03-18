+++
draft = false
date="2009-10-29 23:06:35"
title="Coding: Consistency when invariant checking"
tag=['coding']
category=['Coding']
+++

I wrote a while ago about <a href="http://www.markhneedham.com/blog/2009/02/14/coding-assertions-in-constructors/">reading the ASP.NET MVC source code and noticing that it makes use of code inside its constructors to ensure that null values can't be passed in</a> and while I'm still not convinced this is the way to go I think if we do take this approach then we need to ensure we do so consistently.

Something which happens quite often is that you'll come across code which makes use of defensive programming in one of its constructors like so:



~~~java

public class SomeObject 
{
	public SomeObject(Dependency1 valueOne, Dependency2 valueTwo)
	{
		AssertThat.isNotNull(valueOne);
		AssertThat.isNotNull(valueTwo);
		// and so on
	}
}
~~~

This is fine in itself but you'll often find another constructor defined close by which looks like this:


~~~java

public class SomeObject 
{
	public SomeObject(Dependency1 valueOne, Dependency2 valueTwo)
	{
		this.valueOne = null;
		this.valueTwo = null;
	}
}
~~~

Depending which constructor you use the outcome is quite different and you probably wouldn't expect the default constructor to allow nulls seeing as the other one prevents you from doing this.

This inconsistency can happen for a variety of reasons.

<h4>Test only constructor</h4>
It might be a <a href="http://www.markhneedham.com/blog/2009/09/12/tdd-test-only-constructors/">test only constructor</a> which is not intended to be called in production case. It's much easier to get an object under test if we don't have to supply any parameters. 

In that case though we're testing the object constructed in a much different state than it will be when we really use it so the value of this type of testing is questionable.

It's probably best to look why we need that test only constructor and see if we can change the code so that we can avoid that problem.

<h4>An implicit domain concept</h4>
Another reason is that the original pre condition of the object might have changed and now it isn't always the case that we need to provide 'Dependency1' and 'Dependency2'.

In this case I think it would make more sense to make that more explicit, perhaps by making use of the <a href="http://www.markhneedham.com/blog/2008/08/16/null-handling-strategies/">null object pattern</a> or by finding another abstraction which doesn't require nulls to be passed around. 

Either way we should probably look to ensure that both constructors either ignore nulls or both stop them from being set.

<h4>Didn't realise pre conditions were being checked</h4>
Although this one might seem a bit far fetched it's pretty easy for this to be the case if there are different people working on the code base.

Someone might glance at the class, see that it doesn't quite allow them to construct the object the way they want and create another constructor without realising the way the original one was working.

In this case talking more about the way that we're solving this type of problem across the code base should be enough to ensure that we get some kind of consistency.
