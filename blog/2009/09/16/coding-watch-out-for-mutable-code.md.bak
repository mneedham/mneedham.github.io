+++
draft = false
date="2009-09-16 23:31:58"
title="Coding: Watch out for mutable code"
tag=['coding']
category=['Coding']
+++

I've been doing some more work recently on trying to <a href="http://www.markhneedham.com/blog/2009/09/02/coding-reduce-fields-delay-calculations/">reduce the number of fields in some of our classes and moving any logic related to calculations into the methods that use the logic</a> but managed to break part of our application recently by doing that a bit too casually and not realising that the code I'd inlined was actually being mutated later on.

The code I'd refactored originally looked like this:


~~~csharp

public class MutableFactory
{
	public MutableClass BuildMyMutableClass() 
	{
		var mutableClass = new MutableClass() 
		{
			MutableProperty = new MutableProperty() {
				RandomValue = true
			};
		}; 


		// later on in the code and hidden away in another method
		mutableClass.MutableProperty.RandomValue = false;
	}
}

public class MutableClass
{
	public MutableProperty MutableProperty { get; set; }
} 

public class MutableProperty
{
	public bool RandomValue { get; set; }
}
~~~

After I refactored it this is what it looked like:


~~~csharp

public class MutableFactory
{
	public MutableClass BuildMyMutableClass() 
	{
		var mutableClass = new MutableClass();

		// later on in the code and hidden away in another method
		mutableClass.MutableProperty.RandomValue = false;
	}
}

public class MutableClass
{
	public MutableProperty MutableProperty 
	{ 
		get 
		{ 
			return new Mutable { RandomValue = true }; 
		}
	}
} 

public class MutableProperty
{
	public bool RandomValue { get; set; }
}
~~~

Originally when we retrieve 'mutableClass.Mutable.RandomValue' it has a value of 'false' but after the refactoring it always returns 'true'

As a result of my inlining the logic, whenever that property was called the logic was recalculated and the mutation of the data which had happened earlier on was lost.

Luckily my colleague Matt Dunn spotted that this was what was happening while we were running the code through the debugger but we shouldn't have even needed to resort to that in the first place!

The mistake I made here was not to check the test coverage around this bit of code before I made the change, something which Michael Feathers emphasises constantly in <a href="http://www.amazon.co.uk/Working-Effectively-Legacy-Michael-Feathers/dp/8131715078/ref=sr_1_3?ie=UTF8&s=books&qid=1253107118&sr=8-3">Working with Legacy Code</a>.

I was under the assumption that the changes I was making were very minimal and wouldn't actually break anything! In hindsight I should have put a test around this code first and then done the refactoring. 

If I'd done that then the mutation would have quickly become obvious to me i.e. <a href="http://dahliabock.wordpress.com/2009/09/16/why-one-should-not-live-without-tests/">the feedback loop would have been significantly quicker than it was</a>. 

We do now have tests around the offending code and an additional benefit of working out how to test this functionality was that we noticed how many dependencies the object was actually relying on and have started taking steps to try and solve that problem.

Taking a step back from this situation I'm still of the belief that having setters all over the place is really not a good idea - <a href="http://www.markhneedham.com/blog/2009/05/23/coding-setters-reduce-trust/">we lose trust in the code</a> since we don't know when an object might be mutated and that mutation may happen in ways that we don't expect. 

Maybe we don't need every object in our system to be <a href="http://www.infoq.com/articles/dhanji-prasanna-concurrency">immutable</a> but I think we could get away with having much more immutability than we do now, certainly in the code base I'm working on. 
