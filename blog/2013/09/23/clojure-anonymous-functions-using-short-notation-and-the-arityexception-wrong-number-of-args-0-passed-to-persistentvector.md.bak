+++
draft = false
date="2013-09-23 21:42:12"
title="Clojure: Anonymous functions using short notation and the 'ArityException Wrong number of args (0) passed to: PersistentVector'"
tag=['clojure']
category=['Clojure']
+++

<p>In the time I've spent playing around with Clojure one thing I've always got confused by is the error message you get when trying to return a vector using the anonymous function shorthand.</p>


<p>For example, if we want function which creates a vector with the values 1, 2, and the argument passed into the function we could write the following:</p>



~~~lisp

> ((fn [x] [1 2 x]) 6)
[1 2 6]
~~~

<p>However, when I tried to convert it to the shorthand '#()' syntax I got the following exception:</p>



~~~lisp

> (#([1 2 %]) 6)
clojure.lang.ArityException: Wrong number of args (0) passed to: PersistentVector
                                      AFn.java:437 clojure.lang.AFn.throwArity
                                       AFn.java:35 clojure.lang.AFn.invoke
                                  NO_SOURCE_FILE:1 user/eval575[fn]
                                  NO_SOURCE_FILE:1 user/eval575
~~~

<p>On previous occasions I've just stopped there and gone back to the long hand notation but this time I wanted to figure out why it didn't work as I expected.</p>


<p>I came across <a href="http://stackoverflow.com/questions/13204993/anonymous-function-shorthand">this StackOverflow post</a> which explained the way the shorthand gets expanded:</p>



~~~lisp

#() becomes (fn [arg1 arg2] (...))
~~~

<p>which means that:</p>



~~~lisp

#(([1 2 %]) 6) becomes ((fn [arg] ([1 2 arg])) 6)
~~~

<p>We are evaluating the vector <cite>[1 2 arg]</cite> as a function but aren't passing any arguments to it. One way it can be used as a function is if we want to return a value at a specific index e.g.</p>



~~~lisp

> ([1 2 6] 2)
6
~~~

<p>We don't want to evaluate a vector as a function, rather we want to return the vector using the shorthand syntax. To do that we need to find a function which will return the argument passed to it and then pass the vector to that function.</p>


<p>The <cite><a href="http://clojuredocs.org/clojure_core/clojure.core/identity">identity</a></cite> function is one such function:</p>



~~~lisp

> (#(identity [1 2 %]) 6)
[1 2 6]
~~~

<p>Or if we want to be more concise the <cite><a href="http://clojuredocs.org/clojure_core/clojure.core/-%3E">thread-first (->)</a></cite> works too:</p>



~~~lisp

> (#(-> [1 2 %]) 6)
[1 2 6]
~~~
