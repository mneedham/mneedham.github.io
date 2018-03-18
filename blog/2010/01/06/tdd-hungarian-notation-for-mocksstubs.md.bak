+++
draft = false
date="2010-01-06 00:08:14"
title="TDD: Hungarian notation for mocks/stubs"
tag=['tdd']
category=['Testing']
+++

A fairly common discussion that I've had with several of my colleagues is around the way that we name the variables used for mocks and stubs in our tests.

There seems to be about a 50/50 split between including 'Stub' or 'Mock' on the end of those variable names and not doing so.

In a simple example test using Rhino Mocks as the testing framework this would be the contrast between the two approaches:


~~~csharp

[Test]
public void ShouldDoSomething()
{
	var someDependency = MockRepository.CreateMock<ISomeDependency>();

	someDependency.Expect(x => x.SomeMethod()).Return("someValue");

	var myController = new MyController(someDependency);
        myController.DoSomething()

	someDependency.VerifyAllExpectations();
}
~~~


~~~csharp

[Test]
public void ShouldDoSomething()
{
	var someDependencyMock = MockRepository.CreateMock<ISomeDependency>();

	someDependencyMock.Expect(x => x.SomeMethod()).Return("someValue");

	var myController = new MyController(someDependencyMock);
        myController.DoSomething()

	someDependencyMock.VerifyAllExpectations();
}
~~~

I favour the former where we don't specify this information because I think it adds unnecessary noise to the name and is a detail about the implementation of the object behind that variable which I don't care about when I'm reading the test.

I do care about it if I want to change something but if that's the case then I can easily see that it's a mock or stub by looking at the place where it's instantiated.

From my experience we often tend to end up with the situation where the variable name suggests that something is a mock or stub and then it's used in a different way:


~~~csharp

[Test]
public void ShouldDoSomething()
{
	var someDependencyMock = MockRepository.CreateMock<ISomeDependency>();

	someDependencyMock.Stub(x => x.SomeMethod()).Return("someValue");

	var myController = new MyController(someDependencyMock);
        myController.DoSomething()
}
~~~

That then becomes a pretty misleading test because the reader is unsure whether the name is correct and the stub call is incorrect or whether it should in fact be a stub and the name is wrong.

The one time that I've seen that extra information being useful is when we have really long tests - perhaps when writing tests around legacy code which is tricky to get under test.

In this situation it is very nice to be able to  easily see exactly what we're doing with each of our dependencies.

Hopefully this is only a temporary situation before we can work out how to write simpler tests which don't require this extra information.
