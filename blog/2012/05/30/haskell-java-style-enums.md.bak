+++
draft = false
date="2012-05-30 11:10:15"
title="Haskell: Java Style Enums"
tag=['haskell']
category=['Haskell']
+++

I've been playing around with <a href="http://projecteuler.net/problem=31">problem 31 of Project Euler</a> which is defined as follows:

<blockquote>
In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).

It is possible to make £2 in the following way:

1 £1 + 150p + 220p + 15p + 12p + 31p

How many different ways can £2 be made using any number of coins?
</blockquote>

Having coded way too much in Java my first thought was that the coins could be represented as an Enum but I wasn't sure how to do that in Haskell.

As it turns out <a href="http://stackoverflow.com/questions/6000511/better-way-to-define-an-enum-in-haskell">the question has been asked on Stack Overflow</a> and there's an Enum type class we can implement to achieve the same thing.

In this case:


~~~haskell

data UKCoin = OnePence | TwoPence | FivePence | TenPence | TwentyPence | FiftyPence | OnePound | TwoPounds 
              deriving (Eq, Show)
~~~


~~~haskell

instance Enum UKCoin where
    fromEnum = fromJust . flip lookup table
    toEnum = fromJust . flip lookup (map swap table)
table = [(OnePence, 1), (TwoPence, 2), (FivePence, 5), (TenPence, 10), (TwentyPence, 20), 
         (FiftyPence, 50), (OnePound, 100), (TwoPounds, 200)]
~~~

If we want to get the monetary value of a coin we use 'fromEnum':


~~~haskell

> fromEnum TwoPounds
200
~~~

And if we wanted to go back to the enum value we'd do this:


~~~haskell

> (toEnum 200) :: UKCoin
TwoPounds
~~~

If we want to get a list of all the instances of 'UKCoin' we can just do a map over 'table':


~~~haskell

> let ukCoins = map fst table
> ukCoins
[OnePence,TwoPence,FivePence,TenPence,TwentyPence,FiftyPence,OnePound,TwoPounds]
~~~
