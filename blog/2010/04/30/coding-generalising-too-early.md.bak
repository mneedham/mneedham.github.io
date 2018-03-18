+++
draft = false
date="2010-04-30 07:12:26"
title="Coding: Generalising too early"
tag=['coding']
category=['Coding']
+++

I've previously written about the value of <a href="http://www.markhneedham.com/blog/2009/10/31/coding-copypaste-then-refactor/">adding</a> <a href="http://www.markhneedham.com/blog/2009/08/30/coding-group-the-duplication-then-remove-it/">duplication</a> to code before removing it and we had an interesting situation this week where we failed to do that and ended up generalising a piece of code too early to the point where it actually didn't solve the problem anymore.

The problem we were trying to solve was around the validation of some dependent fields and to start with we had this requirement:


~~~text

Given 2 fields...

Field 1
Field 2 - Can be empty if Field 1 is 'Foo'. Otherwise must have a value.
~~~

We wrote an object that looked a bit like this to do that logic:


~~~csharp

public class DependentOnField1 : IValidateFields
{
	public bool IsSatisfied(Field field)
	{
		if(OtherFieldIsFoo())
		{
			return true;
		}		

		return string.IsNullOrEmpty(field.Value);
	}
}
~~~

Later on we had the following requirement:


~~~text

Given 2 more fields...

Field 3 
Field 4 - Must have a value of more than 0 if Field 3 is 'Bar'. Otherwise can be empty. 
~~~

It seemed at first glance that they were the same type of validation because in both cases there is talk of dependence between fields.

We started refactoring the 'DependentOnField1' object into a state where we would be able to use it for both cases. This meant that we needed to parameterise the object so that we could vary the dependent field.



We eventually ended up with an interface that could be called like this:


~~~csharp

var field1DependenceValidator = DependentOn.Field(field1);
~~~


~~~csharp

public class DependentOn : IValidateFields
{
	public static DependentOn Field(Field field)
	{
		return new DependentOn(field);
	}
}
~~~

Unfortunately while refactoring this object we hadn't taken into account the fact that the requirement for fields 3 and 4 is slightly different to that for fields 1 and 2. With fields 1 & 2 we only needed one condition to be true whereas with fields 3 and 4 two conditions needed to be true - field 3 must be 'Bar' AND field 4 must be greater than 0.

We initially tried to hack in the fields 3/4 requirement like this:


~~~csharp

public class DependentOn : IValidateFields
{
	public bool IsSatisfied(Field field)
	{		
		if(OtherFieldIsX() && Double.Parse(field.Value) > 0)
		{
			return true;
		}		

		return string.IsNullOrEmpty(field.Value);
	}
}
~~~

Unfortunately that breaks the way that validation works for fields 1 & 2 and every other attempt we made seemed to make the situation worse and worse until after about half an hour of wrestling with this we decided to revert everything and just create a new object for this new type of validation.

We would <strong>accept some duplication until we were able to see a more meaningful abstraction that we could pull out</strong>.

Dave Cameron, who first taught me this approach, recently wrote <a href="http://intwoplacesatonce.com/2010/04/multiple-return-values-and-refactoring-javascript/">a post describing how he removed some duplication in JavaScript</a> code and you can see from the initial example in his post that he waited until he was exactly sure where the duplication was before getting rid of it.

I think this is the best approach and the rule of thumb seems to be that we should wait until we have the same thing 3 times before trying to remove the duplication.

