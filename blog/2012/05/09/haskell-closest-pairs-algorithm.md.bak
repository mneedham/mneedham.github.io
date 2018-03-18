+++
draft = false
date="2012-05-09 00:05:56"
title="Haskell: Closest Pairs Algorithm"
tag=['haskell']
category=['Haskell']
+++

As I mentioned in <a href="http://www.markhneedham.com/blog/2012/05/07/haskell-maximum-int-value/">a post a couple of days ago</a> I've been writing the closest pairs algorithm in Haskell and while the brute force version works for small numbers of pairs it starts to fall apart as the number of pairs increases:


~~~text

time ./closest_pairs 100 bf 
./closest_pairs 100 bf  0.01s user 0.00s system 87% cpu 0.016 total

time ./closest_pairs 1000 bf
./closest_pairs 1000 bf  3.59s user 0.01s system 99% cpu 3.597 total

time ./closest_pairs 5000 bf
./closest_pairs 5000  554.09s user 0.36s system 99% cpu 9:14.46 total
~~~

Luckily there's a divide and conquer algorithm we can use which brings down the running time from O(n<sup>2</sup>) to O(n log(n)) which is significantly quicker as n increases in size.

That <a href="http://en.wikipedia.org/wiki/Closest_pair_of_points_problem">algorithm is defined like so</a>:

<blockquote>
<ol>
<li>Sort points along the x-coordinate</li>
<li>Split the set of points into two equal-sized subsets by a vertical line x = x<sub>mid</sub></li>
<li>Solve the problem recursively in the left and right subsets. This will give the left-side and right-side minimal distances d<sub>Lmin</sub>  and d<sub>Rmin</sub>  respectively.</li>
<li>Find the minimal distance d<sub>LRmin</sub>  among the pair of points in which one point lies on the left of the dividing vertical and the second point lies to the right (a split pair).</li>
<li>The final answer is the minimum among d<sub>Lmin</sub>, d<sub>Rmin</sub>, and d<sub>LRmin</sub>.</li>
</ol>
</blockquote>

By step 4 in which we'll look for a closest pair where the x and y values are in opposite subsets  we don't need to consider the whole list of points again since we already know that the closest pair of points is no further apart than <cite>dist</cite> = min(d<sub>Lmin</sub>, d<sub>Rmin</sub>). 

We can therefore filter out a lot of the values by only keeping values which are within <cite>dist</cite> of the middle x value. 

If a point is further away than that then we already know that the distance between it and any point on the other side will be greater than <cite>dist</cite> so there's no point in considering it.

I used the <a href="http://rosettacode.org/wiki/Closest-pair_problem#C.23">C# version from Rosetta Code</a> as a template and this is what I ended up with:


~~~haskell

import Data.Maybe
import Data.List
import Data.List.Split
import Data.Function

dcClosest :: (Ord a, Floating a) => [Point a] -> (Point a, Point a)
dcClosest pairs
  if length pairs <= 3 then = fromJust $ bfClosest pairs    
  else 
    foldl (\closest (p1:p2:_) -> if distance (p1, p2) < distance closest then (p1, p2) else closest) 
          closestPair 
          (windowed 2 pairsWithinMinimumDelta)
  where sortedByX = sortBy compare pairs	      
        (leftByX:rightByX:_) = chunk (length sortedByX `div` 2) sortedByX
        closestPair = if distance closestLeftPair < distance closestRightPair then closestLeftPair else closestRightPair  
          where closestLeftPair =  dcClosest leftByX
                closestRightPair = dcClosest rightByX
        pairsWithinMinimumDelta = sortBy (compare `on` snd) $ filter withinMinimumDelta sortedByX
          where withinMinimumDelta (x, _) = abs (xMidPoint - x) <= distance closestPair   
                  where (xMidPoint, _) = last leftByX
~~~

If the number of pairs is 3 or less then we can just use the brute force algorithm since the whole splitting the list in half thing doesn't work so well with a list of less than 4 items.

The main function is a fold which goes over all the pairs of points where we've determined that there might be a closest pair with one point on the left hand side of our 'sorted by x list' and the other on the right hand side. 

We use the '<a href="http://www.markhneedham.com/blog/2012/02/28/haskell-creating-a-sliding-window-over-a-collection/">windowed</a>' function to pair up the points which in this case does something like this:


~~~haskell

> windowed 2 [(0,0), (1,1), (2,2), (1.1, 1.2)]
[[(0.0,0.0),(1.0,1.0)],[(1.0,1.0),(2.0,2.0)],[(2.0,2.0),(1.1,1.2)]]
~~~

We pass along the closest pair that we've found from pairs of points on the left and right hand sides of the list as our seed value and check whether any of the split pairs are closer together than that one. By the time the fold is finished we will have the closest pair in the list.

The code in the where section is used to split the list into two halves, sort it by x and then work out which side of the list has the closest pair. That's all done recursively and then the last bit of code works out which values we need to consider for the split pairs part of the algorithm.

I learnt about the '<a href="http://stackoverflow.com/questions/2788195/haskell-sorting">on</a>' function while writing this algorithm which makes it really easy to pick a function to sort a collection with e.g. 'compare `on` snd' lets us sort a list in ascending order based on the second value in a tuple.

One problem with the way I've written this algorithm is that it places a lot of focus on the split pair bit of the code when actually a big part of why it works is that we're sorting it into an order that makes it easier to work with and then dividing the problem by 2 each time.

My current thinking is that perhaps I should have had that code in the main body of the function rather than hiding it away in the where section.

It isn't actually necessary to execute the foldl all the way through since we'll often know there's not going to be a split pair before we go through all the pairs. I thought it reads pretty nicely as it is thought and it runs pretty quickly as it is anyway!

Using the same data set as before (and getting the same answers!):


~~~text

> time ./closest_pairs 1000 dc
./closest_pairs 1000 dc  0.02s user 0.00s system 91% cpu 0.024 total

> time ./closest_pairs 5000 dc
./closest_pairs 5000 dc  0.11s user 0.01s system 97% cpu 0.118 total
~~~


I described the code for <a href="http://www.markhneedham.com/blog/2012/05/08/haskell-generating-random-numbers/">generating random numbers</a> in an earlier blog post but I'll include it again to show how the algorithm is wired up:


~~~haskell

import Control.Monad.State (State, evalState, get, put)
import System.Random (StdGen, mkStdGen, random)
import System

type R a = State StdGen a
rand :: R Double
rand = do
  gen <- get
  let (r, gen') = random gen
  put gen'
  return r

randPair :: R (Double, Double)
randPair = do
  x <- rand
  y <- rand
  return (x,y)

runRandom :: R a -> Int -> a
runRandom action seed = evalState action $ mkStdGen seed

normals :: R [(Double, Double)]
normals = mapM (\_ -> randPair) $ repeat ()

main = do 
	args <- getArgs
	let numberOfPairs = read (head args) :: Int
	if length args > 1 && args !! 1 == "bf" then 
		putStrLn $ show ( (bfClosest $ take numberOfPairs $ runRandom normals 42))
	else 
		putStrLn $ show ( (dcClosest $ take numberOfPairs $ runRandom normals 42))
~~~

The <a href="http://hpaste.org/68299">full code is on hpaste</a> if anyone has any suggestions for how to improve it.
