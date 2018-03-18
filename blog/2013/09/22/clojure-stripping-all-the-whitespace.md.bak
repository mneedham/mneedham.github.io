+++
draft = false
date="2013-09-22 18:54:47"
title="Clojure: Stripping all the whitespace"
tag=['clojure']
category=['Clojure']
+++

<p>When putting together data sets to play around with, one of the more boring tasks is stripping out characters that you're not interested in and more often than not those characters are white spaces.</p>


<p>Since I've been building data sets using Clojure I wanted to write a function that would do this for me.</p>


<p>I started out with the following string:</p>



~~~lisp

(def word " with a  little bit of space we can make it through the night  ")
~~~

<p>which I wanted to format in such a way that there would be a maximum of one space between each word.</p>


<p>I start out by using the <cite><a href="http://clojure.github.io/clojure/clojure.string-api.html#clojure.string/trim">trim</a></cite> function but that only removes white space from the beginning and end of a string:</p>



~~~lisp

> (clojure.string/trim word)
"with a  little bit of space we can make it through the night"
~~~

<p>I wanted to get rid of the space in between 'a' and 'little' as well so I wrote the following code to split on a space and filter out any excess spaces that still remained before joining the words back together:</p>



~~~lisp

> (clojure.string/join " " 
                       (filter #(not (clojure.string/blank? %)) 
                               (clojure.string/split word #" ")))
"with a little bit of space we can make it through the night"
~~~

<p>I wanted to try and make it a bit easier to read by using the <a href="http://clojuredocs.org/clojure_core/clojure.core/-%3E%3E">thread last (->>) macro</a> but that didn't work as well as I'd hoped because <cite>clojure.string/split</cite> doesn't take the string in as its last parameter:</p>



~~~lisp

>  (->> (clojure.string/split word #" ") 
   (filter #(not (clojure.string/blank? %))) 
   (clojure.string/join " "))
"with a little bit of space we can make it through the night"
~~~

<p>I worked around it by creating a specific function for splitting on a space:</p>



~~~lisp

(defn split-on-space [word] 
  (clojure.string/split word #"\s"))
~~~

<p>which means we can now chain everything together nicely:</p>



~~~lisp

>  (->> word 
        split-on-space 
        (filter #(not (clojure.string/blank? %))) 
        (clojure.string/join " "))
"with a little bit of space we can make it through the night"
~~~

<p>I couldn't find a cleaner way to do this but I'm sure there is one and my googling just isn't up to scratch so do let me know in the comments!</p>

