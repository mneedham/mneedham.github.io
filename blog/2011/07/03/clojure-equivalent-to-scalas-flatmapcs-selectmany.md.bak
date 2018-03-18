+++
draft = false
date="2011-07-03 22:50:47"
title="Clojure: Equivalent to Scala's flatMap/C#'s SelectMany"
tag=['clojure']
category=['Clojure']
+++

I've been playing around with Clojure a bit over the weekend and one thing I got stuck with was working out how to achieve the functionality provided by Scala's <cite>flatMap</cite> or C#'s <cite>SelectMany</cite> methods on collections.

I had a collection of zip files and wanted to transform that into a collection of all the file entries in those files.

If we just use <cite>map</cite> then we'll end up with a collection of collections which is more difficult to deal with going forward.

In Scala we'd do the following:


~~~scala

import scala.collection.JavaConversions._

val zip1 = new ZipFile(new File("/Users/mneedham/Documents/my-zip-file.zip"))
val zip2 = new ZipFile(new File("/Users/mneedham/Documents/my-zip-file2.zip"))

List(zip1, zip2).flatMap(_.entries)
~~~

I was originally make using of <cite>map</cite> followed by <cite>flatten</cite> but I learnt from my colleague <a href="http://fragmental.tw/">Phil Calcado</a> that the function I wanted is <cite><a href="http://clojure.github.com/clojure/clojure.core-api.html#clojure.core/mapcat">mapcat</a></cite> which leads to this solution:


~~~lisp

(def zip1 (new ZipFile (file "/Users/mneedham/Documents/my-zip-file.zip")))
(def zip2 (new ZipFile (file "/Users/mneedham/Documents/my-zip-file2.zip")))

(mapcat (fn [file] (enumeration-seq (.entries file))) (list zip1 zip2))
~~~

I also learnt about the various functions available to create sequences, such as <cite>enumeration-seq</cite> from other types which are listed at <a href="http://clojure.org/sequences">the bottom of this page</a>.

Scala uses implicit conversions to do that and presumably you'd hide away the conversion in a helper function in Clojure.
