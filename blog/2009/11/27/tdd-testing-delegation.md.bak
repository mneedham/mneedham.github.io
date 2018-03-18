+++
draft = false
date="2009-11-27 14:43:45"
title="TDD: Testing delegation"
tag=['tdd']
category=['Testing']
+++

I recently came across an <a href="http://www.rallydev.com/engblog/2009/11/17/units-are-not-classes/">interesting blog post by Rod Hilton on unit testing</a> and it reminded me of a couple of conversations <a href="http://fragmental.tw/">Phil</a>, <a href="http://twitter.com/raphscallion">Raph</a> and I were having about the best way to test classes which delegate some responsibility to another class.

An example that we ran into recently was where we wrote some code which required one controller to delegate to another.


~~~java

public class ControllerOne extends Controller {
    public ModelAndView handleRequest(HttpServletRequest request, HttpServletResponse response) throws Exception {
    }
}
~~~


~~~java

public class ControllerTwo extends Controller {
	private final ControllerOne controllerOne;
	
	public ControllerTwo(ControllerOne controllerOne) {
		this.controllerOne = controllerOne;
	}

    public ModelAndView handleRequest(HttpServletRequest request, HttpServletResponse response) throws Exception {
		....
		return controllerOne.handleRequest(...);
    }
}
~~~

My initial thought when working out how to test this code was that we should check that the request is actually getting routed via ControllerOne:


~~~java

@Test
public void theTest() {
	ControllerOne controller One = mock(ControllerOne.class);

	ControllerTwo controllerTwo = new ControllerTwo(controllerOne);

	controllerTwo.handleRequest(...)

	verify(controllerOne).handleRequest(...);
}
~~~

When we discussed this Raph and Phil both pointed out that we didn't care that specifically about the implementation of how the request was handled. What we care about is that the result we get after the request is handled is as expected.

We therefore changed our test to be more like this:


~~~java

@Test
public void theTest() {
	ControllerOne controller One = mock(ControllerOne.class);
	ModelAndView myModelAndView = new ModelAndView();
	when(controllerOne.handleRequest(...).thenReturn(myModelAndView);

	ControllerTwo controllerTwo = new ControllerTwo(controllerOne);

	ModelAndView actualModelAndView = controllerTwo.handleRequest(...)

	assertThat(actualModelAndView, equalTo(myModelAndView));
}
~~~

I've been finding more and more recently that when it comes to writing tests which do some sort of delegation the 'stub + assert' approach seems to work out better than just verifying.

You lose the fine grained test that verifying mocks provides but we can still pretty much tell indirectly whether the dependency was called because if it wasn't then it's unlikely (but of course still possible) that we would have received the correct 'ModelAndView' in our assertion. 

My current approach is that I'd probably only mock and verify an interaction if the dependency is a service which makes a network call or similarly expensive call where the interaction is as important as the result obtained. 

For example we probably wouldn't want to make that call multiple times and with verification we're able to ensure that doesn't happen.

I find as I've used mocking frameworks more I feel like I'm drifting from a <a href="http://martinfowler.com/articles/mocksArentStubs.html#ClassicalAndMockistTesting">mockist style of testing to one getting closer to the classicist approach</a>. I wonder if that's quite a normal progression.
