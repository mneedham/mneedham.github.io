+++
draft = false
date="2012-03-20 23:55:51"
title="Haskell: Newbie currying mistake"
tag=['haskell']
category=['Haskell']
+++

As I <a href="http://www.markhneedham.com/blog/2012/03/20/haskell-chaining-functions-to-find-the-middle-value-in-a-collection/">mentioned in my last post</a> I've spent a bit of this evening writing a merge sort function and one of the mistakes I made a few times was incorrectly passing arguments to the recursive calls of 'merge'.

For example, this is one of the earlier versions of the function:


~~~haskell

middle :: [Int] -> Int
middle = floor . (\y -> y / 2) .  fromIntegral . length	
msort :: [Int] -> [Int]
msort unsorted = 	
  let n = middle unsorted
  in 
    if n == 0 then unsorted 
    else  
      let (left, right) = splitAt n unsorted
      in merge (msort left) (msort right)
  where 
    merge [] right = right
    merge left [] = left
    merge left@(x:xs) right@(y:ys) = if x < y then x : merge(xs, right) else y : merge (left, ys)
~~~

Which doesn't actually compile:


~~~text

    Couldn't match expected type `[a0]' with actual type `[a0] -> [a0]'
    In the return type of a call of `merge'
    In the second argument of `(:)', namely `merge (xs, right)'
    In the expression: x : merge (xs, right)
~~~

My defence for this mistake is that many of the other languages I've programmed in take function parameters separated by a comma but in this case I've actually only succeeded in currying the 'merge' function.

i.e. it thinks I only wanted to pass one value to it and return a function, hence the error message!

One correction would be to change the code to read like this so we can explicitly see that a function which takes 2 arguments can be called with each argument separately:


~~~haskell

msort :: [Int] -> [Int]
msort unsorted = 	
  let n = middle unsorted
  in 
    if n == 0 then unsorted 
    else  
      let (left, right) = splitAt n unsorted
      in merge (msort left) (msort right)
  where 
    merge [] right = right
    merge left [] = left
    merge left@(x:xs) right@(y:ys) = if x < y then x : merge(xs)(right) else y : merge (left)(ys)
~~~

We can do exactly the same with the '/' function to use a simpler example:


~~~haskell

-- a long way of dividing 2 by 3
> ((/) 2) 3
0.6666666666666666
~~~

The type of '/' is:


~~~haskell

> :t (/)
(/) :: Fractional a => a -> a -> a
~~~

which means it takes in a 'Fractional' and then returns a function which takes in a 'Fractional' and returns a 'Fractional'. 

In Haskell <a href="http://stackoverflow.com/questions/4768453/type-signature-vs-function-equation-in-haskell">function application is left associative</a> which means that  'f x y' is the same as '(f x) y' so we can omit the parentheses and pass both arguments together:


~~~haskell

> (/) 2 3
0.6666666666666666
~~~

And we can do the same thing in the merge sort of course:


~~~haskell

msort :: [Int] -> [Int]
msort unsorted = 	
  let n = middle unsorted
  in 
    if n == 0 then unsorted 
    else  
      let (left, right) = splitAt n unsorted
      in merge (msort left) (msort right)
  where 
    merge [] right = right
    merge left [] = left
    merge left@(x:xs) right@(y:ys) = if x < y then x : merge xs right else y : merge left ys 
~~~

A fairly simple mistake to make but it had me confused for a while!

------

Updated the explanation around how we can pass arguments to '/' after my colleague <a href="https://twitter.com/#!/gavri">Gavri</a> <a href="https://twitter.com/#!/gavri/status/182331266681671680">pointed out that the initial explanation was incorrect</a>.
