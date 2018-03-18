+++
draft = false
date="2012-06-19 00:21:52"
title="The Little Schemer: Attempt #2"
tag=['software-development', 'little-schemer']
category=['Software Development']
+++

A few weeks ago I asked the twittersphere for some advice on how I could get better at writing recursive functions and one of the pieces of advice was to work through <a href="http://www.amazon.co.uk/The-Little-Schemer-Daniel-Friedman/dp/0262560992/ref=sr_1_1?ie=UTF8&qid=1340064292&sr=8-1">The Little Schemer</a>.

I first heard about The Little Schemer a couple of years ago and after going through the first few pages I got bored and gave up.

I still found the first few pages a bit trivial this time around as well but my colleague <a href="https://twitter.com/#!/jennifersmithco">Jen Smith</a> encouraged me to keep going and once I'd got about 20 pages in it became clearer to me why the first few pages had been written the way they had.

I'm just under half way through at the moment and so far the whole thing that the authors are trying to get you to do is <strong>think through problems in a way that makes them easily solvable using recursion</strong>. 

In the first few pages that approach seems ridiculously over the top but it gets you thinking in the right way and means that when you reach the exercises where you need to write your own functions it's not too much of a step up.

Since I've been learning Haskell for the last few months I thought it'd be interesting to try and use that language even though Clojure would be a more natural fit.

I initially wrote the solutions to exercises using idiomatic Haskell before realising I was probably missing the point by doing that:


~~~haskell

multiInsertL new old [] = []
multiInsertL new old (x:xs) | x == old = new:old:multiInsertL new old xs
                            | otherwise = x:multiInsertL new old xs	
~~~

I came across the <a href="http://hackage.haskell.org/package/cond">cond</a> package which lets you simulate a Scheme/Clojure 'cond' and so far all the functions in the exercises have made use of that.


~~~haskell

multiInsertL2 new old lat = cond [(null lat, []),
                                  (head lat == old, new:old:multiInsertL2 new old (tail lat)),
                                  (otherwise, (head lat):multiInsertL2 new old (tail lat))]
~~~

I wouldn't write Haskell like this normally but I think it's helpful for me while I'm getting used to the different patterns you can have in recursive functions.

As we go through the exercises the authors describe 'commandments' that you should follow when writing recursive functions which are really useful for me as a novice.

My favourite one so far is the 4th commandment:

<blockquote>
Always change at least one argument while recursing. It must be changed to be closer to termination. The changing argument must be tested in the termination condition:
<ul>
<li>when using cdr, test termination with null? and</li>
<li>when using sub1, test termination with zero?</li>
</ul>
</blockquote>

So many times when I've tried to write recursive functions I've ended up putting them into an infinite loop but following this rule should help avoid that!

The cool thing about this book is that you can work through a few problems, put it down for a few days before picking it back up and you'll still be able to pick up from where you left off quite easily.

Highly recommended so far!
