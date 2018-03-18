+++
draft = false
date="2013-09-26 19:11:29"
title="Clojure: Writing JSON to a file - \"Exception Don't know how to write JSON of class org.joda.time.DateTime\""
tag=['clojure']
category=['Clojure']
+++

<p>As I mentioned in an earlier post I've been transforming <a href="http://www.markhneedham.com/blog/2013/09/26/clojure-writing-json-to-a-filereading-json-from-a-file/">Clojure hash's into JSON strings</a> using <a href="https://github.com/clojure/data.json">data.json</a> but ran into trouble while trying to parse a hash which contained a <a href="http://www.joda.org/joda-time/">Joda Time</a> DateTime instance.</p>


<p>The date in question was constructed like this:</p>



~~~lisp

(ns json-date-example
  (:require [clj-time.format :as f])
  (:require [clojure.data.json :as json]))

(defn as-date [date-field]
  (f/parse (f/formatter "dd MMM YYYY") date-field ))

(def my-date 
  (as-date "18 Mar 2012"))
~~~

<p>And when I tried to convert a hash containing that object into a string I got the following exception:</p>



~~~lisp

> (json/write-str {:date my-date)})

java.lang.Exception: Don't know how to write JSON of class org.joda.time.DateTime
 at clojure.data.json$write_generic.invoke (json.clj:367)
    clojure.data.json$eval2818$fn__2819$G__2809__2826.invoke (json.clj:284)
    clojure.data.json$write_object.invoke (json.clj:333)
    clojure.data.json$eval2818$fn__2819$G__2809__2826.invoke (json.clj:284)
    clojure.data.json$write.doInvoke (json.clj:450)
    clojure.lang.RestFn.invoke (RestFn.java:425)
~~~

<p>Luckily it's quite easy to get around this by passing a function to <cite>write-str</cite> that converts the DateTime into a string representation before writing that part of the hash to a string.</p>


<p>The function looks like this:</p>



~~~lisp

(defn as-date-string [date]
  (f/unparse (f/formatter "dd MMM YYYY") date))

(defn date-aware-value-writer [key value] 
  (if (= key :date) (as-date-string value) value))
~~~

<p>And we make use of the writer like so:</p>



~~~lisp

> (json/write-str {:date my-date} :value-fn date-aware-value-writer)
"{\"date\":\"18 Mar 2012\"}"
~~~

<p>If we want to read that string back again and reify our date we create a reader function which converts a string into a DateTime. The <cite>as-date</cite> function from the beginning of this post does exactly what we want so we'll use that:</p>



~~~lisp

(defn date-aware-value-reader [key value] 
  (if (= key :date) (as-date value) value))
~~~

<p>We can then pass the reader as an argument to <cite>read-str</cite>:</p>



~~~lisp

> (json/read-str "{\"date\":\"18 Mar 2012\"}" :value-fn date-aware-value-reader :key-fn keyword)
{:date #<DateTime 2012-03-18T00:00:00.000Z>}
~~~
