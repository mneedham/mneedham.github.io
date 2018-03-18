+++
draft = false
date="2009-05-26 13:20:01"
title="Refactoring: Removing duplication more safely"
tag=['coding', 'refactoring']
category=['Coding', 'Incremental Refactoring']
+++

One of the most important things that I've learnt from the <a href="http://www.markhneedham.com/blog/category/coding-dojo/">coding dojo sessions</a> that we've been running over the last six months is the importance of <a href="http://www.markhneedham.com/blog/2009/05/15/coding-dojo-14-rock-scissors-paper-tdd-as-if-you-meant-it/">small step refactorings</a>.

Granted we have been trying to take some of the practices to the extreme but the basic idea of trying to <strong>keep the tests green</strong> for as much time as well as <strong>keeping our code in a state where it still compiles </strong>(in a static language) is very useful no matter what code we're working on.

Recently a colleague and I were doing some work on our code base to try and remove some duplication - we had two classes which were doing pretty much the same thing but they were named just slightly differently.

The implementation was also slightly different - one was a list containing objects with Key and Value properties on and the other was a dictionary/map of key/value pairs.

We spent a bit of time checking that we hadn't misunderstood what these two different classes were doing and having convinced ourselves that we knew what was going on decided to get rid of one of them - one was used in around 50% more places than the other so we decided to keep that one.

We now needed to replace the usages of the other one. 

My pre-coding dojo refactoring approach would have been to just find the first place that the one we wanted to replace was being used, delete that and then let the compiler guide me to replacing all its usages and then do that with the second usage and so on.

The problem with this approach is that we would probably have had the code in a state where it didn't compile for maybe half an hour, leading to a situation where we would be unable to run our tests for any of this time which would mean that we would lose confidence that the changes we were making actually worked.

The approach we therefore took was to add in the class we wanted to keep side by side with the one we wanted to get rid of and slowly move our tests across to setup data for that.

We therefore ended up with code looking a bit like this to start with:


~~~csharp

public class IHaveUsages
{
	public IDictionary<OldType, string> OldType { get; set; }
	public IList<NewType> OldType2 { get; set; }
}
~~~

When changing tests we took the approach of commenting out the old setup code to start with so that we could see exactly what was going on in the setup and then delete it once we had done so. I've written previously about my <a href="http://www.markhneedham.com/blog/2009/01/17/the-danger-of-commenting-out-code/">dislike for commented code</a> but we were using it in this case as a mechanism to guide our refactoring and we didn't ever check the code in with these comments in so I think it was a reasonable approach. 


~~~csharp

[Test]
public void SomeTest()
{
	// some test stuff
	new IHaveUsages 
	{
		// OldType = new Dictionary<OldType, string> {{new OldType("key"), "value"}},
		OldType2 = new List<NewType> { new NewType { Key = "key", Value = "value" } } 
	}
}
~~~

The intention was to try and reduce the number of places that OldType was being used until the point where there were none left which would allow us to safely remove it.

Once we had made that change to the test setup we needed to make the changes in the class using that data to get our green bar back.

On a couple of occasions we found methods in the production code which took in the OldType as a parameter. In order to refactor these areas we decided to take a copy of the method and renamed it slightly before re-implementing it using the NewType.


~~~csharp

private void OldMethod(OldType oldType) 
{
	// Do some stuff
}
~~~


~~~csharp

private void OldMethod2(NewType newType) 
{
	// replicate what's being done in DoSomeStuffOn
}
~~~

We then looked for the usages of 'OldMethod' and replaced those with calls to 'OldMethod2', also ensuring that we passed in NewType to the method instead of OldType.

I'm intrigued as to whether there is an even better way to perform this refactoring - when I chatted with <a href="http://pilchardfriendly.wordpress.com/">Nick</a> about this he suggested that it might have been even easier to create a temporary inheritance hierarchy with NewType extending OldType. We could then just change any calls which use OldType to use NewType before eventually getting rid of OldType.

I haven't tried this approach out yet but if it makes our feedback cycle quicker and chances of failing less then I'm all for it.
