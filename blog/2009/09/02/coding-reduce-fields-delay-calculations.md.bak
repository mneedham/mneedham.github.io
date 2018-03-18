+++
draft = false
date="2009-09-02 23:52:06"
title="Coding: Reduce fields, delay calculations"
tag=['coding']
category=['Coding']
+++

A pattern in code which I've noticed quite frequently lately is that of executing calculations in the constructor of an object and then storing the result in a field on the object.

From the small amount of experience I have playing around with functional languages I have come across the idea of lazy evaluation of functions quite frequently and I think it's something that we can apply in object oriented languages as well.

When we store a value of a calculation in a field we are opening up the ability for that value to be changed before we use it.

We can certainly reduce/remove the chance of that happening by making fields read only or final but as <a href="http://www.infoq.com/articles/dhanji-prasanna-concurrency">Dhanji points out in his InfoQ article</a>, if we are storing reference objects there is still a chance they could be mutated before we use them.

Even if we can manage to work our way around that problem I still feel that we increase the complexity of classes by having more fields as well as decreasing the readability of the code in the constructor since we now have all this extra information standing in our way when perhaps we don't even care about it at all since it won't be used until later on anyway.

I'm not sure if it's a given but I never expect calculations to be done in the constructors of objects when I create them - at most I would expect the fields I pass in to be stored but any more than that is surprising and I think it's good to avoid surprises if we can!

I don't think the automated properties in C# 3.0 have really helped much and code like this is quite common:


~~~csharp

public class SomeObject
{
	public SomeObject(Dependency1 dependency1, Dependency2 dependency2)
	{
		Field1 = dependency1.Calculation1();
		Field2 = dependency1.Calculation2();
		Field3 = dependency2.Calculation1();
		Field4 = dependency2.Calculation2();
		// and so on
	}

	public decimal Field1 { get; set; }
	public decimal Field2 { get; set; }
	public decimal Field3 { get; set; }
	public decimal Field4 { get; set; }
}
~~~

This one is relatively easy to simplify since we just need to store 'dependency1' and 'dependency2' and then delegate if the properties are called:


~~~csharp

public class SomeObject
{
	private readonly Dependency1 dependency1;
	private readonly Dependency2 dependency2

	public SomeObject(Dependency1 dependency1, Dependency2 dependency2)
	{
		this.dependency1 = dependency1;
		this.dependency2 = dependency2;
		// and so on
	}

	public decimal Field1 { get { return dependency1.Calculation1(); }
	public decimal Field2 { get { return dependency1.Calculation2(); }
	public decimal Field3 { get { return dependency2.Calculation1(); }
	public decimal Field4 { get { return dependency2.Calculation2(); }
}
~~~

Now when we look at the constructor we can see that 'SomeObject' depends on those 2 classes and when we want to see what a call to 'Field1' does we can see straight away instead of having to scroll back up to the constructor to check.

In a way we have tightened the coupling between 'SomeObject' and 'Dependency1' and 'Dependency2' by storing those in fields and I was <a href="http://www.markhneedham.com/blog/2009/08/25/coding-coupling-and-expressiveness/">pondering the wisdom of doing this sort of thing in a previous post</a> but I think I prefer to take this coupling over the alternative choice.

The choice isn't quite as clear cut if we are getting a value from a dependency and then performing a calculation on that value.

For example:


~~~csharp

public class SomeObject
{
	public SomeObject(Dependency1 dependency1)
	{
		Result = CalculateValueFrom(dependency1.OtherDependency);
	}

	public decimal Result { get; set; }
}
~~~

In this case I would still favour storing 'Dependency1' and then executing that calculation later although a <a href="http://www.markhneedham.com/blog/2009/08/17/law-of-demeter-some-thoughts/">law of demeter</a> violation is more often than not staring us in the face and perhaps this isn't the right class to be performing this calculation.
