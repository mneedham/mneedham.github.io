+++
draft = false
date="2011-07-12 22:42:49"
title="Scala: Pattern matching a pair inside map/filter"
tag=['scala']
category=['Scala']
+++

More than a few times recently we've wanted to use pattern matching on a collection of pairs/tuples and have run into trouble doing so.

It's easy enough if you don't try and pattern match:

~~~scala

> List(("Mark", 4), ("Charles", 5)).filter(pair => pair._2 == 4)
res6: List[(java.lang.String, Int)] = List((Mark,4))
~~~

But if we try to use pattern matching:

~~~scala

List(("Mark", 4), ("Charles", 5)).filter(case(name, number) => number == 4)
~~~

We end up with this error:


~~~text

<console>:1: error: illegal start of simple expression
       List(("Mark", 4), ("Charles", 5)).filter(case(name, number) => number == 4)
~~~

It turns out that we can only use this if we pass the function to filter using {} instead of ():


~~~scala

> List(("Mark", 4), ("Charles", 5)).filter { case(name, number) => number == 4 }
res7: List[(java.lang.String, Int)] = List((Mark,4))
~~~

It was pointed out to me on the <a href="http://www.scala-lang.org/node/813">Scala IRC channel</a> that the reason for the compilation failure has nothing to do with trying to do a pattern match inside a higher order function but that it's not actually possible to use a case token without the {}.

<blockquote>
[23:16] mneedham: hey - trying to understand how pattern matching works inside higher order functions. Don't quite get this code -> https://gist.github.com/1079110 any ideas?

[23:17] dwins: mneedham: scala requires that "case" statements be inside curly braces. nothing to do with higher-order functions

[23:17] mneedham: is there anywhere that's documented or is that just a known thing?

[23:18] mneedham: I expected it to work in normal parentheses 

[23:21] amacleod: mneedham, it's documented.  Whether it's documented simply as "case statements need to be in curly braces" is another question 
</blockquote>

The first line of Section 8.5 'Pattern Matching Anonymous Functions' of the <a href="http://www.scala-lang.org/docu/files/ScalaReference.pdf">Scala language spec</a> proves what I was told:

<blockquote>
Syntax:
BlockExpr ::= ‘{’ CaseClauses ‘}
</blockquote>

It then goes into further detail about how the anonymous function gets converted into a pattern matching statement which is quite interesting reading.
