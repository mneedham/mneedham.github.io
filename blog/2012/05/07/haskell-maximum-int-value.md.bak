+++
draft = false
date="2012-05-07 09:18:02"
title="Haskell: Maximum Int value"
tag=['haskell']
category=['Haskell']
+++

One of the algorithms covered in <a href="https://www.coursera.org/course/algo">Algo Class</a> was the <a href="http://en.wikipedia.org/wiki/Closest_pair_of_points_problem">closest pairs algorithm</a> - an algorithm used to determine which pair of points on a plane are closest to each other based on their <a href="http://en.wikipedia.org/wiki/Euclidean_distance">Euclidean distance</a>.

My real interest lies in writing the divide and conquer version of the algorithm but I started with the brute force version so that I'd be able to compare my answers.

This is the algorithm:


~~~text

minDist = infinity
for each p in P:
  for each q in P:
    if p ≠ q and dist(p, q) < minDist:
      minDist = dist(p, q)
      closestPair = (p, q)
return closestPair
~~~

'infinity' in this case could be the maximum value that an Int could hold which on a 64 bit architecture would be 2<sup>63</sup> so I hardcoded that into my implementation:
o

~~~haskell

bfClosest :: (Ord a, Floating a) => [(a, a)] -> Maybe ((a, a), (a, a))
bfClosest pairs = 
  snd $ foldl (\ acc@(min, soFar) (p1, p2) -> 
                if distance p1 p2 < min then (distance p1 p2, Just(p1, p2)) else acc) 
              (2^63, Nothing) 
              [(pairs !! i, pairs !! j) | i <- [0..length pairs - 1], j <- [0..length pairs-1 ], i /= j]
  where distance (x1, y1) (x2, y2) =  sqrt $ ((x1 - x2) ^ 2) + ((y1 - y2) ^ 2)
~~~

We're comparing each point with all the others in the list by folding over a collection of all the combinations and then passing the pair with the smallest distance between points as part of our accumulator.

More by chance than anything else I was reading <a href="http://learnyouahaskell.com/types-and-typeclasses">the Learn You a Haskell chapter on types and type classes</a> and came across the <cite><a href="http://zvon.org/other/haskell/Outputprelude/maxBound_f.html">maxBound</a></cite> function which does exactly what I want:


~~~haskell

> 2 ^ 63
9223372036854775808

> maxBound :: Int
9223372036854775807
~~~

We can't plug that straight into the function as is because the fold inside 'bfClosest' expects a float and had been automatically coercing 2<sup>63</sup> into the appropriate type.

We therefore use 'fromIntegral' to help us out:


~~~haskell

bfClosest :: (Ord a, Floating a) => [(a, a)] -> Maybe ((a, a), (a, a))
bfClosest pairs = 
  snd $ foldl (\ acc@(min, soFar) (p1, p2) -> 
                if distance p1 p2 < min then (distance p1 p2, Just(p1, p2)) else acc) 
              (fromIntegral (maxBound :: Int), Nothing) 
              [(pairs !! i, pairs !! j) | i <- [0..length pairs - 1], j <- [0..length pairs-1 ], i /= j]
  where distance (x1, y1) (x2, y2) =  sqrt $ ((x1 - x2) ^ 2) + ((y1 - y2) ^ 2)
~~~
