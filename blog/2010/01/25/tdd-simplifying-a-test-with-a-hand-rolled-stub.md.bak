+++
draft = false
date="2010-01-25 21:23:31"
title="TDD: Simplifying a test with a hand rolled stub"
tag=['tdd']
category=['Testing']
+++

I wrote a couple of weeks ago about my thoughts on <a href="http://www.markhneedham.com/blog/2010/01/15/tdd-hand-written-stubs-vs-framework-generated-stubs/">hand written stubs vs framework generated stubs</a> and I noticed an interesting situation where it helped me out while trying to simplify some test code.

The code in question was making use of several framework generated stubs/mocks and one in particular was trying to return different values depending on the value passed as a parameter.

The test was failing and I spent about half an hour unsuccessfully trying to work out why it wasn't working as expected before I decided to replace it with a hand rolled stub that did exactly what I wanted.

This is a simplified version of the test:


~~~csharp

[Test]
public void SomeTest()
{
	var service = MockRepository.GenerateStub<IService>();

	service.Stub(x => x.SomeMethod("call1")).Return("aValue");
	service.Stub(x => x.SomeMethod("call2")).Return("anotherValue");

	// and so on

	new SomeObject(service).AnotherMethod();

       // some assertions
}
~~~ 

For the sake of the test I only wanted 'service' to return a value of 'aValue' the first time it was called and then 'anotherValue' for any other calls after that.

I therefore wrote the following hand rolled stub to try and simplify the test for myself and plugged it into the original test:


~~~csharp

public class AValueOnFirstCallThenAnotherValueService : IService
{
	private int numberOfCalls = 0;

	public string SomeMethod(string parameter)
	{
		if(numberOfCalls == 0)
		{
			numberOfCalls++;
			return "aValue";
		}
		else
		{
			numberOfCalls++;
			return "anotherValue";
		}
	}
}
~~~


~~~csharp

[Test]
public void SomeTest()
{
	var service = new AValueOnFirstCallThenAnotherValueService();

	new SomeObject(service).AnotherMethod();

       // some assertions
}
~~~ 

I've never tried this particular approach before but it made it way easier for me to identify what was going wrong and I was then able to get the test to work as expected and move onto the next one.

In retrospect it should have been possible for me to work out why the original framework generated stub wasn't working but it seemed like the right time to cut my losses and the time to write the hand generated one and get it working was an order of magnitude less.
