+++
draft = false
date="2009-04-27 20:30:52"
title="Coding: Weak/Strong APIs"
tag=['coding']
category=['Coding']
+++

An interesting problem that I've come across a few times in the last couple of week centres around how strongly typed we should make the arguments to public methods on our objects.

There seem to be benefits and drawbacks with each approach so I'm not sure which approach is better - it possibly depends on the context.

When we have a strong API the idea is that we pass an object as the argument to a method on another object.

To given an example, recently a colleague and I were working on a little application to compare two objects and show the differences between them.

One of the decisions to be made was how to accumulate the differences. We created PropertyDifference and PropertyDifferences objects to do this, but the question became who should have the responsibility for creating the PropertyDifference.

The choice was between having PropertyDifferences API look like this:


~~~csharp

public class PropertyDifferences
{
	public void Add(PropertyDifference propertyDifference) 
	{
		// code to add a difference
	}
}
~~~

Or like this:


~~~csharp

public class PropertyDifferences
{
	public void Add(string propertyName, object actualValue, object expectedValue) 
	{
		var propertyDifference = new PropertyDifference(propertyName, actualValue, expectedValue)
		// code to add a difference
	}
}
~~~

In the former the client (ObjectComparer) needs to create the PropertyDifference before passing it to PropertyDifferences whereas in the latter that responsibility for doing that rests with PropertyDifferences.

I'm in favour of the former strong API approach which James Noble describes in his paper '<a href="http://www.laputan.org/pub/patterns/noble/noble.pdf">Arguments and Results</a>' as the Arguments Object.

What I like about this approach is that it simplifies the API of PropertyDifferences - we just have to pass in a PropertyDifference and then we don't need to worry about it. I also find it more expressive than having each of the arguments individually.

However, while reading through <a href="http://www.amazon.co.uk/Object-Design-Responsibilities-Collaborations-Addison-Wesley/dp/0201379430/ref=sr_1_1?ie=UTF8&s=books&qid=1240826439&sr=8-1">Object Design</a> this morning I've started to see that there can be some benefits in the weak API approach as well.

(from page 7 of the book)
<blockquote>
As we conceive our design, we must constantly consider each object's value to its immediate neighbourhood. Does it provide a useful service? Is it easy to talk to? Is it a pest because it is constantly asking for help?...The fewer demands an object makes, the easier it is to use.
</blockquote>

By that logic PropertyDifferences is making itself more difficult to use by demanding that it gets sent a PropertyDifference since objects which use it now need to create that object. I suppose the other way of reading that could be that if PropertyDifferences demands that it gets three different arguments instead of one then that is more demanding.

The other advantage I can see with the weak API is that we can reduce the places in the code where we new up a PropertyDifference. If we then decide to change the way that you create a PropertyDifference then we have less places to change.

The down side is that we end up coupling PropertyDifferences and PropertyDifference which maybe isn't so bad since they are fairly closely related.

I still favour having a stronger API on objects since I believe it makes objects more expressive and I currently consider that to be the most important thing when coding but weaker APIs certainly have their place too.
