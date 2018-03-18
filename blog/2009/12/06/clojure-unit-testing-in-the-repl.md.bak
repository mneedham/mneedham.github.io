+++
draft = false
date="2009-12-06 03:28:05"
title="Clojure: Unit testing in the REPL"
tag=['clojure']
category=['Clojure']
+++

One thing which I think is great about coding with F# is the <a href="http://www.markhneedham.com/blog/2009/07/20/coding-quick-feedback/">quick feedback that we can get by defining and then testing out functions in the REPL</a>.

We can do the same thing in Clojure but it's even better because we can also define and run unit tests which I think is pretty neat.

Nurullah Akkaya has a <a href="http://nakkaya.com/2009/11/18/unit-testing-in-clojure/">good post which describes how to use clojure.test</a>, a testing framework written by <a href="http://stuartsierra.com/software/clojure-stuff">Stuart Sierra</a> so I've been using that to define some tests cases for the <a href="http://www.markhneedham.com/blog/2009/11/30/clojure-parsing-an-rss-feed/">little RSS feed parser that I'm writing</a>.

To use clojure.test straight out the box you need the <a href="http://github.com/richhickey/clojure">latest version of the clojure source code</a> as Stuart Sierra <a href="http://stuartsierra.com/software/clojure-stuff">points out on his website</a>.

I ran the ant task for the project and then launched the REPL pointing to the 'alpha snapshot' jar instead of the '1.0.0' jar and it seems to work fine.

I managed to break the 'get-title' function while playing with it before so I thought that would be a good one to try out the tests in the REPL with.

This function is supposed to strip out the name and the following colon which appears in every title and just show the title of the blog post.

I originally had this definition:


~~~lisp

(defn get-title [title]
  (second (first (re-seq #".*:\s(.*)" title))))
~~~

I hadn't realised that this strips from the last colon in the string and therefore returns the wrong result for some inputs.

I created the following tests:


~~~lisp

(use 'clojure.test)
(deftest test-get-title
  (is (= "Clojure - It's awesome"  (get-title "Mark Needham: Clojure - It's awesome")))
  (is (= "A Book: Book Review" (get-title "Mark Needham: A Book: Book Review"))))
~~~

We can run those with the following function:


~~~lisp

(run-tests)
~~~


~~~text

FAIL in (test-get-title) (NO_SOURCE_FILE:19)
expected: (= "A Book: Book Review" (get-title "Mark Needham: A Book: Book Review"))
  actual: (not (= "A Book: Book Review" "Book Review"))

Ran 1 tests containing 2 assertions.
1 failures, 0 errors.
~~~

Changing the function helps solve the problem:


~~~lisp

(defn- get-title [title]
  (second (first (re-seq #"[a-zA-Z0-9 ]+:\s(.*)" title))))
~~~


~~~text

Ran 1 tests containing 2 assertions.
0 failures, 0 errors.
~~~

We can also run the assertions directly without having to call 'run-tests':


~~~lisp

(is (= "A Book: Book Review" (get-title "Mark Needham: A Book: Book Review")))
~~~


~~~text

true
~~~


~~~lisp

(is (= "Something Else" (get-title "Mark Needham: A Book: Book Review")))
~~~


~~~text

expected: (= "Something Else" (get-title "Mark Needham: A Book: Book Review"))
  actual: (not (= "Something Else" "A Book: Book Review"))
false
~~~

Nurullah has <a href="http://nakkaya.com/2009/11/18/unit-testing-in-clojure/">more detail in his post about how to integrate tests into a build</a> although I don't need to do that just yet!
