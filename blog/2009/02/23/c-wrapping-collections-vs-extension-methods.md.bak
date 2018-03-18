+++
draft = false
date="2009-02-23 20:24:26"
title="C#: Wrapping collections vs Extension methods"
tag=['c', 'net']
category=['.NET']
+++

Another interesting thing I've noticed in C# world is that there seems to be a trend towards using extension methods as much as possible. One area where this is particularly prevalent is when working with collections. 

From reading <a href="http://www.markhneedham.com/blog/2008/11/06/object-calisthenics-first-thoughts/">Object Calisthenics</a> and working with <a href="http://pilchardfriendly.blogspot.com/">Nick</a> I have got used to wrapping collections and defining methods on the wrapped class for interacting with the underlying collection.


For example, given that we have a collection of Foos that we need to use in our system we might wrap that in an object Foos.


~~~csharp

public class Foos
{
    private readonly IEnumerable<Foo> foos;

    public Foos(IEnumerable<Foo> foos)
    {
        this.foos = foos;
    }

    public Foo FindBy(string id)
    {
        return foos.Where(foo => foo.Id == id).First();
    }

    // some other methods to apply on the collection
}
~~~

Extension methods provide another way of achieving the same thing while not needing to wrap it.


~~~csharp

public static class FooExtensions
{
    public static Foo FindBy(this IEnumerable<Foo> foos, string id)
    {
        return foos.Where(foo => foo.Id == id).First();
    }
}
~~~

It seems like there isn't much difference in wrapping the collection compared to just using an extension method to achieve the same outcome.

The benefit I see in wrapping is that we take away the ability to do anything to the collection that we don't want to happen. You only have the public API of the wrapper to interact with.

The benefit of the extension method approach is that we don't need to create the object Foos - we can just call a method on the collection.

I'm not sure which is a better approach - certainly languages which provide the ability to open classes seem to favour taking that approach over wrapping but I still think it's nice to have the wrapper as it means you don't have to be explicitly passing collections all around the code.

But maybe that's just me.
