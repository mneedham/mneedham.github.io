+++
draft = false
date="2012-04-15 13:44:09"
title="Haskell: Reading in multiple lines of arguments"
tag=['haskell']
category=['Haskell']
+++

I've mostly avoided doing any I/O in Haskell but as <a href="https://code.google.com/codejam/contest/1460488/dashboard#s=p1">part of the Google Code Jam</a> I needed to work out how to read a variable number of lines as specified by the user.

The input looks like this:


~~~text

4
3 1 5 15 13 11
3 0 8 23 22 21
2 1 1 8 0
6 2 8 29 20 8 18 18 21
~~~

The first line indicates how many lines will follow. In this case we need to read in 4 lines.

The function to parse the input needed a type of 'IO [String]'. This was one of my first attempts:


~~~haskell

readInput = do
  line <- getLine
  let count :: Int
      count = read line
  return $ [getLine | x <- [1..count]]  
~~~

Unfortunately that doesn't have the correct signature:


~~~text

> :t readInput
readInput :: IO [IO String]
~~~

I thought I might be able to read the value from <cite>getLine</cite> and return a collection of those but that didn't even compile:


~~~haskell

readInput = do
  line <- getLine
  let count :: Int
      count = read line
  return $ [do line <- getLine; line | x <- [1..count]]   
~~~


~~~text

Couldn't match expected type `IO b0' with actual type `[Char]'
Expected type: IO b0
Actual type: String
  In the expression: line
  In the expression:
    do { line <- getLine;
         line }
~~~

I didn't really understand what the error message was saying so I removed the syntactic sugar that 'do' provides and replaced it with the equivalent function calls.


~~~haskell

readInput = do
  line <- getLine
  let count :: Int
      count = read line
  return $ [getLine >>= \line -> line | x <- [1..count]]   
~~~


~~~text

Couldn't match expected type `IO b0' with actual type `[Char]'
Expected type: IO b0
Actual type: String
In the expression: line
In the second argument of `(>>=)', namely `\ line -> line'
~~~

<cite>getLine</cite> returns us an IO Monad and '>>=' allows us to read a value from a Monad. However, it expects the function passed as its second argument to return a Monad which leaves us in the same problematic situation!


~~~haskell

readInput = do
  line <- getLine
  let count :: Int
      count = read line
  return $ [getLine >>= \line -> return line | x <- [1..count]] 
~~~


~~~text

> :t readInput
readInput :: IO [IO String]
~~~

I eventually came across <a href="http://stackoverflow.com/questions/9666034/haskell-replicatem-io">a StackOverflow post which covered similar ground</a> and used the <cite><a href="http://www.haskell.org/ghc/docs/latest/html/libraries/base/Control-Monad.html#v:replicateM">replicateM</a></cite> function to solve the problem.


~~~text

> :t replicateM
replicateM :: Monad m => Int -> m a -> m [a]
~~~

This is the function I ended up with:


~~~haskell

readInput :: IO [String]
readInput = do
  line <- getLine
  let count :: Int
      count = read line
  lines <- replicateM (count) $ do
    line <- getLine
    return line
  return lines 
~~~

If we wanted to print the arguments back to the user we could define our main function like so:


~~~haskell

main = do
       lines <- readInput
       mapM_ (\(idx, line) -> putStrLn $ "Arg #" ++ show idx ++ " " ++ line) (zip [1..] lines)
~~~


~~~text

> ./google_code_jam         
2
Mark
Needham
Arg #1 Mark
Arg #2 Needham
~~~
