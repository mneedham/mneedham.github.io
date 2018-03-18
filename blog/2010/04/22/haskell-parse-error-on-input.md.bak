+++
draft = false
date="2010-04-22 23:35:27"
title="Haskell: parse error on input `='"
tag=['haskell']
category=['Haskell']
+++

I've been trying to follow the '<a href="http://irekjozwiak.com/entry/2009/06/13/Monads-for-Java-C---programmers.html">Monads for Java/C++ programmers</a>' post in ghci and getting the following type of error when trying out the code snippets:


~~~haskell

Prelude> a = 3

<interactive>:1:2: parse error on input `='
~~~

I figured there must be something wrong with my installation of the compiler since I was copying and pasting the example across and having this problem. Having reinstalled that, however, I still had the same problem.

I eventually came across <a href="http://greenokapi.net/blog/2007/02/19/chapter-1-of-hudaks-haskell-school-of-expression/">this blog post</a> which points to a <a href="http://ircarchive.info/haskell/2007/2/19/27.html">mailing list thread from a few years ago</a> where pjd explains that the 'let' construct is required when defining a variable from ghci and wouldn't necessarily be needed in a normal program:

<blockquote>
<strong>pjd</strong>	osfameron: about the ghci thing, you have to prefix definitions with "let"

as in: let simple x y z = x * (y + z)

<strong>pjd</strong>	the reason for this is that ghci is in an implicit do block

<strong>pjd</strong>	so it's not exactly like top-level haskell
</blockquote> 

We have to use a 'let' in front of any variable/function definitions and then it will work as expected:


~~~haskell

Prelude> let a = 3
3
~~~

<a href="http://book.realworldhaskell.org/read/getting-started.html">According to Real World Haskell</a>:

<blockquote>
This syntax is ghci-specific
The syntax for let that ghci accepts is not the same as we would use at the “top level” of a normal Haskell program.
</blockquote>
