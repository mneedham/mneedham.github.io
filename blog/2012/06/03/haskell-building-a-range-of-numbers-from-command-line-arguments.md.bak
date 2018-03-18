+++
draft = false
date="2012-06-03 20:13:54"
title="Haskell: Building a range of numbers from command line arguments"
tag=['haskell']
category=['Haskell']
+++

I'm working through some of the <a href="http://mitpress.mit.edu/sicp/">SICP problems</a> in Haskell and for <a href="http://www.billthelizard.com/2010/02/sicp-exercise-122-timed-prime-test.html">problem 1.22</a> you need to write a function which will indicate the first 3 prime numbers above a starting value.

It is also suggested to only consider odd numbers so to find the prime numbers above 1000 the function call would look like this:


~~~haskell

> searchForPrimes [1001,1003..]
[1009,1013,1019]
~~~

I wanted to be able to feed in the range of numbers from the command line so that I'd be able to call the function with different values and see how long it took to work it out.

I initially tried passing the above array to the program as a command line argument wrapped in a string and then parse it using <cite>read</cite> which works if you provide a complete array:


~~~haskell

> read "[1,2]" :: [Int]
[1,2]
~~~

But not so well for ranges:


~~~haskell

> read "[1,2..]" :: [Int]
*** Exception: Prelude.read: no parse
~~~

Instead I thought I could just provide the first two values for the proposed range and then work from there.

To help me do this I came across the <cite>enumFromThen</cite> function which has the following signature:


~~~haskell

> :t enumFromThen
enumFromThen :: Enum a => a -> a -> [a]
~~~

From the Haskell source this function seems to call the literal range syntax which I mentioned above:


~~~haskell

enumFromThen x y = map toEnum [fromEnum x, fromEnum y ..]
~~~

I was actually expecting there to be a literal range syntax definition which made a call to the various enumFrom... methods since the literal syntax seems more like <a href="http://en.wikibooks.org/wiki/Haskell/Syntactic_sugar">syntactic sugar</a> on top of the function call approach but apparently not!

I use it like this:


~~~haskell

main = do
  args <- getArgs
  let (first:second:_) = map read args in 
    putStrLn $ show $ searchForPrimes (enumFromThen first second)
~~~

Which I suppose could just as easily be written like this:


~~~haskell

main = do
  args <- getArgs
  let (first:second:_) = map read args in 
    putStrLn $ show $ searchForPrimes ([first, second..])   
~~~

And I've gone full circle!
