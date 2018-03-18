+++
draft = false
date="2013-01-09 00:12:25"
title="Knapsack Problem in Haskell"
tag=['haskell', 'knapsack']
category=['Haskell', 'Algorithms']
+++

<p>I recently described two versions of the <a href="http://www.markhneedham.com/blog/2013/01/07/knapsack-problem-python-vs-ruby/">Knapsack problem written in Ruby and Python</a> and one common thing is that I used a global cache to store the results of previous calculations.</p>


<p>From my experience of coding in Haskell it's not considered very idiomatic to write code like that and although I haven't actually tried it, potentially more tricky to achieve.</p>


<p>I thought it'd be interesting to try and write the algorithm in Haskell with that constraint in mind and my first version looked like this:</p>



~~~haskell

ref :: a -> IORef a
ref x = unsafePerformIO (newIORef x)   

knapsackCached1 :: [[Int]] -> Int -> Int -> IORef (Map.Map (Int, Int) Int) -> Int
knapsackCached1 rows knapsackWeight index cacheContainer = unsafePerformIO $ do
  cache <- readIORef cacheContainer
  if index == 0 || knapsackWeight == 0 then do
    return 0
  else
    let (value:weight:_) = rows !! index
         best = knapsackCached1 rows knapsackWeight prevIndex cacheContainer  in
    if weight > knapsackWeight && lookupPreviousIn cache == Nothing then do
      let updatedCache =  Map.insert (prevIndex, knapsackWeight) best cache
      writeIORef cacheContainer updatedCache
      return $ fromJust $ lookupPreviousIn updatedCache
    else
      if lookupPreviousIn cache == Nothing then do
        let newBest = maximum [best, value + knapsackCached1 rows (knapsackWeight-weight) prevIndex cacheContainer]
            updatedCache = Map.insert (prevIndex, knapsackWeight) newBest cache
        writeIORef cacheContainer updatedCache
        return $ fromJust $ lookupPreviousIn updatedCache
      else
        return $ fromJust $ lookupPreviousIn cache
  where lookupPreviousIn cache = Map.lookup (prevIndex,knapsackWeight) cache
        prevIndex = index-1
~~~

<p>We then call it like this:</p>



~~~haskell

let (knapsackWeight, numberOfItems, rows) = process contents
     cache = ref (Map.empty :: Map.Map (Int, Int) Int)
knapsackCached1 rows knapsackWeight (numberOfItems-1) cache
~~~


<p>As you can see, we're passing around the cache as a parameter where the cache is a Map wrapped inside an <a href="http://www.haskell.org/ghc/docs/latest/html/libraries/base/Data-IORef.html">IORef</a> - a data type which allows us to pass around a mutable variable in the IO monad.</p>


<p>We write our new value into the cache on lines 11 and 17 so that our updates to the map will be picked up in the other recursive steps.</p>


<p>Apart from that the shape of the code is the same as the Ruby and Python versions except I'm now only using a map with a pair as the key instead of an array + map as in the other versions.</p>


<p>The annoying thing about this solution is that we have to pass the cache around as a parameter when it's just a means of optimisation and not part of the actual problem.</p>


<p>An alternative solution could be the following where we abstract the writing/reading of the map into a <cite>memoize</cite> function which we wrap our function in:</p>



~~~haskell

memoize :: ((Int, Int) -> Int) -> (Int, Int) -> Int                  
memoize fn mapKey = unsafePerformIO $ do 
  let cache = ref (Map.empty :: Map.Map (Int, Int) Int)
  items <- readIORef cache
  if Map.lookup mapKey items == Nothing then do
    let result = fn mapKey
    writeIORef cache $  Map.insert mapKey result items
    return result
  else
    return (fromJust $ Map.lookup mapKey items)        
        
knapsackCached :: [[Int]] -> Int -> Int -> Int
knapsackCached rows weight numberOfItems = 
  inner (numberOfItems-1, weight)
  where inner = memoize (\(i,w) -> if i < 0 || w == 0 then 0
                                   else
                                     let best = inner (i-1,w) 
                                         (vi:wi:_) = rows !! i in 
                                     if wi > w then best
                                     else maximum [best, vi + inner (i-1, w-wi)]) 
~~~

<p>We can call that function like this:</p>



~~~haskell

let (knapsackWeight, numberOfItems, rows) = process contents
     cache = ref (Map.empty :: Map.Map (Int, Int) Int)
knapsackCached rows knapsackWeight numberOfItems
~~~

<p>Here we define an inner function inside <cite>knapsackCached</cite> which is a partial application of the memoize function. We then pass our cache key to that function on the previous line.</p>


<p>One thing which I noticed while writing this code is that there is some strangeness around the use of 'in' after let statements. It seems like if you're inside an if/else block you need to use 'in' unless you're in the context of a Monad (do statement) in which case you don't need to.</p>


<p>I was staring a screen of compilation errors for about an hour until I realised this!</p>


<p>These are the timings for the two versions of the algorithm:</p>



~~~text

# First one
$ time ./k knapsack2.txt 
real	0m14.993s user	0m14.646s sys	0m0.320s

# Second one
$ time ./k knapsack2.txt 
real	0m12.594s user	0m12.259s sys	0m0.284s
~~~

<p>I'm still trying to understand exactly how to <a href="http://book.realworldhaskell.org/read/profiling-and-optimization.html">profile</a> <a href="http://www.haskell.org/haskellwiki/Performance/GHC">and</a> <a href="http://stackoverflow.com/questions/3276240/tools-for-analyzing-performance-of-a-haskell-program">then</a> <a href="http://www.haskell.org/ghc/docs/7.4.1/html/users_guide/runtime-control.html">optimise</a> the program so any tips are always welcome.</p>

