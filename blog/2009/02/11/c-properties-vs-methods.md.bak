+++
draft = false
date="2009-02-11 11:20:08"
title="C#: Properties vs Methods"
tag=['c', 'net']
category=['.NET']
+++

I was browsing through our tests today and noticed a test along these lines (simplified for example purposes):


~~~csharp

[Test, ExpectedException(typeof(Exception))]
public void ShouldThrowExceptionIfNoBarSet()
{
    var bar = new Foo(null).Bar;
}
~~~


~~~csharp

public class Foo
{
	private readonly string bar;

	public Foo(string bar)
	{
    		this.bar = bar;
	}

	public string Bar
	{
    		get
    		{
        		if (bar == null)
        		{
            		throw new Exception("No bar");
        		}
        		return bar;
    		}
	}
}
~~~

What I found strange here is that 'bar' is never used and Resharper points out as much. If we try to remove it, however, the code no longer compiles.


~~~csharp

[Test, ExpectedException(typeof(Exception))]
public void ShouldThrowExceptionIfNoBarSet()
{
    new Foo(null).Bar;
}
~~~


~~~text

Only call, assignment, increment, decrement, and new object expressions can be used as a statement.
~~~

We therefore need to assign the call to Bar to a variable even though we never intend to reference it.

This problem wouldn't happen if Bar was a method instead.


~~~csharp

[Test, ExpectedException(typeof(Exception))]
public void ShouldThrowExceptionIfNoBarSet()
{
    new Foo(null).Bar();
}
~~~


~~~csharp

public string Bar()
{
    if (bar == null)
    {
        throw new Exception("No bar");
    }
    return bar;
}
~~~

Which got me thinking how do we know when to use a method and when to use a property?

Clearly if there are parameters to be passed in then we have no choice but to use a method since we can't call properties with parameters. 

If we are simply returning data values then we might as well just use properties since this is what they were made for. We can even make use of automated properties to smooth the process.

Which leaves the situation where there is some logic that needs to be calculated, no outside data is needed to do this calculation and a result is returned to the client.

Probably because of the Java influence my preference would be to do this using a method but I don't really have any other justification for not using a property to achieve the same thing.

Discussing this briefly with <a href="http://twitter.com/davcamer">Dave</a> we thought maybe if a property is used then the execution needs to be idempotent (i.e. return the same result every time) although the argument could be made that well written methods should also be side effect free. Eric Evans' advocates writing <a href="http://domaindrivendesign.org/discussion/messageboardarchive/SideEffectFreeFunctions.html">side effect free functions</a> in <a href="http://domaindrivendesign.org/">Domain Driven Design</a> for example.

Does anyone have any compelling reasons why or why not to use one or the other?
