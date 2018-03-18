+++
draft = false
date="2009-01-02 22:35:31"
title="F# Option Types"
tag=['net', 'f', 'null-handling']
category=['.NET', 'F#']
+++

I've been spending a bit of time working through the <a href="http://manning.com/petricek/">Real World Functional Programming</a> book to learn a bit about F# and one of the cool features I came across today (while reading <a href="http://blogs.msdn.com/chrsmith/archive/2008/07/10/mastering-f-lists.aspx">Chris Smith's post on F# lists</a>) is the Option type.

I first came across this idea a few months ago when discussing <a href="http://www.markhneedham.com/blog/2008/08/16/null-handling-strategies/">null handling strategies</a> with a <a href="http://markthomas.info/blog/">colleague</a> who pointed out that you could get around this problem in Scala by using the <a href="http://blog.danielwellman.com/2008/03/using-scalas-op.html">Option class</a>. 

From what I can tell this works pretty much the same way and solves the problem that we have when we want to perform an operation but don't know whether or not a value will be returned. 

If a value is returned then we don't have a problem, but if not then we want a clean way of handling this.

One example of this is when trying to retrieve a value from a collection. When we try to get a value which doesn't exist this would typically throw an exception.

To give an F# example, trying to find the value 7 in a list from 1-5:


~~~text

List.find (fun x -> x = 7) [1..5];;
~~~

This throws the following exception:


~~~text

System.Collections.Generic.KeyNotFoundException: The item was not found in the collection
   at Microsoft.FSharp.Core.Operators.not_found[T]()
   at <StartupCode$FSI_0277>.$FSI_0277._main()
~~~

Luckily there is another way of trying to find this value:


~~~text

List.tryfind (fun x -> x = 7) [1..5];;
~~~


~~~text

val it : int option = None
~~~

Note that the type is now 'int option' with a value of 'None'. If we search for a value that does exist:


~~~text

List.tryfind (fun x -> x = 3) [1..5];;
~~~


~~~text

val it : int option = Some 3
~~~

We get a return value of 'Some 3'. 

The beauty of this approach comes when pattern matching against these values. To give a contrived example:


~~~text

let find value list =
    let option = List.tryfind(fun item -> item = value) list
    match option with
    | None -> printfn "Value %d not found" value
    | Some(valueFound) -> printfn "Found value: %d" valueFound;;
~~~


~~~text

> find 1 [1..5];;
Found value: 1
val it : unit = ()
~~~


~~~text

> find 6 [1..5];;
Value 6 not found
val it : unit = ()
~~~

I really like this idea and it seems cleaner than approaches I have used in C# and Java to achieve a similar outcome. I'm sure I'll come across more usages for it as my knowledge of F# increases.

Incidentally, Luis Diego Fallas has written a cool post showing <a href="http://langexplr.blogspot.com/2008/06/using-f-option-types-in-c.html">how to use option types in C#</a>. The syntax obviously isn't quite as clean as it is in F# but it still reads reasonably nicely.
