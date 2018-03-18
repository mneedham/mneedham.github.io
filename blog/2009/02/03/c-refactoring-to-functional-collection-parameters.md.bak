+++
draft = false
date="2009-02-03 07:18:40"
title="C#: Refactoring to functional collection parameters"
tag=['net', 'functional-programming']
category=['.NET']
+++

I wrote about a month or so ago about the <a href="http://www.markhneedham.com/blog/2008/12/17/functional-collection-parameters-in-c/">functional collection parameters</a> now available in C# and certainly one of the most fun refactorings for me is trying to get code written using a for loop into a state where it is using one of these.

With a bit of help from my colleague <a href="http://jamescrisp.org/">James Crisp</a>, these are some of the most common refactorings that I have come across so far.

There's a little bit of repetition with regards to my previous post but I think it's interesting to see the procedural approach to solving this problems versus the functional approach.

For the sake of the examples, the following classes are common:


~~~csharp

public class Foo
{
    private String bar;
    private String baz;
    private readonly bool specialFlag;

    public Foo(string bar, string baz, bool specialFlag)
    {
        this.bar = bar;
        this.baz = baz;
        this.specialFlag = specialFlag;
    }

    public bool HasSpecialFlag()
    {
        return specialFlag;
    }
}

public class NewFoo
{
    public NewFoo(Foo foo)
    {       
    }
}

public class NumericFoo
{
    public int Value { get; set; }
}
~~~ 

<h3>Going from one collection to another conditionally</h3>


~~~csharp

var foos = new List<Foo> {new Foo("bar1", "baz2", true), new Foo("bar2", "baz2", false)}.Where(foo => foo.HasSpecialFlag());

var newFoos = new List<NewFoo>();
foreach (var foo in foos)
{
    newFoos.Add(new NewFoo(foo));
}
~~~

We started off well using the 'Where' method to reduce the original list but we can do even better!


~~~csharp

var foos = new List<Foo> {new Foo("bar1", "baz2", true), new Foo("bar2", "baz2", false)};
foos.Where(foo => foo.HasSpecialFlag())
    .Select(foo => new NewFoo(foo));
~~~

Not significantly less code but it removes the need for more state in our code and makes the code more expressive at the same time which can only be a good thing.


<h3>Returning just one result</h3>

I came across some code last week which was iterating through a collection and then returning the first item which matched a certain criteria.

This would be useful if we wanted to get the first Foo object which has the special flag set for example.


~~~csharp

private Foo GetSpecialFoo(List<Foo> foos)
{
    foreach (var foo in foos)
    {
        if(foo.HasSpecialFlag())
        {
            return foo;
        }
    }
    return null;
}
~~~

My initial thoughts on coming upon this code were that it should be possible to get rid of the loop but I wasn't sure how to do the return. Luckily the 'First' method solves this problem.


~~~csharp

private Foo GetSpecialFoo(List<Foo> foos)
{
    return foos.Where(foo => foo.HasSpecialFlag()).First();
}
~~~

<h3>Accumulating some values</h3>
Adding values in collections together is surely one of the most common operations we do and functional collection parameters can help us here too.


~~~csharp

var numericFoos = new List<NumericFoo> {new NumericFoo {Value = 2}, new NumericFoo {Value = 5}};
int total = 0;
foreach (var numericFoo in numericFoos)
{
    total += numericFoo.Value;
}
~~~

Introducing a functional approach here gives us the following code:


~~~csharp

var numericFoos = new List<NumericFoo> {new NumericFoo {Value = 2}, new NumericFoo {Value = 5}};
int total = numericFoos.Sum(foo => foo.Value);
~~~

