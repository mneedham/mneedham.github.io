+++
draft = false
date="2009-10-28 22:43:01"
title="Coding: Connascence - Some examples"
tag=['coding']
category=['Coding']
+++

I've been reading Meilir Page Jones' '<a href="http://www.amazon.co.uk/Fundamentals-Object-oriented-Design-Object-Technology/dp/020169946X/ref=sr_1_3?ie=UTF8&s=books&qid=1256562881&sr=8-3">Fundamentals of Object Oriented Design in UML</a>' recently and one of the chapters that I found the most interesting is the one where he talks about 'connascence'.

Connascence describes the relation between two different bits of code and two bits of code are said to be connascent if <strong>a change to one bit of code would require a change to the other bit of the code </strong> or if <strong>some change to another piece of code would require both bits of code to change</strong> for our program to still be correct.

I think this principal is quite similar to the idea of <a href="http://www.markhneedham.com/blog/2009/08/25/coding-coupling-and-expressiveness/">coupling</a> which we seem to use more frequently these days but I found it quite compelling that as I was reading through the different types of connascence that Page-Jones describes I was easily able to identify mistakes I've made and seen made in code.

There are many different types of connascence and Jim Weirich goes through many of them in his presentation from <a href="http://mwrc2009.confreaks.com/">MountainWest RubyConf 2009</a>  titled '<a href="http://mwrc2009.confreaks.com/14-mar-2009-18-10-the-building-blocks-of-modularity-jim-weirich.html">The building blocks of modularity</a>'. 

I'll just cover a couple of the ones that seem to cause the most pain from my experience.

<h3>Connascence of execution</h3>
This describes the situation where <strong>two different lines of code have to be executed in a certain order for the program to be executed correctly</strong>.

A typical example of this type of connascence occurs when we <a href="http://www.markhneedham.com/blog/2009/09/16/coding-watch-out-for-mutable-code/">make use of setter methods to construct objects</a>:


~~~csharp

public void SomeMethod()
{
	var someObject = new SomeObject();
	someObject.Property1 = new Property1();

	// some where else far far away

	SomeOtherMethod(someObject);
}

private void SomeOtherMethod(SomeObject someObject)
{
	someObject.Property1.AnotherProperty = new AnotherProperty();
}
~~~

In this example we need line 2 to be executed before line 13 otherwise we'll get a null pointer exception. These two lines therefore have connascence of execution.

Quite often line 13 of this example would be hidden away in a chain of method calls and it wouldn't be completely obvious that it relies on a line further up being executed first.

We eventually end up making what we think is an innocuous reordering of the method calls and suddenly our code doesn't work any more.

In this case to reduce this type of connascence we might look at using a constructor to create our objects, use one of the builder/factory patterns or at least try and capture related code in the same method so that the potential for confusion is reduced.

<h3>Connascence of algorithm</h3>
This typically <strong>describes the situation where we are making use of a data structure in a specific way such that all the pieces of code which interact with that data structure need to know exactly how that data structure works in order to make use of it</strong>. 

This problem seems to happen particularly when we're <a href="http://www.markhneedham.com/blog/2009/10/23/coding-the-primitive-obsession/">over using lists when perhaps another level of abstraction is required</a>.

One example of this might be where a piece of code assumes that another piece of code inserts a certain value into a list.


~~~csharp

public class AClassWhichPutsASpecificItemInAList
{
	public List<SomeObject> CreateTheEvil()
	{
		var myEvilList = new List<SomeObject>();

		myEvilList.Add(new SomeObject("SomeSpecialName"));
		// and so on

		return myEvilList;
	}
}
~~~


~~~csharp

public class SomeOtherClassFarFarAway
{
	public void SomeMethod(List<SomeObject> someObjects)
	{
		var speciallyNamedObject = someObjects.Where(s.Name == "SomeSpecialName").First();
	}
}
~~~

Despite the fact that these two classes never refer to each other they have connascence of algorithm because if 'AClassWhichPutsASpecificItemInAList' decides not to put that value into the list then 'SomeOtherClassFarFarAway' may stop working so we will need to change that as well.

This type of connascence is much more implicit than some of the other types and it may not be immediately obvious that two pieces of code are related.

We could get around this problem by encapsulating this type of logic in its own type so that at least we only have to deal with it once. 

The goal is to try and <a href="http://www.markhneedham.com/blog/2009/04/23/ddd-making-implicit-concepts-explicit/">make an implicit piece of code more explicit</a>.

<h3>Connascence of convention</h3>
This describes the situation where there is <strong>an implicit convention for the meaning behind the value of a certain piece of code such that every other bit of code that touches it needs to know this convention</strong>. This is quite similar to connascence of algorithm.

An example that I came across recently was around how we passed around the value of an option selected on a form by the user.

The user could either select 'Yes', 'No' or they could choose not to answer the question. If they entered 'Yes' then they would need to answer another question immediately after this.

Later on we needed to pass this data to the service layer. A value of 'No' if they selected that, the answer to the next question if they answered 'Yes' and 'None' if they didn't enter anything. 

We ended up having code similar to this in the service call and then again in the binder:


~~~csharp

public class TheServiceThatUsesThatValue
{
	public void CallTheService(string theAnswer)
	{
		var theRequest = new ServiceRequest();

		if(theAnswer == "None")
		{
			theRequest.TheAnswer = "None";
		}
		else if(theAnswer == "No")
		{
			theRequest.TheAnswer = "No";
		}
		else
		{
			theRequest.TheAnswer = LookUpTheCodeFor(theAnswer);
		}

	}	
}
~~~

We eventually gave up on the idea of passing 'None' around because that was the bit causing the most confusion. Instead we stored the answer in a nullable data type and then did the conversion to 'None' when necessary in the Service class.

<h3>In summary</h3>
There are just a couple of the examples that Page-Jones outlines but the general idea is that we want to try and minimise the connascence in our system by creating well encapsulated objects.

Within those objects it makes sense to keep connascence high and in fact if it's not then it might suggest that we have another object waiting to get out. 
