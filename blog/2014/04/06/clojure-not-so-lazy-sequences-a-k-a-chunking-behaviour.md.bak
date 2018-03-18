+++
draft = false
date="2014-04-06 22:07:47"
title="Clojure: Not so lazy sequences a.k.a chunking behaviour"
tag=['clojure']
category=['Clojure']
+++

<p>I've been playing with Clojure over the weekend and got caught out by the behaviour of lazy sequences due to chunking - something which was <a href="https://twitter.com/stilkov/status/452411800349605888">obvious</a> <a href="https://twitter.com/philandstuff/status/452412009074941952">to</a> <a href="https://twitter.com/Developerdave/status/452430573836193792">experienced</a> <a href="https://twitter.com/puredanger/status/452430894700048384">Clojurians</a> although not me.</p>


<p>I had something similar to the following bit of code which I expected to only evaluate the first item of the infinite sequence that the range function generates:</p>



~~~lisp

> (take 1 (map (fn [x] (println (str "printing..." x))) (range)))
(printing...0
printing...1
printing...2
printing...3
printing...4
printing...5
printing...6
printing...7
printing...8
printing...9
printing...10
printing...11
printing...12
printing...13
printing...14
printing...15
printing...16
printing...17
printing...18
printing...19
printing...20
printing...21
printing...22
printing...23
printing...24
printing...25
printing...26
printing...27
printing...28
printing...29
printing...30
printing...31
nil)
~~~

<p>The reason this was annoying is because I wanted to shortcut the lazy sequence using <cite><a href="http://clojuredocs.org/clojure_core/clojure.core/take-while">take-while</a></cite>, much like the poster of <a href="http://stackoverflow.com/questions/3407876/how-do-i-avoid-clojures-chunking-behavior-for-lazy-seqs-that-i-want-to-short-ci">this StackOverflow question</a>.</p>


<p>As I understand it when we have a lazy sequence the granularity of that laziness is 32 items at a time a.k.a one chunk, something that Michael Fogus <a href="http://blog.fogus.me/2010/01/22/de-chunkifying-sequences-in-clojure/">wrote about 4 years ago</a>. This was a bit surprising to me but it sounds like it makes sense for the majority of cases.</p>


<p>However, if we want to work around that behaviour we can wrap the lazy sequence in the following <cite>unchunk</cite> function provided by Stuart Sierra:</p>



~~~lisp

(defn unchunk [s]
  (when (seq s)
    (lazy-seq
      (cons (first s)
            (unchunk (next s))))))
~~~

<p>Now if we repeat our initial code we'll see it only prints once:</p>



~~~lisp

> (take 1 (map (fn [x] (println (str "printing..." x))) (unchunk (range))))
(printing...0
nil)
~~~
