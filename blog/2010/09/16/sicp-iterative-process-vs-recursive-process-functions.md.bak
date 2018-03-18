+++
draft = false
date="2010-09-16 18:48:31"
title="SICP: Iterative process vs Recursive process functions"
tag=['sicp-2']
category=['SICP']
+++

I was working my way through some of the exercises in <a href="http://mitpress.mit.edu/sicp/full-text/book/book-Z-H-4.html#%_toc_start">SICP</a> over the weekend and one that I found particularly interesting was <a href="http://mitpress.mit.edu/sicp/full-text/book/book-Z-H-11.html#%_thm_1.11">1.11</a> where you have to write a function by means of a recursive process and then by means of an iterative process.

<blockquote>
A function f is defined by the rule that f(n) = n if n<3 and f(n) = f(n - 1) + 2f(n - 2) + 3f(n - 3) if n> 3. Write a procedure that computes f by means of a recursive process. Write a procedure that computes f by means of an iterative process.
</blockquote> 

To write that function recursively is relatively straight forward:

(in Clojure)

~~~lisp

(defn f [n]
  (if (< n 3)
    n
    (+ (f (- n 1)) (* 2 (f (- n 2))) (* 3 (f (- n 3))))))
~~~

The solution to this problem by means of an iterative process will still use recursion but we won't need to keep a track of all the previous calls to the function on the stack because we will keep the current state of the calculation in parameters that we pass to the function.

This will also mean that the second function is <a href="http://cs.hubfs.net/forums/permalink/8022/8022/ShowThread.aspx#8022">tail recursive</a>.

I was initially a bit stuck about how to write this function but luckily <a href="http://in.linkedin.com/in/shishirdas">Shishir</a> was around and had a better idea. 

The solution we eventually ended up with looks like this:


~~~lisp

(defn g [n a b c count]
  (cond (< n 3) n
	(> count (- n 3)) a
	:else (g n (+ a (* 2 b) (* 3 c)) a b (+ count 1))))

(defn f [n]
  (g n 2 1 0 0))
~~~

I think there should be a way to get rid of the first condition but I'm not sure exactly how to do that - <a href="http://community.schemewiki.org/?sicp-ex-1.11">the solution on the wiki</a> is a bit better.

The difference in the approach to writing the iterative version is that we needed to think about solving the problem from the bottom down rather than from the top down.

In this case that meant that we needed to pass around parameters for the first 3 values of n i.e. 1, 2 and 3 which had values of 0, 1 and 2 respectively.

The way we've passed the parameters through the function means that 'a' represents the value that we'll eventually want to return when we reach the exit condition of the function.

We pass 'a' and 'b' into the next function call as 'b' and 'c' which means that we lose the current f(n-3) value on the next recursion of the function.

I still find writing these types of functions quite tricky so I'd be interested in any advice that people have about this.
