+++
draft = false
date="2009-12-09 22:10:27"
title="Haskell vs F#: Function composition"
tag=['f', 'haskell']
category=['F#']
+++

I'm reading through John Hughes' '<a href="http://www.cs.chalmers.se/~rjmh/Papers/whyfp.html">Why functional programming matters</a>' paper and one thing I've come across which is a bit counter intuitive to me is the Haskell function composition operator.

I've <a href="http://www.markhneedham.com/blog/2009/01/12/f-partial-function-application-with-the-function-composition-operator/">written previously about F#'s function composition operator</a> which is defined as follows:


~~~ocaml

let inline (>>) f g x = g(f x)
~~~

To write a function which doubled all the values in a list and then returned the odd values we'd do this:


~~~ocaml

let doubleThenOdd = List.map (fun x -> x*2) >> List.filter (fun x -> x % 2 <> 0)
~~~

Of course it's not possible for there to be any values!


~~~text

doubleThenOdd [1..5];;
val it : int list = []
~~~

Based on that understanding I would expect the Haskell function composition operator ('.') to work in the same way:


~~~haskell

let doubleThenOdd = map (\ x -> x*2) . filter (\ x -> (mod x 2) /= 0)
~~~

But it doesn't!


~~~text

Prelude> doubleThenOdd [1..5]
[2,6,10]
~~~

In Haskell the functions are applied from right to left rather than left to right as I had expected.

The definition of '.' is therefore:


~~~text

(f . g) x = f (g x)
~~~

So to get what I wanted we'd need to switch around 'map' and 'filter':


~~~haskell

let doubleThenOdd = filter (\ x -> (mod x 2) /= 0) . map (\ x -> x*2)
~~~


~~~text

Prelude> doubleThenOdd [1..5]
[]
~~~

It's not too difficult to follow once I worked out that it was different to what I was used to but I was very confused for a while!

Is there a reason why they implement this operator differently?
