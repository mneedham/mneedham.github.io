+++
draft = false
date="2013-09-17 01:03:37"
title="Clojure: Merge two maps but only keep the keys of one of them"
tag=['clojure']
category=['Clojure']
+++

<p>I've <a href="http://www.markhneedham.com/blog/2013/09/17/clojure-updating-keys-in-a-map/">been playing around with Clojure maps</a> recently and I wanted to merge two maps of rankings where the rankings in the second map overrode those in the first while only keeping the teams from the first map.</p>


<p>The <cite><a href="http://clojuredocs.org/clojure_core/clojure.core/merge">merge</a></cite> function overrides keys in earlier maps but also adds keys that only appear in later maps. For example, if we merge the following maps:</p>



~~~lisp

> (merge {"Man. United" 1500 "Man. City" 1400} {"Man. United" 1550 "Arsenal" 1450})
{"Arsenal" 1450, "Man. United" 1550, "Man. City" 1400}
~~~

<p>we get back all 3 teams but I wanted a function which only returned 'Man. United' and 'Man. City' since those keys appear in the first map and 'Arsenal' doesn't.</p>


<p>I <a href="http://stackoverflow.com/questions/2753874/how-to-filter-a-persistent-map-in-clojure">wrote the following function</a>:</p>



~~~lisp

(defn merge-rankings [initial-rankings override-rankings]
  (merge initial-rankings
         (into {} (filter #(contains? initial-rankings (key %)) override-rankings))))
~~~

<p>If we call that we get the desired result:</p>



~~~lisp

> (merge-rankings {"Man. United" 1500 "Man. City" 1400} {"Man. United" 1550 "Arsenal" 1450})
{"Man. United" 1550, "Man. City" 1400}
~~~

<p>An alternative version of that function could use <cite><a href="http://clojuredocs.org/clojure_core/clojure.core/select-keys">select-keys</a></cite> like so:</p>



~~~lisp

(defn merge-rankings [initial-rankings override-rankings]
  (select-keys (merge initial-rankings override-rankings) (map key initial-rankings)))
~~~

<p>bitemyapp points out in the comments that we can go even further and use the <cite><a href="http://clojuredocs.org/clojure_core/clojure.core/keys">keys</a></cite> function instead of <cite>map key</cite>, like so:</p>



~~~lisp

(defn merge-rankings [initial-rankings override-rankings]
  (select-keys (merge initial-rankings override-rankings) (keys initial-rankings)))
~~~

<p>Now let's generify the function so it would make sense in the context of any maps, not just ranking related ones:</p>



~~~lisp

(defn merge-keep-left [left right]
  (select-keys (merge left right) (keys left)))
~~~
