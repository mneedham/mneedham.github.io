+++
draft = false
date="2010-01-15 21:44:36"
title="TDD: Hand written stubs vs Framework generated stubs"
tag=['tdd']
category=['Testing']
+++

A few months ago <a href="http://blog.objectmentor.com/articles/2009/10/28/manual-mocking-resisting-the-invasion-of-dots-and-parentheses">Uncle Bob wrote a post about TDD where he suggested that he preferred to use hand created stubs in his tests</a> wherever possible and only resorted to using a Mockito created stub as a last resort.

I've tended to use framework created ones but my colleague Matt Dunn and I noticed that it didn't seem to work out too well for us writing some tests around a controller where the majority of our tests were making exactly the same call to that repository and expected to receive the same return value but a few select edge cases expected something different. 

The edge cases came along later on by which time we'd already gone past the stage of putting the stub expectation setup in every test and had moved it up into a setup method which ran before all test.

We tried to keep on using the same stub instance of the dependency which meant that we were trying to setup more than one stub expectation on the same method with different return values.


~~~csharp

[TestFixture]
public SomeControllerTests
{
	private ITheDependency theDependency;

	[SetUp]
	public void Before()
	{
		theDependency = MockRepository.GenerateStub<ITheDependency>();
		theDependency.Stub(t => t.SomeMethod()).Return(someResult);

		controller = new Controller(theDependency);
	}
	
	....

	[Test]
	public void SomeAnnoyingEdgeCaseTest()
	{
		theDependency.Stub(t => t.SomeMethod().Return(someOtherResult);

		controller.DoSomething();

		// and so on...
	}

}
~~~



We were struggling to remember where we had setup the various return values and could see a few ways to try and reduce this pain.

The first was to extract those edge case tests out into another test fixture where we would setup the stub expectation on a per test basis instead of using a blanket approach for all of them.

This generally works pretty well although it means that we now have our tests in more than one place which can be a bit annoying unless you know that's what's being done.

Another way which Matt suggested is to <strong>make use of a hand written stub for the tests which aren't bothered about the return value and then use a framework created one for specific cases</strong>.

The added benefit of that is that it's more obvious that the latter tests care about the result returned because it's explicitly stated in the body of the test.

We found that our tests were easier to read once we'd done this and we spent much less time trying to work out what was going on.

I think framework generated stubs do have thier place though and as <a href="http://blog.objectmentor.com/articles/2009/10/28/manual-mocking-resisting-the-invasion-of-dots-and-parentheses">Colin Goudie points out in the comments on Uncle Bob's post</a> it probably makes more sense to make use of a framework generated stub when each of our tests returns different values for the same method call.

If we don't do that then we end up writing lots of different hand written stubs which I don't think adds much value. 

I still start out with a framework generated stub but if it's becoming overly complicated or repetitive then I'm happy to switch to a hand written one.

It'd be interesting to hear others' approaches on this.
