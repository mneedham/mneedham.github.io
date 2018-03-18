+++
draft = false
date="2012-05-30 12:08:25"
title="Haskell: Using type classes to generify Project Euler #31"
tag=['haskell']
category=['Haskell']
+++

As I mentioned in my previous post I've been working on <a href="http://www.markhneedham.com/blog/2012/05/30/haskell-java-style-enums/">Project Euler #31</a> and initially wasn't sure how to write the algorithm.

I came across <a href="http://stackoverflow.com/questions/1106929/find-all-combinations-of-coins-when-given-some-dollar-value">a post on StackOverflow which explained it in more detail</a> but unfortunately the example used US coins rather than UK ones like in the Project Euler problem.

To start with I created two versions of the function - one for US coins and one for UK coins:


~~~haskell

combinations :: Int -> [USCoin] -> [USCoin] -> [[USCoin]]
combinations 0 current _ = [current]
combinations _  current [] = []
combinations total p (c:cs) = concatMap (\ times -> combinations (total - (times * fromEnum c)) (p ++ replicate times c) cs) 
                                        [0,1..(total `div` fromEnum c)] 
~~~


~~~haskell

combinationsUK :: Int -> [UKCoin] -> [UKCoin] -> [[UKCoin]]
combinationsUK 0 current _ = [current]
combinationsUK _  current [] = []
combinationsUK total p (c:cs) = concatMap (\ times -> combinationsUK (total - (times * fromEnum c)) (p ++ replicate times c) cs) 
                                          [0,1..(total `div` fromEnum c)] 
~~~

As we can see the only difference between the two functions is the type being passed around and they are almost identical as well:


~~~haskell

data USCoin = Quarter | Dime | Nickel | Penny deriving (Eq, Show)
~~~


~~~haskell

instance Enum USCoin where
    fromEnum = fromJust . flip lookup usTable
    toEnum = fromJust . flip lookup (map swap usTable)
usTable = [(Quarter, 25), (Dime, 10), (Nickel, 5), (Penny, 1)]
~~~



~~~haskell

data UKCoin = OnePence | TwoPence | FivePence | TenPence | TwentyPence | FiftyPence | OnePound | TwoPounds deriving (Eq, Show) 
~~~


~~~haskell

instance Enum UKCoin where
    fromEnum = fromJust . flip lookup ukTable
    toEnum = fromJust . flip lookup (map swap ukTable)
ukTable = [(OnePence, 1), (TwoPence, 2), (FivePence, 5), (TenPence, 10), 
           (TwentyPence, 20), (FiftyPence, 50), (OnePound, 100), (TwoPounds, 200)]
~~~

We can run those two functions like this:


~~~haskell

> length $ combinations 200 [] (reverse $ map fst usTable)
1463

> length $ combinationsUK 200 [] (reverse $ map fst ukTable)
73682
~~~

After spending a lot of the past week reading about type classes I figured we could probably make use of one here so I created a 'Coin' type class:


~~~haskell

class Coin a where 
  value :: a -> Int
~~~

And then implemented that with 'USCoin' and 'UKCoin':


~~~haskell

instance Coin USCoin where value coin = fromEnum coin
instance Coin UKCoin where value coin = fromEnum coin
~~~

Then we need to make some small adjustments to 'combinations' to make it work with 'Coin' instead:


~~~haskell

combinations :: (Coin a) => Int -> [a] -> [a] -> [[a]]
combinations 0 current _ = [current]
combinations _  current [] = []
combinations total p (c:cs) = 
  concatMap (\ times -> combinations (total - (times * value c)) (p ++ replicate times c) cs) 
            [0,1..(total `div` value c)] 
~~~

Instead of calling 'fromEnum' we call 'value' and the function can now be used with any types which implement the Coin type class should we wish to do that.

We can actually go even further and get rid of our Enum type class instances and just put that code onto the Coin type class:


~~~haskell

class Eq a => Coin a where 
  table :: [(a, Int)]

  value :: a -> Int
  value = fromJust . flip lookup table
~~~


~~~haskell

instance Coin USCoin where 
  table = [(Quarter, 25), (Dime, 10), (Nickel, 5), (Penny, 1)]	

instance Coin UKCoin where 
  table = [(OnePence, 1), (TwoPence, 2), (FivePence, 5), (TenPence, 10), (TwentyPence, 20), (FiftyPence, 50), (OnePound, 100), (TwoPounds, 200)]
~~~

We can then call the function with either of those coins:


~~~haskell

> length $ combinations 200 [] (reverse $ map fst (table :: [(USCoin, Int)]))
1463

> length $ combinations 200 [] (reverse $ map fst (table :: [(UKCoin, Int)]))
73682
~~~
