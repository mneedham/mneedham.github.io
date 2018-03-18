+++
draft = false
date="2009-02-28 09:50:45"
title="Coding: Implicit vs Explicit modeling "
tag=['coding', 'modeling']
category=['Coding']
+++

When it comes to object  modeling there seem to be two distinct approaches that I have come across.

<h3>Implicit modeling</h3>

The first approach is where we do what I like to think of as implicit modeling.

With this approach we would probably use less objects than in the explicit approach and we would have objects being populated as we moved through the work flow of our application.

I call it <strong>implicit modeling because we need to imply where we are based on the internal state of our objects</strong> - we can typically work this out by seeing what is and is not set to null.

The disadvantage of this approach is that sometimes data which should have been set isn't set because an error occurred somewhere so we then end up with our object in an invalid state - it has one extra null value than it was supposed to have.

We need to understand more context to work out whether this was intentionally set to null or whether there was a problem somewhere which caused it to happen. I find myself doing a lot of debugging with this approach.

<h3>Explicit modeling</h3>

The alternate approach is to add more objects into our code which describe the work flow  and current state more explicitly.

With this approach we will probably end up writing more code than with the implicit approach and there will be more 'mapping' code written transitioning data between our objects.

The advantage of doing this is that it becomes much more easier to work out what is going on when reading the code without necessarily having to dive deep into the logic behind it. 

We spend a lot more time reading code than writing it so I'm happy to write more code if it helps to save time when others have to look at it later on.

<h3>A contrived example</h3>
To give a somewhat contrived example let's say we have a Foo in our application which we only have an identifier for when we first get it but will have a Bar and Baz later on in our application.


~~~csharp

public class Foo 
{
	public string Id {get; set;}
	public string Bar {get;set;}
	public string Baz {get; set;}
}
~~~

The implicit approach to modeling would involve setting the values of say Id and leaving Bar and Baz undefined until we have them.

The more explicit approach might involved having another object called 'FooReference' which just has the Id and then we can load the actual Foo from that:


~~~csharp

public class FooReference 
{
	public string Id {get;set;}
}

public class Foo 
{
	public Foo(FooReference fooReference, string bar, string baz}
	{
		// and so on...
	}
}
~~~

This way we can tell from just reading the code when we have a real Foo and when we just have a placeholder for it, which I think makes the code much more expressive.

<h3>Combining the two approaches</h3>

An approach which is half way between the two extremes involves being able to specifically state when we are deliberately not setting values on an object by introducing the concept of an optional or blank object for example.

I haven't tried this approach (only been told about it) but it sounds like a pretty good compromise for avoiding over complicating the code while also maintaining the expressiveness.

