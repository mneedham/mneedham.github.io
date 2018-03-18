+++
draft = false
date="2012-02-25 23:40:07"
title="Haskell: Viewing the steps of a reduce"
tag=['haskell']
category=['Haskell']
+++

I've been playing around with Haskell a bit over the last week and in the bit of code I was working on I wanted to fold over a collection but see the state of the fold after each step.

I remembered Don Syme showing me how to do something similar during the F# Exchange last year while we were <a href="http://fssnip.net/8R">writing some code to score a tennis game</a> by using <cite><a href="http://msdn.microsoft.com/en-us/library/ee340364.aspx">Seq.scan</a></cite>.

I didn't realise there was also a scan function in Haskell which could be defined in terms of <cite>foldl</cite> if we wanted to:


~~~haskell

foldscanl :: (a -> b -> a) -> a -> [b] -> [a]
foldscanl fn acc ls = foldl (\ x y -> x ++ [fn (last x) y]) [acc] ls
~~~


~~~haskell

*Main> foldscanl (+) 0 [1..10]
[0,1,3,6,10,15,21,28,36,45,55]
~~~

The <a href="http://hackage.haskell.org/packages/archive/base/latest/doc/html/src/GHC-List.html#scanl">actual function is defined like so</a>:


~~~haskell

scanl                   :: (a -> b -> a) -> a -> [b] -> [a]
scanl f q ls            =  q : (case ls of
                                []   -> []
                                x:xs -> scanl f (f q x) xs)
~~~


~~~haskell

*Main> scanl (*) 1 [1..10]
[1,1,2,6,24,120,720,5040,40320,362880,3628800]
~~~

I've been finding <cite>scanl</cite> particularly useful for working out whether the function I'm using to fold over the collection is actually working correctly.

There's also a <cite>scanr</cite> if we want to fold over the collection from the right hand side.
