+++
draft = false
date="2009-09-13 22:21:22"
title="TDD: Testing sub classes"
tag=['tdd']
category=['Testing']
+++

We ran into another interesting testing dilemma while <a href="http://www.markhneedham.com/blog/2009/09/13/coding-an-abstract-classasp-net-mvc-dilemma/">refactoring the view model code which I described in an earlier post to the point where we have an abstract class and three sub classes</a> which means that we now have 3 classes which did the same thing 80% of the time.

As <a href="http://www.markhneedham.com/blog/2009/09/02/coding-reduce-fields-delay-calculations/">I mentioned in a post a couple of weeks ago</a> one of the main refactorings that we did was to move some calls to dependency methods from the constructor and into properties so that those calls would only be made if necessary.

After we'd done this the code looked a bit like this:

~~~csharp

public abstract class ParentModel
{
	private readonly Dependency1 dependency1;

	...

	public decimal Field1 { get { return dependency1.Calculation1(); } }
	public decimal Field2 { get { return dependency1.Calculation2(); } }
}

public class BusinessProcess1Model : ParentModel { }
public class BusinessProcess2Model : ParentModel { }
public class BusinessProcess3Model : ParentModel { }
~~~
We wanted to ensure that the tests we had around this code made sure that the correct calls were made to 'depedency1' but because ParentModel is an abstract class the only way that we can do this is by testing one of its sub classes.

The question is <strong>should we test this behaviour in each of the sub classes and therefore effectively test the same thing three times or do we just test it via one of the sub classes and assume that's enough?</strong>

Neither of the options seems really great although if we cared only about behaviour then we would test each of the sub classes independently and forget that the abstract class even exists for testing purposes.

While the logic behind this argument is quite solid we would end up breaking 3 tests if we needed to refactor our code to call another method on that dependency for example.

I suppose that makes sense in a way since we have actually changed the behaviour of all those classes but it seems to me that we only really need to know from one failing test that we've broken something and anything beyond that is a bit wasteful.

In C# it's not actually possible for 'Field1' or 'Field2' to be overriden with an alternate implementation unless we defined those properties as 'virtual' on the 'ParentModel' which we haven't done.

We could however use the 'new' keyword to redefine what those properties do if the callee had a reference directly to the sub class instead of to the abstract class which means it is possible for a call to 'Field1' to not call 'dependency1' which means that maybe we do need to test each of them individually.

I'm not sure which approach I prefer, neither seems better than the other in my mind.
