+++
draft = false
date="2012-04-08 20:11:57"
title="Haskell: Processing program arguments"
tag=['haskell']
category=['Haskell']
+++

My <a href="http://getprismatic.com/newsfeed">Prismatic news feed</a> recently threw up an interesting tutorial titled '<a href="http://yannesposito.com/Scratch/en/blog/Haskell-the-Hard-Way/">Haskell the Hard Way</a>' which has an excellent and easy to understand section showing how to do IO in Haskell.

About half way down the page there's an exercise to write a program which sums all its arguments which I thought I'd have a go at.

We need to use the <cite><a href="http://zvon.org/other/haskell/Outputsystem/getArgs_f.html">System.getArgs</a></cite> function to get the arguments passed to the program. It has the following signature:


~~~haskell

> :t getArgs
getArgs :: IO [String]
~~~

Using that inside a 'do' block means that we can get the list of arguments as a List of String values.

We then need to work out how to convert the list of strings into a list of integers so that we can add them together.

The way I've done that before is with the <cite>read</cite> function:


~~~haskell

> map (\x -> read x :: Int) ["1", "2"]
[1,2]
~~~

That works fine as long as we assume that only numeric values will be passed as arguments but if not then we can end up with an exception:


~~~haskell

> map (\x -> read x :: Int) ["1", "2", "blah"]
[1,2,*** Exception: Prelude.read: no parse
~~~

I wanted to try and avoid throwing an exception like that but instead add up any numbers which were provided and ignore everything else. The type signature of the function to process the inputs therefore needed to be:

<blockquote>
[String] -> [Maybe Int]
</blockquote>

With a <a href="http://stackoverflow.com/questions/5121371/how-to-catch-a-no-parse-exception-from-the-read-function-in-haskell">bit of help from a Stack Overflow post</a> I ended up with the following code:


~~~haskell

import Data.Maybe

intify :: [String] -> [Maybe Int]
intify =  map maybeRead2

maybeRead2 :: String -> Maybe Int
maybeRead2 = fmap fst . listToMaybe . reads
~~~

<cite>reads</cite> has the following signature:


~~~haskell

> :t reads
reads :: Read a => ReadS a
~~~

which initially threw me off as I had no idea what 'ReadS' was. It's actually a synonym:


~~~haskell

type ReadS a = String -> [(a,String)]
~~~
(defined in <cite>.<a href="http://hackage.haskell.org/trac/ghc/wiki/Building/GettingTheSources?redirectedfrom=GhcDarcs">/Text/ParserCombinators/ReadP.hs</a></cite>)


In our case I thought it'd do something like this:


~~~haskell

> reads "1"
[(1, "1")]
~~~

But defining the following in a file:


~~~haskell

a :: [(Int, String)]
a = reads "1"
~~~

suggests that the string version gets lost:


~~~haskell

> a
[(1,"")]
~~~

I'm not sure I totally understand how that works!

Ether way, we then take the list of tuples and convert it into a Maybe using <cite>listToMaybe</cite>. So if we'd just parsed "1" we might end up with this:


~~~haskell

> listToMaybe [(1, "")]
Just (1,"")
~~~

I only have a basic understanding of <cite>fmap</cite> yet because I'm not up to that chapter in '<a href="http://learnyouahaskell.com/functors-applicative-functors-and-monoids">Learn Me A Haskell</a>'. 

As far as I know it's used to apply a function to a value inside a container type object, i.e. the Maybe in this case, and then return the container type with its new value

In our case we start with 'Just(1, "")' and we want to get to 'Just 1' so we use the 'fst' function to help us do that.

The main method of the program reads like this to wire it all together:


~~~haskell

main = do args <- getArgs
          print (sum $ map (fromMaybe 0) $ (intify args))
~~~

I'm using <cite><a href="http://www.haskell.org/ghc/docs/latest/html/libraries/base/Data-Maybe.html">fromMaybe</a></cite> to set a default value of 0 for any 'Nothing' values in the collection.

I compile the code like this:


~~~text

> ghc --make learn_haskell_hard_way 
[1 of 1] Compiling Main             ( learn_haskell_hard_way.hs, learn_haskell_hard_way.o )
Linking learn_haskell_hard_way ...
~~~ 

And then run it:


~~~text

>./learn_haskell_hard_way 1 2 3 4    
10

> ./learn_haskell_hard_way 1 2 3 4 mark says hello 5
15
~~~
