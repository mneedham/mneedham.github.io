+++
draft = false
date="2014-05-31 00:03:48"
title="Clojure: Destructuring group-by's output"
tag=['clojure']
category=['Clojure']
+++

<p>One of my favourite features of Clojure is that it allows you to destructure a data structure into values that are a bit easier to work with.</p>


<p>I often find myself referring to <a href="http://blog.jayfields.com/2010/07/clojure-destructuring.html">Jay Fields' article</a> which contains several examples showing the syntax and is a good starting point.</p>


<p>One recent use of destructuring I had was where I was working with a vector containing events like this:</p>



~~~lisp

user> (def events [{:name "e1" :timestamp 123} {:name "e2" :timestamp 456} {:name "e3" :timestamp 789}])
~~~

<p>I wanted to split the events in two - those containing events with a timestamp greater than 123 and those less than or equal to 123.</p>
 

<p>After remembering that the function I wanted was <cite><a href="http://clojuredocs.org/clojure_core/1.2.0/clojure.core/group-by">group-by</a></cite> and not <cite><a href="http://clojuredocs.org/clojure_core/1.2.0/clojure.core/partition-by">partition-by</a></cite> (I always make that mistake!) I had the following:</p>



~~~lisp

user> (group-by #(> (->> % :timestamp) 123) events)
{false [{:name "e1", :timestamp 123}], true [{:name "e2", :timestamp 456} {:name "e3", :timestamp 789}]}
~~~

<p>I wanted to get 2 vectors that I could pass to the web page and this is fairly easy with destructuring:</p>



~~~lisp

user> (let [{upcoming true past false} (group-by #(> (->> % :timestamp) 123) events)] 
       (println upcoming) (println past))
[{:name e2, :timestamp 456} {:name e3, :timestamp 789}]
[{:name e1, :timestamp 123}]
nil
~~~

<p>Simple!</p>

