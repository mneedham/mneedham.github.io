+++
draft = false
date="2009-01-12 22:22:43"
title="F#: Partial Function Application with the Function Composition Operator"
tag=['net', 'f', 'currying', 'functional-programming']
category=['.NET', 'F#']
+++

In my continued reading of F# one of the ideas I've come across recently is that of partial function application.

This is a way of allowing us to combine different functions together and allows some quite powerful syntax to be written.

The term 'currying' is perhaps a better known term for describing this although as I understand they are not exactly the same.

<a href="http://en.wikipedia.org/wiki/Currying">Currying</a> is where we return a function that has been partially applied, in such a way that we can chain together a group of functions with a single argument.

I first came across this idea with the <a href="http://www.markhneedham.com/blog/2009/01/06/f-forward-operator/">forward piping operator</a> when reading about Matthew Podwysocki's <a href="http://www.codeplex.com/FsTest">FsTest</a> project but there is an even cleaner way of chaining functions together using <a href="http://blogs.msdn.com/chrsmith/archive/2008/06/14/function-composition.aspx">Function Composition</a>.

The function composition operator (>>) is defined thus:


~~~text

> (>>);;
val it : (('a -> 'b) -> ('b -> 'c) -> 'a -> 'c)
~~~

We take in two functions ('a -> 'b and 'b -> 'c) and one value ('a).
We evaluate the first function ('a -> 'b) with the argument 'a and then pass the result to the second function ('b -> 'c).

The way I understand this:

<ul>
<li>The first function takes in 'a (which is the 3rd argument passed to >>) and returns 'b</li>
<li>The second function takes in 'b (which is the return value of the first function) and returns 'c (which is the return value of >>)</li>
</ul>

Chris Smith perhaps best explains this as follows:


~~~text

> let inline (>>) f g x = g(f x)
val inline ( >> ) : ('a -> 'b) -> ('b -> 'c) -> 'a -> 'c
~~~

Given two functions (f, g) and a value x compute the result of f(x) and pass the result to g.

From my reading so far this operator makes it even easier to write code in a <a href="http://en.wikipedia.org/wiki/Declarative_programming">declarative</a> way (although I suppose the functional programming approach does encourage that in the first place).

We can achieve a lot of this nice declarative style by using the forward piping operator (|>) but the function composition operator takes it one step further:

Say we want to take a list of numbers, square all of them and then only show the negative ones:


~~~text

let findOddSquares = List.map (fun x-> x*x) >> List.filter (fun x -> x%2 <> 0);;
~~~

If we did this using the forward piping operator it would read like this i.e. we need to explicitly define the list:


~~~text

let findOddSquares list = list |> List.map (fun x-> x*x) |> List.filter (fun x -> x%2 <> 0);;
~~~

It's not that much more verbose but there's less code for doing the same thing if we use the function composition operator. I still think the forward piping operator works nicely when we just want to switch the order of the function and the data though:


~~~text

> [1..10] |> findOddSquares
val it : int list = [1; 9; 25; 49; 81]
~~~

As with all my F# posts, I'm still learning so please point out if I have anything wrong. Chris Smith has  <a href="http://blogs.msdn.com/chrsmith/archive/2008/06/14/function-composition.aspx">a closer to real life example</a>  of how to use partial function application that probably shows the benefits more than I have here.

* Update *

As pointed out in the comments I'm actually finding the odd squares not the negative ones as I originally posted.
