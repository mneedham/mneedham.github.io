+++
draft = false
date="2012-03-19 23:25:47"
title="Functional Programming: One function at a time"
tag=['functional-programming', 'haskell']
category=['Haskell']
+++

As I mentioned in an earlier post I got a bit stuck working out all the diagonals in the 20x20 grid of <a href="http://projecteuler.net/problem=11">Project Euler problem 11</a> and my <a href="http://www.markhneedham.com/blog/2012/03/13/functional-programming-shaping-the-data-to-fit-a-function/">colleague Uday ended up showing me how to do it</a>.

I realised while watching him solve the problem that we'd been using quite different approaches to solving the problem and that his way worked way better than mine, at least in this context.

My approach was to try and drive out the solution from the top down which meant in this case:

<ul>
<li>Get all of the diagonals left to right by iterating over a 2 dimensional array and accumulating sub arrays of the values 1 row and 1 column greater than the current position.</li>
</ul>

I was stuck for ages trying to work out how to do that whereas Uday made it much easier by just focusing on one of the functions that we'd need, getting that to work and then moving onto the next one.

After we'd iterated with that approach a few times we had a bunch of functions that we could compose together to solve the initial problem.

We started with a simple function to find the value at position (x,y) in the array:


~~~haskell

findValue :: Int -> Int -> [[Int]] -> Int
findValue x y grid = (grid !! x) !! y 
~~~

We then worked on writing a function in the REPL which would find all the diagonals going down from the current position


~~~haskell

[findValue (0+z) (0+z) grid | z <- [0..19]]
~~~

We eventually realised that running that from anywhere but the top left hand corner would throw an exception since we'd gone out of bounds of the array:


~~~text

> [findValue (1+z) (1+z) grid | z <- [0..19]]
[49,31,23,51,3,67,20,97,45,3,24,44,52,26,32,40,4,5,48,*** Exception: Prelude.(!!): index too large
~~~

We then wrote a function to check that a given point was actually in the array:


~~~haskell

hasItemSingle :: [a] -> Int -> Bool
hasItemSingle array position = position >= 0 && (length array - 1) >= position

hasItem :: [[a]] -> Int -> Int -> Bool
hasItem array x y = hasItemSingle array x && hasItemSingle (array !! x) y
~~~

And our function to calculate the diagonals then used that:


~~~text

> [findValue (1+z) (1+z) grid | z <- [0..19], hasItem grid (1+z) (1+z) ]
[49,31,23,51,3,67,20,97,45,3,24,44,52,26,32,40,4,5,48]
~~~

That function eventually ended up like this:


~~~haskell

diagonalAt :: Int -> Int -> [[Int]] -> [Int]
diagonalAt x y grid = [findValue (x+z) (y+z) grid | z <- [0..(length grid)], hasItem grid (x + z) (y + z)]
~~~

The nice thing about taking this approach of only thinking about one function at a time is that you can actually make some progress since you only need to think about a small part of the problem as compared to the whole thing.

I still start off trying to solve a problem from the outside in but if I get stuck then I start looking for some simple functions that I can write to get started and help me work towards an overall solution.
