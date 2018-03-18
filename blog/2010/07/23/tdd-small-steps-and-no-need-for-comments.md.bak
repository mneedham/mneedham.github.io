+++
draft = false
date="2010-07-23 02:52:03"
title="TDD, small steps and no need for comments"
tag=['tdd']
category=['Testing']
+++

I recently came <a href="http://sixrevisions.com/web-development/5-good-habits-that-will-make-you-a-better-coder/">a blog post written by Matt Ward describing some habits to make you a better coder</a> and while he presented a lot of good ideas I found myself disagreeing with his 2nd tip:

<blockquote>
2. Write Your Logic through Comments


When it comes to coding, there are many tenets and ideas I stand by. One of this is that code is 95% logic. Another is that logic doesn’t change when translated from human language into a programming language.

What this means is that if you can write it in code, you can write it in a spoken language like English or French.

...

Instead of just jumping into coding the function, <strong>I could step back and write the logic in plain English as comments.</strong>
</blockquote>

I've tried this approach before and although it can be useful I found that <strong>quite frequently I ended up with a more complicated solution</strong> than if I'd driven it out with a test first approach.

The advantage of driving the code from examples/tests is that it helps to put you in a mindset where you only need to care about one specific way that a particular object may be used.

As a result we often end up with simpler code than if we'd tried to imagine the whole design of that object up front.

I find it more difficult to keep a lot of code in my head but having just one example is relatively easy. The less code I have to think about at any one time the less mistakes I make.

As we add additional examples which describe different ways that the object may be used I've often found that the code ends up becoming more generalised and we end up with a simpler solution than we might have imagined when we started.

Matt goes on to say:
<blockquote>
This way, I can think through the full logic and try to iron out the wrinkles before I actually get into writing the code. I’ve found this to be an incredibly valuable habit that tends to result in fewer bugs.
</blockquote>

Using a TDD approach "<a href="http://www.growing-object-oriented-software.com/">allows us to describe in code what we want to achieve before we consider how</a>" so the examples that we write provide an executable specification of what we expect the code to do. 

I don't have a problem with making mistakes when coding. I make mistakes all the time but having the safety net of tests helps me fix them pretty quickly. 

Matt ends this section with the following:

<blockquote>
As a bonus, since I will rarely actually delete the comments, writing the logic through comments also means that my code will already be documented, making it easier for others to follow my logic if they ever have to work on it, or even just for myself, if I have to come back to it several months or years down the road!
</blockquote>

There are other ways of documenting code which don't involve peppering it with comments. We can <strong>write our code in a way that reveals intent</strong> such that instead of having this: 


~~~text

// FUNCTION: Lock On Time
// This function will accept two time values, indicating the range through
// which it should return an unlocked status.
  
  // Create a new data object

  // Using the data object, get the current time
  
  // IF the current time falls within the range passed to the function

    // Return false – meaning that we are currently unlocked

  // ELSE

    // Return true – meaning that we are currently locked.

  // ENDIF

// END FUNCTION
~~~

We have something closer to this:


~~~csharp

public bool ShouldBeLockedBasedOn(DateTime startOfTimeRange, DateTime endOfTimeRange)
{
	var dataObject = CreateDataObject();
	var currentTime = dataObject.CurrentTime;

	if(currentTime.IsBetween(startOfTimeRange, endOfTimeRange) 
	{
		return false;
	}
	return true;
}
~~~

...where 'IsBetween' would be an extension method on DateTime. We could have that as a private method but I think it reads better this way.

Comments don't tend to be maintained in the same way that code is from my experience so as soon as the code around them changes we'll find that they quickly become misleading rather than helpful.

There are certainly times when it makes sense to put comments in code but using them as a substitute for writing intention revealing code isn't one of those!
