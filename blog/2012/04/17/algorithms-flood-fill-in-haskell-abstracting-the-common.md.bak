+++
draft = false
date="2012-04-17 07:22:12"
title="Algorithms: Flood Fill in Haskell - Abstracting the common"
tag=['haskell', 'algorithms']
category=['Haskell', 'Algorithms']
+++

In the comments of <a href="http://www.markhneedham.com/blog/2012/04/07/algorithms-flood-fill-in-haskell/">my blog post describing the flood fill algorithm in Haskell</a> David Turner pointed out that the way I was passing the grid around was quite error prone.


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

I actually did pass the wrong grid variable around while I was writing it and ended up quite confused as to why it wasn't working as I expected.

David's suggestion based on the above version of the algorithm was that I might want to use the state monad to thread state rather than explicitly passing it around like I am here.

I had a go at writing the function using the state monad but realised while doing so that rather than doing that I could fold over a cells neighbours rather than using the state monad to thread state.

I didn't see the 'neighbours' concept the first time I wrote it but David <a href="http://hpaste.org/66803">wrote a version of the algorithm</a> in which he introduced that.

This is the resulting function:


~~~haskell

floodFill :: Array (Int, Int) Colour ->  (Int, Int) -> Colour -> Colour -> Array (Int, Int) Colour 
floodFill grid point target replacement = 
  if(target == replacement) then
    grid
  else	
    let gridWithSquareReplaced = if onGrid point then grid // [(point, replacement)] else grid 
        validNeighbours = filter (onGrid `and` sameAsTarget) neighbours in
	
        foldl (\grid point -> floodFill grid point target replacement) gridWithSquareReplaced validNeighbours 
		
        where neighbours = let (x,y) = point in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
              sameAsTarget point = grid ! point == target
              onGrid = inRange $ bounds grid   

and :: (a -> Bool) -> (a -> Bool) -> a -> Bool
and f g x = f x && g x
~~~

I initially get all of the neighbouring squares but then filter those out if they don't fit on the grid or aren't of the required colour. We can then use 'foldl' to iterate over each neighbour passing the grid along as the accumulator.

David also wrote a more succinct function to work out whether or not a value fits on the grid so I've stolen that as well!

I'm still not sure I totally understand when I should be using 'let' and 'where' but in this example the functions I've put in the 'where' section are helper functions whereas the values I defined in the 'let' section are domain concepts.

Whether that's the correct way to think of the two I'm not sure!
