+++
draft = false
date="2010-02-08 23:17:47"
title="Functional C#: Extracting a higher order function with generics"
tag=['c']
category=['.NET']
+++

While working on some code with <a href="http://www.the-arm.com/">Toni</a> we realised that we'd managed to create two functions that were almost exactly the same except they made different service calls and returned collections of a different type.

The similar functions were like this:


~~~csharp

private IEnumerable<Foo> GetFoos(Guid id)
{
    IEnumerable<Foo> foos = new List<Foo>();
    try
    {
        foos = fooService.GetFoosFor(id);
    }
    catch (Exception e)
    {
        // do some logging of the exception
    }
    return foos;
}
~~~


~~~csharp

private IEnumerable<Bar> GetBars(Guid id)
{
    IEnumerable<Bar> bars = new List<Bar>();
    try
    {
        bars = barService.GetBarsFor(id);
    }
    catch (Exception e)
    {
        // do some logging of the exception
    }
    return bars;
}
~~~

We're defining the empty lists so that if the service throws an exception we can make use of an empty list further on in the code. A failure of the service in this context doesn't mean that the application should stop functioning.

My thinking here was that we should be able to pull out the service calls into a function but the annoying thing is that they return different types of collections so I initially thought that we'd be unable to remove the duplication.

Thinking about the problem later on I realised we could just define the return value of the service call in the function to use generics.

We therefore end up with this solution:


~~~csharp

private IEnumerable<Bar> GetBars(Guid id)
{
	return GetValues(() => barService.GetBarsFor(id));
}
~~~


~~~csharp

private IEnumerable<Foo> GetFoos(Guid id)
{
	return GetValues(() => fooService.GetFoosFor(id));
}
~~~


~~~csharp

private IEnumerable<T> GetValues<T>(Func<IEnumerable<T>> getValues)
{
    IEnumerable<T> values = new List<T>();
    try
    {
        values = getValues();
    }
    catch (Exception e)
    {
        // do some logging of the exception
    }
    return values;
}
~~~

I think the code is still quite readable and it's relatively obvious what it's supposed to be doing. 
