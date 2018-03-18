+++
draft = false
date="2009-01-21 23:49:13"
title="C#: Builder pattern still useful for test data"
tag=['c', 'net']
category=['.NET']
+++

I had thought that with the ability to use the new <a href="http://davidhayden.com/blog/dave/archive/2006/12/04/ObjectInitializationExpressions.aspx">object initalizer</a> syntax in C# 3.0 meant that the builder pattern was now no longer necessary but some recent refactoring efforts have made me believe otherwise.

My original thought was that the builder pattern was really useful for providing a nicely chained way of creating objects, but after a bit of discussion with some colleagues I have come across three different reasons why we might want to use the builder pattern to create test data:

<ul>
<li>It creates a nice to read fluent interface describing the object being created. This argument holds more for Java rather than C# where we now have object initializers.</li>
<li>Domain objects are a bit complicated to create - encapsulate this logic in the builder.</li>
<li>We want to default non null data on some of the fields in our object. If we don't explicitly set a value for a property in C# it defaults to null.</li>
</ul>

Even with the object initializer syntax we can still end up having to specify extra data that we don't really care about in our test. The following is not uncommon:


~~~csharp

new Foo {Bar = "bar", Baz = "baz", Bling = "bling"};
~~~


~~~csharp

public class Foo
{
    public string Bar {get; set;}
    public string Baz { get; set; }
    public string Bling { get; set; }
}
~~~

Let's say we only care about Bar for this test though but Baz and Bling are both being used in our code so we end up with a Null Reference Exception if we don't set values for them. We can quickly end up having this redundant data being repeated across all our tests.

In steps the builder pattern!


~~~csharp

new FooBuilder().Bar("bar").Build();
~~~


~~~csharp

public class FooBuilder
{
    private string bar = "defaultBar";
    private string baz = "defaultBaz";
    private string bling = "defaultBling";

    public FooBuilder Bar(string value)
    {
        bar = value;
        return this;
    }

    public FooBuilder Baz(string value)
    {
        baz = value;
        return this;
    }

    public FooBuilder Bling(string value)
    {
        bling = value;
        return this;
    }

    public Foo Build()
    {
        return new Foo {Bar = bar, Baz = baz, Bling = bling};
    }
}
~~~

It takes a bit more code to setup but every time we use the builder it saves us typing in extra data that we don't need.

It would be even better if we could not have to call that 'Build' method and we can get around this by using the <a href="http://realfiction.net/?q=node/138">implicit operator</a>, the problem being that you need to apply it to the target class (i.e. Foo) rather than the class you want to implicitly convert from (i.e. FooBuilder).

I don't really want to change a production code class just for test purposes so the 'Build' will have to stay in there for the time being.
