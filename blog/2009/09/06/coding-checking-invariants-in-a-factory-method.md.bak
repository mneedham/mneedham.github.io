+++
draft = false
date="2009-09-06 00:46:01"
title="Coding: Checking invariants in a factory method"
tag=['coding']
category=['Coding']
+++

Something which we discussed quite frequently when studying <a href="http://domaindrivendesign.org/">Domain Driven Design</a> in our technical book club earlier this year was where the code which checked whether we had setup an object correctly should reside.

Shortly after that I suggested that I <a href="http://www.markhneedham.com/blog/2009/02/14/coding-assertions-in-constructors/">didn't think it should go in the constructor of an object</a> but that we should rely on objects to be good citizens and not pass in null values or the like to other objects.

However, for code that's on the edge of our system we can't really rely on that approach so our code needs to be a bit more defensive. 

On those occasions an approach which seems to work relatively well is to introduce a factory method which is responsible for creating an object or throwing an exception if the object can't be created in a consistent state. 

<a href="http://intwoplacesatonce.com/">Dave</a> and I made use of this pattern while working on some code to get a 'User' object into our system.

We realised that there were three different scenarios that we needed to handle:

<ul>
<li>All the authentication details for a user were available in the headers of the HTTP request <ul><li>Create a logged in user</li></ul></li>
<li>There were no authentication details available for a user
<ul><li>Create an anonymous user</li></ul></li>
<li>Some of the authenticated details for a user were available - something has gone wrong
 <ul><li>Throw an exception</li></ul></li>
</ul>

We created a method with the following signature:


~~~csharp

public static User CreateUserFrom(NameValueCollection headers)  { }
~~~

'headers' are the values that we retrieve from the HTTP request headers.

Whenever I've used static factory methods on an object previusly, it's mainly been for providing a way of creating an object while giving the client more information on the specific type of object that they are about to create. 

As Dave pointed out, the factory method is also useful for providing a simplified interface to clients and allowing the factory to take away some of the complexity of the object creation which is what we wanted to do here.

We ended up with code that looked a bit like this:


~~~csharp

public class User
{
	public static readonly User Anonymous = new AnonymousUser("", "");

	private readonly string userName;
	private readonly string customerId;

	private User(string userName, string customerId)
	{
		this.userName = userName;
		this.customerId = customerId;
	}

	public static User CreateUserFrom(NameValueCollection headers)  
	{ 
		var userName = headers["user-name-header-tag"];
		var customerId = headers["customer-id-header-tag"];

		var invariants = new List<string> { userName, customerId };

		if(invariants.All(i => i == null)
		{
			return Anonymous;
		}

		if(invariants.Any(i => i == null)
		{
			throw new Exception("Attempt to create user failed as not all header tags were available");
		}
	
		return new User(userName, customerId);
	}
}

public AnonymousUser : User
{
	public AnonymousUser(string userName, string customerId) : base(userName, customerId) {}
}
~~~

In this example 'AnonymousUser' is an implementation of the <a href="http://en.wikipedia.org/wiki/Null_Object_pattern">null object pattern</a>.  

When discussing our approach with <a href="http://lizdouglass.wordpress.com/">Liz</a> she reminded me that Eric Evans actually talks about invariant handling in the book and suggests that checking invariants in factory methods certainly is appropriate on some occasions:

<blockquote>
A FACTORY is responsible for ensuring that all invariants are met for the object or AGGREGATE it creates; yet you should always think twice before removing the rules applying to an object outside that object. The FACTORY can delegate invariant checking to the product, and this is often best.

But FACTORIES have a special relationship with their products. They already know their product's internal structure, and their entire reason for being involves the implementation of their product. Under some circumstances, there are advantages to placing invariant logic in the FACTORY and reducing clutter in the product. This is especially appealing with AGGREGATE rules (which span many objects). It is especially unappealing with FACTORY METHODS attached to other domain objects.
</blockquote>

I'm not sure if what we have is an aggregate root since 'User' doesn't act as the gateway to access any other objects but the approach seemed to work reasonably well here nonetheless.
