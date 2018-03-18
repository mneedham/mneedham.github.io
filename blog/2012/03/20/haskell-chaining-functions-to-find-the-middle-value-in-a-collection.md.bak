+++
draft = false
date="2012-03-20 23:36:03"
title="Haskell: Chaining functions to find the middle value in a collection"
tag=['haskell']
category=['Haskell']
+++

I've been playing around with writing merge sort in Haskell and eventually ended up with the following function:


~~~haskell

msort :: [Int] -> [Int]
msort unsorted = 	
  let n = floor (fromIntegral(length unsorted) / 2)
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

The 3rd line was annoying me as it has way too many brackets on it and I was fairly sure that it should be possible to just combine the functions <a href="http://www.markhneedham.com/blog/2009/01/12/f-partial-function-application-with-the-function-composition-operator/">like I learnt to do in F# a few years ago</a>.

It's pretty easy to do that for the first two functions 'length' and 'fromIntegral' which we can do like this:


~~~haskell

middle = fromIntegral . length
~~~

The third line now reads like this:


~~~haskell

let n = floor ((middle unsorted) / 2)
~~~

It's a slight improvement but still not that great. 

The problem with working out how to chain the division bit is that our value needs to be passed as the first argument to '/' so we can't do the following...


~~~haskell

middle = ((/) 2) . fromIntegral . length
~~~

...since that divides 2 by the length of our collection rather than the other way around!


~~~haskell

> middle [1,2,3,4,5,6]
0.3333333333333333
~~~

Instead we want to create an anonymous function around the '/' function and then apply floor:


~~~haskell

middle :: [Int] -> Int
middle = floor . (\y -> y / 2) .  fromIntegral . length
~~~

And merge sort now looks like this:


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

Which I think is pretty neat!
