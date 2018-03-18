+++
draft = false
date="2016-01-24 22:01:43"
title="Clojure: First steps with reducers"
tag=['clojure']
category=['Clojure']
+++

<p>
I've been playing around with Clojure a bit today in preparation for <a href="https://skillsmatter.com/meetups/7794-using-clojure-neo4j-to-build-a-meetup-recommendation-engine">a talk I'm giving next week</a> and found myself writing the following code to apply the same function to three different scores:
</p>



~~~clojure

(defn log2 [n]
  (/ (Math/log n) (Math/log 2)))

(defn score-item [n]
  (if (= n 0) 0 (log2 n)))

(+ (score-item 12) (score-item 13) (score-item 5)) 9.60733031374961
~~~

<p>
I'd forgotten about folding over a collection but quickly remembered that I could achieve the same result with the following code:
</p>



~~~clojure

(reduce #(+ %1 (score-item %2)) 0 [12 13 5]) 9.60733031374961
~~~

<p>The added advantage here is that if I want to add a 4th score to the mix all I need to do is append it to the end of the vector:
</p>



~~~clojure

(reduce #(+ %1 (score-item %2)) 0 [12 13 5 6]) 12.192292814470767
~~~

<p>
However, while Googling to remind myself of the order of the arguments to reduce I kept coming across <a href="http://clojure.org/reference/reducers">articles and documentation about reducers</a> which I'd heard about but never used.
</p>


<p>As I understand they're used to <a href="http://ianrumford.github.io/blog/2013/08/25/some-trivial-examples-of-using-clojure-reducers/">achieve performance gains and easier composition of functions over collections</a> so I'm not sure how useful they'll be to me but I thought I'd give them a try.
</p>


<p>Our first step is to bring the namespace into scope:</p>



~~~clojure

(require '[clojure.core.reducers :as r])
~~~

<p>Now we can compute the same result using the <cite>reduce</cite> function:</p>



~~~clojure

(r/reduce #(+ %1 (score-item %2)) 0 [12 13 5 6]) 12.192292814470767
~~~

<p>So far, so identical. If we wanted to calculate individual scores and then filter out those below a certain threshold the code would behave a little differently:</p>



~~~clojure

(->>[12 13 5 6]
    (map score-item)
    (filter #(> % 3))) (3.5849625007211565 3.700439718141092)

(->> [12 13 5 6]
     (r/map score-item)
     (r/filter #(> % 3))) #object[clojure.core.reducers$folder$reify__19192 0x5d0edf21 "clojure.core.reducers$folder$reify__19192@5d0edf21"]
~~~

<p>Instead of giving us a vector of scores the reducers version returns a reducer which can pass into <cite>reduce</cite> or <cite>fold</cite> if we want an accumulated result or <cite>into</cite> if we want to output a collection. In this case we want the latter:</p>



~~~clojure

(->> [12 13 5 6]
     (r/map score-item)
     (r/filter #(> % 3))
     (into [])) (3.5849625007211565 3.700439718141092)
~~~

<p>
With a measly 4 item collection I don't think the reducers are going to provide much speed improvement here but we'd need to use the <cite><a href="http://clojure.org/reference/reducers#_using_reducers">fold</a></cite> function if we want processing of the collection to be done in parallel.
</p>


<p>One for next time!</p>

