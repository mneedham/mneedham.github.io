+++
draft = false
date="2013-09-17 00:24:48"
title="Clojure: Updating keys in a map"
tag=['clojure']
category=['Clojure']
+++

<p>I've been playing with Clojure over the last few weeks and as a result I've been using a lot of maps to represent the data.</p>


<p>For example if we have the following map of teams to <a href="http://www.glicko.net/glicko/glicko.pdf">Glicko</a> ratings and ratings deviations:</p>



~~~lisp

(def teams { "Man. United" {:points 1500 :rd 350} 
             "Man. City"   {:points 1450 :rd 300} })
~~~

<p>We might want to increase Man. United's points score by one for which we could use the <cite><a href="http://clojuredocs.org/clojure_core/1.2.0/clojure.core/update-in">update-in</a></cite> function:</p>



~~~lisp

> (update-in teams ["Man. United" :points] inc)
{"Man. United" {:points 1501, :rd 350}, "Man. City" {:points 1450, :rd 300}}
~~~

<p>The 2nd argument to <cite>update-in</cite> is a nested associative structure i.e. a sequence of keys into the map in this instance.</p>
 

<p>If we wanted to reset Man. United's points score we could use <cite><a href="http://clojuredocs.org/clojure_core/clojure.core/assoc-in">assoc-in</a></cite>:</p>



~~~lisp

> (assoc-in teams ["Man. United" :points] 1)
{"Man. United" {:points 1, :rd 350}, "Man. City" {:points 1450, :rd 300}}
~~~

<p>If we want to update multiple keys at once then we can chain them using the <a href="http://clojuredocs.org/clojure_core/clojure.core/-%3E">-></a> (thread first) macro:</p>



~~~lisp

(-> teams
    (assoc-in ["Man. United" :points] 1600)
    (assoc-in ["Man. United" :rd] 200))
{"Man. United" {:points 1600, :rd 200}, "Man. City" {:points 1450, :rd 300}}
~~~

<p>If instead of replacing just one part of the value we want to replace the whole entry we could use <cite><a href="http://clojuredocs.org/clojure_core/clojure.core/assoc">assoc</a></cite> instead:</p>



~~~lisp

> (assoc teams "Man. United" {:points 1600 :rd 300})
{"Man. United" {:points 1600, :rd 300}, "Man. City" {:points 1450, :rd 300}}
~~~

<p><cite>assoc</cite> can also be used to add a new key/value to the map. e.g.</p>



~~~lisp

> (assoc teams "Arsenal" {:points 1500 :rd 330})
{"Man. United" {:points 1500, :rd 350}, "Arsenal" {:points 1500, :rd 330}, "Man. City" {:points 1450, :rd 300}}
~~~

<p><cite><a href="http://clojuredocs.org/clojure_core/clojure.core/dissoc">dissoc</a></cite> plays the opposite role and returns a new map without the specified keys:</p>



~~~lisp

> (dissoc teams "Man. United" "Man. City")
{}
~~~

<p>And those are all the map based functions I've played around with so far...</p>

