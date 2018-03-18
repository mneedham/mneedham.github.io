+++
draft = false
date="2012-12-30 22:39:16"
title="Haskell: Pattern matching a list"
tag=['haskell']
category=['Haskell']
+++

<p>As I mentioned <a href="http://www.markhneedham.com/blog/2012/12/29/haskell-initialising-a-map/">in a post yesterday</a> I've been converting a clustering algorithm into Haskell and I wanted to get the value from doing a bit wise or on two values in a list.</p>


<p>I forgot it was possible to pattern match on lists until I <a href="http://www.markhneedham.com/blog/2012/04/15/haskell-a-simple-parsing-example-using-pattern-matching/">came across a post I wrote about 8 months ago</a> where I'd done this so my initial code looked like this:</p>



~~~haskell

> import Data.Bits
> map (\pair -> (pair !! 0) .|. (pair !! 1)) [[1,2], [3,4]]
[3,7]
~~~

<p>We can pattern match against the list like so:</p>



~~~haskell

> map (\(x:y:_) -> x .|. y) [[1,2], [3,4]]
[3,7]
~~~

<p>Here <cite>x</cite> takes the first value, <cite>y</cite> takes the second value and the rest of the list is assigned to <cite>_</cite> which we don't use in this case.</p>


<p>There are loads of examples of pattern matching against different data structures in <a href="http://learnyouahaskell.com/syntax-in-functions">Learn You A Haskell</a> and hopefully next time I'll remember and won't write hideous code like the first example!</p>

