+++
draft = false
date="2009-10-23 23:39:05"
title="Value objects: Immutability and Equality"
tag=['domain-driven-design']
category=['Domain Driven Design']
+++

A couple of weeks ago I was working on some code where I wanted to create an object composed of the attributes of several other objects.

The object that I wanted to construct was a read only object so it seemed to make sense to make it a <a href="http://c2.com/cgi/wiki?ValueObject">value object</a>. The object would  be immutable and once created none of the attributes of the object would change.

This was my first attempt at writing the code for this object:


~~~csharp

public class MyValueObject
{
    private readonly string otherValue;
    private readonly SomeMutableEntity someMutableEntity;

    public MyValueObject(SomeMutableEntity someMutableEntity, string otherValue)
    {
        this.someMutableEntity = someMutableEntity;
        this.otherValue = otherValue;
    }

    public string SomeValue { get { return someMutableEntity.SomeValue; } }

    public int SomeOtherValue {get { return someMutableEntity.SomeOtherValue; }}

    public string OtherValue { get { return otherValue; } }

    public bool Equals(MyValueObject obj)
    {
        if (ReferenceEquals(null, obj)) return false;
        if (ReferenceEquals(this, obj)) return true;
        return Equals(obj.OtherValue, OtherValue) && Equals(obj.SomeOtherValue, SomeOtherValue) && Equals(obj.SomeValue, SomeValue);
    }

    public override bool Equals(object obj)
    {
		// other equals stuff here
    }
}
~~~

It wasn't immediately obvious to me what the problem was with this solution but it felt really weird to be making use of properties in the equals method.

After discussing this strangeness with <a href="http://intwoplacesatonce.com/">Dave</a> he pointed out that 'MyValueObject' is not immutable because although the reference to 'SomeMutableEntity' inside the object cannot be changed the object itself had lots of setters and could therefore be changed from outside this class. 

There are two ways to get around this problem:

<ol>
<li>We still inject 'SomeMutableEntity' but we extract the values from it in the constructor and don't keep a reference to it.</li>
<li>The client that creates 'MyValueObject' constructs the object with the appropriate values</li>
</ol>

The first solution would work but it feels really weird to pass in the whole object when we only need a small number of its attributes - it's a case of <a href="http://www.markhneedham.com/blog/2009/08/25/coding-coupling-and-expressiveness/">stamp coupling</a>. 

It also seems quite misleading as an API because it suggests that 'MyValueObject' is made up of 'SomeMutableEntity' which isn't the case.

My preferred solution is therefore to allow the client to construct 'MyValueObject' with all the parameters individually.


~~~csharp

public class MyValueObject
{
    private readonly string otherValue;
    private readonly int someOtherValue;
    private readonly string someValue;

    public MyValueObject(string someValue, string otherValue, int someOtherValue)
    {
        this.someValue = someValue;
        this.otherValue = otherValue;
        this.someOtherValue = someOtherValue;
    }

    public string SomeValue { get { return someValue; } }

    public int SomeOtherValue { get { return someOtherValue; } }

    public string OtherValue { get { return otherValue; } }
}
~~~

The constructor becomes a bit more complicated but it now feels a bit more intuitive and 'MyValueObject' lives up to its role as a value object.

The equals method can now just compare equality on the fields of the object.


~~~csharp

public class MyValueObject
{
	...

	public bool Equals(MyValueObject obj)
	{
	    if (ReferenceEquals(null, obj)) return false;
	    if (ReferenceEquals(this, obj)) return true;
	    return Equals(obj.otherValue, otherValue) && Equals(obj.someValue, someValue) && obj.someOtherValue == someOtherValue;
	}
}
~~~

A client might create this object like so:


~~~csharp

var myValueObject = new MyValueObject(someMutableEntity.SomeValue, otherValue, someMutableEntity.SomeOtherValue);
~~~
