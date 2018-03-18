+++
draft = false
date="2012-04-07 00:25:34"
title="Algorithms: Flood Fill in Haskell"
tag=['haskell', 'algorithms']
category=['Haskell', 'Algorithms']
+++

<a href="http://en.wikipedia.org/wiki/Flood_fill">Flood fill</a> is an algorithm used to work out which nodes are connected to a certain node in a multi dimensional array. In this case we'll use a two dimensional array.

The idea is that we decide that we want to change the colour of one of the cells in the array and have its immediate neighbours who share its initial colour have their colour changed too i.e. the colour floods its way through the grid.

The algorithm is described on Wikipedia like so:

<blockquote>
Flood-fill (node, target-color, replacement-color):
<ol>
<li>If the color of node is not equal to target-color, return.</li>
<li>Set the color of node to replacement-color.</li>
<li>
	<ul>
 	<li>Perform Flood-fill (one step to the west of node, target-color, replacement-color).</li>
 	<li>Perform Flood-fill (one step to the east of node, target-color, replacement-color).</li>
 	<li>Perform Flood-fill (one step to the north of node, target-color, replacement-color).</li>
 	<li>Perform Flood-fill (one step to the south of node, target-color, replacement-color).</li>
	</ul>
</li>
<li>Return.</li>
</blockquote>

I decided to have a go at implementing it in Haskell and ended up with the following code:


~~~haskell

import Data.Array
data Colour = White | Black | Blue | Green | Red deriving (Show, Eq) 
~~~


~~~haskell

inBounds :: Array (Int, Int) Colour -> (Int, Int) -> Bool
inBounds grid (x, y) = x >= lowx && x <= highx && y >= lowy && y <= highy
	where ((lowx, lowy), (highx, highy)) =  bounds grid

replace :: Array (Int, Int) Colour -> (Int, Int) -> Colour -> Array (Int, Int) Colour
replace grid point replacement = if inBounds grid point then grid // [(point, replacement)] else grid
~~~	

~~~haskell

floodFill :: Array (Int, Int) Colour ->  (Int, Int) -> Colour -> Colour -> Array (Int, Int) Colour
floodFill grid point@(x, y) target replacement =
  if((not $ inBounds grid point) ||  grid ! (x,y) /= target) then grid 
  else 
    gridNorth
    where grid' = replace grid point replacement
          gridEast = floodFill grid' (x+1, y) target replacement
          gridWest = floodFill gridEast (x-1, y) target replacement
          gridSouth = floodFill gridWest (x, y+1) target replacement
          gridNorth = floodFill gridSouth (x, y-1) target replacement
~~~

Since we can't mutate the array, but only create new instances of it, we have to pass it onto the next recursive call such that the recursive call to the 'East' passes its result to the one recursing to the 'West' and so on.

It seemed to be easier to check that the square we wanted to change was actually in the grid in the <cite>replace</cite> function rather than before calling it so I pushed the logic into there. The <cite><a href="http://cvs.haskell.org/Hugs/pages/libraries/base/Data-Array.html#v%3Abounds">bounds</a></cite> function was useful for allowing me to work out if we were still on the grid.

If we start with this grid:


~~~haskell

> printGrid $ (toComplexArray [[White, White, White, Blue, Blue], [Blue, White, Blue, Blue, Blue], [Blue, Blue, Blue, Green, Green], [Green, Red, Blue, Black, Black], [Blue, Blue, Blue, Green, Blue]])

White White White Blue  Blue
Blue  White Blue  Blue  Blue
Blue  Blue  Blue  Green Green
Green Red   Blue  Black Black
Blue  Blue  Blue  Green Blue
~~~

Let's say we want to change the 'Blue' value on the second line down, third row across (position 1,2) in the array to be 'Red':


~~~haskell

> printGrid $ floodFill (toComplexArray [[White, White, White, Blue, Blue], [Blue, White, Blue, Blue, Blue], [Blue, Blue, Blue, Green, Green], [Green, Red, Blue, Black, Black], [Blue, Blue, Blue, Green, Blue]]) (1,2) Blue Red

White White White Red   Red
Red   White Red   Red   Red
Red   Red   Red   Green Green
Green Red   Red   Black Black
Red   Red   Red   Green Blue
~~~

The <cite>toComplexArray</cite> function is used to convert a list into an 'Array' because it's much easier to create a list for testing purposes. The <a href="https://github.com/mneedham/haskell/blob/master/PrintArray.hs">code for that is on github</a> if you're interested.

I described the <cite>printGrid</cite> function <a href="http://www.markhneedham.com/blog/2012/04/03/haskell-print-friendly-representation-of-an-array/">in my last post</a> and the rest of the code is on <a href="https://github.com/mneedham/haskell/blob/master/flood_fill.hs">my github haskell repository</a>.
