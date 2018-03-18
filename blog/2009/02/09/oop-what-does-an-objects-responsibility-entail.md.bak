+++
draft = false
date="2009-02-09 16:52:10"
title="OOP: What does an object's responsibility entail?"
tag=['oop']
category=['OOP']
+++

One of the interesting discussions I've been having recently with some colleagues is around where the responsibility lies for describing the representation of an object when it is to be used in another bounded context - e.g. on the user interface or in a call to another system.

I believe that an object should be responsible for deciding how its data is used rather than having another object reach into it, retrieve its data and then decide what to do with it. 

Therefore if we had an object Foo whose data was needed for a service call to another system my favoured approach would be for Foo to populate the FooMessage with the required data.


~~~csharp

public class Foo 
{
	private string bar;

	public Foo(string bar)
	{
		this.bar = bar;
	}

	public void Populate(IFooMessage fooMessage) 
	{
		fooMessage.Bar = bar;
	}
}
~~~


~~~csharp

public interface IFooMessage 
{
	string Bar { get; set; }
}
~~~


~~~csharp

public class FooMessage : IFooMessage
{
	public string Bar { get; set; }
}
~~~

The advantage of this approach is that Foo has kept control over its internal data, encapsulation has been preserved. Although we could just expose 'Bar' and make it possible to build the FooMessage from somewhere else, this violates Tell Don't Ask and opens up the possibility that Foo's internal data could be used elsewhere in the system outside of its control.

The question to be answered is <strong>whether or not it should be Foo's responsibility to generate a representation of itself</strong>. In discussion about this it was suggested that Foo has more than one responsibility if we design the class as I have.

Uncle Bob's definition of the Single Responsibility Principle (SRP) in Agile Software Development: Principles, Patterns and Principles describes it thus:

<blockquote>
A class should have only one reason to change.
</blockquote>

In this example Foo would need to change if there was a change to the way that it needed to be represented as an IFooMessage as well as for other changes not related to messaging. Foo is not dependent on a concrete class though, only an interface definition, so the coupling isn't as tight as it might be.

It might just be my interpretation of SRP but it seems like there is a trade off to be made between ensuring encapsulation and SRP in this instance.

The other way to create a FooMessage is to <strong>create a mapper class</strong> which takes the data out of the Foo class and then creates the FooMessage for us. 

We might end up with something like this:


~~~csharp

public class FooMapper 
{
	public FooMessage ConvertToMessage(Foo foo) 
	{
		return new FooMessage { Bar = foo.Bar; }
	}
}
~~~

Whereby Foo needs to expose Bar as a property in order to allow this mapping to be done.

This is somewhat similar to the way that NHibernate handles the persistence and loading of objects for us - unless we use the Active Record pattern an object is not responsible for saving/loading itself. 

What I don't like about this approach is that it doesn't strike me as being particularly object oriented - in fact the mapper class would be an example of an <a href="http://jupitermoonbeam.blogspot.com/2008/09/agent-nouns-are-code-smells.html">agent noun class</a>.

A cleaner solution which allows us to keep encapsulation in tact would be to make use of reflection to build the FooMessage from our mapper, probably by creating private properties on Foo as they are easier to reflect on than fields. The downside to the reflection approach is that code written in this way is probably more difficult to understand.

I know I've oversimplified the problem with my example but ignoring that, where should this type of code go or do we choose to make a trade off between the two approaches and pick which one best suits our situation?
