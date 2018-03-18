+++
draft = false
date="2009-09-13 00:19:42"
title="Coding: An abstract class/ASP.NET MVC dilemma"
tag=['coding']
category=['Coding', '.NET']
+++

I previously described <a href="http://www.markhneedham.com/blog/2009/09/02/coding-reduce-fields-delay-calculations/">a refactoring that we have been working on to reduce the number of fields and delay calculations</a> and the actual goal behind this refactoring was to get the code into shape so that we could add in the logic for a new business process that our application needed to handle.

The code in question defines view models being used by different partial views which are rendered depending on the business process that the user is currently executing.

We decided that the best way to add in this new code was drive our code towards a stage where we could have an abstract class and then sub classes for each of the specific business processes around this area.

Before this we had been using the same class everywhere but it was becoming a bit too complicated to understand as we attempted to add in this new functionality - there was already scattered if/else logic for the two business processes that were already being handled in the same place.

The views were defined like this, where the generic type on 'ViewModel' is the name of the specific business process model class:

~~~text

ParentPage.aspx : ViewModel

BusinessProcess1Partial.aspx : ViewModel
BusinessProcess2Partial.aspx : ViewModel
BusinessProcess3Partial.aspx : ViewModel
~~~
The classes in question are roughly like this:

~~~csharp

public abstract class ParentModel
{
	private readonly Dependency dependency;

	public ParentModel(Dependency depedency)
	{
		this.dependency = dependency;
	}	

	public string GetValueOne()
	{
		return dependency1.GetValueOne();
	}
}

public class BusinessProcessModel1 : ParentModel
{
	public BusinessProcessModel1(Dependency dependency) : base(dependency) { }

	public int SomeBusinessProcess1SpecificThing()
	{
		// do some calculation
	}
}

public class BusinessProcessModel2 : ParentModel
{
	public BusinessProcessModel1(Dependency dependency) : base(dependency) { }

	public int SomeBusinessProcess2SpecificThing()
	{
		// do some calculation
	}
}
~~~
It worked quite well for the majority of what we wanted to do but we eventually got to the stage where there was a property which we needed on the 'ParentModel' for the 'ParentPage' which was also needed by BusinessProcessModel1 and BusinessProcessModel2 but not by BusinessProcessModel3.

We actually had the data required for that property at the time of construction of all three of the business processes so we decided to add it to the 'ParentModel' and even though it seems quite evil to do this we couldn't see an immediately obvious alternative.

Our initial thought was that perhaps we could make use of some role based interfaces and then define those interfaces as part of the 'ViewModel' generic that each page extends. As far as I understand it's not possible to do this though because any types we use with 'ViewModel' need to be classes.

An approach which we considered but didn't try out is to have a 'ParentModel' representing the top level page and then have each of the business proceess models as propertys on that.

By doing that we could reduce the need to have the class hierarchy although we would increase the complexity of the code for rendering the business process specific partials since we'd need to introduce if statements into the parent view to ensure that the correct property from that was selected.

Neither option seems that great. Has anyone found a better solution?
