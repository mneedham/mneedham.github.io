+++
draft = false
date="2009-05-02 14:38:36"
title="F#: Stuff I get confused about"
tag=['f']
category=['F#']
+++

Coming from the world of C# I've noticed that there are a couple of things that I sometimes get confused about when playing around with stuff in F# land.

<h3>Passing arguments to functions</h3>
The way that we pass arguments to functions seems to be a fairly constant cause of confusion at the moment especially when doing that as part of a chain of other expressions where the use of brackets starts to become necessary.

In C# I'm used to putting the arguments in parentheses but that doesn't quite work in F#.

For example in <a href="http://www.markhneedham.com/blog/2009/04/13/f-a-day-of-writing-a-little-twitter-application/">my twitter application</a> I was trying to append two lists together similar to this:


~~~ocaml

let first_item = Seq.singleton("mark")
let second_item = Seq.singleton "needham"
let joined_items = Seq.append (first_item, second_item)
~~~

Which doesn't compile with the following error message:


~~~text

The type 'b * 'c' is not compatible with the type 'seq<'a>'
~~~

What we've done here is pass in a tuple containing 'first_item' and 'second_item' instead of passing them separately as arguments to the function.

The correct way of doing this is like so:


~~~ocaml

let joined_items = Seq.append first_item second_item
~~~

<h3>Values and Expressions</h3>

As I understand it in everything that we create in F# is an expression and when those expressions get evaluated we end up with some values.

I <a href="http://www.markhneedham.com/blog/2009/04/16/coding-dojo-12-f/">wrote previously how we got confused about this distinction in a coding dojo</a> a couple of weeks ago. That particular example was around how we need to create functions which take in an argument of type 'unit' if they are to be picked up by the XUnit.NET test runner.

<a href="http://www.twitter.com/davcamer">Dave</a> explains how this works in the comments of that post:

Given this code:


~~~ocaml

let should_do_something () = Assert.AreEqual(2,2)
~~~

<blockquote>
...
The extra space implies that should_do_something is a function, which takes one argument which is a unit. This is more similar to the syntax for declaring a one argument function where the argument is actually a value, such as

let square_it x = x * x
</blockquote>

When we put brackets around the arguments we are passing to functions they stop being passed as arguments as the compiler now tried to evaluate what's in the brackets first and pass it to the function.

To give an example from playing around with Seq.append, if we do this:


~~~ocaml

let joined_items = Seq.append (first_item second_item)
~~~

We get a compilation error over 'first_item':


~~~text

The value is not a function can cannot be applied
~~~ 

Here the compiler attempts to evaluate the function 'first_item' with an argument 'second_item' but since 'first_item' is actually a value and not a function this is impossible.

<h3>Referencing other types in our code</h3>
From my experiences so far it seems that F# uses <a href="http://en.wikipedia.org/wiki/One-pass_compiler">one pass compilation</a> such that you can only reference types or functions which have been defined either earlier in the file you're currently in or appear in a file which is specified earlier in the compilation order.

This seems a bit restrictive to me although I'm sure there's probably some benefits of this approach that I'm not yet aware of, maybe around type checking.
