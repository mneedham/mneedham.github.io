+++
draft = false
date="2013-09-22 23:07:04"
title="Clojure/Emacs/nrepl: Stacktrace-less error messages"
tag=['clojure', 'emacs', 'nrepl']
category=['Clojure']
+++

<p>Ever since I started using the Emacs + nrepl combination to play around with Clojure I've been getting fairly non descript error messages whenever I pass the wrong parameters to a function.</p>


<p>For example if I try to update a non existent key in a form I get a Null Pointer Exception:</p>



~~~lisp

> (update-in {} [:mark] inc)
NullPointerException   clojure.lang.Numbers.ops (Numbers.java:942)
~~~

<p>In this case it's clear that the hash doesn't have a key ':mark' so the function blows up. However,  sometimes the functions are more complicated and this type of reduced stack trace isn't very helpful for working out where the problem lies.</p>


<p>I eventually came across <a href="https://groups.google.com/forum/#!msg/nrepl-el/x8vhEbckycY/93unZrJI1RkJ">a thread in the nrepl-el forum</a> where Tim King suggested that adding the  following lines to the Emacs configuration file should sort things out:</p>


<em>~/.emacs.d/init.el</em>

~~~lisp

(setq nrepl-popup-stacktraces nil)
(setq nrepl-popup-stacktraces-in-repl t)
~~~

<p>I added those two lines, restarted Emacs and after calling the function again got a much more detailed stack trace:</p>



~~~lisp

> (update-in {} [:mark] inc)

java.lang.NullPointerException: 
                 Numbers.java:942 clojure.lang.Numbers.ops
                 Numbers.java:110 clojure.lang.Numbers.inc
                     core.clj:863 clojure.core/inc
                     AFn.java:161 clojure.lang.AFn.applyToHelper
                     AFn.java:151 clojure.lang.AFn.applyTo
                     core.clj:603 clojure.core/apply
                    core.clj:5472 clojure.core/update-in
                  RestFn.java:445 clojure.lang.RestFn.invoke
                 NO_SOURCE_FILE:1 user/eval9
...
~~~

<p>From reading this stack trace we learn that the problem happens when the <cite>inc</cite> function is called with a parameter of 'nil'. We'd see the same thing if we called it directly:</p>



~~~lisp

> (inc nil)

java.lang.NullPointerException: 
                                  Numbers.java:942 clojure.lang.Numbers.ops
                                  Numbers.java:110 clojure.lang.Numbers.inc
                                  NO_SOURCE_FILE:1 user/eval14
...
~~~

<p>Although Clojure error messages do baffle me at times, I hope things will be better now that I'll be able to see on which line the error occurred.</p>

