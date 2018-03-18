+++
draft = false
date="2012-11-06 12:42:36"
title="Clojure: Thread last (->>) vs Thread first (->)"
tag=['clojure']
category=['Clojure']
+++

In many of the Clojure examples that I've come across the <a href="http://clojuredocs.org/clojure_core/clojure.core/-%3E%3E">thread last (->>)</a> macro is used to make it easier (for people from a non lispy background!) to see the transformations that the initial data structure is going through.

In one of my recent posts I showed how <a href="http://www.markhneedham.com/blog/2012/10/30/clojure-mahouts-entropy-function/">Jen & I had rewritten Mahout's entropy function in Clojure</a>:


~~~lisp

(defn calculate-entropy [counts data-size]
  (->> counts
       (remove #{0})
       (map (partial individual-entropy data-size))
       (reduce +)))
~~~

Here we are using the thread last operator to first pass <cite>counts</cite> as the last argument of the <cite>remove</cite> function on the next line, then to pass the result of that to the <cite>map</cite> function on the next line and so on.

The function expands out like this:


~~~lisp

(remove #{0} counts)
~~~


~~~lisp

(map (partial individual-entropy data-size) (remove #{0} counts))
~~~


~~~lisp

(reduce + (map (partial individual-entropy data-size) (remove #{0} counts)))
~~~

We can also use <cite>clojure.walk/macroexpand-all</cite> to see the expanded form of this function:


~~~lisp

user> (use 'clojure.walk)
user> (macroexpand-all '(->> counts                                                                                                                                                                  
                             (remove #{0})                                                                                                                                                                     
                             (map (partial individual-entropy data-size))                                                                                                                                      
                             (reduce +)))
(reduce + (map (partial individual-entropy data-size) (remove #{0} counts)))   
~~~

I recently came across the <a href="http://clojuredocs.org/clojure_core/clojure.core/-%3E">thread first (->)</a> macro while <a href="http://blog.jayfields.com/2012/09/clojure-refactoring-from-thread-last-to.html">reading one of Jay Fields' blog posts</a> and thought I'd have a play around with it.

The thread first (->) macro is similar but it passes its first argument as the first argument to the next form, then passes the result of that as the first argument to the next form and so on.

It's pointless to convert this function to use <cite>-></cite> because all the functions take the previous result as their last argument but just in case we wanted to the equivalent function would look like this:


~~~lisp

(defn calculate-entropy [counts data-size]
  (-> counts
      (->> (remove #{0}))
      (->> (map (partial individual-entropy data-size)))
      (->> (reduce +))))
~~~

As you can see we end up using ->> to pass <cite>counts</cite> as the last argument to <cite>remove</cite>, then <cite>map</cite> and then <cite>reduce</cite>.

The function would expand out like this:


~~~lisp

(->> counts (remove #{0})) 
~~~


~~~lisp

(->> (->> counts (remove #{0})) (map (partial individual-entropy data-size)))
~~~


~~~lisp

(->> (->> (->> counts (remove #{0})) (map (partial individual-entropy data-size))) (reduce +))
~~~

If we then evaluate the <cite>->></cite> macro we end up with the nested form:


~~~lisp

(->> (->> (remove #{0} counts) (map (partial individual-entropy data-size))) (reduce +))
~~~


~~~lisp

(->> (map (partial individual-entropy data-size) (remove #{0} counts)) (reduce +))
~~~


~~~lisp

(reduce + (map (partial individual-entropy data-size) (remove #{0} counts)))
~~~

I haven't written enough Clojure to come across a real use for the thread first macro but Jay has <a href="http://blog.jayfields.com/2012/09/clojure-refactoring-from-thread-last-to.html">an example on his blog showing how he refactored some code which was initially using the thread last macro to use thread first instead</a>.
