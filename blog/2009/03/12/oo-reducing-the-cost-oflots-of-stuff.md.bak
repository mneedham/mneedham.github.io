+++
draft = false
date="2009-03-12 04:04:22"
title="OO: Reducing the cost of...lots of stuff!"
tag=['oop', 'object-oriented-programming']
category=['OOP']
+++

I've been working in the world of professional software development for a few years now and pretty much take it as a given that the best way to write code which is easy for other people to understand and work with is to write that code in an object oriented way.

Not everyone agrees with this approach of course and I've been told on occasions that I'm 'over object orienting' (is that even a word?) solutions. However, I think there are big advantages to be had from following an OO approach and I thought I'd explore these here.

Writing code in an object oriented way provides a way for us to manage  complexity in an application. There always seems to be some degree of complexity, even in simple looking problems, so it makes sense to look for ways to mitigate that.

I think it's fair to say that it is easier to write code in a procedural or quasi procedural/object oriented way whereby we tend to use 'objects' as data containers which we can shove data into and then take data out to use wherever we need to, and to start with we really don't see any ill effects from doing this - the application still does what it's supposed to, our acceptance tests pass and we chalk up our story points.

Then comes the time when we need to make changes to that code, and those times keep coming - <a href="http://twitter.com/discredittech/statuses/1310519088">a quote from Toby Young's presentation at QCon London</a> has him suggesting the following:

<blockquote>
92% of cost is maintaining/supporting/upgrading existing systems; only 8% on new stuff.
</blockquote>

Given that type of data I think it makes sense for us to try and make it as easy as possible to make those changes.

From my experience we tend to get this 'nightmare to change mix of object oriented and procedural code' mainly due to violations of the <a href="http://www.dcmanges.com/blog/37">law of demeter</a> i.e. putting getters on our classes and from copious use of setters which leave our objects in an inconsistent state.

We can immediately get a lot of benefits by not doing this - by setting up our objects in their constructors and by telling objects what to do rather than asking for data from them and choosing what to do with that data elsewhere.

So what are these benefits?

<h3>Reduced cost of change</h3>

One example I came across lately was to do with the creation of models to use on our views - using the ASP.NET MVC framework.

The models were being assembled somewhat similarly to this:


~~~csharp

var parentModel = new ParentModel
				  {
					ChildModel = new ChildModel
								 {
									Property1 = new OtherObject(SomeCollection(), parentModel.SomeOtherProperty);
								 }				
				  };
~~~

It starts off fairly harmless, using the object initializer syntax, but what if we decide to change Property1 to be say Property2 as happened to us?

If we had set this through the constructor then we would have only had to make the change in one place and then we could have moved on.

In actual fact it turned out that there were 4 places where we were setting Property1 - all of them from within the controller in a similar way to the above example.

After a bit of investigation I realised that only one of those cases was being tested even though the property was being constructed slightly differently in a couple of the places.

As Michael Feathers teaches us in <a href="http://www.amazon.co.uk/Working-Effectively-Legacy-Robert-Martin/dp/0131177052/ref=sr_1_1?ie=UTF8&s=books&qid=1236791368&sr=8-1">Working Effectively with Legacy Code</a> if we're going to try and refactor code we need to ensure first of all that there is a test which covers that functionality so that if we mistake we are informed of it.

This took longer than I expected due to the fact that there was quite a bit of setup needed since the only place to test this was through the controller. 

If we had followed an object oriented approach here then not only would these tests have been easier to write, but they would have been written in the first place and not got forgotten about in the mess of the controller.

In theory what was a very simple change ended up taking a few hours.

<h3>Code that is much easier to test</h3>
As I mentioned earlier when we code in an object oriented way it becomes much easier to test because the context that we need to consider in our tests is massively reduced.

In the above example we should be able to test whether of not Property1 was being set correctly directly from the ChildModel rather than having to test it from our controller. Unfortunately by having it set through a setter we can't do this in a meaningful way.

The creation of 'OtherObject' should be done inside the ChildModel and we can pass in the other data into the constructor of the class and then call Property1 in our test to see whether or not we get the expected result. We might end up with a ChildModel that looks more like this:


~~~csharp

public class ChildModel
{
	public ChildModel(IEnumerable<string> someCollection, string selectedValue)
	{
		this.someCollection = someCollection;
		this.selectedValue = selectedValue;
	}
	
	public SomeObject Property1
	{
		get 
		{
			return new SomeObject(someCollection, selectedValue);
		}
	}
}	
~~~

I know the example is contrived but hopefully the idea that putting this type of logic leads to easier to test units of code is clear.

<h3>Less need to debug</h3>
Another truly annoying consequence of creating train wreck code is that you end up with null pointer/reference exceptions all over the place and it's quite difficult to immediately tell which part of the train caused the problem.

Since it would take a long time to get that segment of code under test and identify the problem that way out comes the debugger so that we can find out what went wrong.

It might help solve the problem this time but unless we change our coding style to remove this type of problem from happening then it's just as likely to happen again tomorrow and we'll be back to square one.

I hate using the debugger - it takes a long time to step through code compared to a TDD cycle and once you've solved the problem there isn't an executable example/test that you can run to ensure that it doesn't make a reappearance.

If we can write our code in an object oriented fashion then we pretty much remove this problem and our time can be spent much more effectively adding real value to our application.
