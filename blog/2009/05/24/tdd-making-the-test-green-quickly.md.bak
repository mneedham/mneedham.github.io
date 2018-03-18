+++
draft = false
date="2009-05-24 23:43:28"
title="TDD: Making the test green quickly"
tag=['tdd']
category=['Testing']
+++

Although <a href="http://www.markhneedham.com/blog/2009/05/23/its-not-about-equal-keyboard-time/">I pointed out some things that I disagreed with</a> in <a href="http://ca.rroll.net/2009/05/23/is-your-pair-hogging-the-keyboard/">Nick's post about pair programming</a> one thing that I really liked in that post was that he emphasised the importance of getting tests from red to green as quickly as possible. 

<blockquote>
I remember the best programming sessions I’ve had was with Stacy Curl, now an ex-thoughtworker and whom I believe was also a chess player. He would always look to quickly make my tests pass, even if it was to just echo the output that my tests would sometimes expect.
</blockquote>

The idea that we didn't have to implement the real functionality after writing the first test for a method was an idea that I feel really freed me up when doing TDD - previous to this I had often spent a lot of time thinking how exactly I wanted to implement the code to make the test pass and I was never entirely satisfied with this approach.

Kent Beck refers to the patterns used to go from red to green quickly as the Green Bar Patterns in his book <a href="http://www.markhneedham.com/blog/2008/10/07/test-driven-development-by-example-book-review/">Test Driven Development by Example</a>.

<h3>Fake It</h3>

This was an idea which I was first introduced to a couple of years ago while pairing with Dan North - the idea is that if you don't know how to implement the real code to make a test pass you just do the minimum to <strong>make it pass by inserting a <a href="http://c2.com/cgi/wiki?FakeIt">fake implementation</a></strong>.

For example, if we have a test checking the calculation of the factorial of 5:


~~~csharp

[Test]
public void ShouldCalculateFactorial() 
{
	Assert.AreEqual(120, CalculateFactorial(5));
}
~~~

The fake implementation of this would be to return the value '120':


~~~csharp

public int CalculateFactorial(int value) 
{
	return 120;
}
~~~

I've found that it actually makes pair programming quite fun when we take this approach as it becomes a bit of a game between the two people to try and come up with a test case that forces the other person to write the real implementation code.

The thing to be careful with here is that sometimes it can actually end up being more complicated faking code for specific inputs and in these cases it may be easier to just implement the solution.

<h3>Triangulate</h3>

For me triangulating is the <strong>next step that we take after inserting a fake implementation to try and drive towards a more generic solution</strong>.

The guidance in the book is that we should look to triangulate when we have two or more examples/tests.

In the factorial example perhaps we would drive some example tests which forced us to implement the two parts of the recursive function.

Given we started with CalculateFactorial(5) our next step would probably be to calculate the factorial of 0.


~~~csharp

[Test]
public void ShouldCalculateFactorial() 
{
	Assert.AreEqual(120, CalculateFactorial(5));
	Assert.AreEqual(1, CalculateFactorial(0));
}
~~~

Leading to an implementation like this:


~~~csharp

public int CalculateFactorial(int value) 
{
	if(value == 0) return 1;
	return 120;
}
~~~

We now have one example for each branch. The next test would look to drive the implementation of the else side of the expression.


~~~csharp

[Test]
public void ShouldCalculateFactorial() 
{
	Assert.AreEqual(1, CalculateFactorial(0));

	Assert.AreEqual(24, CalculateFactorial(4));
	Assert.AreEqual(120, CalculateFactorial(5));
}
~~~

We could still try to fake the implementation here...



~~~csharp

public int CalculateFactorial(int value) 
{
	if(value == 0) return 1;
	else
	{
		if(value == 4) return 24;
		return 120;
	}
}
~~~

...although it would probably be easier to just put the obvious implementation in as that's easier than branching it out for different input values at this stage.


~~~csharp

public int CalculateFactorial(int value) 
{
	if(value == 0) return 1;
	return value * CalculateFactorial(value - 1);
}
~~~


<h3>Obvious implementation</h3>
As I alluded to above obvious implementation is <strong>where you know exactly how to implement the production code to make your test pass</strong> so you might as well just go ahead and write that code straight away.

The trap I've run into many times is thinking that I know how to make a test pass by doing the 'obvious implementation' before writing way too much code in an attempt to do so - it wasn't as obvious as I had thought! 

This is where the other two approaches can be helpful.
