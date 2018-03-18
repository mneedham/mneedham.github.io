+++
draft = false
date="2013-09-19 23:57:49"
title="Clojure: See every step of a reduce"
tag=['clojure']
category=['Clojure']
+++

<p>Last year I wrote about <a href="http://www.markhneedham.com/blog/2012/02/25/haskell-viewing-the-steps-of-a-reduce/">a Haskell function called <cite>scanl</cite></a> which returned the intermediate steps of a fold over a collection and last week I realised that I needed a similar function in Clojure to analyse a reduce I'd written.</p>


<p>A simple reduce which adds together the numbers 1-10 would look like this:</p>



~~~lisp

> (reduce + 0 (range 1 11))
55
~~~

<p>If we want to see the intermediate values of this function called then instead of using <cite><a href="http://clojuredocs.org/clojure_core/1.3.0/clojure.core/reduce">reduce</a></cite> there's a function called <cite><a href="http://clojuredocs.org/clojure_core/1.3.0/clojure.core/reductions">reductions</a></cite> which gives us exactly what we want:</p>



~~~lisp

> (reductions + 0 (range 1 11))
(0 1 3 6 10 15 21 28 36 45 55)
~~~

<p>I found this function especially useful when analysing <a href="http://www.markhneedham.com/blog/2013/09/14/glicko-rating-system-a-simple-example-using-clojure/">my implementation of the Glicko ranking algorithm</a> to work out whether a team's ranking was being updated correctly after a round of matches.</p>


<p>I initially thought the <cite>reductions</cite> function was only useful as a debugging tool and that you'd always end up changing your code back to use <cite>reduce</cite> after you'd solved the problem but I realise I was mistaken.</p>


<p>As part of <a href="http://www.markhneedham.com/blog/2013/09/14/glicko-rating-system-a-simple-example-using-clojure/">my implementation of the Glicko algorithm</a> I wrote a bit of code that applied a reduce across a collection of football seasons and initially just returned the final ranking of each team:</p>



~~~lisp

(def initial-team-rankings { "Man Utd" {:points 1200} "Man City" {:points 1300}})

(defn update-team-rankings [teams year]
  (reduce (fn [ts [team _]] (update-in ts [team :points] inc)) teams teams))
~~~


~~~lisp

> (reduce update-team-rankings initial-team-rankings (range 2004 2013))
{"Man City" {:points 1309}, "Man Utd" {:points 1209}}
~~~

<p>I realised it would actually be quite interesting to see the rankings after each season for which <cite>reductions</cite> comes in quite handy.</p>


<p>For example if we want to find the rankings after 3 seasons we could write the following code:</p>



~~~lisp

> (nth (reductions update-team-rankings initial-team-rankings (range 2004 2013)) 3)
{"Man City" {:points 1303}, "Man Utd" {:points 1203}}
~~~

<p>Or we could join the result back onto our collection of years and create a map so we can look up the year more easily:</p>



~~~lisp

(def final-rankings
  (zipmap (range 2003 2013) (reductions update-team-rankings initial-team-rankings (range 2004 2013))))
~~~


~~~lisp

> (get final-rankings 2006)
{"Man City" {:points 1303}, "Man Utd" {:points 1203}}
~~~
