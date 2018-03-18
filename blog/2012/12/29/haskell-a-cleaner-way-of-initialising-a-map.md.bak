+++
draft = false
date="2012-12-29 20:14:12"
title="Haskell: A cleaner way of initialising a map"
tag=['haskell']
category=['Haskell']
+++

<p>I recently wrote a blog post <a href="http://www.markhneedham.com/blog/2012/12/29/haskell-initialising-a-map/">showing a way of initialising a Haskell map</a> and towards the end of the post I realised how convoluted my approach was and wondered if there was an easier way and indeed there is!</p>


<p>To recap, this is the code I ended up with to populate a map with binary based values as the keys and node ids as the values:</p>



~~~haskell

import Data.Map 

toMap :: [Int] -> Map Int [Int]
toMap nodes = fromList $ map asMapEntry $ (groupIgnoringIndex . sortIgnoringIndex) nodesWithIndexes
              where nodesWithIndexes = (zip [0..] nodes)

groupIgnoringIndex = groupBy (\(_,x) (_,y) -> x == y) 
sortIgnoringIndex = sortBy (\(_,x) (_,y) -> x `compare` y)

asMapEntry :: [(Int, Int)] -> (Int, [Int]) 
asMapEntry nodesWithIndexes = 
   ((snd . head) nodesWithIndexes, Prelude.foldl (\acc (x,_) -> acc ++ [x]) [] nodesWithIndexes)
~~~


~~~haskell

> assocs $ toMap [1,2,5,7,2,4]
[(1,[0]),(2,[4,1]),(4,[5]),(5,[2]),(7,[3])]
~~~

<p>To sum up what we're trying to do: when a key doesn't have an entry we want to create one with a list containing the appropriate value and if the key already has a value then we want to append that value to the existing list.</p>


<p>As it turns out the <cite><a href="http://www.haskell.org/ghc/docs/6.12.2/html/libraries/containers-0.3.0.0/Data-Map.html#v%3AinsertWith">insertWith</a></cite> function does exactly what we want:</p>



~~~haskell

> let emptyMap = empty :: Map Int [Int]
> assocs $ foldl (\acc (id,val) -> insertWith (++) val [id] acc) emptyMap nodesWithIndexes
[(1,[0]),(2,[4,1]),(4,[5]),(5,[2]),(7,[3])]
~~~

<p>Based on this experience it would appear that the same type of thing applies when coding in Haskell as when coding in Clojure.</p>


<p>To <a href="http://blog.jayfields.com/2012/09/replacing-common-code-with-clojureset.html">paraphrase Jay Fields</a>:</p>


<blockquote>If you've written a fair amount of Clojure code [...] then chances are you've probably reinvented a few functions that are already available in the standard library.</blockquote>
