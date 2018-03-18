+++
draft = false
date="2009-08-30 13:13:50"
title="Coding: Group the duplication, then remove it"
tag=['coding']
category=['Coding']
+++

One of the most common activities for software developers is removing duplication from code and <a href="http://intwoplacesatonce.com/">Dave</a> recently showed me a technique which I hadn't seen before for doing this more effectively -  first group all the code into one place without removing any of the duplication and then remove the duplication when everything is in one place.

The code where we tried out this technique was being used to construct the model for the navigation at the top of the pages on the website we're working on and before we grouped the duplication the code looked a bit like this:


~~~csharp

public enum Options 
{
	Login = 1,
	Logout = 2
	// and so on
}

public class NavigationModel
{
	public NavigationModel(Options options, string messageOne, string messageTwo)
	{
		Configuration = options;
		MessageOne = messageOne;
		MessageTwo = messageTwo;
	}

	public Options Configuration { get; private set; }
	public string MessageOne { get; private set; }
	public string MessageTwo { get; private set; }
}
~~~

Which was then used in other parts of the code base like this:


~~~csharp

var messageOne = someRepository.GetMessageOne();
var messageTwo = someRepository.GetMessageTwo();
var navigationModel = new NavigationModel(Options.Login, messageOne, messageTwo);
~~~


~~~csharp

var messageOne = someRepository.GetMessageOne();
var messageTwo = someRepository.GetMessageTwo();
var navigationModel = new NavigationModel(Options.Logout, messageOne, messageTwo);
~~~

There are actually 7 different types of 'Options' and the 'NavigationModel' was setup in 6 different places across 3 different controllers.

The first step was to create a static factory method on 'NavigationModel' for each of the different configurations without trying to remove the duplication, just putting it all in one place.


~~~csharp

public class NavigationModel
{
	public NavigationModel(Options options, string messageOne, string messageTwo)
	{
		Configuration = options;
		MessageOne = messageOne;
		MessageTwo = messageTwo;
	}

	public static NavigationModel ForLoggedInUser(IRepository someRepository)
	{
		var messageOne = someRepository.GetMessageOne();
		var messageTwo = someRepository.GetMessageTwo();
		return new NavigationModel(Options.Logout, messageOne, messageTwo);
	}

	public static NavigationModel ForAnonymousUser(IRepository someRepository)
	{
		var messageOne = someRepository.GetMessageOne();
		var messageTwo = someRepository.GetMessageTwo();
		return new NavigationModel(Options.Login, messageOne, messageTwo);
	}

	public Options Configuration { get; private set; }
	public string MessageOne { get; private set; }
	public string MessageTwo { get; private set; }
}
~~~

All we've done is move the code from the controller into the 'NavigationModel' but already the duplication seemed more obvious. 

Being forced to come up with a name for each of the creation methods actually made it more obvious that in the case of the anonymous user there was no need to make any calls to the repository since 'MessageOne' and 'MessageTwo' would never be used in this case. 

We hadn't realised that this was the case until everything was grouped but it meant that we could save an unnecessary network call to get that data which is always good.

Another interesting side effect was that we realised that two of the creation methods we had just written were exactly the same which allowed us to remove one of them.

The next step was to push the repository calls into the constructor which is now private since noone calls it from outside this class any more:


~~~csharp

public class NavigationModel
{
	private NavigationModel(Options options, IRepository someRepository)
	{
		Configuration = options;
		MessageOne = someRepository.GetMessageOne();
		MessageTwo = someRepository.GetMessageTwo();
	}

	private NavigationModel(Options options)
	{
		Configuration = options;
		MessageOne = "";
		MessageTwo = "";
	}

	public static NavigationModel ForLoggedInUser(IRepository someRepository)
	{
		return new NavigationModel(Options.Logout, someRepository);
	}

	public static NavigationModel ForAnonymousUser(IRepository someRepository)
	{
		return new NavigationModel(Options.Login);
	}

	public Options Configuration { get; private set; }
	public string MessageOne { get; private set; }
	public string MessageTwo { get; private set; }
}
~~~

The thinking for the next step which we haven't done as yet is to delay the call to 'someRepository' until it is actually needed by converting 'MessageOne' and 'MessageTwo' into methods which delegate to it.

I'm not sure of the best way to handle the case where either of those methods were called for the anonymous user case where we don't actually have a repository - perhaps the best way would be to create a <a href="http://www.markhneedham.com/blog/2008/08/16/null-handling-strategies/">null object version</a> of the repository I'm not sure?

I was initially unsure how following this approach would be beneficial and I wanted to just remove the duplication straight away instead of grouping it first but from this experience I can certainly see how useful it can be.
