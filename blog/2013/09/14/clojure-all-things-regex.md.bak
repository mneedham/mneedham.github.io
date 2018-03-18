+++
draft = false
date="2013-09-14 01:24:51"
title="Clojure: All things regex"
tag=['clojure']
category=['Clojure']
+++

<p>I've been doing some <a href="http://www.markhneedham.com/blog/2013/08/26/clojureenlive-screen-scraping-a-html-file-from-disk/">scrapping of web pages recently using Clojure and Enlive</a> and as part of that I've had to write regular expressions to extract the data I'm interested in.</p>


<p>On my travels I've come across a few different functions and I'm never sure which is the right one to use so I thought I'd document what I've tried for future me.</p>


<h3>Check if regex matches</h3>

<p>The first regex I wrote was while scrapping the <a href="http://www.rsssf.com/ec/ec200203det.html">Champions League results</a> from the Rec.Sport.Soccer Statistics Foundation and I wanted to determine which spans contained the match result and which didn't.</p>


<p>A matching line would look like this:</p>



~~~text

Real Madrid-Juventus Turijn 2 - 1
~~~

<p>And a non matching one like this:</p>



~~~text

53’Nedved 0-1, 66'Xavi Hernández 1-1, 114’Zalayeta 1-2
~~~

<p>I wrote the following regex to detect match results:</p>



~~~text

[a-zA-Z\s]+-[a-zA-Z\s]+ [0-9][\s]?.[\s]?[0-9]
~~~

<p>I then wrote the following function using <cite><a href="http://clojuredocs.org/clojure_core/clojure.core/re-matches">re-matches</a></cite> which would return true or false depending on the input:</p>



~~~lisp

