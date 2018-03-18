+++
draft = false
date="2012-03-31 22:49:18"
title="Haskell: Pattern matching data types with named fields"
tag=['haskell']
category=['Haskell']
+++

One of my favourite things about coding in Haskell is that I often end up pattern matching against data types.

I've been playing around with modelling cars coming into and out from a car park and changing the state of the car park accordingly.

I started with these data type definitions:


~~~haskell

data CarParkState = Available Bool Int Int | AlmostFull Bool Int Int | Full Bool Int deriving (Show)
data Action = Entering | Leaving deriving (Show) 
data Sticker = Handicap | None deriving (Show) 
~~~

which were used in the following function:


~~~haskell

car_park_state :: CarParkState -> (Action, Sticker) -> CarParkState
car_park_state (Available _ 8 handicap) (Entering, None) = AlmostFull True 9 handicap
car_park_state (AlmostFull _ 11 handicap) (Entering, None) = Full True handicap
car_park_state (AlmostFull _ 9 handicap) (Leaving, None) = Available True 8 handicap

-- there are more states but I've cut them for brevity
~~~

This code isn't too bad but it's not obvious what the numbers '8', '11' and '9' are referring to without scrolling back up to the data type definition and checking.

By coincidence I came across a <a href="http://en.wikibooks.org/wiki/Haskell/More_on_datatypes">Haskell data types wiki page</a> which introduced me to the concept of named fields.

This means that rather than referring to the arguments of a data type by position we can give them a name instead:


~~~haskell

data CarParkState = Available  { changed :: Bool, normalSpaces :: Int, handicapSpaces :: Int } | 
                    AlmostFull { changed :: Bool, normalSpaces :: Int, handicapSpaces :: Int } | 
                    Full       { changed :: Bool, handicapSpaces :: Int } deriving (Show)
~~~

The <cite>car_park_state</cite> function now reads like this:


~~~haskell

car_park_state :: CarParkState -> (Action, Sticker) -> CarParkState
car_park_state state@(Available  {normalSpaces=8})  (Entering, None) = AlmostFull True 9 (handicapSpaces state)
car_park_state state@(AlmostFull {normalSpaces=11}) (Entering, None) = Full True (handicapSpaces state)
car_park_state state@(AlmostFull {normalSpaces=9})  (Leaving, None)  = Available True 8 (handicapSpaces state)
~~~

There's more code in this solution than the original although to me <cite>car_park_state</cite> is clearer since you can tell what it's doing just by glancing at the code.

I'm not sure which of these approaches is considered idiomatic Haskell but my feeling is that it's probably the former since it's more concise.

On the other hand, the value of named fields goes up as the total number of parameters in a data types increases since people will find it increasingly difficult to remember which parameter is in each position.
