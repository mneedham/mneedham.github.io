+++
draft = false
date="2009-11-17 11:10:37"
title="Clojure: A first look at recursive functions"
tag=['clojure']
category=['Clojure']
+++

I'm working through Stuart Halloway's '<a href="http://www.amazon.com/gp/product/1934356336?ie=UTF8&tag=marneesblo-20&linkCode=as2&camp=1789&creative=390957&creativeASIN=1934356336">Programming Clojure</a>' book and I just got to the section where it first mentions recursive functions.

It's a simple function to countdown from a given number to zero and then return that sequence.

This was one of the examples from the book:


~~~lisp

(defn countdown [result x] 
  (if (zero? x)
    result
    (recur (conj result x) (dec x))))
~~~

That function could then be called like this:


~~~lisp

(countdown [] 5) 
~~~

I wanted to see what the function would look if we didn't have the empty vector as a parameter.

From playing around with F# and Scala my first thought would be to write the function like this:


~~~lisp

(defn count-down [from]
  (defn inner-count [so-far x]
    (if (zero? x)
      so-far
      (inner-count (conj so-far x) (dec x))))
  (inner-count [] from))
~~~

As the book points out a bit further on, Clojure doesn't perform automatic tail call optimisation so we end up with a stack overflow exception if we run the function with a big enough input value.

Clojure does optimise calls to 'recur' so it makes more sense to use that if we want to avoid that problem.

This is an example which makes use of that:


~~~lisp

(defn count-down [from]
  (defn inner-count [so-far x]
    (if (zero? x)
      so-far
      (recur (conj so-far x) (dec x))))
  (inner-count [] from))
~~~

<a href="http://groups.google.com/group/clojure/browse_thread/thread/4e7a4bfb0d71a508?pli=1">Looking through the Clojure mailing list at a similar problem</a> I noticed that one of the suggestions was to arity overload the function to include an accumulator.


~~~lisp

(defn count-down
  ([from]
    (count-down [] from))
  ([so-far from]
    (if (zero? from)
      so-far
      (recur (conj so-far from) (dec from)))))
~~~

Written this way it feels a little bit like Haskell or Erlang but probably not idiomatic Clojure.

Anyway on the next page Halloway shows a better way to do this with much less code!


~~~lisp

(into [] (take 5 (iterate dec 5)))
~~~

I noticed that in Scala the idea of using 'take' and 'drop' on streams of values seems to be quite popular so I'm intrigued as to whether I'll find the same thing with Clojure.
