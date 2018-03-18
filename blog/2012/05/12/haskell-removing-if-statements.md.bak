+++
draft = false
date="2012-05-12 15:46:31"
title="Haskell: Removing if statements"
tag=['haskell']
category=['Haskell']
+++

When I was looking over <a href="http://www.markhneedham.com/blog/2012/05/09/haskell-closest-pairs-algorithm/">my solution to the closest pairs algorithm</a> which I wrote last week I realised there there were quite a few if statements, something I haven't seen in other Haskell code I've read.

This is the initial version that I wrote:


~~~haskell

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

We can remove the first if statement which checks the length of the list and replace it with pattern matching code like so:


~~~haskell

dcClosest :: (Ord a, Floating a) => [Point a] -> (Point a, Point a)
dcClosest pairs
  | length pairs <= 3 = fromJust $ bfClosest pairs    
  | otherwise = foldl (\closest (p1:p2:_) -> if distance (p1, p2) < distance closest then (p1, p2) else closest)
                      closestPair 
                      (windowed 2 pairsWithinMinimumDelta)
    ...
~~~

We can also get rid of the if statement inside the first argument passed to 'foldl' and replace it with a call to 'minimumBy':


~~~haskell

dcClosest :: (Ord a, Floating a) => [Point a] -> (Point a, Point a)
dcClosest pairs
  | length pairs <= 3 = fromJust $ bfClosest pairs    
  | otherwise = foldl (\closest (p1:p2:_) -> minimumBy (compare `on` distance) [closest, (p1, p2)])
                      closestPair 
                      (windowed 2 pairsWithinMinimumDelta)
    ...
~~~

We can do the same to replace the if statement where we work out the closestPair which results in this final version of the code:


~~~haskell

dcClosest :: (Ord a, Floating a) => [Point a] -> (Point a, Point a)
dcClosest pairs
  | length pairs <= 3 = fromJust $ bfClosest pairs    
  | otherwise = foldl (\closest (p1:p2:_) -> minimumBy (compare `on` distance) [closest, (p1, p2)])
                      closestPair 
                      (windowed 2 pairsWithinMinimumDelta)
  where sortedByX = sortBy compare pairs	      
        (leftByX:rightByX:_) = chunk (length sortedByX `div` 2) sortedByX    
        closestPair = minimumBy (compare `on` distance) [closestLeftPair, closestRightPair]
          where closestLeftPair =  dcClosest leftByX
                closestRightPair = dcClosest rightByX     
        pairsWithinMinimumDelta = sortBy (compare `on` snd) $ filter withinMinimumDelta sortedByX
          where withinMinimumDelta (x, _) = abs (xMidPoint - x) <= distance closestPair
                  where (xMidPoint, _) = last leftByX
~~~

It takes up marginally less space and I think the change to use pattern matching on the length of 'pairs' makes the biggest difference as the code is now lined up at the same level of indentation.

The other changes would have more of an impact if there were more than 2 things being compared - right now I think either of the versions of the code are equally readable.
