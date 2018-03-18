+++
draft = false
date="2009-06-18 18:31:59"
title="Functional Collection Parameters: A different way of thinking about collections"
tag=['functional-programming', 'functional-collection-parameters']
category=['.NET']
+++

One of the changes that I've noticed in my coding now compared to around 7 or 8 months ago is that whenever there's some operations to be performed on a collection I am far more inclined to think of how to do those operations using a functional approach.

I've written previously about the ways I've been <a href="http://www.markhneedham.com/blog/2008/12/17/functional-collection-parameters-in-c/">making use</a> <a href="http://www.markhneedham.com/blog/2009/02/03/c-refactoring-to-functional-collection-parameters/">of</a> <a href="http://www.markhneedham.com/blog/2009/06/16/functional-collection-parameters-handling-the-null-collection/">functional</a> <a href="http://www.markhneedham.com/blog/2009/01/19/f-vs-c-vs-java-functional-collection-parameters/">collection</a> parameters in my code but what I hadn't really considered was that the way of thinking about the problem we want to solve is slightly different. 

While <a href="http://twitter.com/deanrcornish">Dean</a> and I were talking through <a href="http://www.markhneedham.com/blog/2009/06/16/functional-collection-parameters-handling-the-null-collection/">the refactoring that I mentioned in my post about handling null collections</a>, we realised that the way it was originally written followed a very sequential mindset.


~~~csharp

public IEnumerable<Foo> MapFooMessages(IEnumerable<FooMessage> fooMessages)
{
	var result = new List<Foo>();
	if(fooMessages != null)
	{
		foreach(var fooMessage in fooMessages)
		{
			result.Add(new Foo(fooMessage));
		}
	}
	return result;
}
~~~

<ul>
<li>Create a new collection</li>
<li>Take an existing collection</li>
<li>If it's not null then iterate over the existing collection</li>
<li>Add each item to the new collection</li>
<li>Return the new collection</li>
</ul>

I find when I'm thinking about doing this type of code now my thought process is <strong>more focused towards the collection as a whole</strong> rather than about the individual items in the collection. 

If I do want to only apply an operation on a subset of the collection then I need to first apply another function to the whole collection that filters the collection down. I find myself thinking about what I want to happen rather than how I want to do it - <strong>a declarative approach over an imperative one in summary</strong>.

One of the LINQ C# extension methods which I sometimes find myself abusing is the 'ForEach' one which I feel is used a lot more times than is necessary and often ends up with complicated lambda blocks inside it which could be avoided by using some of the other functions.

To give a very simple example of some code I came across recently:


~~~csharp

public IEnumerable<string> GetFooKeys(IEnumerable<Foo> foos)
{
	var list = new List<string>();
	foos.Where(foo => foo.Opted).ToList().ForEach(foo => list.Add(foo.Key));
	return list;
}
~~~

We are making use of functional collection parameters but we can easily do this without using the 'ForEach' method:


~~~csharp

public IEnumerable<string> GetFooKeys(IEnumerable<Foo> foos)
{
	return foos.Where(foo => foo.Opted).Select(foo => foo.Key);
}
~~~

I think the danger with 'ForEach' is that we are creating side effects which may be unexpected. In this case there's not really that much problem as we're just adding a value to a list but it is possible to do anything else in the ForEach block as well.

I also came across a good post written by one of the 8th light guys talking about <a href="http://blog.8thlight.com/articles/2009/6/16/a-functional-refactoring-in-scala">the use of ForEach in Scala and how we can use it in a way that minimises side effects</a>.
