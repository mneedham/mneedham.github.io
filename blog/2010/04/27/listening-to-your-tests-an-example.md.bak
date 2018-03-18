+++
draft = false
date="2010-04-27 22:34:22"
title="Listening to your tests: An example"
tag=['coding']
category=['Coding']
+++

I was recently reading a blog post by Esko Luontola where he talks about <a href="http://blog.orfjackal.net/2010/04/direct-and-indirect-effects-of-tdd.html">the direct and indirect effects of TDD</a> and one particularly interesting point he makes is that driving our code with a TDD approach helps to amplify the problems caused by writing bad code.

<blockquote>
if the code is not maintainable, it will be hard to change. Also if the code is not testable, it will be hard to write tests for it. If the code would not be written iteratively and no tests would be written for it, life would be much easier to the developer. In other words, TDD increases the pain caused by bad code, because it's not possible to avoid changing the code, nor avoid writing tests for it.
</blockquote> 

This is something Steve Freeman and Nat Pryce talk about in <a href="http://www.growing-object-oriented-software.com/">their book</a> and we recently had an example of this which really stemmed from a <a href="http://www.markhneedham.com/blog/2010/04/18/coding-another-outside-in-example/">failure to drive this particular piece of code from the outside in</a>.

We'd reached the stage where one object was taking in 8 different parameters in the constructor and then only used 2 of them in any one path through the code.

The code was pretty bad but it was even more noticeable how much of a mess we'd made when we had to write a new test.

This is a rough example of what the test fixture had begun to look like:


~~~csharp

[TestFixture]
public class BadObjectTests
{
	private double parameter1 = 0.10;
	private double parameter2 = 0.20;
	private double parameter3 = 0.30

	[Test]
	public void ATestGoneABitWrong()
	{
		var badObject = CreateBadObject();
		var result = badObject.CalculateSomething()

		Assert.That(result, Is.EqualTo(parameter1));
	}

	private BadObject CreateBadObject()
	{
		return new BadObject(parameter1, parameter2, parameter3...);
	}
}
~~~

As a general guideline it's good if we're able to keep the context of a test all in one place but since the 'BadObject' had become increasingly difficult to construct we'd pulled that out into another method and extracted all its parameters as fields in the test fixture.

The alternative was to have all 8 parameters created in each test and then construct the 'BadObject' each time and in retrospect that would actually have made it more obvious that we were doing something wrong.

With that second approach we would undoubtably start <a href="http://blog.iancartwright.com/2009/04/test-code-is-just-code.html">copy/pasting tests</a> which would provide another signal that we need to look at the design of the code and make it easier to test.

In this case the solution was to create several smaller objects which actually used all the parameters being passed in. I think we ended up with around 4 objects instead of 1 and each had simple tests that were easy to write.
