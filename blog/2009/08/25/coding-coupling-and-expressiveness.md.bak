+++
draft = false
date="2009-08-25 22:42:55"
title="Coding: Coupling and Expressiveness"
tag=['coupling']
category=['Coding']
+++

We came across an interesting situation in our code base recently whereby two coding approaches which I consider important for writing maintainable code seemed to come into conflict with each other.

The code we were working on needed to retrieve some customer details from a backend system by making use of the current user's 'customerId' which we can retrieve from the 'LoggedInUser'.

My initial thought was that since we only needed one property of the 'LoggedInUser' we could just pass in the 'customerId' instead of the 'LoggedInUser':


~~~csharp

public class Repository
{
	public Customer RetrieveCustomer(string customerId)
	{
		var backEndSystemCustomer = backEndSystem.RetrieveCustomer(customerId);
		return MapCustomer(backEndSystemCustomer);
	}
}
~~~

Which we would use like this:

~~~csharp

public class SomeController
{
	...
	public ActionResult DoSomething()
	{
		repository.RetrieveCustomer(loggedInUser.CustomerId);
		// and so on
	}
}
~~~

I recently came across quite a nice post which explains <a href="http://codeodor.com/index.cfm/2009/6/17/Strive-for-low-coupling-and-high-cohesion-What-does-that-even-mean/2902">different types of cohesion and coupling</a> that we might find in our code and from my understanding the above code has data coupling which is the loosest type of coupling that we can have apart from message coupling:

<blockquote>Data coupling is when modules share data through, for example, parameters. Each datum is an elementary piece, and these are the only data which are shared (e.g. passing an integer to a function which computes a square root).</blockquote>

It seemed to me that it was better to couple the repository to the data it required rather than to the 'LoggedInUser' which would be stamp coupling:

<blockquote>Stamp coupling (Data-structured coupling) is when modules share a composite data structure and use only a part of it, possibly a different part (e.g. passing a whole record to a function which only needs one field of it). This may lead to changing the way a module reads a record because a field, which the module doesn't need, has been modified.</blockquote>

In this case I was thinking about coupling of classes instead of coupling of modules (perhaps wrongly?)

Discussing this with <a href="http://intwoplacesatonce.com/">Dave</a>, he pointed out that the method wasn't really very expressive and that it is actually possible to pass in any string we want - even one that might not even be a customerId. The chance of making a mistake when using this API is quite high.

We therefore changed the method signature so that it takes in a 'LoggedInUser' instead and then just takes the 'customerId' from that object.

We only build a 'LoggedInUser' from one place in our application and everyone on the team knows that so it's much less likely that someone would make a mistake and pass in the wrong instance.


~~~csharp

public class Repository
{
	public Customer RetrieveCustomer(LoggedInUser user)
	{
		var backEndSystemCustomer = backEndSystem.RetrieveCustomer(user.CustomerId);
		return MapCustomer(backEndSystemCustomer);
	}
}
~~~

I think the code is definitely nicer like this although LoggedInUser and Repository are now coupled even though the repository only cares about one property of LoggedInUser.

It seems to me though that the main reason we care about coupling is that loosely coupling our code makes it easier to change but on the other hand making our code more expressive makes it easier to read which is also important for making it easy to change.

Maybe it's not such a big deal anyway - I just found it interesting that I thought I'd done the right thing and it turned out that a way I had previously rejected turned out to be more appropriate.
