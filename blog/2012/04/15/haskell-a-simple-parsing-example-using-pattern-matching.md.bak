+++
draft = false
date="2012-04-15 14:22:45"
title="Haskell: A simple parsing example using pattern matching"
tag=['haskell']
category=['Haskell']
+++

As part of <a href="https://code.google.com/codejam/contest/1460488/dashboard#s=p1">the second question in the Google Code Jam</a> I needed to be able to parse lines of data which looked like this:


~~~text

3 1 5 15 13 11
~~~

where

<blockquote>The first integer will be N, the number of Googlers, and the second integer will be S, the number of surprising triplets of scores. The third integer will be p, as described above. Next will be N integers ti: the total points of the Googlers.
</blockquote>

This seemed like it should be easy to do but my initial search led me to the <a href="http://book.realworldhaskell.org/read/using-parsec.html"> Parsec chapter</a> in Real World Haskell which seemed a bit over the top for my problem.

All we really need to do is split on a space and then extract the parts of the resulting list.

I thought there'd be a 'split' function to do that in the base libraries but if there is I couldn't see it.

However, there are a bunch of useful functions in the '<a href="http://hackage.haskell.org/packages/archive/split/0.1.4.2/doc/html/Data-List-Split.html">Data.List.Split</a>' module which we can install using <a href="http://www.haskell.org/cabal/">cabal</a> - a RubyGems like tool which came with my Haskell installation.

Installing the <a href="http://hackage.haskell.org/package/split-0.1.4.2">split module</a> was as simple as: 


~~~text

cabal update
cabal install split
~~~


There's a list of all the packages available through cabal <a href="http://hackage.haskell.org/package/">here</a>.

I needed the <cite>splitOn</cite> function:


~~~text

import Data.List.Split
> :t splitOn
splitOn :: Eq a => [a] -> [a] -> [[a]]
~~~

We can then split on a space and extract the  appropriate values using pattern matching like so:


~~~haskell

let (_:surprisingScores:p:googlers) = map (\x -> read x :: Int) $ splitOn " " "3 1 5 15 13 11"
~~~


~~~text

> surprisingScores 
1
~~~


~~~text

> p
5
~~~


~~~text

> googlers 
[15,13,11]
~~~
