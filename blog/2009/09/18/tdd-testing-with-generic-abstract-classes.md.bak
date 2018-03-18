+++
draft = false
date="2009-09-18 00:40:09"
title="TDD: Testing with generic abstract classes"
tag=['tdd']
category=['Testing']
+++

In a post I wrote earlier in the week I described <a href="http://www.markhneedham.com/blog/2009/09/13/tdd-testing-sub-classes/">a dilemma we were having testing some code which made use of abstract classes</a> and Perryn Fowler, Liz Keogh and Pat Maddox pointed out that a useful approach for this problem would be to make use of an <a href="http://c2.com/cgi-bin/wiki?AbstractTestCases">abstract test class</a>. 

The idea here is that we create an equivalent hierarchy to our production code for our tests which in the example that I provided would mean that we have roughly the following setup:


~~~csharp

public abstract class ParentModelTest
{
}
 
public class BusinessProcess1ModelTest : ParentModelTest { }
public class BusinessProcess2ModelTest : ParentModelTest { }
public class BusinessProcess3ModelTest : ParentModelTest { }
~~~

We then want to create an abstract method on the 'ParentModelTest' class to create the object under test and we'll implement this method in the sub classes.

We can then put the common tests into the abstract class and they will be run when we run the tests for each of the sub class tests.

My colleague Matt Dunn and I were looking at how you would implement this and he pointed out that it provided quite a nice opportunity to use generics to achieve our goal. 

If we make the abstract test class take in generic parameters then it allows us to create our specific type in the 'create' method rather than having to create 'ParentModel' and then casting that for our specific sub class tests.


~~~csharp

public abstract class ParentModelTest<T> where T : ParentModel
{
	protected abstract T CreateModel();	

	[Test]
	public void ShouldTestThoseCommonDependencies()
	{
		var model = CreateModel();
		// Do some awesome testing that's common across all 3 sub classes here
	}
}
~~~


~~~csharp

[TestFixture]
public class BusinessProcessModel1Test : ParentModelTest<BusinessProcessModel1>
{
	protected override BusinessProcessModel1 CreateModel()
	{
		return new BusinessProcessModel1(...);
	}

	[Test]
	public void ShouldDoSomeEquallyOutstandingStuff() 
	{
		var model = CreateModel();
		// and test away
	}
}
~~~

It seems to work quite well and we realised that it's actually a pattern that we had also used to test that our controllers would actually be injected with all their dependencies from our DI container or whether we have forgotten to register some of them.

We have an abstract class similar to this which all our controller tests extend:


~~~csharp

public abstract class ContainerTest<T> where T : Controller
{
	[Test]
	public void ShouldHookUpAllDependencies()
	{
		var container = CreateTheContainer();

		var controller = container.Resolve<T>();

		Assert.IsNotNull(controller);
	}
}
~~~


~~~csharp

public class AwesomeControllerTest : ContainerTest<AwesomeController> { }
~~~

When we haven't got all the dependencies injected correctly the code will actually blow up on the resolve step so the last line is not strictly necessary but the test seems like it's not testing anything at first glance without it.
