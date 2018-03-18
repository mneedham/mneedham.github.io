+++
draft = false
date="2010-06-22 22:27:58"
title="C#: StackTrace"
tag=['c']
category=['.NET']
+++

<a href="http://twitter.com/dermotkilroy">Dermot</a> and I were doing a bit of work on a mini testing DSL that we've been writing to try and make some of our interaction tests a bit more explicit and one of the things that we wanted to do was find out which method was being called on one of our collaborators.

We have a stub collaborator which gets injected into our system under test. It looks roughly like this:


~~~csharp

public class StubCollaborator : IGotForcedToCollaborate
{
	public double Method1()
	{
		return CannedValue();
	}

	public double Method2()
	{
		return CannedValue();
	}

	private double CannedValue()
	{
		return 10;
	}

}
~~~

We wanted to try and capture which of the methods on that object had been called by our system under test and then assert on that value from our test.

While trying to work out how to do this we came across the 'StackTrace' object. We use it like so to work out which public method on that object has been called:


~~~csharp

public class StubCollaborator : IGotForcedToCollaborate
{
	private MethodBase methodCalled;

	..
	
	private double CannedValue()
	{
		methodCalled =  new StackTrace().GetFrames()
                			.Select(f =>f.GetMethod())
                			.Where(m => m.DeclaringType.Name == GetType().Name)
                			.Where(m => m.IsPublic)
                			.First()
		return 10;
	}

	public string GetMethodCalled()
	{
		return methodBase.Name;
	}	

}
~~~

We needed to only find the public methods because 'CannedValue' was showing up on the stack trace and since it's private this was an easy way to exclude it.

I'm sure there are other ways to get this type of information but we were able to solve our problem really quickly with this solution.
