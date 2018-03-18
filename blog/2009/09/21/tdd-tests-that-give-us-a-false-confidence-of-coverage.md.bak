+++
draft = false
date="2009-09-21 22:49:49"
title="TDD: Tests that give us a false confidence of coverage"
tag=['tdd']
category=['Testing']
+++

During J.B. Rainsberger's presentation at Agile 2009 titled '<a href="http://www.infoq.com/presentations/integration-tests-scam">Integration tests are a scam</a>' he suggests that having lots of integrationt tests covering our code can give us a false sense of confidence that we are testing our code and I think the same can happen with unit tests as well if we're not careful how we write them.

It's important to ensure that our unit tests are actually testing something useful otherwise the cost of writing and maintaining them will outweigh the benefits that we derive from doing so.

I've come across two type of test recently which don't test an awful lot but can lead us to thinking our code is well covered at the unit level if we just glance at the test names and don't take the time to examine exactly what's going on which is what seems to happen a lot of the time.

<h3>Only testing for 'IsNotNull'</h3>
I think testing that a value we want to do some assertions against isn't null is a great start since it can help us avoid null reference exceptions in our tests but it's only the first assertion that we want to make, not the only one!

The name of these tests is nearly always misleading and it often seems like these tests are a work in progress but one which never gets finished.

The following is not unusual:


~~~csharp

[Test]
public void ShouldPopulateParentModelOnAction()
{
	var someController = new SomeController(...);

	// There'd probably be more casting to actually retrieve the actual model 
	// but we'll ignore that for the sake of this example
	var parentModel = someController.SomeAction();

	Assert.IsNotNull(parentModel);
}
~~~

The problem I have with this type of test is that the name suggests we have completely tested that the controller action is correctly populating the model but in reality all we're testing is that we got a model and not that its contents are accurate.

It's surprisingly easy when skimming through tests to not even notice that this is the case.

The danger we're toying with by doing this is that others might assume that this area of the code is tested and subsequently do refactorings around this code assuming that the tests are providing a safety net when in actual fact they aren't.

Certainly sometimes 'IsNotNull' is all we care about and in those cases it's fine just to test for that but I think that most of the time it's just a lazy way out of properly testing a piece of code.

<h3>Testing expectations on stubs</h3>
I'm not sure if this is just a Rhino Mocks problem but I've come across quite a few tests recently which make expectations on stubs and then sometimes verify those expectations.

Most of the time the creation of the stubbed dependency is hidden away in a setup method so the tests wouldn't be quite as clear cut as this but this is what's happening:


~~~csharp

[Test]
public void ShouldRetrieveSomeValuesFromTheRepository()
{
	var theRepository = MockRepository.GenerateStub<ITheRepository>();
	theRepository.Expect(r => r.SomeMethod()).Return("someValue");
	
	var systemUnderTest = new SystemUnderTest(theRepository);

	systemUnderTest.DoSomething();
}
~~~

or


~~~csharp

[Test]
public void ShouldRetrieveSomeValuesFromTheRepository()
{
	var theRepository = MockRepository.GenerateStub<ITheRepository>();
	theRepository.Expect(r => r.SomeMethod()).Return("someValue");
	
	var systemUnderTest = new SystemUnderTest(theRepository);

	systemUnderTest.DoSomething();

	theRepository.VerifyAllExpectations();
}
~~~

The problem with both of these tests is that they aren't doing anything useful for us.

From <a href="http://www.markhneedham.com/blog/2009/07/28/reading-code-rhino-mocks/">my understanding of the Rhino Mocks code</a> what we are effectively doing is creating a stub on 'theRepository' which will return a value of 'someValue' the first time that 'SomeMethod' is called on it. The 'VerifyAllExpectations just falls through and does nothing because we've created a stub and not a mock.

We could just as easily not call any method on the system under test and we'd still get a green bar.

If we intend to test the way that the system under test interacts with its dependencies then we want to make sure we've actually created a mock and then ensure that we check that the expectations have actually been called. 

The test above could become a bit more like this for that purpose:


~~~csharp

[Test]
public void ShouldRetrieveSomeValuesFromTheRepository()
{
	var theRepository = MockRepository.GenerateMock<ITheRepository>();
	theRepository.Expect(r => r.SomeMethod()).Return("someValue");
	
	var systemUnderTest = new SystemUnderTest(theRepository);

	systemUnderTest.DoSomething();

	theRepository.VerifyAllExpectations();
}
~~~


<h3>In summary</h3>
I've previously just ignored tests like this and just got on with what I was doing but I think it's important to try and clean them up so that they can make a greater contribution to our testing efforts - Uncle Bob's Boy Scout Rule applies here - leave the tests in a better state than you found them.

That way we can move towards having justifiable confidence that we can make changes to our code without fear that we've broken some piece of functionality.
