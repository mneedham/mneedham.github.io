+++
draft = false
date="2012-12-31 22:27:15"
title="Haskell: Strictness and the monadic bind"
tag=['haskell']
category=['Haskell']
+++

<p>As I mentioned towards the end of my post about <a href="http://www.markhneedham.com/blog/2012/12/31/haskell-an-impressively-non-performant-union-find/">implementing the union find data structure in Haskell</a> I <a href="https://github.com/mneedham/algorithms2/blob/master/MutableLeaders.hs">wrote another version</a> using a mutable array and having not seen much of a performance improvement started commenting out code to try and find the problem.</p>


<p>I eventually narrowed it down to the <cite>union</cite> function which was defined like so:</p>



~~~haskell

union :: IO (IOArray Int Int) -> Int -> Int -> IO (IOArray Int Int)
union arrayContainer x y = do
    actualArray <- arrayContainer
    ls <- getAssocs actualArray
    leader1 <- readArray actualArray x
    leader2 <- readArray actualArray y
    let newValues = (map (\(index, value) -> (index, leader1)) . filter (\(index, value) -> value == leader2)) ls
    sequence $ map (\(idx, val) -> writeArray actualArray idx val) newValues
    return actualArray   
~~~

<p>I was using Unix's <cite><a href="http://en.wikipedia.org/wiki/Time_(Unix)">time</a></cite> function to get the execution time since this meant I didn't need to make any changes to the program and this level of granularity was ok.</p>


<p>The first time I ran the program it executed in 36.379 seconds and my first hunch was that a lot of time was being taken up writing to the array so I commented out that line:</p>



~~~haskell

union :: IO (IOArray Int Int) -> Int -> Int -> IO (IOArray Int Int)
union arrayContainer x y = do
    actualArray <- arrayContainer
    ls <- getAssocs actualArray
    leader1 <- readArray actualArray x
    leader2 <- readArray actualArray y
    let newValues = (map (\(index, value) -> (index, leader1)) . filter (\(index, value) -> value == leader2)) ls
    -- sequence $ map (\(idx, val) -> writeArray actualArray idx val) newValues
    return actualArray  
~~~

<p>The execution time decreased to 33.381 seconds so the writing of the array was actually only a small part of the total execution time.</p>


<p>I thought it was quite strange that it was taking so long to execute since things are generally lazily evaluated in Haskell and my assumption was that <cite>newValues</cite> wasn't being evaluated since I hadn't used it anywhere. I decided to comment that out to see what difference it would make:</p>



~~~haskell

union :: IO (IOArray Int Int) -> Int -> Int -> IO (IOArray Int Int)
union arrayContainer x y = do
    actualArray <- arrayContainer
    ls <- getAssocs actualArray
    leader1 <- readArray actualArray x
    leader2 <- readArray actualArray y
    -- let newValues = (map (\(index, value) -> (index, leader1)) . filter (\(index, value) -> value == leader2)) ls
    -- sequence $ map (\(idx, val) -> writeArray actualArray idx val) newValues
    return actualArray 
~~~

<p>The execution time was now 33.579 seconds so commenting out that line hadn't actually made any difference. I assumed <cite>ls</cite> wasn't being evaluated since it isn't being used but I thought I'd better check:</p>



~~~haskell

union :: IO (IOArray Int Int) -> Int -> Int -> IO (IOArray Int Int)
union arrayContainer x y = do
    actualArray <- arrayContainer
    -- ls <- getAssocs actualArray
    leader1 <- readArray actualArray x
    leader2 <- readArray actualArray y
    -- let newValues = (map (\(index, value) -> (index, leader1)) . filter (\(index, value) -> value == leader2)) ls
    -- sequence $ map (\(idx, val) -> writeArray actualArray idx val) newValues
    return actualArray  
~~~

<p>The execution time now reduced to 3.882 seconds thereby suggesting that <cite><a href="http://hackage.haskell.org/packages/archive/array/0.2.0.0/doc/html/Data-Array-MArray.html#v%3AgetAssocs">getAssocs</a></cite> was being strictly evaluated. </p>


<p>We are doing what's called a monadic bind which (at least) <a href="http://www.haskell.org/ghc/docs/7.2.2/html/users_guide/interactive-evaluation.html">within GHCI is strictly evaluated</a> but <a href="http://www.haskell.org/haskellwiki/What_a_Monad_is_not">isn't necessarily evaluated like this everywhere else</a>:</p>


<blockquote>
Monad operations (bind and return) have to be non-strict in fact, always! However other operations can be specific to each monad. For instance some are strict (like IO), and some are non-strict (like []).
</blockquote>

<p>From my observations it would seem that the <cite>IOArray</cite> is one of those monads which evaluates bind strictly.</p>


<p>I tried looking at the Haskell source code to see if I could find any code to prove what I'd observed but I'm not entirely sure what I should be looking for!</p>

