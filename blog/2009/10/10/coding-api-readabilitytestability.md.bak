+++
draft = false
date="2009-10-10 00:21:45"
title="Coding: API readability/testability"
tag=['tdd', 'test-only-constructors']
category=['Coding']
+++

About a month ago or so <a href="http://www.markhneedham.com/blog/2009/09/12/tdd-test-only-constructors/">I described how we did some work to ensure that we were calling a class the same way in our tests as in our production code</a> and while I think that was a good choice in that situation we came across a similar problem this week where we weren't so sure.

The piece of code in question was being used to create the view model for a page and one of the pieces of data that we wanted to show on this page was the date on which something would be valid which is currently today's date.

We were working with some code that looked a bit like this:


~~~csharp

public class SomeRandomModel
{
	...

	public static SomeRandomModel CreateForSomeSituation(string value1, string value2)
	{
		return new SomeRandomModel(value1, value2);
	}

	public string SomeDate()
	{
		return DateTime.Today.ToDisplayFormat();
	}
}
~~~


~~~csharp

public static class DateTimeExtensions 
{
	public static string ToDisplayFormat(this DateTime aDateTime)
	{
		return String.Format("{0:MMM d, yyyy}", aDateTime)
	}
}
~~~

Initially we put the following test around the code:


~~~csharp

[Test]
public void ShouldConstructModelForSomeSituation()
{
	var model = SomeRandomModel.CreateForSomeSituation("", "");

	...

	Assert.AreEqual(DateTime.Today.ToDisplayFormat(), model.SomeDate()); 
}
~~~

The problem with this test is that it could theoretically fail if the 'DateTime.Today' in the test and the 'DateTime.Today' in the code were fired near enough to midnight that they returned different days.

It's not quite as big a problem as we would have if we were actually comparing the equality of the two dates but it's still not great to write a test which might fail sporadically.

We therefore need to find a way to control the input to the code so that we can test the output. 

The problem is that the date is always going to be today at the moment so it seems to unnecessarily complicate the 'CreateForSomeSituation' method if we had to pass in 'DateTime.Today' as a parameter.

Our current solution was therefore to create a test only method which takes in a date and then get the original method to delegate to the test only one while passing in 'DateTime.Today' as the extra parameter.


~~~csharp

public class SomeRandomModel
{
	private readonly DateTime aDateTime;
	...

	public static SomeRandomModel CreateForSomeSituation(string value1, string value2)
	{
		return CreateForSomeSituation(value1, value2, DateTime.Today);
	}

	public static SomeRandomModel CreateForSomeSituationForTest(string value1, string value2, DateTime aDateTime)
	{
		return new SomeRandomModel(value1, value2, aDateTime);
	}

	public string SomeDate()
	{
		return aDateTime.ToDisplayFormat();
	}
}
~~~

Our test now becomes:


~~~csharp

[Test]
public void ShouldConstructModelForSomeSituation()
{
	var model = SomeRandomModel.CreateForSomeSituationForTest("", "", new DateTime(2009, 10, 10));

	...

	Assert.AreEqual("10 Oct 2009", model.SomeDate()); 
}
~~~

We can now specify our expectation a bit more cleanly since we aren't tied to 'DateTime.Today'.

It helped solve our problem reasonably well but it still seems a bit weird to me to have 'test only' code but I'm not sure what a better solution would be.
