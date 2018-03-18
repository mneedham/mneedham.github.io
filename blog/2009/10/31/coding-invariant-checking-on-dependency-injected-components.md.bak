+++
draft = false
date="2009-10-31 03:00:40"
title="Coding: Invariant checking on dependency injected components"
tag=['coding']
category=['Coding']
+++

I've written a couple of times previously about <a href="http://www.markhneedham.com/blog/2009/10/29/coding-consistency-when-invariant-checking/">invariant checking</a> <a href="http://www.markhneedham.com/blog/2009/02/14/coding-assertions-in-constructors/">in constructors</a> and I had an interesting discussion with some colleagues recently around doing this type of defensive programming when the object in question has its dependencies injected by a container.

Quite often we would see code similar to this in a controller:


~~~java

public class SomeController 
{
	public SomeController(Dependency1 valueOne, Dependency2 valueTwo)
	{
		AssertThat.isNotNull(valueOne);
		AssertThat.isNotNull(valueTwo);
		// and so on
	}
}
~~~

Where 'SomeController' would have 'Dependency1' and 'Dependency2' set up in a Spring configuration file in this example.

I can't really see much benefit in this type of pre condition checking although <a href="http://twitter.com/raphscallion">Raph</a> pointed out that if we got the configuration for this bean wrong then having these assertions would allow us to get quicker feedback.

While that is true it seems to me that we would maybe achieve quicker feedback by a few seconds in return for the clutter that we end up creating in our code. We have to read those assertions every time we come to this class. 

I would prefer to have some <a href="http://www.markhneedham.com/blog/2009/09/18/tdd-testing-with-generic-abstract-classes/">specific tests for the dependency injection container</a> if we're interested in getting quick feedback in that area. 

That seems to be a cleaner solution than having these types of checks in production code or am I missing something?
