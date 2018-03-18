+++
draft = false
date="2010-05-04 18:36:58"
title="F#: The Kestrel Revisited"
tag=['f']
category=['F#']
+++

A couple of days I wrote about <a href="http://www.markhneedham.com/blog/2010/05/03/coding-the-kestrel/">a 'returning' function</a> that I'd written to simplify a bit of F# code that I've been working on.

It's defined like so:


~~~ocaml

let returning t f = f(t); t 
~~~

And can then be used like this:


~~~ocaml

let build (t:Type) =
    returning (Activator.CreateInstance(t)) (fun t -> 
        t.GetType().GetProperties() |> Array.iter (fun p -> p.SetValue(t, createValueFor p, null)))
~~~

While I quite like this function it didn't quite feel like idiomatic F# to me. 

With idiomatic F# we would tend to design our functions in such a way that we can pipe data through a series of them by making use of the <a href="http://www.markhneedham.com/blog/2009/01/06/f-forward-operator/">forward</a> or <a href="http://www.markhneedham.com/blog/2009/01/12/f-partial-function-application-with-the-function-composition-operator/">function composition operators</a>.

With that idea in mind I decided to try switching the arguments to 'returning' around and renaming it so that the code would read more naturally:


~~~ocaml

let andApply f t = f(t); t 
~~~


~~~ocaml

let build (t:Type) =
    Activator.CreateInstance(t) |>
    andApply (fun t ->  t.GetType().GetProperties() |> Array.iter (fun p -> p.SetValue(t, createValueFor p, null)))
~~~

We partially apply the 'andApply' function to create a new function which takes in a type which is provided on the left hand side of the '|>' operator.

I think this now reads better than the original version.

What I find interesting is that when writing functions which I intend to be used like this the way I name them is different and the name only makes sense if it's used in that context.

Using the 'andApply' function on its own without making use of partial function application wouldn't read as cleanly as it does at the moment.

