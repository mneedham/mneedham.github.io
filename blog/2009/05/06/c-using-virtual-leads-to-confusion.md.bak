+++
draft = false
date="2009-05-06 19:30:50"
title="C#: Using virtual leads to confusion?"
tag=['c', 'net']
category=['.NET']
+++

A colleague and I were looking through some code that I worked on a couple of months ago where I had created a one level hierarchy using inheritance to represent the response status that we get back from a service call.

The code was along these lines:


~~~csharp

public class ResponseStatus
{
    public static readonly ResponseStatus TransactionSuccessful = new TransactionSuccessful();
    public static readonly ResponseStatus UnrecoverableError = new UnrecoverableError();

    public virtual bool RedirectToErrorPage
    {
        get { return true; }
    }
}

public class UnrecoverableError : ResponseStatus
{
    
}

public class TransactionSuccessful : ResponseStatus
{
    public override bool RedirectToErrorPage
    {
        get { return false; }
    }
}
~~~

Looking at it now it does seem a bit over-engineered, but the main confusion with this code is that when you click through to the definition of 'RedirectToError' it goes to the ResponseStatus version of that property and it's not obvious that it is being overridden in a sub class, this being possible due to my use of the <a href="http://msdn.microsoft.com/en-us/library/9fkccyh4(VS.71).aspx">virtual</a> key word.

You therefore need to look in two places to work out what's going on which isn't so good.

A solution which we came up with which is a bit cleaner is like so:


~~~csharp

public abstract class ResponseStatus
{
    public static readonly ResponseStatus TransactionSuccessful = new TransactionSuccessful();
    public static readonly ResponseStatus UnrecoverableError = new UnrecoverableError();

    public abstract bool RedirectToErrorPage { get; }
}

public class UnrecoverableError : ResponseStatus
{
    public override bool RedirectToErrorPage
    {
        get { return true; }
    }
}

public class TransactionSuccessful : ResponseStatus
{
    public override bool RedirectToErrorPage
    {
        get { return false; }
    }
}
~~~

When you have more response statuses then I suppose there does become a bit more duplication but it's traded off against the improved ease of use/reading that we get.

It's generally considered good practice to <a href="http://www.artima.com/lejava/articles/designprinciples4.html">favour composition over inheritance</a> and from what I can tell the virtual keyword is only ever going to be useful if you're creating an inheritance hierarchy.

An interesting lesson learned. 
