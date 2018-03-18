+++
draft = false
date="2011-07-16 22:19:47"
title="Clojure: Extracting child elements from an XML document with zip-filter"
tag=['clojure']
category=['Clojure']
+++

I've been following <a href="http://nakkaya.com/2009/12/07/zipping-xml-with-clojure/">Nurullah Akkaya's blog post</a> about navigating XML documents using the Clojure <a href="http://richhickey.github.com/clojure-contrib/zip-filter-api.html">zip-filter</a> API and I came across an interesting problem in a document I'm parsing which goes beyond what's covered in his post.

Nurullah provides a neat <cite>zip-str</cite> function which we can use to convert an XML string into a zipper object:


~~~lisp

(require '[clojure.zip :as zip] '[clojure.xml :as xml])
(use '[clojure.contrib.zip-filter.xml])

(defn zip-str [s]
  (zip/xml-zip (xml/parse (java.io.ByteArrayInputStream. (.getBytes s)))))
~~~

The fragment of the document I'm parsing looks like this:


~~~lisp

(def test-doc (zip-str "<?xml version='1.0' encoding='UTF-8'?>
<root>
  <Person>
    <FirstName>Charles</FirstName>
    <LastName>Kubicek</LastName>
  </Person>
  <Person>
    <FirstName>Mark</FirstName>
    <MiddleName>H</MiddleName>
    <LastName>Needham</LastName>
  </Person>	
</root>"))
~~~

I wanted to be able to get the full names of each of the people such that I'd have a collection which looked like this:


~~~lisp

("Charles Kubicek" "Mark H Needham")
~~~

My initial thinking was to get all the child elements of the <cite>Person</cite> element and operate on those:


~~~lisp

(require '[clojure.contrib.zip-filter :as zf])

(xml-> test-doc :Person zf/children text)
~~~

Unfortunately that gives back all the names in one collection like so:


~~~lisp

("Charles" "Kubicek" "Mark" "H" "Needham") 
~~~

Since it's not mandatory to have a <cite>MiddleName</cite> element it's not possible to work out which names go with which person!

A bit of googling led me to <a href="http://stackoverflow.com/questions/2057797/how-do-i-combine-results-from-zip-filter-queries-on-an-xml-tree-in-clojure">stackoverflow</a> where Timothy Pratley suggests that we need to get up to the <cite>Person</cite> element and then pick each of the child elements individually.

We can do that by mapping over the collection with a function which creates a vector for each <cite>Person</cite> containing all their names.

In pseudo-code this is what we want to do:


~~~lisp

> (map magic-function (xml-> test-doc :Person))
(["Charles" "Kubicek"] ["Mark" "H" "Needham"])
~~~

Timothy suggests the <cite>juxt</cite> function which is defined like so:

<blockquote>
juxt

Takes a set of functions and returns a fn that is the juxtaposition of those fns.  The returned fn takes a variable number of args, and returns a vector containing the result of applying each fn to the args (left-to-right).
</blockquote>

A simple use of <cite>juxt</cite> could be to create some values containing my name:


~~~lisp

((juxt #(str % " loves Clojure") #(str % " loves Scala")) "Mark")
~~~

Which returns:


~~~lisp

["Mark loves Clojure" "Mark loves Scala"] 
~~~

We can use <cite>juxt</cite> to build the collection of names and then use <cite><a href="http://clojuredocs.org/clojure_core/clojure.string/join">clojure.string/join</a></cite> to separate them with a space.

The code to do this ends up looking like this:


~~~lisp

(require '[clojure.string :as str])

(defn get-names [doc]
  (->> (xml-> doc :Person)
       (map (juxt #(xml1-> % :FirstName text) #(xml1-> % :MiddleName text) #(xml1-> % :LastName text)))
       (map (partial filter seq))
       (map (partial str/join " "))))
~~~

We use a <cite>filter</cite> on the second last line to get rid of any nil values in the vector (e.g. no middle name) and then combine the names on the last line. 

We can then call the function:


~~~lisp

> (get-names test-doc)
("Charles Kubicek" "Mark H Needham")  
~~~
