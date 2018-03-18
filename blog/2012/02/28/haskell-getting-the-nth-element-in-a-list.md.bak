+++
draft = false
date="2012-02-28 00:02:21"
title="Haskell: Getting the nth element in a list"
tag=['haskell']
category=['Haskell']
+++

I started trying to solve some of the <a href="http://projecteuler.net/problems">Project Euler problems</a> as a way to learn a bit of Haskell and <a href="http://projecteuler.net/problem=7">problem 7</a> is defined like so:

<blockquote>
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
</blockquote>

I read that the <a href="http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes">Sieve of Eratosthenes</a> is a useful algorithm for working out all the prime numbers and there's <a href="http://en.literateprograms.org/Sieve_of_Eratosthenes_(Haskell)#chunk use:primes_naive">a page on the Literate Programs wiki explaining how to derive them using it</a>.

The most naive implementation of all the primes ends up reading like this:


~~~haskell

primes = 2 : sieve [3,5..]  where
    sieve []     = []
    sieve (p:xs) = p : sieve (xs `minus` [p,p+2*p..])
~~~

That gives an infinite sequence of all the prime numbers but I wanted to be able to specifically pick the 10,001st prime number which I assumed would be named 'nth' or something like that.

As it turns out we actually need to use the '!!' operator which I found out from <a href="http://scienceblogs.com/goodmath/2009/11/writing_basic_functions_in_has.php">Mark Chu-Carroll's blog post</a>:


~~~haskell

*Main> :t (!!)
(!!) :: [a] -> Int -> a
~~~


~~~haskell

problem_7 = primes !! 10000 -- 0 indexed so we need to get the position one before 10,001
~~~

It takes a while to run but we end up with the answer:


~~~haskell

*Main> problem_7
104743
~~~
