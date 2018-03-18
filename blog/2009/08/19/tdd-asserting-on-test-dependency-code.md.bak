+++
draft = false
date="2009-08-19 23:19:45"
title="TDD: Asserting on test dependency code"
tag=['tdd']
category=['Testing']
+++

Something I've noticed a bit lately is tests which setup a load of dependencies for a test and then do assertions on that setup before getting on to calling the system under test.

The code tends to be similar to this:


~~~csharp

public void ShouldHopefullyDoSomeAwesomeStuff()
{
	// setup via expectations for dependency1 and dependency2
	Assert.IsNotNull(dependency1.DependedOnMethod);	

	new SystemUnderTest(dependency1, dependency2).DoThatStuff();

	// test assertions
}
~~~ 

I've done this a fair few times myself and I used to believe that it actually made the test more valuable since we were ensuring that the dependencies were in a good state before we executed the test.

Looking at those types of assertions nowadays it feels like waste to me because we are basically testing our ability to setup the test correctly which is not the point of writing the test.

In addition tests written like this are more noisy and difficult to read for me at least as I find my eye is drawn to the assertions (and therefore typically to the end of the test) so having more than one block of these is a bit confusing.

If we're not sure that we've set up the dependency correctly then an alternative is to try and simplify the setup of that dependency so that it's really obvious that we've done it right.

There are a couple of ways that I've come across for doing this:

<ul>
<li>Ensure that all the setup for the test is done inside the test and <a href="http://www.markhneedham.com/blog/2008/12/19/tdd-mock-expectations-in-setup/">not in setup methods</a>.</li>
<li>Extract away test data setup that we don't care about by making use of <a href="http://nat.truemesh.com/archives/000714.html">test data builders</a> where possible.</li>
</ul>

I've previously suggested that I found it quite useful to <a href="http://www.markhneedham.com/blog/2009/04/13/tdd-balancing-dryness-and-readability/">extract methods for groups/individual expectations/stub calls</a> but I think this may have inadvertently led to the above pattern since the code that we care about is now hidden a click away from where we need it.

I think I'd probably take the hit of having some duplication in tests instead of making the test more difficult to understand although like with all things there's definitely a trade off to make.
