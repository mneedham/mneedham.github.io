+++
draft = false
date="2012-10-27 12:27:10"
title="Kaggle Digit Recognizer: K-means optimisation attempt"
tag=['machine-learning-2', 'kaggle']
category=['Machine Learning']
+++

I recently wrote a blog post explaining how <a href="https://twitter.com/jennifersmithco">Jen</a> and I <a href="http://www.markhneedham.com/blog/2012/10/23/kaggle-digit-recognizer-a-k-means-attempt/">used the K-means algorithm</a> to classify digits in <a href="http://www.kaggle.com/c/digit-recognizer">Kaggle's Digit Recognizer problem</a> and one of the things we'd read was that with this algorithm you often end up with situations where it's difficult to classify a new item because if falls between two labels.

We decided to have a look at the output of our classifier function to see whether or not that was the case.

As a refresher, this was our original function to determine the label for a new test data row...

~~~lisp

(defn which-am-i [unranked-value]
  (let [all-the-gaps (map #(find-gap %1 unranked-value) all-the-averages)]
    [(ffirst (sort-by second all-the-gaps)) all-the-gaps]))
~~~

...and that would return a result like this:


~~~lisp

user>  (which-am-i (first test-data))
[0 ([0 1763.5688862988827] [1 2768.1143197890624] [2 2393.9091578180937] 
[3 2598.4629450761286] [4 2615.1233720558307] [5 2287.1791665580586] 
[6 2470.096959417967] [7 2406.0132574502527] [8 2489.3635108564304] [9 2558.0054056506265])]
~~~

We first changed the function to return another entry in the vector representing the top two picks:


~~~lisp

(defn which-am-i [unranked-value]
  (let [all-the-gaps (map #(find-gap %1 unranked-value) all-the-averages)
        top-two (take 2 (sort-by second all-the-gaps))]
    [(ffirst (sort-by second all-the-gaps)) top-two all-the-gaps]))
~~~

If we run that:


~~~lisp

user> (which-am-i (first test-data))
[2 ([2 1855.3605185002546] [0 2233.654619238101]) 
([0 2233.654619238101] [1 2661.7148686603714] [2 1855.3605185002546] 
[3 2512.429018687221] [4 2357.637631775974] [5 2457.9850052966344] 
[6 2243.724487123002] [7 2554.1158473740174] [8 2317.567588716217] [9 2520.667565741239])]   
~~~

In this case the difference between the top 2 labels is about 400 but we next changed the function to output the actual difference so we could see how close the top 2 were over the whole test set:


~~~lisp

(defn which-am-i [unranked-value]
  (let [all-the-gaps (map #(find-gap %1 unranked-value) all-the-averages)
        top-two (take 2 (sort-by second all-the-gaps))
        difference-between-top-two (Math/abs (apply - (map second top-two)))]
    [(ffirst (sort-by second all-the-gaps)) top-two difference-between-top-two all-the-gaps]))
~~~

We then ran it like this, taking just the first 10 differences on this occasion:


~~~lisp

user>  (take 10 (->> test-data (map which-am-i) (map #(nth % 2))))
(378.2941007378465 523.6102802591759 73.57510749262792 3.8557350283749656 5.806672422475231 
183.90928740097775 713.1626629833258 335.38646365464047 538.6191727330108 161.68429111785372) 
~~~

From visually looking at this over a larger subset we noticed that there seemed to be a significant number of top twos within a distance of 50.

We therefore changed the function to use <a href="http://clojuredocs.org/clojure_core/1.2.0/clojure.core/shuffle">shuffle</a> to randomly pick between those two labels when the distance was that small.


~~~lisp

(defn which-am-i [unranked-value]
  (let [all-the-gaps (map #(find-gap %1 unranked-value) all-the-averages)
        top-two (take 2 (sort-by second all-the-gaps))
        difference-between-top-two (Math/abs (apply - (map second top-two)))
        very-close (< difference-between-top-two 50)
        best-one (if very-close (ffirst (shuffle top-two)) (ffirst top-two))]
    [best-one top-two all-the-gaps]))
~~~

Our assumption was that this might marginally improve the performance of the algorithm but it actually made it marginally worse, with a new accuracy of 79.3%

At this point we weren't really sure what we should be doing to try and improve the algorithm's performance so we moved onto random forests but it's interesting that you can get a reasonable accuracy even with such a simple approach!
