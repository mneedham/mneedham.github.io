+++
draft = false
date="2013-09-20 21:13:01"
title="Clojure: Converting an array/set into a hash map"
tag=['clojure']
category=['Clojure']
+++

<p>When I was <a href="http://www.markhneedham.com/blog/2013/08/31/elo-rating-system-ranking-champions-league-teams-using-clojure/">implementing the Elo Rating algorithm</a> a few weeks ago one thing I needed to do was come up with a base ranking for each team.</p>


<p>I started out with a set of teams that looked like this:</p>



~~~lisp

(def teams #{ "Man Utd" "Man City" "Arsenal" "Chelsea"})
~~~

<p>and I wanted to transform that into a map from the team to their ranking e.g.</p>



~~~text

Man Utd -> {:points 1200}
Man City -> {:points 1200}
Arsenal -> {:points 1200}
Chelsea -> {:points 1200}
~~~

<p>I had read the documentation of <cite><a href="http://clojuredocs.org/clojure_core/1.2.0/clojure.core/array-map">array-map</a></cite>, a function which can be used to transform a collection of pairs into a map, and it seemed like it might do the trick.</p>


<p>I started out by building an array of pairs using <cite><a href="http://clojuredocs.org/clojure_core/1.2.0/clojure.core/mapcat">mapcat</a></cite>:</p>



~~~lisp

> (mapcat (fn [x] [x {:points 1200}]) teams)
("Chelsea" {:points 1200} "Man City" {:points 1200} "Arsenal" {:points 1200} "Man Utd" {:points 1200})
~~~

<p><cite>array-map</cite> constructs a map from pairs of values e.g.</p>



~~~lisp

> (array-map "Chelsea" {:points 1200} "Man City" {:points 1200} "Arsenal" {:points 1200} "Man Utd" {:points 1200})
("Chelsea" {:points 1200} "Man City" {:points 1200} "Arsenal" {:points 1200} "Man Utd" {:points 1200})
~~~

<p>Since we have a collection of pairs rather than individual pairs we need to use the <cite><a href="http://clojuredocs.org/clojure_core/1.2.0/clojure.core/apply">apply</a></cite> function as well:</p>



~~~lisp

> (apply array-map ["Chelsea" {:points 1200} "Man City" {:points 1200} "Arsenal" {:points 1200} "Man Utd" {:points 1200}])
{"Chelsea" {:points 1200}, "Man City" {:points 1200}, "Arsenal" {:points 1200}, "Man Utd" {:points 1200}}
~~~

<p>And if we put it all together we end up with the following:</p>



~~~lisp

> (apply array-map (mapcat (fn [x] [x {:points 1200}]) teams))
{"Man Utd"  {:points 1200}, "Man City" {:points 1200}, "Arsenal"  {:points 1200}, "Chelsea"  {:points 1200}}
~~~

<p>It works but the function we pass to <cite>mapcat</cite> feels a bit clunky. Since we just need to create a collection of team/ranking pairs we can use the <cite><a href="http://clojuredocs.org/clojure_core/clojure.core/vector">vector</a></cite> and <cite><a href="http://clojuredocs.org/clojure_core/clojure.core/repeat">repeat</a></cite> functions to build that up instead:</p>



~~~lisp

> (mapcat vector teams (repeat {:points 1200}))
("Chelsea" {:points 1200} "Man City" {:points 1200} "Arsenal" {:points 1200} "Man Utd" {:points 1200})
~~~

<p>And if we put the <cite>apply array-map</cite> code back in we still get the desired result:</p>



~~~lisp

> (apply array-map (mapcat vector teams (repeat {:points 1200})))
{"Chelsea" {:points 1200}, "Man City" {:points 1200}, "Arsenal" {:points 1200}, "Man Utd" {:points 1200}}
~~~

<p>Alternatively we could use <cite><a href="http://clojuredocs.org/clojure_core/clojure.core/assoc">assoc</a></cite> like this:</p>



~~~lisp

> (apply assoc {} (mapcat vector teams (repeat {:points 1200})))
{"Man Utd" {:points 1200}, "Arsenal" {:points 1200}, "Man City" {:points 1200}, "Chelsea" {:points 1200}}
~~~

<p>I also came across the <cite><a href="http://clojuredocs.org/clojure_core/clojure.core/into">into</a></cite> function which seemed useful but took in a collection of vectors:</p>



~~~lisp

> (into {} [["Chelsea" {:points 1200}] ["Man City" {:points 1200}] ["Arsenal" {:points 1200}] ["Man Utd" {:points 1200}] ])
~~~

<p>We therefore need to change the code to use <cite>map</cite> instead of <cite>mapcat</cite>:</p>



~~~lisp

> (into {} (map vector teams (repeat {:points 1200})))
{"Chelsea" {:points 1200}, "Man City" {:points 1200}, "Arsenal" {:points 1200}, "Man Utd" {:points 1200}}
~~~

<p>However, my favourite version so far uses the <cite><a href="http://clojuredocs.org/clojure_core/clojure.core/zipmap">zipmap</a></cite> function like so:</p>



~~~lisp

> (zipmap teams (repeat {:points 1200}))
{"Man Utd" {:points 1200}, "Arsenal" {:points 1200}, "Man City" {:points 1200}, "Chelsea" {:points 1200}}
~~~

<p>I'm sure there are other ways to do this as well so if you know any let me know in the comments.</p>

