+++
draft = false
date="2012-10-23 19:04:20"
title="Kaggle Digit Recognizer: A K-means attempt"
tag=['machine-learning-2']
category=['Machine Learning']
+++

Over the past couple of months Jen and I have been playing around with the <a href="http://www.kaggle.com/c/digit-recognizer">Kaggle Digit Recognizer problem</a> - a 'competition' created to introduce people to Machine Learning.

<blockquote>
The goal in this competition is to take an image of a handwritten single digit, and determine what that digit is.
</blockquote>

You are given an input file which contains multiple rows each containing 784 pixel values representing a 28x28 pixel image as well as a label indicating which number that image actually represents.

One of the algorithms that we tried out for this problem was a variation on the <a href="http://en.wikipedia.org/wiki/K-means_clustering">k-means clustering</a> one whereby we took the values at each pixel location for each of the labels and came up with an average value for each pixel.

So we'd end up with something like this:


~~~text

Label 0: Pixel 1: 214, Pixel 2: 12, Pixel 3: 10...Pixel 784: 23
Label 1: Pixel 1: 234, Pixel 2: 0, Pixel 3: 25...Pixel 784: 0
Label 2: Pixel 1: 50, Pixel 2: 23, Pixel 3: 20...Pixel 784: 29
...
Label 9: Pixel 1: 0, Pixel 2: 2, Pixel 3: 10...Pixel 784: 1
~~~

When we needed to classify a new image we calculated the distance between each pixel of the new image against the equivalent pixel of each of the 10 pixel averaged labels and then worked out which label our new image was closest to.

We started off with some code to load the training set data into memory so we could play around with it:


~~~lisp

(require '[clojure.string :as string])    
(use 'clojure.java.io)

(defn parse [reader]
  (drop 1 (map #(string/split % #",") (line-seq reader))))

(defn get-pixels [pix] (map #( Integer/parseInt %) pix))

(defn create-tuple [[ head & rem]] {:pixels (get-pixels rem) :label head})

(defn parse-train-set [reader] (map create-tuple (parse reader)))

(defn read-train-set [n]
  (with-open [train-set-rd (reader "data/train.csv")]
    (vec (take n (parse-train-set train-set-rd)))))
~~~

One thing we learnt was that it's helpful to just be able to take a small subset of the data set into memory rather than loading the whole thing in straight away. I ended up crashing my terminal a few times by evaluating a 40,000 line file into the Slime buffer - not a good idea!

To get the first row we'd do this:


~~~lisp

user> (first (read-train-set 1))
{:pixels (0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0...), :label "0"}  
~~~

We wrote the following code to work out the average pixel values for each of the labels:


~~~lisp

(def all-the-data (read-train-set 1000))

(defn find-me-all-the [number] (filter #(= (str number) (:label %)) all-the-data))

(defn mean [& v]
  (float
   (/ (apply + v) (count v) )))

(defn averages [rows] (apply map mean (map :pixels rows)) )

(def all-the-averages
  (map vector (range 0 9) (map #(averages (find-me-all-the %)) (range 0 9))))
~~~

It's mostly self explanatory although we had to use <cite>float</cite> in the mean calculation so that we'd get a decimal value rather than a fraction. 

<a href="https://twitter.com/jennifersmithco">Jen</a> also came up with a neat way of using <cite>apply</cite> in the <cite>averages</cite> function to map the <cite>mean</cite> function across each individual pixel.

I found it easier to follow when we ran the function with a smaller data set:


~~~lisp

user> (averages [ {:pixels [1 2 3]} {:pixels [4 5 6]}])
(2.5 3.5 4.5) 
~~~

That expands out to this:


~~~lisp

user> (apply map mean [[1 2 3] [4 5 6]])
~~~

Which is conceptually the same as doing this:


~~~lisp

user> (map mean [1 2 3] [4 5 6])
~~~


We can get the averages for the label '0' like so:


~~~lisp

user> (first all-the-averages)
[0 (1.317757 3.3551402 6.196262 7.373831155...74767 171.61682 147.51402 96.943924 48.728973 22.299065 3.037383 )] 
~~~

To work out what label an untrained collection of pixels is closest to we wrote the following functions:


~~~lisp

(defn distance-between [fo1 fo2]
  (Math/sqrt (apply + (map #(* % %) (map - fo1 fo2)))))

(defn find-gap [averages unranked-value]
  (vector (first averages) (distance-between (second averages) unranked-value)))

(defn which-am-i [unranked-value]
  (let [all-the-gaps (map #(find-gap %1 unranked-value) all-the-averages)]
    [(ffirst (sort-by second all-the-gaps)) all-the-gaps]))
~~~

<cite>distance-between</cite> finds the <a href="http://en.wikipedia.org/wiki/Euclidean_distance">euclidean distance</a> between the pixel values, <cite>find-gap</cite> then uses this to find the distance from each of the trained labels set of pixels to the test data set and we can then call <cite>which-am-i</cite> to find out which label a new set of pixels should be classified as:


~~~lisp

user> (first test-data)
(0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0...)  

user>  (which-am-i (first test-data))
[0 ([0 1763.5688862988827] [1 2768.1143197890624] [2 2393.9091578180937] 
[3 2598.4629450761286] [4 2615.1233720558307] [5 2287.1791665580586] 
[6 2470.096959417967] [7 2406.0132574502527] [8 2489.3635108564304] [9 2558.0054056506265])] 
~~~

The <cite>which-am-i</cite> function first returns its prediction and then also includes the distance from the test data set to each of the trained labels so that we can tell how close it was to being classified as something else. 

We got an accuracy of 80.657% when classifying new values with this algorithm which isn't great but doesn't seem too bad given how simple it is and that we were able to get it up and running in a couple of hours.

The <a href="https://github.com/jennifersmith/machinenursery">code is on Jen's github</a> if you're interested in seeing more.
