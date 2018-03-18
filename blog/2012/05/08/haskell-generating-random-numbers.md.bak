+++
draft = false
date="2012-05-08 22:09:17"
title="Haskell: Generating random numbers"
tag=['haskell']
category=['Haskell']
+++

As I <a href="http://www.markhneedham.com/blog/2012/05/07/haskell-maximum-int-value/">mentioned in my last post</a> I've been coding the closest pairs algorithm in Haskell and needed to create some pairs of coordinates to test it against.

I've tried to work out how to create lists of random numbers in Haskell before and always ended up giving up because it seemed way more difficult than it should be but this time I came across a <a href="http://stackoverflow.com/questions/2110535/sampling-sequences-of-random-numbers-in-haskell">really good explanation of how to do it by jrockway on Stack Overflow</a>.

I thought it'd be interesting to work up to his answer by first looking at the functions available to help us generate random numbers.

<a href="http://hackage.haskell.org/packages/archive/random/latest/doc/html/System-Random.html#v:mkStdGen">mkStdGen</a> is a function which creates a random number generator for a given seed value and seems like a good place to start.

<blockquote>
mkStdGen :: Int -> StdGen


The function mkStdGen provides an alternative way of producing an initial generator, by mapping an Int into a generator. Again, distinct arguments should be likely to produce distinct generators.
</blockquote>

We can combine that with 'randomR' to give us a random value in a range that we choose or with 'random' to get a random value in a default range.

<blockquote>
randomR :: RandomGen g => (a, a) -> g -> (a, g)


Takes a range (lo,hi) and a random number generator g, and returns a random value uniformly distributed in the closed interval [lo,hi], together with a new generator. It is unspecified what happens if lo>hi. For continuous types there is no requirement that the values lo and hi are ever produced, but they may be, depending on the implementation and the interval.
</blockquote>


~~~haskell

> fst $ randomR (1,10) (mkStdGen 66)
8
~~~


~~~haskell

> let randomNumber :: Int; x = fst $ random (mkStdGen 66)
> randomNumber
-4755267682593970340
~~~

For now I'm ignoring the new random generator that is provided as the second part of the tuple that these two functions return.

If we want to create an infinite list of random numbers then something like this will do the trick:


~~~haskell

let values :: [Int]; values = map fst $ scanl (\(r, gen) _ -> random gen) (random (mkStdGen 1)) $ repeat ()
~~~

We use the 'repeat' function to create an infinite sequence of nothing then run a scanl across that infinite sequence, called 'random' with a new instance of the random number generator each time:


~~~haskell

> take 10 values
[7917908265643496962,-1017158127812413512,-1196564839808993555,128524678767915218,3573078269730797745,-2026762924287790163,-5402471397730582264,-8620480566299071809,5987841344909700899,1198540087579679591]
it :: [Int]
~~~

In this version we're passing the next generator along as part of the accumulator of the 'scanl' function but another way to do that would be to encapsulate it inside a State monad:

Using the State monad our random number function would read like this:


~~~haskell

myRand :: State StdGen Int
myRand = do
	gen <- get
	let (r, nextGen) = random gen
	put nextGen
	return r
~~~

The state monad contains some state (the random number generator) and creates values (the random numbers). 

Line 3 gets the current generator.
Line 4 creates a new number and generator which it assigns to 'r' and 'nextGen'
Line 5 updates the State monad with the new generator
Line 6 returns the value that was created.

We change 'values' to read like this:


~~~haskell

let values = mapM (\_ -> myRand) $ repeat ()
~~~

'mapM (\_ -> myRand)' is <a href="http://www.haskell.org/ghc/docs/6.12.2/html/libraries/base-4.2.0.1/Control-Monad.html#v%3Asequence">the same as</a> doing 'sequence $ map (\_ -> myRand)' and we need to do that because we want to return a State Monad with an array of Ints rather than an array of State Monads each with an Int.

In order to evaluate those values we call 'evalState' which returns the final result from the State monad i.e. the random value created:


~~~haskell

> evalState values $ mkStdGen 1
[7917908265643496962,-1017158127812413512,-1196564839808993555,128524678767915218,3573078269730797745,-2026762924287790163,-5402471397730582264,-8620480566299071809,5987841344909700899,1198540087579679591,5081506216124746781,-2413363174299075397,-6804412472718217891,4559850124463334118,-362777938400029309,-23100237439495333,-2426472460098089322,...]
~~~

In our case we want to get an infinite sequence of pairs to represent the coordinates on a plane so we need to have a random function that creates those:


~~~haskell

myRandPair :: State StdGen (Int, Int)
myRandPair = do
	x <- myRand
	y <- myRand
	return (x, y)	
~~~

We then change 'values' accordingly:


~~~haskell

> let values = mapM (\_ -> myRandPair) $ repeat ()
> evalState values $ mkStdGen 1
[(7917908265643496962,-1017158127812413512),(-1196564839808993555,128524678767915218),(3573078269730797745,-2026762924287790163),(-5402471397730582264,-8620480566299071809),(5987841344909700899,1198540087579679591),(5081506216124746781,-2413363174299075397),(-6804412472718217891,4559850124463334118),(-362777938400029309,-23100237439495333)...]
~~~

If we want to get back some different pairs then we just need to change the initial seed value that we pass to 'mkStdGen'.

<a href="http://stackoverflow.com/questions/2110535/sampling-sequences-of-random-numbers-in-haskell">jrockway explains this in more detail in his post</a>  in which he also wraps the State monad inside an alias to make the code easier to understand.
