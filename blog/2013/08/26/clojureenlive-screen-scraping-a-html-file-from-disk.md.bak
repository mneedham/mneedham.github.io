+++
draft = false
date="2013-08-26 17:58:58"
title="Clojure/Enlive: Screen scraping a HTML file from disk"
tag=['clojure', 'enlive']
category=['Clojure']
+++

<p>I wanted to play around with some Champions League data and I came across the <a href="http://www.rsssf.com/ec/">Rec Sport Soccer Statistics Foundation</a> which has collected results of all matches since the tournament started in 1955.</p>


<p>I wanted to get a list of all the matches for a specific season so I started out by downloading the file:</p>



~~~bash

$ pwd
/tmp/football
$ wget http://www.rsssf.com/ec/ec200203det.html
~~~

<p>The next step was to load that page and then run a CSS selector over it to extract the matches. In Ruby land I usually use <a href="http://nokogiri.org/">nokogiri</a> or <a href="http://rubygems.org/gems/selenium-webdriver">Web Driver</a> to do this but I'd heard that Clojure's <a href="https://github.com/cgrand/enlive">enlive</a> is good for this type of work so I thought I'd give it a try.</p>


<p>I found a <a href="https://gist.github.com/AlexBaranosky/782367">couple</a> <a href="http://clj-me.cgrand.net/2009/04/27/screenscraping-with-enlive/">of examples</a> showing how to get started but they both seemed to rely on the web page being at a HTTP URI rather than on disk.</p>


<p>I eventually spotted an example which <a href="http://stackoverflow.com/questions/11094837/is-there-a-parser-for-html-to-hiccup-structures">passed in HTML as a string</a> to <cite>html-resource</cite> and decided to load the contents of my file as a string and then pass that in:</p>



~~~lisp

(ns ranking-algorithms.parse
  (:use [net.cgrand.enlive-html]))

(defn fetch-page
  [file-path]
  (html-resource (java.io.StringReader. (slurp file-path))))
~~~

<p>The next step was to take that page representation and extract the matches. Since the page isn't particularly well laid out for that purpose I ended up writing a regular expression to find the matching parts:</p>



~~~lisp

(defn matches [file]
  (->> file
       fetch-page
       extract-rows
       (map extract-content)
       (filter recognise-match?)))

(defn extract-rows [page]
  (select page [:div.Section1 :p :span]))

(defn extract-content [row]
  (first (get row :content)))

(defn recognise-match? [row]
  (and (string? row) (re-matches #"[a-zA-Z\s]+-[a-zA-Z\s]+ [0-9][\s]?.[\s]?[0-9]" row)))
~~~

<p>The interesting part is <cite>extract-rows</cite> where we apply the CSS selector 'div.Section1 p span', the only difference being that we prefix the selector with ':'.</p>


<p>We then filter everything through <cite>recgonise-match?</cite> to find the matches since almost every row of the page is returned by our CSS selector. Unfortunately I don't think there is a more specific selector that I could have used.</p>


<p>When I execute that function I ended up with the following output:</p>



~~~text

> (matches "/tmp/football/ec200203det.html")
( ... "Lokomotiv\nMoskou-Borussia Dortmund 1 - 2" "Borussia\nDortmund-AC Milan 0 - 1" 
"Real\nMadrid-Lokomotiv Moskou 2 - 2" "Real\nMadrid-Borussia Dortmund 2 - 1" 
"AC Milan-Lokomotiv\nMoskou 1 - 0" "Borussia Dortmund-Real\nMadrid 1 - 1" 
"Lokomotiv\nMoskou-AC Milan 0 - 1" ... )
~~~

<p>The next step was to split out the strings into a structure that I can use in a rankings algorithm so I applied another function to each string to pull out the appropriate parts:</p>



~~~lisp

(defn matches [file]
  (->> file
       fetch-page
       extract-rows
       (map extract-content)
       (filter recognise-match?)
       (map as-match)))

(defn cleanup [word]
  (clojure.string/replace word "\n" " "))

(defn as-match
  [row]
  (let [match
        (first (re-seq #"([a-zA-Z\s]+)-([a-zA-Z\s]+) ([0-9])[\s]?.[\s]?([0-9])" row))]
    {:home (cleanup (nth match 1)) :away (cleanup (nth match 2))
     :home_score (nth match 3) :away_score (nth match 4)}))
~~~

<p>If we run the function now we get a much nicer output to play with:</p>



~~~text

> (matches "/tmp/football/ec200203det.html")
( ...  {:home "AC Milan", :away "Internazionale Milaan", :home_score "0", :away_score "0"} 
       {:home "Juventus Turijn", :away "Real Madrid", :home_score "3", :away_score "1"} 
       {:home "Internazionale Milaan", :away "AC Milan", :home_score "1", :away_score "1"} )
~~~
