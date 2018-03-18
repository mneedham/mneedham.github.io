+++
draft = false
date="2009-11-23 20:08:20"
title="Writing a Java function in Clojure"
tag=['java', 'clojure']
category=['Java', 'Clojure']
+++

A function that we had to write in Java on a project that I worked on recently needed to indicate whether there was a gap in a series of data points or not.

If there were gaps at the beginning or end of the sequence then that was fine but gaps in the middle of the sequence were not.


~~~text

null, 1, 2, 3 => no gaps
1, 2, 3, null => no gaps
1, null, 2, 3 => gaps
~~~

The Java version looked a bit like this:


~~~java

public boolean hasGaps(List<BigInteger> values) {
    Iterator<BigInteger> fromHead = values.iterator();
    while (fromHead.hasNext() && fromHead.next() == null) {
        fromHead.remove();
    }

    Collections.reverse(values);

    Iterator<BigInteger> fromTail = values.iterator();
    while (fromTail.hasNext() && fromTail.next() == null) {
        fromTail.remove();
    }

    return values.contains(null);
}
~~~

We take the initial list and then remove all the null values from the beginning of it, then reverse the list and remove all the values from the end.

We then check if there's a null value and if there is then it would indicate there is indeed a gap in the list.

To write this function in Clojure we can start off by using the '<a href="http://clojure.org/api#toc237">drop-while</a>' function to get rid of the trailing nil values.

I started off with this attempt:


~~~lisp

(defn has-gaps? [list]
    let [no-nils] [drop-while #(= % nil) list]
  no-nils)
~~~

Unfortunately that gives us the following error!


~~~text

Can't take value of a macro: #'clojure.core/let (NO_SOURCE_FILE:16)
~~~

It thinks we're trying to pass around the 'let' macro instead of evaluating it - I forgot to put in the brackets around the 'let'!

I fixed that with this next version:


~~~lisp

(defn has-gaps? [list]
    (let [no-nils] [drop-while nil? list]
  no-nils))
~~~

But again, no love:


~~~lisp

java.lang.IllegalArgumentException: let requires an even number of forms in binding vector (NO_SOURCE_FILE:23)
~~~

The way I understand it the 'let' macro takes in a vector of bindings as its first argument and what I've done here is pass in two vectors instead of one.

In the bindings vector we need to ensure that there are an even number of forms so that each symbol can be bound to an expression.

I fixed this by putting the two vectors defined above into another vector:


~~~lisp

(defn has-gaps? [list]
    (let [[no-nils] [(drop-while nil? list)]]
  no-nils))
~~~

We can simplify that further so that we don't have nested vectors:


~~~lisp

(defn has-gaps? [list]
    (let [no-nils (drop-while nil? list)]
  no-nils))
~~~

The next step was to make 'no-nils' a function so that I could make use of that function when the list was reversed as well:


~~~lisp

(defn has-gaps? [list]
    (let [no-nils (fn [x] (drop-while nil? x))]
  (no-nils list)))
~~~

I then wrote the rest of the function to reverse the list and then <a href="http://www.markhneedham.com/blog/2009/11/21/clojure-checking-for-a-nil-value-in-a-collection/">check the remaining list for nil</a>:


~~~lisp

(defn has-gaps? [list]
    (let [[no-nils] [(fn [x] (drop-while nil? x))]
          [nils-removed] [(fn [x] ((comp no-nils reverse no-nils) x))]]
  (some nil? (nils-removed list))))
~~~

The '<a href="http://clojure.org/api#toc151">comp</a>' function can be used to compose a set of functions which is what I needed.

It seemed like the 'nils-removed' function wasn't really necessary so I inlined that:


~~~lisp

(defn has-gaps? [list]
    (let [no-nils (fn [x] (drop-while nil? x))]
  (some nil? ((comp no-nils reverse no-nils) list))))
~~~

The function can now be used like this:

~~~text

user=> (has-gaps? '(1 2 3))
nil
user=> (has-gaps? '(nil 1 2 3))
nil
user=> (has-gaps? '(1 2 3 nil))
nil
user=> (has-gaps? '(1 2 nil 3))
true
~~~

I'd be intrigued to know if there's a better way to do this.
