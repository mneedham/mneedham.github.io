+++
draft = false
date="2009-11-25 11:59:11"
title="Clojure: The 'apply' function"
tag=['clojure']
category=['Clojure']
+++

In my continued playing around with Clojure I came across the '<a href="http://clojure.org/api#toc86">apply</a>' function which is used when we want to call another function with a number of arguments but have actually been given a single argument which contains the argument list.

The example that I've been trying to understand is applying '<a href="http://clojure.org/api#toc537">str</a>' to a collection of values.

I started off with the following:

~~~lisp

(str [1 2 3])
=> "[1 2 3]"
~~~
This just returns the string representation of the vector that we passed it, but what we actually want is to get an output of "123".

The 'apply' function allows us to do that:


~~~lisp

(apply str [1 2 3])
=> "123"
~~~

That is semantically/conceptually the same as doing this:


~~~lisp

(str 1 2 3)
=> "123"
~~~

I didn't quite understand how that could work though and my assumption was that somewhere in the Clojure source the above function call would be happening.

The definition of 'apply' is as follows:


~~~lisp

(defn apply
  "Applies fn f to the argument list formed by prepending args to argseq."
  {:arglists '([f args* argseq])}
  [#^clojure.lang.IFn f & args]
    (. f (applyTo (spread args))))
~~~

The first thing which I hadn't realised is that when you have an '&' before a parameter definition then any arguments provided will be put into a list.

If we break down the example above we end up with the following:


~~~lisp

(. str (applyTo (spread [[1 2 3]])))
~~~

The 'spread' function is defined like so:


~~~lisp

(defn spread
  {:private true}
  [arglist]
  (cond
   (nil? arglist) nil
   (nil? (next arglist)) (seq (first arglist))
   :else (cons (first arglist) (spread (next arglist)))))
~~~

In this case we only have one item in 'arglist' so on line 6 the 'next arglist' expression evaluates to nil.

This means that we create a seq from the first argument of the 'arglist' which is '[1 2 3]'.

Working our way back up to the 'apply' function what we end up with is this:


~~~lisp

(. str (applyTo (seq [1 2 3]))) 
=> "123"
~~~

This calls through to an 'applyTo' method defined on the 'clojure.lang.IFn' interface.

I'm not sure which of the implementations 'str' maps to but it seems like the 'str' function would eventually be called from the Java code with each of the values in the sequence passed in as a separate argument which is pretty neat!
