+++
draft = false
date="2009-11-21 22:11:22"
title="Clojure: Checking for a nil value in a collection"
tag=['clojure']
category=['Clojure']
+++

Something which I wanted to do recently was write a function that would indicate whether a collection contained a nil value.

I initially incorrectly thought the '<a href="http://clojure.org/api#toc170">contains?</a>' function was the one that I wanted:


~~~lisp

(contains? '(1 nil 2 3) nil)
=> false
~~~

I thought it would work the same as the Java equivalent but that function actually checks whether a key exists in a collection rather than a value. It's more useful when dealing with maps.

There's <a href="http://groups.google.com/group/clojure/browse_frm/thread/49173d05a6781f62/47084ba4eec07c26?lnk=gst&q=contains%3F#47084ba4eec07c26">more discussion on the consistency of the API on the mailing list</a>.

Luckily the documentation guides us towards the '<a href="http://clojure.org/api#toc523">some</a>' function:

My first attempt was to write an anonymous function to check if there was a 'nil' in the list:


~~~lisp

(some #(= % nil) '(1 nil 2 3))
=> true
~~~


~~~lisp

(some #(= % nil) '(1  2 3))
=> nil
~~~

<a href="http://twitter.com/fogus/status/5904916921">fogus showed me an even better way</a> by making use of the built in '<a href="http://clojure.org/api#toc388">nil?</a>' function:


~~~lisp

(some nil? '(1 nil 2 3))
~~~

Another approach would be to make use of the Java 'contains' method as <a href="http://twitter.com/philip_schwarz">Philip Schwarz</a> <a href="http://twitter.com/philip_schwarz/statuses/5905264987">pointed out</a>:


~~~lisp

(.contains '(1 nil 2 3) nil)
=> true
~~~

I noticed that when you use Java methods in Clojure with collections then the result will either be 'true' or 'false' whereas when you use Clojure built in functions then it's more likely to be 'true' or 'nil'.

I guess this is linked to the idea that <a href="http://www.markhneedham.com/blog/2009/11/20/clojure-a-few-things-ive-been-tripping-up-on/">'nil' is false in Clojure</a> so it doesn't make much difference what the return value is.

When I'm using a language I've got into the habit of just trying out the API in the way that I expect it to work rather than paying a lot of attention to what the API documentation says. 

I think this is something I'll need to work out to avoid much frustration!
