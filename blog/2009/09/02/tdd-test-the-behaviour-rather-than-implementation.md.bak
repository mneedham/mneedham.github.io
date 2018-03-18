+++
draft = false
date="2009-09-02 00:42:52"
title="TDD: Test the behaviour rather than implementation"
tag=['tdd']
category=['Testing']
+++

I <a href="http://www.markhneedham.com/blog/2009/08/30/coding-group-the-duplication-then-remove-it/">previously wrote about some duplicated code</a> we'd taken the time to remove from our code base and one something else that we found when working with this code is that a lot of the tests around this code were testing the implementation/internal state of the object rather than testing the behaviour that they expected to see.

I find it makes more sense to test the behaviour since this is the way that the object will most likely be used in our production code.

For example, in the code I posted previously we were setting up the way that a navigation bar was going to behave in different scenarios.

This was one of the tests we had:

~~~csharp

public void ShouldSetLogin()
{
	var navigationModel = new NavigationModel(Options.Login);
	Assert.IsTrue(navigationModel.IsConfiguredWith(Options.Login));
}
~~~

For this (cut down for example purposes) code:

~~~csharp

public enum Options 
{
	Login = 1,
	Logout = 2
	// and so on
}
~~~


~~~csharp

public class NavigationModel
{
	public NavigationModel(Options options)
	{
		Configuration = options;
	}

	public Options Configuration { get; private set; }


	public bool IsConfiguredWith( Options expectations)
	{
		return expectations == Configuration & expectations);
	}

	public bool ShowLogin() 
	{
		return IsConfiguredWith(Options.Login);
	}
}
~~~

There were 7 different types of options as I mentioned in the previous post and the NavigationModel was being setup with each of them and the 'IsConfiguredWith' method was then being called to check whether the value had been set. 

The strange thing was that everything we wanted to test could be done by calling methods like 'ShowLogin' which  made us of the 'IsConfiguredWith' method anyway.

The first refactoring was therefore to change the tests to make use of these methods instead of calling on an implementation detail of the NavigationModel:


~~~csharp

public void ShouldShowLogin()
{
	var navigationModel = new NavigationModel(Options.Login);
	Assert.IsTrue(navigationModel.ShowLogin());
}
~~~

There's not really that much difference in what the test does in this case but by changing all the tests to make calls to the methods that we use in our production code we were able to make the 'IsConfiguredWith' method private which is quite nice since it was only being used inside the tests and the 'Show...' methods so it didn't really make sense to have them public.

The next step after this was to create the factory methods that I mentioned in the previous post and since each of these methods encapsulated more behaviour the tests started to look a bit better:


~~~csharp

public void ShouldShowLoginAndOption1AndOption2ForAnonymousUser()
{
	var NavigationModel = NavigationModel.ForAnonymousUser();

	Assert.IsTrue(navigationModel.ShowLogin());
	Assert.IsTrue(navigationModel.ShowOption1());
	// and so on
}
~~~

This is quite a simple example but I found it interesting that with just a little bit of tweaking we could change our tests to execute the same methods that will be run in production and combined with the other refactoring we can now encapsulate the way we are determining whether a user can see a certain option or not and potentially change the implementation of that in the future if we want to.
