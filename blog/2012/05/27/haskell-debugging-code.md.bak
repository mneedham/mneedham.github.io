+++
draft = false
date="2012-05-27 22:16:38"
title="Haskell: Debugging code"
tag=['haskell']
category=['Haskell']
+++

In my <a href="http://www.markhneedham.com/blog/2012/05/20/haskell-my-first-attempt-with-quickcheck-and-hunit/">continued attempts to learn QuickCheck</a>, one thing I've been doing is comparing the results of my <a href="http://www.markhneedham.com/blog/2012/05/07/haskell-maximum-int-value/">brute force</a> and <a href="http://www.markhneedham.com/blog/2012/05/09/haskell-closest-pairs-algorithm/">divide & conquer versions</a> of the closest pairs algorithm.

I started with this property:


~~~haskell

let prop_dc_bf xs = (length xs > 2) ==> (fromJust $ bfClosest xs) == dcClosest xs
~~~

And then ran it from GHCI, which resulted in the following error:


~~~text

> quickCheck (prop_dc_bf  :: [(Double, Double)] -> Property)
*** Failed! Falsifiable (after 8 tests and 19 shrinks):     
[(-165.0,8.0),(5.0,47.0),(6.0,0.0),(8.0,0.0),(2.0,1.0),(-129.0,17.0),(-15.0,11.0)]
~~~

I wasn't really sure where to start to work out what had gone wrong but I eventually came across Debug.Trace which has the '<a href="http://www.haskell.org/ghc/docs/latest/html/libraries/base/Debug-Trace.html#v%3Atrace">trace</a>' function which I found quite useful.

<blockquote>
trace :: String -> a -> aSource

The trace function outputs the trace message given as its first argument, before returning the second argument as its result.

For example, this returns the value of f x but first outputs the message.

trace ("calling f with x = " ++ show x) (f x)
</blockquote>

The initial divide and conquer algorithm read like this:


~~~haskell

dcClosest :: (Ord a, Floating a) => [Point a] -> Pair a
dcClosest pairs
  | length pairs <= 3 = fromJust $ bfClosest pairs    
  | otherwise = foldl (\closest (p1:p2:_) -> minimumBy (compare `on` distance') [closest, Pair p1 p2])
                      closestPair 
                      (windowed 2 pairsWithinMinimumDelta)
  where sortedByX = sortBy compare pairs	      
        (leftByX:rightByX:_) = chunk (length sortedByX `div` 2) sortedByX    
        closestPair = minimumBy (compare `on` distance') [closestLeftPair, closestRightPair]
          where closestLeftPair =  dcClosest leftByX
                closestRightPair = dcClosest rightByX     
        pairsWithinMinimumDelta = sortBy (compare `on` snd) $ filter withinMinimumDelta sortedByX
          where withinMinimumDelta (x, _) = abs (xMidPoint - x) <= distance' closestPair
                  where (xMidPoint, _) = last leftByX
~~~

So I put a 'trace' before the 'foldl' function to see what was being passed to it:


~~~haskell

dcClosest :: (Ord a, Floating a) => [Point a] -> Pair a
dcClosest pairs
  | length pairs <= 3 = fromJust $ bfClosest pairs    
  | otherwise = trace ("passed in the following: " ++ show (windowed 2 pairsWithinMinimumDelta)) 
                foldl (\closest (p1:p2:_) -> minimumBy (compare `on` distance') [closest, Pair p1 p2])
                      closestPair 
                      (windowed 2 pairsWithinMinimumDelta)
...	
~~~


~~~text

> dcClosest [(-165.0,8.0),(5.0,47.0),(6.0,0.0),(8.0,0.0),(2.0,1.0),(-129.0,17.0),(-15.0,11.0)]
passed in the following: []
(2.0,1.0) (6.0,0.0)
~~~

The function still works the same way but it prints out the trace message as well. 

Having run this a few times I realised that I'd made a mistake with the values that I'd passed to 'foldl' - I was supposed to pass the combination of all the pairs in 'pairsWithinMinimumDelta' but had actually only passed in adjacent ones.

The following change needs to be made to fix that:


~~~haskell

dcClosest :: (Ord a, Floating a) => [Point a] -> Pair a
dcClosest pairs
  | length pairs <= 3 = fromJust $ bfClosest pairs    
  | otherwise =  foldl (\closest (p1, p2) -> minimumBy (compare `on` distance') [closest, Pair p1 p2])
                      closestPair 
                      (combos pairsWithinMinimumDelta)
  where sortedByX = sortBy compare pairs	      
        (leftByX:rightByX:_) = chunk (length sortedByX `div` 2) sortedByX    
        closestPair = minimumBy (compare `on` distance') [closestLeftPair, closestRightPair]
          where closestLeftPair =  dcClosest leftByX
                closestRightPair = dcClosest rightByX     
        pairsWithinMinimumDelta = sortBy (compare `on` snd) $ filter withinMinimumDelta sortedByX
          where withinMinimumDelta (x, _) = abs (xMidPoint - x) <= distance' closestPair
                  where (xMidPoint, _) = last leftByX	
combos :: [a] -> [(a,a)]
combos initial = 
	[(initial !! i, initial !! j) | i <- [0..length initial - 1], j <- [i+1..length initial-1 ], i /= j]
~~~

It's still not perfect because we end up doing too many comparisons in the 'foldl' part of the code.

It does now, however, give the same results as the brute force version.


~~~text

> quickCheck (prop_dc_bf  :: [(Double, Double)] -> Property)
+++ OK, passed 100 tests.
~~~
