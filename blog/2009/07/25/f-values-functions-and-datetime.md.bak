+++
draft = false
date="2009-07-25 14:10:45"
title="F#: Values, functions and DateTime"
tag=['f']
category=['F#']
+++

One of the things I've noticed recently in my playing around with F# is that when we decide to <a href="http://www.markhneedham.com/blog/2009/07/12/f-wrapping-net-library-calls/">wrap calls</a> to the .NET DateTime methods there is a need to be quite careful that we are wrapping those calls with an F# function and not an F# value.

If we don't do this then the DateTime method will only be evaluated once and then return the same value for every call which is probably not the behaviour we're looking for.

The following shows how we could wrap call to get the current time in string format inside a value:


~~~ocaml

let timeNow = System.DateTime.Now.ToLongTimeString()
~~~

If we then execute 'timeNow' to show the current time before and after a sleep this is what we see:
            

~~~ocaml

printfn "The time now is %s" timeNow
System.Threading.Thread.Sleep(2000)
printfn "The time now is %s" timeNow
~~~


~~~text

The time now is 2:00:29 PM
The time now is 2:00:29 PM
~~~

As we can see the time has remained the same despite the fact that we put a sleep in between thew two calls. 

Looking at the C# version of this code via <a href="http://www.red-gate.com/products/reflector/">Reflector</a> we can see that 'timeNow' is just a string:


~~~csharp

public string timeNow;
~~~

The way to get the real current time is to define a function to get the time so that it will be reevaluated each time we ask for the time:


~~~ocaml

let timeNowUpToDate () = System.DateTime.Now.ToLongTimeString()
~~~

If we do the same test as we did above:


~~~ocaml

printfn "The time now is %s" (timeNowUpToDate())
System.Threading.Thread.Sleep(2000)
printfn "The time now is %s" (timeNowUpToDate())
~~~

We get the following results:


~~~ocaml

The time now is 2:05:13 PM
The time now is 2:05:15 PM
~~~

Which is what we were looking for in the first place!

Via Reflector again this is what that code would look like in C#:


~~~csharp

[Serializable]
internal class timeNowUpToDate@127 : FastFunc<Unit, string>
{
    // Methods
    internal timeNowUpToDate@127()
    {
    }

    public override string Invoke(Unit unitVar0)
    {
        return DateTime.Now.ToLongTimeString();
    }
}
~~~

As we can see every time the function is invoked a call to the DateTime API will be made which is what we want to happen.