(defn recognise-match? [row]
  (not (clojure.string/blank? (re-matches #"[a-zA-Z\s]+-[a-zA-Z\s]+ [0-9][\s]?.[\s]?[0-9]" row))))
~~~


~~~lisp

> (recognise-match? "Real Madrid-Juventus Turijn 2 - 1")
true
> (recognise-match? "53’Nedved 0-1, 66'Xavi Hernández 1-1, 114’Zalayeta 1-2")
false
~~~

<p><cite>re-matches</cite> only returns matches if the whole string matches the pattern which means if we had a line with some spurious text after the score it wouldn't match:</p>



~~~lisp

> (recognise-match? "Real Madrid-Juventus Turijn 2 - 1 abc")
false
~~~

<p>If we don't mind that and we just want some part of the string to match our pattern then we can use <cite><a href="http://clojuredocs.org/clojure_core/clojure.core/re-find">re-find</a></cite> instead:</p>



~~~lisp

(defn recognise-match? [row]
  (not (clojure.string/blank? (re-find #"[a-zA-Z\s]+-[a-zA-Z\s]+ [0-9][\s]?.[\s]?[0-9]" row))))
~~~


~~~lisp

> (recognise-match? "Real Madrid-Juventus Turijn 2 - 1 abc")
true
~~~

<h3>Extract capture groups</h3>

<p>The next thing I wanted to do was to capture the teams and the score of the match which I initially did using <cite><a href="http://clojuredocs.org/clojure_core/clojure.core/re-seq">re-seq</a></cite>:</p>



~~~lisp

> (first (re-seq #"([a-zA-Z\s]+)-([a-zA-Z\s]+) ([0-9])[\s]?.[\s]?([0-9])" "FC Valencia-Internazionale Milaan 2 - 1"))
["FC Valencia-Internazionale Milaan 2 - 1" "FC Valencia" "Internazionale Milaan" "2" "1"]
~~~

<p>I then extracted the various parts like so:</p>



~~~lisp

> (def result (first (re-seq #"([a-zA-Z\s]+)-([a-zA-Z\s]+) ([0-9])[\s]?.[\s]?([0-9])" "FC Valencia-Internazionale Milaan 2 - 1")))

> result
["FC Valencia-Internazionale Milaan 2 - 1" "FC Valencia" "Internazionale Milaan" "2" "1"]


> (nth result 1)
"FC Valencia"

> (nth result 2)
"Internazionale Milaan"
~~~

<p><cite>re-seq</cite> returns a list which contains consecutive matches of the regex. The list will either contain strings if we don't specify capture groups or a vector containing the pattern matched and each of the capture groups.</p>
 

<p>For example if we now match only sequences of A-Z or spaces and remove the rest of the pattern from above we'd get the following results:</p>



~~~lisp

> (re-seq #"([a-zA-Z\s]+)" "FC Valencia-Internazionale Milaan 2 - 1")
(["FC Valencia" "FC Valencia"] ["Internazionale Milaan " "Internazionale Milaan "] [" " " "] [" " " "])

> (re-seq #"[a-zA-Z\s]+" "FC Valencia-Internazionale Milaan 2 - 1")
("FC Valencia" "Internazionale Milaan " " " " ")
~~~

<p>In our case <cite>re-find</cite> or <cite>re-matches</cite> actually makes more sense since we only want to match the pattern once. If there are further matches after this those aren't included in the results. e.g.</p>



~~~lisp

> (re-find #"[a-zA-Z\s]+" "FC Valencia-Internazionale Milaan 2 - 1")
"FC Valencia"

> (re-matches #"[a-zA-Z\s]*" "FC Valencia-Internazionale Milaan 2 - 1")
nil
~~~

<p><cite>re-matches</cite> returns nil here because there are characters in the string which don't match the pattern i.e. the hyphen between the two scores.</p>


<p>If we tie that in with our capture groups we end up with the following:</p>



~~~lisp

> (def result 
    (re-find #"([a-zA-Z\s]+)-([a-zA-Z\s]+) ([0-9])[\s]?.[\s]?([0-9])" "FC Valencia-Internazionale Milaan 2 - 1"))

> result
["FC Valencia-Internazionale Milaan 2 - 1" "FC Valencia" "Internazionale Milaan" "2" "1"]

> (nth result 1)
"FC Valencia"

> (nth result 2)
"Internazionale Milaan"
~~~

<p>I also came across the <cite><a href="http://clojuredocs.org/clojure_core/clojure.core/re-pattern">re-pattern</a></cite> function which provides a more verbose way of creating a pattern and then evaluating it with <cite>re-find</cite>:</p>



~~~lisp

> (re-find (re-pattern "([a-zA-Z\\s]+)-([a-zA-Z\\s]+) ([0-9])[\\s]?.[\\s]?([0-9])") "FC Valencia-Internazionale Milaan 2 - 1")
["FC Valencia-Internazionale Milaan 2 - 1" "FC Valencia" "Internazionale Milaan" "2" "1"]
~~~

<p>One difference here is that I had to escape the special sequence '\s' otherwise I was getting the following exception:</p>



~~~lisp

RuntimeException Unsupported escape character: \s  clojure.lang.Util.runtimeException (Util.java:170)
~~~

<p>I wanted to play around with <cite><a href="http://clojuredocs.org/clojure_core/clojure.core/re-groups">re-groups</a></cite> as well but that seemed to throw an exception reasonably frequently when I expected it to work.</cite>

<p>The last function I looked at was <cite><a href="http://clojuredocs.org/clojure_core/clojure.core/re-matcher">re-matcher</a></cite> which seemed to be a long-hand for the '#""' syntax used earlier in the post to define matchers:</p>



~~~lisp

> (re-find (re-matcher #"([a-zA-Z\s]+)-([a-zA-Z\s]+) ([0-9])[\s]?.[\s]?([0-9])" "FC Valencia-Internazionale Milaan 2 - 1"))
["FC Valencia-Internazionale Milaan 2 - 1" "FC Valencia" "Internazionale Milaan" "2" "1"]
~~~

<h3>In summary</h3>

<p>So in summary I think most use cases are covered by <cite>re-find</cite> and <cite>re-matches</cite> and maybe <cite>re-seq</cite> on special occasions. I couldn't see where I'd use the other functions but I'm happy to be proved wrong.</p>

