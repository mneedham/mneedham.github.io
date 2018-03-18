+++
draft = false
date="2012-04-25 21:28:42"
title="Algorithms: Rabin Karp in Haskell"
tag=['haskell', 'algorithms']
category=['Haskell', 'Algorithms']
+++

I recently came across <a href="http://java.dzone.com/articles/algorithm-week-rabin-karp">a blog post describing the Rabin Karp algorithm</a> - an algorithm that uses hashing to find a pattern string in some text - and thought it would be interesting to try and write a version of it in Haskell.

This algorithm is typically used when we want to search for multiple pattern strings in a text e.g. when detecting plagiarism or a primitive way of detecting code duplication but my initial version only lets your search for one pattern.

<blockquote>
For text of length n and p patterns of combined length m, its average and best case running time is O(n+m) in space O(p), but its worst-case time is O(nm)
</blockquote>


~~~text

function RabinKarp(string s[1..n], string sub[1..m])
    hsub := hash(sub[1..m]);  hs := hash(s[1..m])
    for i from 1 to n-m+1
        if hs = hsub
            if s[i..i+m-1] = sub
                return i
        hs := hash(s[i+1..i+m])
    return not found
~~~

On line 2 we compute the initial hash value for the pattern and for the first <cite>m</cite> characters of the text where <cite>m</cite> represents the number of characters in the pattern.

We then work through the text comparing the pattern hash with our current version of the text hash each time. 

If they match then we check that the characters in those positions also match, since two different strings can hash to the same value, and if they do then we're done.

Line 7 is the interesting line because if we recalculate the hash from scratch each time then it will take O(m) time which means the whole algorithm will take O(nm) time since it's called in a loop.

We therefore need to use a <a href="http://en.wikipedia.org/wiki/Rolling_hash">rolling hash</a> which will allow us to work out the value of the next hash from the current one.

For example if we're searching for a three letter pattern in the text 'markus' then on our first iteration of the loop we'll have <cite>hash("mar")</cite> and on the second iteration we need to work out <cite>hash("ark")</cite>.

The hash of "mar" already contains the hash value of "ar" so we need to remove the hash value of the "m" and then add the hash value of "k" to get our new hash value.

I used <a href="http://algs4.cs.princeton.edu/53substring/RabinKarp.java.html">this Java version of the algorithm</a> as a template.

This is the main function:


~~~haskell

import Data.Char
import Data.List
import Data.Maybe

rabinKarp :: String -> String -> Int
rabinKarp text pattern = 
	if pattern == "" then -1 
	else fromMaybe (-1) $ mapOnMaybe fst $ find matchingString $ zip [0..] $ scanl nextHash (hash text m) $ windowed (m+1) text					
	where n = length text
	      m = length pattern	      
	      nextHash currentHash chars = reHash currentHash (head chars) (last chars) m
	      matchingString (offset, textHash) = hash2 pattern m == textHash && pattern == subString text offset m
~~~

I applied the <a href="http://www.markhneedham.com/blog/2012/02/28/haskell-creating-a-sliding-window-over-a-collection/">windowed function</a> to the text to break it down into a collection of smaller strings which included the next character that we would need to look at.

e.g. if we were searching for a 3 character pattern in "markusauerelius" then this would be the collection of values we iterate over.


~~~haskell

windowed 4 "markusauerelius"
["mark","arku","rkus","kusa","usau","saue","auer","uere","erel","reli","eliu","lius"]
~~~

I then use scanl to apply a reduction over that collection, passing in the hash of the previous 3 characters each time in this example. I used scanl instead of foldl so that I could see the value of the hash on each iteration rather than only at the end.

Next I use a zip to get the indexes of each letter in the text and then I look for the first entry in the collection which matches the pattern hash and has the same sequence of characters.

The <cite>mapToMaybe</cite> is used to grab the index of the match and then we return a '-1' if there is no match in the last bit of the line.

I'm assuming that scanl is lazily evaluated and in this case will therefore only evaluate up to where a match is found - if that assumption's wrong then this version  of Rabin Karp is very inefficient!

The <cite>hash</cite> and <cite>reHash</cite> functions referenced above are defined like so:


~~~haskell

globalQ = 1920475943
globalR = 256

hash = hash' globalR globalQ
hash' r q string m = foldl (\acc x -> (r * acc + ord x) `mod` q) 0 $ take m string
~~~


~~~haskell

> hash "markusaerelius" 3
7168370
~~~

Written in English this is the definition of the hash function:

<blockquote>
((r<sup>m-1</sup> * ascii char) + (r<sup>m-2</sup> * ascii char) + ... (r<sup>0</sup> * ascii char)) % q
where r = 256, q = 1920475943
</blockquote>

Which translates to the following in Haskell:

<blockquote>
((256<sup>2</sup> * ord 'm') + (256<sup>1</sup> * ord 'a') + (256<sup>0</sup> * ord 'r')) `mod` 1920475943
</blockquote>

I was having trouble with casting bigger values when I wrote a function which described this more explicitly which is why the current 'hash' function   applies the modulo function on each iteration.

The <cite>reHash</cite> function is defined like this:


~~~haskell

reHash = reHash' globalR globalQ
reHash' r q existingHash firstChar nextChar m = 
	(takeOffFirstChar `mod` fromIntegral q * fromIntegral r + ord nextChar) `mod` fromIntegral q
	where 
		rm = if m >0 then (fromIntegral r ^ fromIntegral (m-1)) `mod` fromIntegral q else 0
		takeOffFirstChar = existingHash - fromIntegral rm * ord firstChar
~~~

In English: 

<blockquote>
reHash = ((existingHash - ((r<sup>m-1</sup> % q) * ascii firstChar)) % q + (r * ascii nextChar)) % q
</blockquote>

First we remove the hash of the first character - which has a value of 'r<sup>m-1</sup> * ascii char' from our hash function - and then we multiply the whole thing by 'r' to push each character up by one position 

e.g. the 2nd character would initially have a hash value of 'r<sup>m-2</sup> * ascii char'. We multiply by 'r' so it now has a hash value of 'r<sup>m-1</sup> * ascii char'.

Then we add the ascii value of the next character along and we have our new hash value.

We can compare the results we get from using <cite>hash</cite> and <cite>reHash</cite> to check it's working:


~~~text

> hash "mar" 3
7168370

> hash "ark" 3
6386283
~~~


~~~text

> reHash 7168370 'm' 'k' 3
6386283
~~~

I hardcoded 'globalQ' to make life a bit easier for myself but in a proper implementation we'd randomly generate it. 

'globalR' would be constant and I wanted it to be available to the <cite>hash</cite> and <cite>reHash</cite> functions without needed to be passed explicitly which is why I've partially applied <cite>hash'</cite> and <cite>reHash'</cite> to achieve this.

We can then run the algorithm like so:


~~~haskell

> rabinKarp "markusaerelius" "sae"
5
~~~


~~~haskell

> rabinKarp "markusaerelius" "blah"
-1
~~~

My whole solution is available on <a href="http://hpaste.org/67606">hpaste</a> and as usual if you see any ways to code this better please let me know.
