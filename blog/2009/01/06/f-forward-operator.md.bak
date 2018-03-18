+++
draft = false
date="2009-01-06 00:19:52"
title="F#: Forward Operator"
tag=['net', 'f']
category=['.NET', 'F#']
+++

Continuing on my F# journey I came across a post by Ben Hall describing the <a href="http://blog.benhall.me.uk/2008/12/learning-new-language-write-some-tests.html">approach he takes when learning a new programming language</a>. 

One of the approaches he describes is that of writing unit tests to help keep your learning on track. I've only been using the F# interactive console so far so I thought I'd give it a try.

After reading about the somewhat <a href="http://devhawk.net/2007/12/12/Practical+F+Parsing+Unit+Testing.aspx">convoluted approach</a> required to use NUnit or MBUnit to write F# unit tests I came across <a href="http://www.codeplex.com/xunit">XUnit.NET</a> via <a href="http://weblogs.asp.net/podwysocki/archive/2008/06/19/announcing-fstest-a-testing-dsl-for-f.aspx">Matthew Podwysocki's blog post about FsTest</a> - a <a href="http://www.codeplex.com/FsTest">testing DSL</a> he's written to use on top of XUnit.NET.

One of the cool F# features I came across while reading Matthew's post is the Forward Operator (|>). 

This is particularly useful for writing test assertions which read like English. For example:


~~~text

[<Fact>] let list_should_contain_3() = [1..5] |> should contain 3
~~~

Typically we would have the function followed by the data we want to apply it against but using this operator allows us to do it the other way around.

From my understanding the <a href="http://www.c-sharpcorner.com/UploadFile/rmcochran/fsharptypes03212008225543PM/fsharptypes.aspx">forward operator</a> (also known as the push operator) pushes the value from the left hand side of the function to the first parameter of the function. 

To use a simpler example of adding 5 to a number.

Normally we would do this:


~~~text

> (fun x -> x+5) 5;;
val it : int = 10
~~~

Using the forward operator we can do this instead:


~~~text

> 5 |> (fun x -> x+5)
val it : int = 10
~~~

If we look at the definition of "|>" this makes a bit more sense:


~~~text

> (|>);;
val it : ('a -> ('a -> 'b) -> 'b) = <fun:clo@84>
~~~

It takes in 2 arguments "'a" and "('a -> 'b)" and returns "'b".

The first argument in this case is the value '5' and the second is a function which takes in an "'a" and returns a "'b", in this case the (x -> x +5) function.

Armed with that knowledge the DSL example hopefully now makes more sense. To recall with the full code:


~~~text

#light
open Xunit

let should f actual = f actual
let contain (expected: int) (actual: int list) = Assert.Contains(expected, actual)

[<Fact>] let list_should_contain_3() = [1..5] |> should contain 3
~~~

This is the same as writing the following:


~~~text

[<Fact>] let list_should_contain_3() = should contain 3 [1..5]
~~~

Working from the 'should' outwards...


~~~text

> should;;
val it : (('a -> 'b) -> 'a -> 'b) = <fun:clo@0_1>
~~~

It expects to take in a function ('a -> 'b), a value ('a) and will return a value ('b).

In this case that function is 'contain':


~~~text

> contain;;
val it : (int -> int list -> unit) = <fun:clo@0_2>
~~~

It expects to take in two values (an int and a list of ints) and doesn't return any value (unit is the equivalent of void in C#.)

Evaluating both together:


~~~text

> should contain;;
val it : (int -> int list -> unit) = <fun:clo@88_1>
~~~

Here we have a partial application of the 'should' function i.e. we have only passed in one of the arguments (the 'contain' function). We have now created another function which requires an int and a list of ints and returns nothing.

If we now take the whole statement together:


~~~text

[1..5] |> should contain 1;;
~~~

It seems like the [1..5] should be applied as the first argument to the 'contain' function but in actual fact the precedence rules dictate that the right hand side of the "|>" gets evaluated first meaning that the 1 is passed as the first argument to 'contain'.

The [1..5] is passed in as the second argument to the 'contain' function completing all the inputs needed by the expression and therefore executing the Assert.Contains(...) assertion.

Matthew Cochran has an article which helps <a href="http://www.c-sharpcorner.com/UploadFile/rmcochran/fsharptypes03212008225543PM/fsharptypes.aspx">explain the operator with some diagrams</a> and Matthew Podwysocki talks about it more in his post about <a href="http://weblogs.asp.net/podwysocki/archive/2008/06/04/language-oriented-programming-and-functional-unit-testing-in-f.aspx">language oriented programming</a>.

I'm new to F# so if I've got anything wrong about the way this works please let me know.
