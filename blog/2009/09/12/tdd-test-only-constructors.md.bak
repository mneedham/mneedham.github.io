+++
draft = false
date="2009-09-12 00:35:12"
title="TDD: Test only constructors"
tag=['tdd']
category=['Testing']
+++

I <a href="http://www.markhneedham.com/blog/2009/09/06/coding-checking-invariants-in-a-factory-method/">wrote previously how we'd been doing some work to change the way that we get a 'User' object into our system</a> and one mistake that we made intially was to have another constructor on the 'User' object which was being used in all our unit tests which involved the user in some way.

The original reason that this 'test constructor' was created was to make it easier to construct a 'fake user' which we were using in some of our functional tests but had ended up being used in unit tests as well.

The constructor being exposed for testing was pretty much the same as the private constructor that we have now.

~~~csharp

public class User
{
	...
	public User(string userName, string customerId)
	{
		this.userName = userName;
		this.customerId = customerId;
	}
}~~~
The problem with this approach to testing is that we aren't actually testing the code which we're using in production so even if the tests pass it doesn't actually tell us very much about our code.

We could be doing everything right in this test constructor and doing something crazy in the static factory method and we wouldn't find out until much later on.

The interesting thing is that the method that we call from the production code isn't as testing friendly as the one we had made public just for testing:

~~~csharp

	public static User CreateUserFrom(NameValueCollection headers)
	{
		var userName = headers["user-name-header-tag"];
		var customerId = headers["customer-id-header-tag"];

		// and so on

		return new User(userName, customerId);
	}~~~
In order to make our test setup code use this method we had to create a NameValueCollection containing key/value pairs with the appropriate keys that reside in the headers of requests coming into our application.

We therefore end up with code similar to this in the test data builder:

~~~csharp

public class UserBuilder
{
	...

	public User Build()
	{
		var headers = new NameValueCollection();
		headers.Add("user-name-header-tag", "randomName");
		headers.Add("customer-id-header-tag", "customerId");
		User.CreateUserFor(headers);
	}
}~~~
This leaks a bit of the implementation of 'CreateUserFrom' into the tests but I prefer this to testing something which is never actually used.
