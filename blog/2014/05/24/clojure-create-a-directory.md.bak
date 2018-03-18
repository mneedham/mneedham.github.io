+++
draft = false
date="2014-05-24 00:12:56"
title="Clojure: Create a directory"
tag=['clojure']
category=['Clojure']
+++

<p>I spent much longer than I should have done trying to work out how to create a directory in Clojure as part of an import script I'm working out so for my future self this is how you do it:</p>



~~~lisp

(.mkdir (java.io.File. "/path/to/dir/to/create"))
~~~

<p>I'm creating a directory which contains today's date so I'd want something like 'members-2014-05-24' if I was running it today. The <a href="https://github.com/clj-time/clj-time">clj-time</a> library is very good for working with dates.</p>


<p>To create a folder containing today's date this is what we'd have:</p>



~~~lisp

(ns neo4j-meetup.core
  (:require [clj-time.format :as f]))

(def format-as-year-month-day (f/formatter "yyyy-MM-dd"))

(defn create-directory-for-today []
  (let [date (f/unparse format-as-year-month-day (t/now))]
    (.mkdir (java.io.File. (str "data/members-" date)))))
~~~

<p>Initial code shamelessly stolen from <a href="https://gist.github.com/halfelf">Shu Wang's gist</a> so thanks to him as well!</p>

