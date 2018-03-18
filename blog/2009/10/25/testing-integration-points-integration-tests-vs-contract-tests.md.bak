+++
draft = false
date="2009-10-25 00:04:12"
title="Testing End Points: Integration tests vs Contract tests"
tag=['testing']
category=['Testing']
+++

We recently changed the way that we test against our main integration point on the project I've been working on so that in our tests we retrieve the service object from our dependency injection container instead of 'newing' one up.

Our tests therefore went from looking like this:


~~~csharp

[Test]
public void ShouldTestSomeService()
{
	var someService = new SomeService();
	// and so on
}
~~~

To something more like this:


~~~csharp

[Test]
public void ShouldTestSomeService()
{
	var someService = UnityFactory.Container.Resolve<ISomeService>();
	// and so on
}
~~~

This actually happened as a side effect of another change we made to inject users into our system via our dependency injection container.

We have some 'authenticated services' which require the request to contain a SAML token for a valid user so it seemed to make sense to use the container in the tests instead of having to duplicate this piece of behaviour for every test.

We needed to add our fake authorised user into the container for our tests but apart from this the container being used is the same as the one being used in the production code. 

Our tests are therefore now calling the services in a way which is much closer to the way that they are called in the code than was previously the case.

I think this is good as it was previously possible to have the tests working but then have a problem calling the services in production because something in the container wasn't configured properly.

The downside is that these tests now have more room for failure than they did previously and they are not just testing the end point which was their original purpose.

In a way what we have done is <strong>convert these tests from being contract tests to integration tests</strong>.

I like the new way but I'm not completely convinced that it's a better approach.
