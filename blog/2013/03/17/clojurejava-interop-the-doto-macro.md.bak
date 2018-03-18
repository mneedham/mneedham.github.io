+++
draft = false
date="2013-03-17 20:21:10"
title="clojure/Java Interop: The doto macro"
tag=['java', 'clojure', 'interop']
category=['Clojure']
+++

<p>I recently wrote about some <a href="http://www.markhneedham.com/blog/2013/03/17/clojurejava-interop-importing-neo4j-spatial-data/">code I've been playing with to import neo4j spatial data</a> and while looking to simplify the code I came across the <cite><a href="http://clojure.org/java_interop#Java Interop-The Dot special form-(doto instance-expr (instanceMethodName-symbol args*)*)">doto</a></cite> macro.</p>


<p>The <cite>doto</cite> macro allows us to chain method calls on an initial object and then returns the resulting object. e.g.</p>



~~~lisp

(doto (new java.util.HashMap) (.put "a" 1) (.put "b" 2))
-> {a=1, b=2}
~~~

<p>In our case this comes in quite useful in the function used to create a stadium node which initially reads like this:~~~


~~~lisp

(defn create-stadium-node [db line]
  (let [stadium-node (.. db createNode)]
    (.. stadium-node (setProperty "wkt" (format "POINT(%s %s)" (:long line) (:lat line))))
    (.. stadium-node (setProperty "name" (:stadium line)))
  stadium-node))
~~~

<p>Here we first create a node, set a couple of properties on the node and then return it.</p>
 

<p>Using the macro it would read like this:</p>



~~~lisp

(defn create-stadium-node [db line]
  (doto (.. db createNode)
    (.setProperty "wkt" (format "POINT(%s %s)" (:long line) (:lat line)))
    (.setProperty "name" (:stadium line))))
~~~

<p>We can also use it to close the transaction at the end of our function although we don't actually have a need for the transaction object which gets returned:~~~


~~~lisp

# the end of our main function
   (.. tx success)
   (.. tx finish)
~~~

<p>...becomes…</p>



~~~lisp

(doto tx (.success) (.finish))
~~~

<p>As far as I can tell this is pretty similar in functionality to the <cite><a href="http://blog.moertel.com/posts/2007-02-07-ruby-1-9-gets-handy-new-method-object-tap.html">Object#tap</a></cite> function in Ruby:</p>



~~~ruby

{}.tap { |x| x[:a] = 1; x[:b] = 2 }
=> {:a=>1, :b=>2}
~~~

<p>Either way it's a pretty neat way of simplifying code.</p>

