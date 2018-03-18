+++
draft = false
date="2009-12-09 02:41:47"
title="Clojure: when-let macro"
tag=['clojure']
category=['Clojure']
+++

In my continued playing around with Clojure I came across the '<a href="http://richhickey.github.com/clojure/clojure.core-api.html#clojure.core/when-let">when-let</a>' macro.

'when-let' is used when we want to bind an expression to a symbol and only execute the body provided as the second argument to the macro if that symbol evaluates to true.

As I <a href="http://www.markhneedham.com/blog/2009/11/20/clojure-a-few-things-ive-been-tripping-up-on/">wrote previously</a>, a value of 'false' or 'nil' would result in the second argument not being evaluated. 

A simple example of using 'when-let' would be:


~~~lisp

(when-let [a 2] (println "The value of a is:" a))
~~~

This is the definition:


~~~lisp

(defmacro when-let
  "bindings => binding-form test

  When test is true, evaluates body with binding-form bound to the value of test"
  [bindings & body]
  (assert-args when-let
     (vector? bindings) "a vector for its binding"
     (= 2 (count bindings)) "exactly 2 forms in binding vector")
   (let [form (bindings 0) tst (bindings 1)]
    `(let [temp# ~tst]
       (when temp#
         (let [~form temp#]
           ~@body)))))
~~~

The 'assert-args' call at the beginning of the macro is quite interesting. 

Two assertions are stated:

<ul>
<li>The first argument should be a vector</li>
<li>That vector should contain exactly two forms</li>
</ul>

I've not used dynamic languages very much before but it seems like this is one way for a dynamic language to fail fast by checking that the arguments are as expected. In a static language that would be a compile time check.

Line 9 is quite interesting as we know that 'bindings' will be a vector so we can take the '0th' and '1st' elements from it and bind them to 'form' and 'tst' respectively. I didn't quite pick up on the first few times I read it.

On line 10 it makes use of 'auto-gensym' to create a unique name which begins with 'temp' and is bound to the value of 'tst' which in the simple example provided would be the value '2'. As I understand it the name would be something like 'temp__304' or something similarly random!

'when 2' evaluates to true which means that we execute the body provided as the second argument.


~~~text

user=> (when-let [a 2] (println "The value of a is:" a))
The value of a is: 2
nil
~~~

This is a bit of a contrived example of using the construct and it seems to be properly used when we're getting a value out of a list and want to check whether or not we've reached the end of that list or not. If we have then eventually we'll have a value of 'nil' bound by the 'let' and then we'll know we're finished.

An example of where the body wouldn't be evaluated is:


~~~text

user=> (when-let [a nil] (println "This won't get printed"))
nil
~~~

I don't really understand why we need to bind 'form' to 'temp' on the second last line as it doesn't seem like the value is used?  I'm sure there's probably something I'm missing there so if anyone could point it out that'd be cool!

As I understand it, the '~@body' on the last line is called the 'splicing unquote' and it allows the individual values in 'body' to be put into the template started at '`(let [temp# ~tst]' individually rather than just being put in there as a list.
