+++
draft = false
date="2012-12-31 20:44:56"
title="Haskell: An impressively non performant union find"
tag=['haskell']
category=['Haskell']
+++

<p>I've spent the best part of the last day debugging a <a href="https://github.com/mneedham/algorithms2/blob/master/clustering.hs">clustering algorithm</a> I wrote as part of the <a href="https://www.coursera.org/course/algo2">Algorithms 2</a> course, eventually coming to the conclusion that the <a href="http://en.wikipedia.org/wiki/Disjoint-set_data_structure">union find data structure</a> I was using wasn't working as expected.</p>


<p>In our algorithm we're trying to group together points which are 'close' to each other and the data structure is particular useful for doing that.</p>


To paraphrase from <a href="http://www.markhneedham.com/blog/2012/12/23/kruskals-algorithm-using-union-find-in-ruby/">my previous post about how we use the union find data structure</a>:</p>


<p>We start out with n connected components i.e. every point is in its own connected component.</p>


<p>We then merge these components together as calculate the neighbours of each point until we've iterated through all the points and have grouped all the points into the appropriate components.</p>


<p>I came across 3 libraries which implement this data structure - <a href="http://hackage.haskell.org/packages/archive/union-find/0.2/doc/html/Data-UnionFind-ST.html">union-find</a>, <a href="http://hackage.haskell.org/packages/archive/equivalence/0.2.3/doc/html/Data-Equivalence-Monad.html">equivalence</a> and <a href="http://hackage.haskell.org/packages/archive/persistent-equivalence/0.3/doc/html/Data-Equivalence-Persistent.html#v:emptyEquivalence">persistent-equivalence</a>.</p>


<p>union-find seemed like it had the easiest API to understand so I plugged it into my program only to eventually realise that it wasn't putting the points into components as I expected.</p>


<p>I eventually narrowed the problem down to the following example:</p>



~~~haskell

> let uf = emptyEquivalence (0,9)
[(0,0),(1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),(9,9)]

> components $ equate 0 1 uf
[(0,0),(1,0),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),(9,9)]

> components $ equate 8 9 $ equate 0 1 $ uf
[(0,0),(1,0),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),(9,8)]

> components $ equate 0 8 $ equate 8 9 $ equate 0 1 $ uf
[(0,0),(1,0),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,0),(9,8)]
~~~

<p>We start out with a union-find where every point is in its own component. The next line puts points '0' and '1' into the same component which it does by making indexes '0' and '1' of the array both have the same value, in this case 0, which is known as the component's leader.</p>


<p>We continue doing that for points '8' and '9' which works fine and our union find now consists of 8 components - the ones with leaders 8 & 0 which have two elements and then ones with leaders 2,3,4,5,6 & 7 which only contain themselves.</p>


<p>Things go wrong on our next step where we try to join nodes '0' and '8'. As I understand it what should happen here is that all the points connected to either '0' or '8' should end up in the same component so we should have a component containing points '0', '1', '8' and '9' but '9' has been missed off in this case.</p>


<p>The implementation is deliberately written to work like this so I thought I'd try writing my own version based on the following Ruby version:</p>



~~~ruby

class UnionFind
  def initialize(n)
    @leaders = 1.upto(n).inject([]) { |leaders, i| leaders[i] = i; leaders }
  end
 
  def connected?(id1,id2)
    @leaders[id1] == @leaders[id2]
  end
 
  def union(id1,id2)
    leader_1, leader_2 = @leaders[id1], @leaders[id2]
    @leaders.map! {|i| (i == leader_1) ? leader_2 : i }
  end
end
~~~

<p>This is <a href="https://github.com/mneedham/algorithms2/blob/master/Leaders.hs">my Haskell equivalent</a> which I adapted from the union-find one that I mentioned above:</p>



~~~haskell

module Leaders (UnionSet, create, components, numberOfComponents, indexes, inSameComponent, union) where

import Control.Concurrent.MVar
import Control.Monad
import Data.Array.Diff as ArrayDiff
import Data.IORef
import qualified Data.List
import Data.Maybe
import System.IO.Unsafe
import qualified Data.Set as Set

arrayFrom :: (IArray a e, Ix i) => (i,i) -> (i -> e) -> a i e
arrayFrom rng f = array rng [ (x, f x) | x <- range rng ]

ref :: a -> IORef a
ref x = unsafePerformIO (newIORef x)

data UnionSet i = UnionSet { leaders :: IORef (DiffArray i i) }

create :: Ix i => (i, i) -> UnionSet i
create is = UnionSet (ref (arrayFrom is id))

extractComponents :: Ix i => DiffArray i i -> [(i, i)]    
extractComponents  = Set.toList . Set.fromList . ArrayDiff.assocs

components :: Ix i => UnionSet i -> [(i,i)]
components (UnionSet leaders) = unsafePerformIO $ do
    l <- readIORef leaders
    return (extractComponents l)
    
numberOfComponents :: Ix i => UnionSet i -> Int
numberOfComponents (UnionSet leaders) = unsafePerformIO $ do
    l <- readIORef leaders
    return (length $ extractComponents l) 

indexes :: Ix i => UnionSet i -> [(i,i)]
indexes (UnionSet leaders) = unsafePerformIO $ do
    l <- readIORef leaders
    return (ArrayDiff.assocs l)       

inSameComponent :: Ix i => UnionSet i -> i -> i -> Bool
inSameComponent (UnionSet leaders) x y = unsafePerformIO $ do
    l <- readIORef leaders
    return (l ! x == l ! y)
    
union x y (UnionSet leaders)  = unsafePerformIO $ do
    ls <- readIORef leaders
    let leader1 = ls ! x 
        leader2 = ls ! y
        newLeaders = map (\(index, value) -> (index, leader2)) . filter (\(index, value) -> value == leader1) $ assocs ls        
    modifyIORef leaders (\l -> l // newLeaders)
    return $ UnionSet leaders
~~~

<p>We can recreate the above example like so:</p>



~~~haskell

> indexes $ Leaders.union 0 8 $ Leaders.union 8 9 $ Leaders.union 0 1 $ create (0,9)
[(0,9),(1,9),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,9),(9,9)]
~~~

<p>Unfortunately it takes 44 seconds to execute which is mainly down to the call to <cite><a href="http://zvon.org/other/haskell/Outputarray/index.html">assocs</a></cite> on line 46. <cite>assocs</cite> gives us a list of all the indexes and their corresponding values which we use to work out which indexes need to be updated with a new leader.</p>


<p>The rest of the code is mostly boiler plate around getting the array out of the <a href="http://www.haskell.org/ghc/docs/latest/html/libraries/base/Data-IORef.html">IORef</a>. The IORef allows us to have a mutable array in this instance. There is a <a href="http://c2.com/cgi/wiki?HaskellExampleForMutabilityOnObjects">page on the c2 wiki which explains how to use IORef in more detail</a>.</p>


<p>Although using the DiffArray allows us to provide a pure external interface around its use, it is <a href="http://www.haskell.org/haskellwiki/Modern_array_libraries#DiffArray_.28module_Data.Array.Diff.29">known to be 10-100x slower than an MArray</a>.</p>


<p>I've been playing around with a version of the union-find data structure which <a href="https://github.com/mneedham/algorithms2/blob/master/MutableLeaders.hs">makes use of an MArray instead</a> and has decreased the execution time to 34 seconds.</p>


<p>Unless anyone has any ideas for how I can get this to perform more quickly I'm thinking that perhaps an array isn't a good choice of underlying data structure at least when using Haskell.</p>

