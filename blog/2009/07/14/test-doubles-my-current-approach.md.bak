+++
draft = false
date="2009-07-14 13:23:52"
title="Test Doubles: My current approach"
tag=['testing', 'test-doubles']
category=['Testing']
+++

My colleague Sarah Taraporewalla recently wrote about <a href="http://sarahtaraporewalla.com/thoughts/testing/canned-stubbed-and-mocked-fake-objects/">her thoughts on  test doubles</a> (to use <a href="http://xunitpatterns.com/">Gerard Meszaros</a>' language) and it got me thinking about the approach I generally take in this area. 

<h3>Stub objects</h3>
I use <a href="http://xunitpatterns.com/Test%20Stub.html">stubs</a> mostly to control the output of depended on components of the system under test where we don't want to verify those outputs.

Most of the time I make use of the mocking library's ability to stub out method calls on these dependencies.

I find that it generally seems to require less effort to do this than to create hand written stubs although chatting to <a href="http://intwoplacesatonce.com/">Dave</a> about this he pointed out that one situation where it would make more sense to use a hand written stub is when stubbing out a <a href="http://www.markhneedham.com/blog/2008/09/24/testing-with-joda-time/">clock/time provider</a>. This is because there are likely to be multiple calls to it all over the place and most of the time you probably want it to return the same value anyway.

I actually quite like the fact that you need to specify all the stub calls that you want to make in each test - it helps you to see when you have too many dependencies and then hopefully you can do something about that. 

On previous projects I worked on we decided the way to get around that problem was to <a href="http://www.markhneedham.com/blog/2008/12/19/tdd-mock-expectations-in-setup/">define all the stub method calls in a setup method</a> but that seems to lead to a world of pain later on when you forget that you've stubbed a method in the setup and now want to assert an expectation on it or (to a lesser extent) write a test which doesn't actually use the stub.

<h3>Fake objects</h3>
I often confuse <a href="http://xunitpatterns.com/Fake%20Object.html">fakes</a> with stubs as seem to be quite similar to each other in their intent - the difference as I understand it is that with a stub we are controlling the output of a dependency whereas a fake just sits there and lets interactions happen with it. The values passed in earlier calls to the fake may be returned in later calls to it.

The most common use of this pattern is to replace a real database with a fake one for testing although on a recent project we were making use of a hand written fake session store to avoid having to refer to the real session in our test code. 

We might have one call to the 'SessionFake' to store a value and then if a retrieve call is made later on we would return the value that we previously stored. 

The approach Sarah describes for stubbing repositories seems quite similar to this as well.

<h3>Mock objects</h3>
I use <a href="http://xunitpatterns.com/Mock%20Object.html">mocks</a>  to replace depended on components of the system under test when I do care about the way that is is used i.e. we want to verify the behaviour of the dependencies.

If we see a mock object being created in a test then we should see a call to a 'verify' method later on to ensure that the expected methods are called on it.

I used to use these all over the place for just about every test where I wanted to control the way that a dependency acted until I realised how fragile and confusing that made the tests.

Now, after recently watching <a href="http://blog.jayfields.com/2009/06/developer-testing-welcome-to-beta-test.html">a presentation by Jay Fields</a>, I try to ensure that I'm only setting up one expectation per test and use of the other test double approaches for any other dependencies that needs to be taken care of in that test.

<h3>Dummy objects</h3>
Most of the time when I pass <a href="http://xunitpatterns.com/Dummy%20Object.html">dummy</a> values into tests they tend to be strings and I prefer to pass in a value of 'irrelevantValue' rather than just passing in a null which may lead to difficult to locate Null Pointer Exceptions further down the line if the value which we thought was just a dummy starts being used.

We are generally only passing in these dummy values to satisfy the requirements of the system under test which may require values to be entered even if the particular piece of functionality that we are testing doesn't make use of them.

<h3>Overall</h3>
I think my current approach to testing leans more towards <a href="http://martinfowler.com/articles/mocksArentStubs.html">mockist rather than classicist</a> although I think I am probably moving more towards the middle as I see the problems we can run into with over mocking.

With test doubles my current approach has minimising the effort required to create them as the most important aspect but I'm sure that will change given a different context. With all the test doubles I generally try and use <a href="http://www.markhneedham.com/blog/2009/01/21/c-builder-pattern-still-useful-for-test-data/">test data builders</a> where it's not overkill.
