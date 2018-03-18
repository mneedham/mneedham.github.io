+++
draft = false
date="2012-04-03 21:52:56"
title="Haskell: Print friendly representation of an Array"
tag=['haskell']
category=['Haskell']
+++

Quite frequently I play around with 2D arrays in Haskell but I've never quite worked out how to print them in a way that makes it easy to see the contents.

I'm using the array from the 'Data.Array' module because it seems to be easier to transform them into a new representation if I want to change a value in one of the cells.

The function to create one therefore looks like this:


~~~haskell

import Data.Array

grid :: Int -> a -> Array(Int, Int) a
grid size value = array ((0,0),(size-1,size-1)) [((x,y),value) | x<-[0..size-1], y<-[0..size-1]]
~~~

Which we can use like this:


~~~haskell

> grid 2 0
array ((0,0),(1,1)) [((0,0),0),((0,1),0),((1,0),0),((1,1),0)]
~~~

I wanted to get the output to read like this:


~~~text

0 0
0 0
~~~

I initially tried to override the 'Show' implementation but wasn't very successful in trying to do that - I'm not sure whether that's actually possible but someone on the IRC channel suggested I should probably try and write my own function to print it out.

I ended up with the following:


~~~haskell

printGrid :: Show a => Array (Int, Int) a -> IO [()]
printGrid grid = sequence $ map (putStrLn . textRepresentation) $ toSimpleArray grid

toSimpleArray :: Array (Int, Int) a -> [[a]]	
toSimpleArray grid = [[grid ! (x, y) | x<-[lowx..highx]] |  y<-[lowy..highy]] 
	where ((lowx, lowy), (highx, highy)) =  bounds grid

textRepresentation :: Show a => [a] -> String
textRepresentation row = foldl (\acc y -> acc ++ (show y) ++ " ") "" row
~~~

The <cite>toSimpleArray</cite> function converts the array back into a format which is easier to deal with. So for a simple array:


~~~haskell

> toSimpleArray (grid 2 0)
[[0,0],[0,0]]
~~~

We then map over the new array and apply <cite>textRepresentation</cite> over each row to get a text representation. 

The <cite>textRepresentation</cite> function works like this:


~~~haskell

> textRepresentation [1, 2, 3]
"1 2 3 "
~~~

After that we map <cite>putStrLn</cite> over the result which gives us a collection of IO monads. 

Unfortunately that still doesn't print the array out so we need <cite>sequence</cite> which I came across in the <a href="http://learnyouahaskell.com/input-and-output">Learn You A Haskell</a> tutorial: 

<blockquote>
sequence takes a list of I/O actions and returns an I/O actions that will perform those actions one after the other. The result contained in that I/O action will be a list of the results of all the I/O actions that were performed.
</blockquote>

And eventually this is how we use <cite>printGrid</cite>:



~~~haskell

> printGrid $ grid 2 0
0 0 
0 0 
[(),()]
~~~

There must be ways to simplify some of that code so if you can see any let me know in the comments!
