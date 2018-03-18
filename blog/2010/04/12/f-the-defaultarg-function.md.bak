+++
draft = false
date="2010-04-12 18:21:41"
title="F#: The 'defaultArg' function"
tag=['f']
category=['F#']
+++

While reading through <a href="http://codebetter.com/blogs/matthew.podwysocki/archive/2009/04/13/from-imperative-to-functional-transposing-maps.aspx">an old blog post by Matthew Podwysocki about writing F# code in a functional rather than imperative way</a> I came across the 'defaultArg' function which I haven't seen previously.

It's quite a simple function that we can use when we want to set a default value if an option type has a value of 'None':

The type signature is as follows:

~~~ocaml

> defaultArg;;
val it : ('a option -> 'a -> 'a) = <fun:clo@0>
~~~

And the definition is relatively simple:

~~~ocaml

let defaultArg x y = match x with None -> y | Some v -> v
~~~

We could then use it if we were looking up a key in a dictionary but wanted to return a default value if there wasn't an entry for that key.

For example:


~~~ocaml

let myMap = Map.add "key" "value" Map.empty                
let result = defaultArg (Map.tryFind "nonExistentKey" myMap) "default"     
> val result : string = "default"
~~~

This is just another of the utility functions we can use in F# to allow us to keep composing functions even when we can get more than one type of result from another function.

