+++
draft = false
date="2009-10-10 11:07:21"
title="TDD: Keeping assertions clear"
tag=['tdd']
category=['Testing']
+++

Something which I noticed was a problem with the first example test that I provided in my post about <a href="http://www.markhneedham.com/blog/2009/10/10/coding-api-readabilitytestability/">API readability and testability</a> is that the assertion we are making is not that great.


~~~csharp

[Test]
public void ShouldConstructModelForSomeSituation()
{
	Assert.AreEqual(DateTime.Today.ToDisplayFormat(), model.SomeDate()); 
}
~~~

It's not really obvious what the expected result is supposed to be except that it should be the 'DisplayFormat'. If that fails then we'll need to navigate to the 'ToDisplayFormat' method to work out what that method does.

I think it should be possible to immediately know why a test failed so that we can address the problem straight away without too much investigation.

In this example we changed the way the code was working which coincidentally allowed us to make the assertion more obvious.


~~~csharp

[Test]
public void ShouldConstructModelForSomeSituation()
{
	Assert.AreEqual("10 Oct 2009", model.SomeDate()); 
}
~~~

<a href="http://erik.doernenburg.com/">Erik</a> pointed out another example of this a few weeks ago while we were working on some HTML helper code.

The tests in question looked roughly like this:


~~~csharp

[Test]
public void ShouldConstructReadOnlyValue()
{
	var readOnlyValue = new HtmlHelper().ReadOnlyValue("someId", "someValue", 'someTextValue');

	...
	var expectedValue = new TestHtmlBuilder().AddLabel("someId", "someTextValue").AddHiddenField("someId", "someValue").Build();

	Assert.AreEqual(expectedValue, readOnlyValue);
}
~~~
The test reads reasonably nicely and it's fairly obvious what it is we're testing for. 

The problem here is that we've hidden away our expectation and in this case we actually found out that the 'TestHtmlBuilder' had extra spaces in some places so all our assertions were incorrect and we didn't even know! 

In addition we end up <strong>duplicating the logic that the 'HtmlHelper' is doing</strong> if we create test assertion helpers like these.


~~~csharp

[Test]
public void ShouldConstructReadOnlyValue()
{
	var readOnlyValue = new HtmlHelper().ReadOnlyValue("someId", "someValue", 'someTextValue');

	...
	var expectedValue = @"<input type=""hidden"" id=""someId"" value=""someId"" /><label for=""someId"">someValue</label>";

	Assert.AreEqual(expectedValue, readOnlyValue);
}
~~~

The new test doesn't look as clean as the old one but the assertion is much more obvious so if it fails then we can quickly work out why.

