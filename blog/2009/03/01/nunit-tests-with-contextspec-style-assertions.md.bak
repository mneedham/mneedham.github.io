+++
draft = false
date="2009-03-01 16:43:46"
title="NUnit: Tests with Context/Spec style assertions"
tag=['c', 'net', 'nunit']
category=['.NET']
+++

I recently started playing around with <a href="http://twitter.com/bellware">Scott Bellware's</a> <a href="http://code.google.com/p/specunit-net/">Spec-Unit</a> and <a href="http://twitter.com/aaronjensen">Aaron's Jensen's</a> <a href="http://codebetter.com/blogs/aaron.jensen/archive/2008/05/08/introducing-machine-specifications-or-mspec-for-short.aspx">MSpec</a>, two frameworks which both provide a way of writing Context/Spec style tests/specifications.

What I particularly like about this approach to writing tests is that we can divide assertions into specific blocks and have them all evaluated even if an earlier one fails.

<a href="http://www.nunit.org/index.php">NUnit</a> is our testing tool of choice at the moment and we wanted to try and find a way to test the mapping between the domain and service layers of the application. 

Testing in the normal way was resulting in a test that was absolutely massive and a bit of a nightmare to debug when something changed.

Luckily <a href="http://twitter.com/davcamer">Dave</a> came up with the idea of using the TestFixtureSetUp attribute on a method which would setup the test data and then call the appropriate method on the object under test.

We could then have smaller tests which asserted various parts of the mapping.


~~~csharp

[TestFixture]
public class FooAdaptorTest 
{
	private Foo foo;
	private FooMessage fooMessage;

	[TestFixtureSetUp]
	public void GivenWeTransformAFoo()
	{
		foo = new Foo { Bar = "bar", Baz = "baz" };
		fooMessage = new FooAdaptor().MapFrom(foo);	
	}

	[Test]
	public void ShouldMapBar() 
	{
		Assert.AreEqual(foo.Bar, fooMessage.Bar);	
	}

	[Test]
	public void ShouldMapBaz() 
	{
		Assert.AreEqual(foo.Baz, fooMessage.Baz);		
	}
}
~~~

Of course this is a very simple example, and in a real example we would test more than just one property per test.

The Setup method does get pretty big depending on how much mapping needs to be done but it seems a reasonable trade off for the increased readability we get in the smaller size of each of the tests.

I know this isn't the normal way of using NUnit but I think it's cool to try and think outside the normal approach to find something that works better for us. 
