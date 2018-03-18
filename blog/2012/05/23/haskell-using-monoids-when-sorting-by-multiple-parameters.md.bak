+++
draft = false
date="2012-05-23 06:44:41"
title="Haskell: Using monoids when sorting by multiple parameters"
tag=['haskell']
category=['Haskell']
+++

On the project I've been working on we had a requirement to sort a collection of rows by 4 different criteria such that if two items matched for the first criteria we should consider the second criteria and so on.

If we wrote that code in Haskell it would read a bit like this:


~~~haskell

data Row = Row { shortListed :: Bool, cost :: Float, distance1 :: Int, distance2 :: Int } deriving (Show, Eq)
~~~


~~~haskell

import Data.Ord
import Data.List

compareRow :: Row -> Row -> Ordering
compareRow x y = if comparing (not . shortListed) x y == EQ then 
                    if comparing cost x y == EQ then
                      if comparing distance1 x y == EQ then
                        comparing distance2 x y
                      else
                        comparing distance1 x y
                    else
                      comparing cost x y
                  else 
                    comparing (not . shortListed) x y
~~~

We can then sort a list of rows like this:


~~~haskell

> let shortListedRow = Row {shortListed = True, cost = 10.0, distance1 = 20, distance2 = 30 }

> let nonShortListedRow = Row {shortListed = False, cost = 10.0, distance1 = 20, distance2 = 30 }

> sortBy compareRow [nonShortListedRow, shortListedRow]
[Row {shortListed = True, cost = 10.0, distance1 = 20, distance2 = 30},
 Row {shortListed = False, cost = 10.0, distance1 = 20, distance2 = 30}]
~~~

It works but it's messy and we couldn't see what abstraction we should be using to simplify the code.

I was continuing with my reading of <a href="http://learnyouahaskell.com/functors-applicative-functors-and-monoids">Functors, Applicative Functors and Monoids</a> yesterday and got to the section on Monoids which showed an example for simplifying this type of code.

The definition of a Monoid from the Haskell source code is:

<blockquote>
Types with an associative binary operation that has an identity
</blockquote>

But I prefer <a href="http://blog.sigfpe.com/2009/01/haskell-monoids-and-their-uses.html">Dan Piponi's definition</a>:

<blockquote>
In Haskell, a monoid is a type with a rule for how two elements of that type can be combined to make another element of the same type. 

To be a monoid there also needs to be an element that you can think of as representing 'nothing' in the sense that when it's combined with other elements it leaves the other element unchanged.
</blockquote>

In our case we have a bunch of things of type 'Ordering' and we want to combine them all together and end up with a final 'Ordering' which takes them all into account.

For example if we were comparing the following two rows:


~~~haskell

> let row1 = Row {shortListed = True, cost = 10.0, distance1 = 1, distance2 = 30 }
> let row2 = Row {shortListed = True, cost = 10.0, distance1 = 100, distance2 = 30 }
> compareRow row1 row2
LT
~~~

When we compare their shortListed value we get back 'EQ', so we compare their cost value and get back 'EQ' and finally we compare their distance1 value which gives back 'LT' which is our final value.

We can make use of the Ordering Monoid to do this rather than all the nested if statements.

Monoid is a <a href="http://www.markhneedham.com/blog/2012/05/22/scalahaskell-a-simple-example-of-type-classes/">type class</a> defined like so:


~~~haskell

class Monoid a where
  mempty  :: a
  mappend :: a -> a -> a
  mconcat :: [a] -> a
  mconcat = foldr mappend mempty
~~~

'mempty' represents the identity value for a monoid i.e. the 'nothing' in Dan Piponi's definition. If we combine anything with this then we should get that thing back.

The most interesting function here is 'mappend' which we use to combine together two elements of a type. Each instance of Monoid needs to define this function for themselves.

The Ordering Monoid is defined like so:


~~~haskell

instance Monoid Ordering where
  mempty         = EQ
  LT `mappend` _ = LT
  EQ `mappend` y = y
  GT `mappend` _ = GT
~~~

What makes this work for us is that we always keep the value on the left unless it's 'EQ' in which case we take the value on the right. 

Therefore as soon as one of our comparisons returns a non 'EQ' value that will be the value that eventually gets returned.

e.g.


~~~text

> GT `mappend` LT `mappend` EQ
GT
~~~

Our 'row1'/'row2' comparison would look like this using 'mappend':


~~~text

> EQ `mappend` EQ `mappend` LT
LT
~~~

We can then change our 'compareRow' function:


~~~haskell

compareRow x y = comparing (not . shortListed) x y `mappend` comparing cost x y `mappend` comparing distance1 x y `mappend` comparing distance2 x y 
~~~

We can simplify this further by making use of 'mconcat' which folds over a list of monoids applying 'mappend' each time.

For example we could replace our 'row1'/'row2' comparison with the following:


~~~text

> mconcat [EQ, EQ, LT]
LT
~~~

And 'compareRow' now reads like this:


~~~haskell

compareRow x y = mconcat [comparing (not . shortListed) x y,  comparing cost x y, comparing distance1 x y, comparing distance2 x y]
~~~

We're still repeating the 'comparing' bit of code every time so I extracted that into a function:


~~~haskell

by :: Ord a => (b -> a) -> b -> b -> Ordering
by fn x y = comparing fn x y
~~~

We then need to apply those functions to x and y to get our collection of monoids we can pass to mconcat:


~~~haskell

compareRow x y = mconcat $ map (\fn -> fn x y) [by (not . shortListed), by cost, by distance1, by distance2]
~~~

<del datetime="2012-05-23T08:24:29+00:00">One problem with this code is that we're now comparing by all the parameters when we can actually stop once we've found a non equality.</del>

<del datetime="2012-05-23T08:25:17+00:00">I'm sure there's a clever way to short circuit this but I'm not sure what it is at the moment!</del>

As BeRewt points out in the comments what I wrote here is not actually the case, it is lazily evaluated!
