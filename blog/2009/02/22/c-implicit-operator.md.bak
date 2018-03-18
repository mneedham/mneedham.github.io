+++
draft = false
date="2009-02-22 22:20:22"
title="C#: Implicit Operator"
tag=['c', 'net']
category=['.NET']
+++

Since it was pointed out in the comments on an earlier post I wrote about using the builder pattern how useful the <a href="http://msdn.microsoft.com/en-us/library/z5z9kes2(VS.71).aspx">implicit operator</a> could be in this context we've been using it wherever it makes sense.

The main benefit that using this approach provides is that our test code becomes more expressive since we don't need to explicitly call a method to complete the building of our object.


~~~csharp

public class FooBuilder 
{
	private string bar = "defaultBar";

	public FooBuilder Bar(string value)
	{
		bar = value;
		return this;
	}

	public static implicit operator Foo(FooBuilder builder) 
	{
		return new Foo { Bar = builder.bar };
	}
}
~~~


~~~csharp

public class Foo 
{
	public string Bar { get; set; }
}
~~~

We can then create a 'Foo' in our tests like this:


~~~csharp

var foo = new FooBuilder().Bar("bar");
~~~

The type of 'foo' is actually 'FooBuilder' but it will be implicitly converted to Foo when needed.

Alternatively we can force it to Foo earlier by explicitly defining the type:


~~~csharp

Foo foo = new FooBuilder().Bar("bar");
~~~

While playing around with the <a href="http://martinfowler.com/apsupp/spec.pdf">specification pattern</a> to try and create a cleaner API for some querying of collections I tried to create a specification builder to chain together several specifications.


~~~csharp

public interface IFooSpecification
{
    bool SatisfiedBy(Foo foo);
    IFooSpecification And(IFooSpecification fooSpecification);
}
~~~


~~~csharp

public abstract class BaseFooSpecification : IFooSpecification
{
    public abstract bool SatisfiedBy(Foo foo);
    public  IFooSpecification And(IFooSpecification fooSpecification)
    {
        return new AndSpecification(this, fooSpecification);   
    }
}
~~~


~~~csharp

public class FooBar : BaseFooSpecification
{
    private readonly string bar;

    public FooBar(string bar)
    {
        this.bar = bar;
    }

    public override bool SatisfiedBy(Foo foo)
    {
        return foo.Bar == bar;
    }
}
~~~


~~~csharp

public class FooQuery 
{
    private FooBar fooBarSpecification;
    private FooBaz fooBazSpecification;

    public FooQuery Bar(string value)
    {
        fooBarSpecification = new FooBar(value);
        return this;
    }

    public FooQuery Baz(string value)
    {
        fooBazSpecification = new FooBaz(value);
        return this;
    }


    public static implicit operator IFooSpecification(FooQuery fooQuery)
    {
        // User-conversion to interface error message displayed by Resharper
		
    }
}
~~~

The intention was to be able to filter a collection of foos with code like the following:


~~~csharp

foos.FindBy(new FooQuery().Bar("bar").Baz("baz"));
~~~

Unfortunately the <a href="http://msdn.microsoft.com/en-us/library/aa664464(VS.71).aspx">C# language specification</a> explicitly doesn't allow this:

<blockquote>
A class or struct is permitted to declare a conversion from a source type S to a target type T provided all of the following are true:

<ul><li> ...</li>
        <li>Neither S nor T is object or an interface-type.</li></ul>

</blockquote>

<blockquote>
User-defined conversions are not allowed to convert from or to <em>interface-types</em>. In particular, this restriction ensures that no user-defined transformations occur when converting to an <em>interface-type</em>, and that a conversion to an interface-type succeeds only if the object being converted actually implements the specified <em>interface-type</em>.
</blockquote>

I tried casting to the BaseFooSpecification abstract class instead and although that does compile it seemed to be leading me down a path where I would need to change the 'FindBy' signature to take in a BaseFooSpecification which I wasn't keen on.

It didn't prove possible to implicitly convert to a BaseFooSpecification when the signature for the method expected an IFooSpecification even though BaseFooSpecification implements IFooSpecification.

I don't think there is a way to get around this in C# 3.0 so I just ended up creating an explicit method to convert between the two - not quite as nice to read but the best I could come up with.
