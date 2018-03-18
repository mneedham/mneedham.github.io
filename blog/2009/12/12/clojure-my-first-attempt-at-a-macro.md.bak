+++
draft = false
date="2009-12-12 03:53:37"
title="Clojure: My first attempt at a macro"
tag=['clojure']
category=['Clojure']
+++

I'm up to the chapter on using macros in Stuart Halloway's '<a href="http://www.amazon.com/gp/product/1934356336?ie=UTF8&tag=marneesblo-20&linkCode=as2&camp=1789&creative=390957&creativeASIN=1934356336">Programming Clojure</a>' book and since I've never used a language which has macros in before I thought it'd be cool to write one.

In reality there's no reason to create a macro to do what I want to do but I wanted to keep the example simple so I could try and understand exactly how macros work.

I want to create a macro which takes in one argument and then prints hello and the person's name.

In the book Halloway suggests that we should start with the expression that we want to end up with, so this is what I want:


~~~lisp

(println "Hello" person)
~~~

My first attempt to do that was:


~~~lisp

(defmacro say-hello [person]
  println "Hello" person)
~~~

I made the mistake of forgetting to include the brackets around the 'println' expression so it doesn't actually pass '"Hello"' and 'person' to 'println'. Instead each symbol is evaluated individually.

When we evaluate this in the REPL we therefore don't quite get what we want:

~~~text

user=> (say-hello "mark")          
"mark"
~~~

Expanding the macro results in:


~~~text

user=> (macroexpand-1 '(say-hello "Mark"))
"Mark"
~~~

Which is the equivalent of doing this:


~~~text

user=> (eval (do println "hello" "Mark")) 
"Mark"
~~~

As I <a href="http://www.markhneedham.com/blog/2009/12/12/clojure-forgetting-the-brackets/">wrote previously</a> this is because 'do' evaluates each argument in order and then returns the last one which in this case is "Mark".

I fixed that mistake and got the following:


~~~lisp

(defmacro say-hello [person]
  (println "Hello" person))
~~~

Which returns the right result...


~~~lisp

user=> (say-hello "Mark")
Hello Mark
nil
~~~

...but actually evaluated the expression rather than expanding it because I didn't escape it correctly:


~~~text

user=> (macroexpand-1 '(say-hello "Mark"))
Hello Mark
nil
~~~

After these failures I decided to try and change one of the examples from the book instead of my trial and error approach.

One approach used is to build a list of Clojure symbols inside the macro definition:


~~~lisp

(defmacro say-hello [person]
  (list println "hello" person))
~~~


~~~text

user=> (macroexpand-1 '(say-hello "Mark"))
(#<core$println__5440 clojure.core$println__5440@681ff4> "hello" "Mark")
~~~

This is pretty much what we want and although the <a href="http://twitter.com/ajlopez/statuses/6540996368">'println' symbol has been evaluated at macro expansion time</a> it doesn't actually make any difference to the way the macro works.

We can fix that by escaping 'println' so that it won't be evaluated until evaluation time:


~~~lisp

(defmacro say-hello [person]
  (list 'println "hello" person))
~~~


~~~text

user=> (macroexpand-1 '(say-hello "Mark"))
(println "hello" "Mark")
~~~

I thought it should also be possible to quote(') the whole expression instead of building up the list:


~~~lisp

(defmacro say-hello [person] 
  '(println "hello" person))
~~~

This expands correctly but when we try to use it this happens:


~~~text

user=> (say-hello "Mark")
java.lang.Exception: Unable to resolve symbol: person in this context 
~~~

The problem is that when we use quote there is no evaluation of any of the symbols in the expression so <a href="http://twitter.com/patrickdlogan/statuses/6536320695">the symbol 'person' is only evaluated at runtime and since it hasn't been bound to any value</a> we end up with the above error.

If we want to use the approach of non evaluation then we need to make use of the backquote(`) which stops evaluation of anything unless it's preceded by a ~.


~~~lisp

(defmacro a [person]
  `(println "hello" ~person))
~~~

This allows us to  evaluate 'person' at expand time and replace it with the appropriate value.

In hindsight the approach I took to write this macro was pretty ineffective although it's been quite interesting to see all the different ways that I've found to mess up the writing of one!

Thanks to <a href="http://twitter.com/ajlopez">A. J. Lopez</a>, <a href="http://twitter.com/patrickdlogan">Patrick Logan</a> and <a href="http://twitter.com/fogus">fogus</a> for helping me to understand all this a bit better than I did to start with!
