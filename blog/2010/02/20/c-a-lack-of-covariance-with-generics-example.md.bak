+++
draft = false
date="2010-02-20 12:17:16"
title="C#: A lack of covariance with generics example"
tag=['c', 'linq']
category=['.NET']
+++

One of the things I find most confusing when reading about programming languages is the idea of <a href="http://codebetter.com/blogs/raymond.lewallen/archive/2006/12/28/Covariance-and-Contravariance.aspx">covariance and contravariance</a> and while I've previously read that covariance is not possible when using generics in C# I recently came across an example where I saw that this was true.

I came across this problem while looking at how to refactor some code which has been written in an imperative style:


~~~csharp

public interface IFoo 
{
	string Bar { get; set; } 
}
    
public class Foo : IFoo 
{ 
	public string Bar { get; set; }
}
~~~


~~~csharp

private IEnumerable<IFoo> GetMeFoos()
{
    var someStrings = new[] { "mike", "mark" };

    var someFoos = new List<IFoo>();
    foreach (var s in someStrings)
    {
        someFoos.Add(new Foo { Bar = s });
    }
    return someFoos;
}
~~~

I changed the code to read like so:


~~~csharp

private IEnumerable<IFoo> GetMeFoos()
{
    var someStrings = new[] { "mike", "mark" };
    return someStrings.Select(s => new Foo { Bar = s });
}
~~~

Which fails with the following compilation error:


~~~text

Error	1	Cannot implicitly convert type 'System.Collections.Generic.IEnumerable<Test.Foo>' to 'System.Collections.Generic.IEnumerable<Test.IFoo>'. An explicit conversion exists (are you missing a cast?)
~~~

I thought the compiler would infer that I actually wanted a collection of 'IFoo' given that I was returning from the method directly after the call to Select but it doesn't.

As I understand it the reason that we can't downcast an IEnumerable of 'Foo' to an IEnumberable of 'IFoo' is that we would run into problems if we worked of the assumption that our original collection only contained Foos in it later on in our program.

For example it would be possible to add any item which implemented the 'IFoo' interface into the collection even if it wasn't a 'Foo':


~~~csharp

// this code won't compile

List<Foo> foos = new List<Foo>();
// add some foos

List<IFoo> ifoos = foos;

foos.Add(new SomeOtherTypeThatImplementsIFoo());
~~~

It's not possible to convert 'SomeOtherTypeThatImplementsIFoo' to 'Foo' so we would run ourself into problems.

<a href="http://blogs.msdn.com/rmbyers/archive/2005/02/16/375079.aspx">Rick Byers has a post from a few years ago where he explains how this works in more detail</a> and also points out that covariance of generics is actually supported by the CLR, just not by C#.

In the case I described we can get around the problem by casting 'Foo' to 'IFoo' inside the 'Select':


~~~csharp

private IEnumerable<IFoo> GetMeFoos()
{
    var someStrings = new[] { "mike", "mark" };
    return someStrings.Select(s => (IFoo) new Foo { Bar = s });
}
~~~
