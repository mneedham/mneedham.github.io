+++
draft = false
date="2009-06-16 20:29:29"
title="Functional Collection Parameters: Handling the null collection"
tag=['c', 'net', 'functional-programming', 'functional-collection-parameters']
category=['.NET']
+++

One of the interesting cases where I've noticed we tend to avoid <a href="http://www.markhneedham.com/blog/2008/12/17/functional-collection-parameters-in-c/">functional</a> <a href="http://www.markhneedham.com/blog/2009/01/19/f-vs-c-vs-java-functional-collection-parameters/">collection parameters</a> in our code base is when there's the possibility of the collection being null.

The code is on the boundary of our application's interaction with another service so it is actually a valid scenario that we could receive a null collection.

When using extension methods, although we wouldn't get a null pointer exception by calling one on a null collection, we would get a 'source is null' exception when the expression is evaluated so we need to protect ourself against this.

As a result of defending against this scenario we have quite a lot of code that looks like this:


~~~csharp

public IEnumerable<Foo> MapFooMessages(IEnumerable<FooMessage> fooMessages)
{
	var result = new List<Foo>();
	if(fooMessagaes != null)
	{
		foreach(var fooMessage in fooMessages)
		{
			result.Add(new Foo(fooMessage));
		}
	}
	return result;
}
~~~

The method that we want to apply here is 'Select' and even though we can't just apply that directly to the collection we can still make use of it.


~~~csharp

private IEnumerable<Foo> MapFooMessages(IEnumerable<FooMessage> fooMessages)
{
	if(fooMessages == null) return new List<Foo>();
	return fooMessages.Select(eachFooMessage => new Foo(eachFooMessage));
}
~~~

There's still duplication doing it this way though so I pulled it up into a 'SafeSelect' extension method:


~~~csharp

public static class ICollectionExtensions
{
       public static IEnumerable<TResult> SafeSelect<TSource, TResult>(this IEnumerable<TSource> source, Func<TSource, TResult> selector)
       {
               return source == null ? new List<TResult>() : source.Select(selector) ;
       }
}
~~~

We can then make use of this extension method like so:


~~~csharp

private IEnumerable<Foo> MapFooMessages(IEnumerable<FooMessage> fooMessages)
{
	return fooMessages.SafeSelect(eachFooMessage => new Foo(fooMessage));
}
~~~

The extension method is a bit different to the original way that we did this as I'm not explicitly converting the result into a list at the end which means that it will only be evaluated when the data is actually needed.

In this particular case I don't think that decision will have a big impact but it's something interesting to keep in mind.
