+++
draft = false
date="2012-05-16 13:16:48"
title="Haskell: Writing a custom equality operator"
tag=['haskell']
category=['Haskell']
+++

In the comments on my post about <a href="http://www.markhneedham.com/blog/2012/05/08/haskell-generating-random-numbers/">generating random numbers</a> to test a function David Turner suggested that this was exactly the use case for which <a href="http://book.realworldhaskell.org/read/testing-and-quality-assurance.html">QuickCheck</a> was intended for so I've been learning a bit more about that this week.

I started with a simple property to check that the brute force (bf) and divide and conquer (dc) versions of the algorithm returned the same result, assuming that there were enough values in the list to have a closest pair:


~~~haskell

prop_closest_pairs xs = length xs >= 2 ==> dcClosest xs == (fromJust $ bfClosest xs)
~~~

I could then run that as follows:


~~~haskell

> import QuickCheck.Test
> quickCheck(prop_closest_pairs :: [(Double, Double)] -> Property)
~~~

It failed pretty quickly because the bf and dc versions of the algorithm sometimes return the pairs in a different order.

e.g. bf may say the closest pair is (2.0, 0.0), (2.1, 1.1) while dc says it's (2.1, 1.1), (2.0, 0.0) which will lead to the quick check property failing because those values aren't equal:


~~~haskell

> ((2.0, 0.0), (2.1, 1.1))  == ((2.1, 1.1), (2.0, 0.0))
False
~~~

The best way I could think of to get around this problem was to create a type to represent a pair of points and then write a custom equality operator.

I initially ended up with the following:


~~~haskell

type Point a = (a, a)
data Pair a = P (Point a) (Point a) 
~~~


~~~haskell

instance Eq (Pair a) where
	P a b == P c d = a == c && b == d || a == d && b == c
~~~

Which didn't actually compile:


~~~text

qc_test.hs:41:58:
    No instance for (Eq a)
      arising from a use of `=='
    In the second argument of `(&&)', namely `b == c'
    In the second argument of `(||)', namely `a == d && b == c'
    In the expression: a == c && b == d || a == d && b == c
~~~

The problem is that while we've made Pair an instance of the Equality type class there's no guarantee that the value contained inside it is an instance of the Equality type class which means we might not be able to compare its values.

We need to add a class constraint to make sure that <a href="http://learnyouahaskell.com/making-our-own-types-and-typeclasses#typeclasses-102">the value inside P is a part of Eq</a>:


~~~haskell

instance (Eq a) => Eq (Pair a) where
	P a b == P c d = a == c && b == d || a == d && b == c
~~~

Now we're saying that we want to make Pair an instance of the Equality type class but only when the value that Pair contains is already an instance of the Equality type class.

In this case we're just storing pairs of doubles inside the Pair so it will work fine.

Now if we compare the two points from above we'll see that they're equal:


~~~haskell

> P (2.0, 0.0) (2.1, 1.1)  == P (2.1, 1.1) (2.0, 0.0)
True
~~~

I had to go and change the existing code to make use of this new but it didn't take more than 5-10 minutes to do that.
