+++
draft = false
date="2010-04-10 11:21:30"
title="Coding: Maybe vs Null Object patterns"
tag=['coding']
category=['Coding']
+++

On the project I'm currently working on my colleague <a href="http://christianralph.blogspot.com/">Christian Blunden</a> has introduced a version of the <a href="http://www.haskell.org/all_about_monads/html/maybemonad.html">Maybe</a> type into the code base, a concept that originally derives from the world of functional programming.

The code looks a bit like this:


~~~csharp

public interface Maybe<T>
{
	bool HasValue();
	T Value();
}	
~~~


~~~csharp

public class Some<T> : Maybe<T>
{
	private readonly T t;

	public Some(T t)
	{
		this.t = t;
	}

	public bool HasValue()
	{	
		return true;
	}

	public T Value()
	{		
		return t;
	}	
}
~~~


~~~csharp

public class None<T> : Maybe<T>
{
	public bool HasValue()
	{	
		return false;
	}

	public T Value()
	{		
		throw new NotImplementedException();
	}	
}
~~~

We would then use it in the code like this:


~~~csharp

public FooRepository
{
	public Maybe<Foo> Find(int fooId)
	{
		var foo = LookUpFooFromDatabase();

		if(foo == null)
		{
			return new None<Foo>();
		}
		return new Some<Foo>(foo);
	}

~~~


~~~csharp

var maybeFoo = fooRepository.Find(1);

if(maybeFoo.HasValue())
{
	// do something with it
}
// fail in misery	
~~~

The benefit we get from using this pattern is that we're explicitly defining in the contract of 'FooRepository.Find' that the method might not return a 'Foo' rather than leaving the callee to work out whether or not they need to check for a null value.

It's effectively the <a href="http://msdn.microsoft.com/en-us/library/1t3y8s4s(VS.80).aspx">Nullable pattern</a> except we can use it for reference types and not just primitives.

An alternative approach which <a href="http://twitter.com/dermotkilroy">Dermot</a> pointed out is the <a href="http://en.wikipedia.org/wiki/Null_Object_pattern">null object pattern</a>.

Typically when using that pattern we would treat the result of calling 'FooRepository.Find' the same regardless of whether we get a real 'Foo' or not.

That pattern would work quite well if we have to show a list of items in a grid, for example, and just showed blank cells if there isn't a real 'Foo'.

In our case we want to distinguish between whether we did or did not find a 'Foo' because the application behaves differently if we can't find one. Therefore in this case the null object pattern doesn't work so well.
