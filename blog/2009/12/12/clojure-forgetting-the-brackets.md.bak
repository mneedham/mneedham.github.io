+++
draft = false
date="2009-12-12 03:51:19"
title="Clojure: Forgetting the brackets"
tag=['clojure']
category=['Clojure']
+++

I've been playing around with macros over the last few days and while writing a simple one forgot to include the brackets to make it evaluate correctly:


~~~lisp

(defmacro say-hello [person]
  println "Hello" person)
~~~

This macro doesn't even expand like I thought it would:


~~~text

user=> (macroexpand-1 '(say-hello blah))
blah
~~~

That seemed a bit strange to me but I eventually realised that I'd missed off the brackets around 'println' and the arguments following it which would have resulted in 'println' being evaluated with those arguments.

I was a bit curious as to why that happened so I tried the following expression without any brackets to see what would happen:


~~~text

user=> println "hello" "mark"
#<core$println__5440 clojure.core$println__5440@681ff4>
"mark"
"random"
~~~

It seems to just evaluate each thing individually and when we put this type of expression into a function definition the function will do the same thing but also return the last thing evaluated:


~~~lisp

(defn say-hello [] println "hello" "mark")
~~~


~~~text

user=> (say-hello)
"mark"
~~~

<a href="http://twitter.com/ajlopez/statuses/6563641565">A. J. Lopez pointed out</a> that this is quite like <a href="http://www.delorie.com/gnu/docs/elisp-manual-21/elisp_125.html">progn</a> in other LISPs and is the same as doing the following:


~~~text

user=> (do println "hello" "mark")
"mark"
~~~

<a href="http://clojure.org/special_forms#toc3">do</a> is defined as follows:
<blockquote>
(do exprs*)
Evaluates the expressions in order and returns the value of the last. If no expressions are supplied, returns nil.
</blockquote>

The way to write a function which passes those two arguments to 'println' is of course to put brackets around the statement:


~~~lisp

(defn say-hello [] (println "hello" "mark"))
~~~


~~~text

user=> (say-hello) 
hello mark
nil
~~~
