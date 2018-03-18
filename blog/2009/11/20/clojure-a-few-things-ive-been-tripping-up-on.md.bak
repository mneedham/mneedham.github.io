+++
draft = false
date="2009-11-20 13:11:03"
title="Clojure: A few things I've been tripping up on"
tag=['clojure']
category=['Clojure']
+++

In my continued playing with Clojure I'm noticing a few things that I keep getting confused about.

<h3>The meaning of parentheses</h3>
<a href="http://krbtech.wordpress.com/2009/03/16/same-temperature-converter-different-language-clojure/">Much like Keith Bennett</a> I'm not used to parentheses playing such an important role in the way that an expression gets evaluated. 

As I understand it if an expression is enclosed in parentheses then that means it will be evaluated as a function.

For example I spent quite a while trying to work out why the following code kept throwing a class cast exception:


~~~lisp

(if (true) 1 0)
~~~

If you run that code in the REPL you'll get the following exception because 'true' isn't a function and therefore can't be applied as such:


~~~text

java.lang.ClassCastException: java.lang.Boolean cannot be cast to clojure.lang.IFn (NO_SOURCE_FILE:0)
~~~

If we don't want something to be treated this way then the parentheses need to disappear!


~~~lisp

(if true 1 0)
~~~

<h3>Truthyness</h3>
Somewhat related to the above is understanding which expressions evaluate to 'true' or 'false'. 

I'm told there are some edge cases but that as a general rule everything except for 'false' and 'nil' evaluates to true. 

I think that's an idea which is more common in languages like Ruby but I'm not yet used to the idea that we can something like this and have it execute:


~~~lisp

(if "mark" 1 0)
~~~

In C# or Java I would except to have to compare "mark" to something in order for it to evaluate to a boolean result.

It seems like a really neat way to reduce the amount of code we have to write though so I like it so far.

<h3>Character Literals</h3>

I've been working through <a href="http://java.ociweb.com/mark/clojure/article.html#Syntax">Mark Volkmann's Clojure tutorial</a> and in one example he defines the following function:


~~~lisp

(def vowel? (set "aeiou"))
~~~

I wanted to try it out to see if a certain character was a vowel so I initially did this:


~~~lisp

=>(vowel? "a")
nil
~~~

"a" is actually a string though which means it's an array of characters when what we really want is a single character.

I thought the following would be what I wanted:


~~~lisp

(vowel? 'a')
~~~

Instead what I got was the following exception:


~~~text

java.lang.Exception: Unmatched delimiter: )
~~~

This one just turned out to be a case of me not reading <a href="http://clojure.org/reader">the manual</a> very carefully and actually the following is what I wanted:


~~~lisp

=> (vowel? \a)
\a
~~~
