+++
draft = false
date="2010-05-04 18:32:28"
title="Coding: Make the mutation obvious"
tag=['coding']
category=['Coding']
+++

Although I'm generally quite opposed to coding approaches whereby we mutate objects, sometimes the way a framework is designed seems to make this a preferable option.

We came across a situation like this last week when we wanted to hydrate an object with data coming back from the browser.

The signature of the action in question looked like this:


~~~csharp

public class SomeController
{
	public ActionResult SomeAction(string id, UserData userData)
	{
	}
~~~

We were able to automatically bind most of the values onto 'UserData' except for the 'id' which was coming in from the URL.

We could have included the 'id' in a hidden field in the page to get around this problem but that seemed like a more complicated/hacky solution.

Instead what we needed to do is the following:


~~~csharp

public class SomeController
{
	public ActionResult SomeAction(string id, UserData userData)
	{
		userData.Id = id.ParseIntoId();
	}
~~~

'ParseIntoId' is an extension method which converts a string representation of an 'id' into an object representation.

While this method is fine as it is, I find that as code gets added it can sometimes be less than obvious that we've actually mutated 'UserData' so I now prefer to explicitly call that out like so:


~~~csharp

public class SomeController
{
	public ActionResult SomeAction(string id, UserData userData)
	{
		var userDataWithId = UpdateUserDataWithId(userData, id);
	}

	private UserData UpdateUserDataWithId(UserData userData, string id)
	{
		userData.Id = id.ParseIntoId();
		return userData;
	}
~~~

We would then want to use 'userDataWithId' after this point in the function.

Of course the original 'UserData' has still been mutated and it doesn't seem worth the extra code that it would take to avoid this so we'll just trust that anyone reading the code would realise that they should use 'userDataWithId' instead!
