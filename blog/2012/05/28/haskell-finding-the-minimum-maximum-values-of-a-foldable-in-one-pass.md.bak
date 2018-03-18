+++
draft = false
date="2012-05-28 11:18:13"
title="Haskell: Finding the minimum & maximum values of a Foldable in one pass"
tag=['haskell']
category=['Haskell']
+++

I recently came across Dan Piponi's blog post '<a href="http://blog.sigfpe.com/2009/01/haskell-monoids-and-their-uses.html">Haskell Monoids & their Uses</a>' and towards the end of the post he suggests creating monoids to work out the maximum and minimum values of a Foldable value in one pass.

<blockquote>
The <cite><a href="http://www.haskell.org/ghc/docs/6.12.2/html/libraries/base-4.2.0.1/Data-Foldable.html">Foldable</a></cite> type class  provides a generic approach to walking through a datastructure, accumulating values as we go. 

The foldMap function applies a function to each element of our structure and then accumulates the return values of each of these applications. 
</blockquote>

A list is one example of a type which implements the Foldable type class like so:


~~~haskell

instance Foldable [] where
    foldr = Prelude.foldr
    foldl = Prelude.foldl
    foldl' = List.foldl'
    foldr1 = Prelude.foldr1
    foldl1 = Prelude.foldl1
~~~

In this case it delegates all of the Foldable functions to previously defined functions from the Prelude or List modules.

The 'foldMap' function mentioned above has the following default implementation:


~~~haskell

foldMap :: Monoid m => (a -> m) -> t a -> m
foldMap f = foldr (mappend . f) mempty
~~~

Dan shows an example where we use 'foldMap' to check whether any values in a Foldable have the value 1 by using the 'Any' monoid:


~~~haskell

> foldMap (Any . (== 1)) [1..20]
Any {getAny = True}
~~~

I couldn't quite understand how it worked so I expanded the 'foldMap' definition which results in the following:


~~~haskell

> Data.Foldable.foldr (\x acc -> acc `mappend` (Any . (== 1)) x) mempty [1..20]
Any {getAny = True}
~~~

So we're folding over the list with an initial seed value of 'Any False' as that's what mempty will evaluate to. For each value we're then calling 'mappend' with two 'Any' values and passing on the result.

So in this example it would go like this:


~~~haskell

Any False `mappend` (Any . (==1)) 20 => Any False `mappend` Any False => Any False
Any False `mappend` (Any . (==1)) 19 => Any False `mappend` Any False => Any False
...
Any False `mappend` (Any . (==1)) 1 => Any False `mappend` Any True => Any True
~~~

In our case we need to define our own monoids to keep track of the maximum value in a Foldable:


~~~haskell

import Data.Monoid
import Data.Foldable

data MaxSoFar a = MaxSoFar { getMaxSoFar :: a } deriving (Eq, Ord, Read, Show, Bounded)
instance (Num a,  Ord a, Bounded a) => Monoid (MaxSoFar a) where
  mempty = MaxSoFar (minBound)
  MaxSoFar x `mappend` MaxSoFar y = MaxSoFar (max x y)
~~~ 

We set 'mempty' to the minimum possible Int value so that anything Int value compared to it will automatically become the max value when it gets compared to that.

For 'mappend' we take the values stored in the two 'MaxSoFar' instances and then select the maximum and return a new MaxSoFar.

We call foldMap like so:


~~~haskell

> foldMap (MaxSoFar) ([1..20] :: [Int])
MaxSoFar {getMaxSoFar = 20}
~~~

MinSoFar is pretty similar in design:


~~~haskell

data MinSoFar a = MinSoFar { getMinSoFar :: a } deriving (Eq, Ord, Read, Show, Bounded)
instance (Num a,  Ord a, Bounded a) => Monoid (MinSoFar a) where
  mempty = MinSoFar maxBound
  MinSoFar x `mappend` MinSoFar y = MinSoFar (min x y) 
~~~

And we can then combine them together like this:


~~~haskell

> foldMap (\x -> (MaxSoFar x, MinSoFar x)) ([1..20] :: [Int])
(MaxSoFar {getMaxSoFar = 20},MinSoFar {getMinSoFar = 1})
~~~

This works because we can make use of what Dan calls the 'Product Monoid', which is a Monoid instance for a tuple:


~~~haskell

instance (Monoid a, Monoid b) => Monoid (a,b) where
  mempty = (mempty, mempty)
  (a1,b1) `mappend` (a2,b2) = (a1 `mappend` a2, b1 `mappend` b2)
~~~

So in our example the fold would go like this:


~~~haskell

(MaxSoFar -9223372036854775808, MinSoFar 9223372036854775807) `mappend` (MaxSoFar 20, MinSoFar 20) => (MaxSoFar 20, MinSoFar 20)
(MaxSoFar 20, MinSoFar 20) `mappend` (MaxSoFar 19, MinSoFar 19) => (MaxSoFar 20, MinSoFar 19)
...
(MaxSoFar 20, MinSoFar 2) `mappend` (MaxSoFar 1, MinSoFar 1) => (MaxSoFar 20, MinSoFar 1)
~~~

We could probably achieve the same thing without using monoids but I think this approach is pretty neat.
