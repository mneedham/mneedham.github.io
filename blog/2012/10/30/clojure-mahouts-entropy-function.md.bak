+++
draft = false
date="2012-10-30 22:46:34"
title="Clojure: Mahout's 'entropy' function"
tag=['clojure', 'mahout']
category=['Clojure']
+++

As I <a href="http://www.markhneedham.com/blog/2012/10/27/kaggle-digit-recognizer-mahout-random-forest-attempt/">mentioned in a couple</a> <a href="http://www.markhneedham.com/blog/2012/10/27/mahout-using-a-saved-random-forestdecisiontree/">of previous posts</a> <a href="https://twitter.com/jennifersmithco">Jen</a> and I have been playing around with <a href="https://cwiki.apache.org/MAHOUT/random-forests.html">Mahout random forests</a> and for a few hours last week we spent some time looking through the code to see how it worked. 

In particular we came across an entropy function which is used to determine how good a particular 'split' point in a decision tree is going to be. 

I <a href="http://computersciencesource.wordpress.com/2010/01/28/year-2-machine-learning-decision-trees-and-entropy/">quite like the following definition</a>:
<blockquote>
The level of certainty of a particular decision can be measured as a number from 1 (completely uncertain) to 0 (completely certain).

Information Theory (developed by Claude Shannon 1948) defines this value of uncertainty as entropy, a probability-based measure used to calculate the amount of uncertainty.

For example, if an event has a 50/50 probability, the entropy is 1. If the probability is 25/75 then the entropy is a little lower.

The goal in machine learning is to get a very low entropy in order to make the most accurate decisions and classifications.
</blockquote>

The function reads like this:


~~~java

  private static double entropy(int[] counts, int dataSize) {
    if (dataSize == 0) {
      return 0.0;
    }

    double entropy = 0.0;
    double invDataSize = 1.0 / dataSize;

    for (int count : counts) {
      if (count == 0) {
        continue; // otherwise we get a NaN
      }
      double p = count * invDataSize;
      entropy += -p * Math.log(p) / LOG2;
    }

    return entropy;
  }
~~~

We decided to see what the function would look like it was written in Clojure and it was clear from looking at how the <cite>entropy</cite> variable is being mutated that we'll need to do a <cite>reduce</cite> over a collection to get our final result.

In my first attempt at writing this function I started with the call to reduce and then worked out from there:


~~~lisp

(defn individual-entropy [x data-size]
  (let [p (float (/ x data-size))]
    (/ (* (* -1 p) (Math/log p)) (Math/log 2.0))))

(defn calculate-entropy [counts data-size]
  (if (= 0 data-size)
    0.0
    (reduce
     (fn [entropy x] (+ entropy (individual-entropy x data-size)))
     0
     (remove (fn [count] (= 0 count)) counts))))
~~~

Jen was pretty much watching on with horror the whole time I wrote this function but I was keen to see how our approaches differed so I insisted she allow me to finish!

We then moved onto Jen's version where instead of writing the code all in one go like I did, we would try to reduce the problem to the point where we wouldn't need to pass a custom anonymous function to <cite>reduce</cite> but could instead pass a <cite>+</cite>.

This meant we'd need to run a <cite>map</cite> over the <cite>counts</cite> collection to get the individual entropy values first and then add them all together. 


~~~lisp

(defn calculate-entropy [counts data-size]
  (->>  counts
       (remove #(= 0 %))
       (map #(individual-entropy % data-size))
       (reduce +)))
~~~

Here we're using the <a href="http://emacswiki.org/emacs/ThreadMacroFromClojure">threading operator</a> to make the code a bit easier rather than nesting functions as I had done.

Jen also showed me a neat way of rewriting the line with the <cite>remove</cite> function to use a set instead:


~~~lisp

(defn calculate-entropy [counts data-size]
  (->>  counts
       (remove #{0})
       (map #(individual-entropy % data-size))
       (reduce +)))
~~~

I hadn't seen this before although <a href="http://blog.jayfields.com/2010/08/clojure-using-sets-and-maps-as.html">Jay Fields has a post showing a bunch of examples of using sets and maps as functions</a>.

In this case if the set is applied to 0 the value will be returned:

~~~lisp

user> (#{0} 0)
0                                                                                                                                                                                                                                     
~~~

But if the set is applied to a non 0 value we'll get a nil back:


~~~lisp

user> (#{0} 2)
nil                                                                                                                                                                                                                                   
~~~

So if we apply that to a collection of values we'd see the 0s removed:


~~~lisp

user> (remove #{0} [1 2 3 4 5 6 0])
(1 2 3 4 5 6) 
~~~

I <a href="http://www.markhneedham.com/blog/2012/03/19/functional-programming-one-function-at-a-time/">wrote a similar post earlier in the year</a> where another colleague showed me his way of breaking down a problem but clearly I still haven't quite got into the mindset so I thought it was worth writing up.
