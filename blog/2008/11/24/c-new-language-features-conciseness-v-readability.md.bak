+++
draft = false
date="2008-11-24 23:41:36"
title="Lambda in C#: Conciseness v Readability"
tag=['c', 'net', 'lambda']
category=['.NET']
+++

One of the things I really disliked when I first came across C# 3.0 code was <a href="http://www.davidhayden.com/blog/dave/archive/2006/11/30/LambdaExpressionsExtensionMethodsLINQ.aspx">lambda functions</a>.  

At the time I remember speaking to my <a href="http://markthomas.info/blog/">Tech Lead</a> and expressing the opinion that they were making the code harder to understand and were valuing <strong>conciseness over readability</strong>. 

After a week of reading about the new C# features and understanding how they worked the code was now more readable to me and a lot of the boiler plate code that I had come to expect was no longer necessary.

My favourite example of the power of lambda is when we want to iterate through a collection of items and apply the same operation to every item in the collection.

In normal C# we might do this:


~~~csharp

public class Foo
{
    private String bar;
    private String baz;

    public Foo(String bar, String baz)
    {
        this.bar = bar;
        this.baz = baz;
    }

    public override string ToString()
    {
        return string.Format("{0} - {1}", bar, baz);
    }

}
~~~


~~~csharp

var foos = new List<Foo>();
foos.Add(new Foo("bar1", "baz1"));
foos.Add(new Foo("bar2", "baz2"));

var fooString = new List<String>();
foreach (var foo in foos)
{
    fooString.Add(foo.ToString());
}
~~~

Using the power of C# 3.0 we can change that last for each statement to read something like this:


~~~csharp

var fooString = foos.Select(f => f.ToString());
~~~

This is much more concise but I think the judgement on its readability depends on one's understanding of the language feature.

One idea I am considering trying is using methods which describe more clearly what the lambda function is doing. This is an idea I came across from Kris Kemper's post about using <a href="http://blog.kriskemper.com/2008/10/23/granularity-of-abstractions/">similar Ruby language features</a>. 

In the example I gave perhaps wrapping the foo.Select(...) in a method called 'ConvertToStringRepresentation()' might make it more readable - it's clearly up for debate though.

When I was learning how lambda worked I found it useful to be able to do the comparison of how you would write code without it and being able to compare that with how you could do it with lambda. I also found having some understanding of how <a href="http://eli.thegreenplace.net/2006/04/18/understanding-ruby-blocks-procs-and-methods/">Ruby blocks</a> worked made it easier as well.

Clearly having powerful language features means that a language is much easier to abuse but I think if used sensibly then <b>readability and conciseness need not be mutually exclusive.</b>
