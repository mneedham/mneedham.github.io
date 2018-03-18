+++
draft = false
date="2012-04-28 17:39:54"
title="Haskell: Int and Integer"
tag=['haskell']
category=['Haskell']
+++

In my <a href="http://www.markhneedham.com/blog/2012/04/25/algorithms-rabin-karp-in-haskell/">last post about the Rabin Karp algorithm</a> I mentioned that I was having some problems when trying to write a hash function which closely matched its English description.

<blockquote>
((rm-1 * ascii char) + (rm-2 * ascii char) + … (r0 * ascii char)) % q
where r = 256, q = 1920475943
</blockquote>

This is my current version of the hash function:


~~~haskell

hash = hash' globalR globalQ
hash' r q string m = foldl (\acc x -> (r * acc + ord x) `mod` q) 0 $ take m string
~~~

And my initial attempt to write the alternate version was this:


~~~haskell

hash2 :: [Char] -> Int -> Int
hash2 = hash2' globalR  globalQ	
hash2' r q string m = (flip mod q . sum . map (\(pow, char) -> ord char *  (r ^ pow)) . zip [m-1, m-2..0]) string
~~~

Unfortunately this version breaks down as we try to create hashes for bigger lists of characters:


~~~text

> hash "markusaere" 10
849698536
~~~


~~~text

> hash2 "markusaere" 10
1239828806
~~~

We can see what's going on if we execute the core bit of the hash function in the REPL:


~~~haskell

> map (\(pow, char) -> ord char * 256 ^ pow) $ zip [9, 8..0] "markusaere"
[0,0,8214565720323784704,30117822508040192,128642860449792,493921239040,1627389952,6619136,29184,101]
~~~

In this case the hash value for the first character is:


~~~haskell

> 256 ^ 9 * ord 'm'
0
~~~

Be default if we do calculations on integers the '<a href="http://en.wikibooks.org/wiki/Haskell/A_Miscellany_of_Types#Integers">Int</a>' type is used:

<blockquote>
"Int" is the more common 32 or 64 bit integer. Implementations vary, although it is guaranteed to be at least 30 bits.
</blockquote>

The maximum value a 64 bit Int can hold is 2<sup>63</sup>, a value that we're exceeding with the first two calculations in our list. 

Since our calculation has exceeded the maximum value of a 64 bit integer we need to <a href="http://www.haskell.org/tutorial/numbers.html">coerce</a> our calculation to use the 'Integer' type which has arbitrary precision up to the limit of the machine's memory.

We can use the 'toInteger' function to do this:


~~~haskell

> toInteger (256 ^ 9) * toInteger (ord 'm')
514737946632791328292864
~~~

We can change the core of the function to use 'toInteger' like so:


~~~haskell

> map (\(pow, char) -> toInteger (ord char) * 256 ^ pow) $ zip [9, 8..0] "markusaere"
[514737946632791328292864,1789334175149826506752,8214565720323784704,30117822508040192,128642860449792,493921239040,1627389952,6619136,29184,101]
~~~

We can then change the hash function to read like this:


~~~haskell

hash2 :: [Char] -> Int -> Int
hash2 value m = fromInteger $ hash2' (toInteger globalR) (toInteger globalQ) value m
	
hash2' :: Integer -> Integer -> [Char] -> Int -> Integer
hash2' r q string m = (sum $ map (\(pow, char) -> toInteger (ord char) *  toInteger (r ^ pow)) $ zip [m-1, m-2..0] string) `mod` q
~~~

When we call the function with the original parameters it now returns the correct answer:


~~~text

> hash2 "markusaere" 10
849698536
~~~
