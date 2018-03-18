+++
draft = false
date="2011-07-10 22:21:16"
title="Clojure: Language as thought shaper"
tag=['clojure']
category=['Clojure']
+++

I recently read <a href="http://soft.vub.ac.be/~tvcutsem/whypls.html">an interesting article by Tom Van Cutsem</a> where he describes some of the goals that influence the design of programming languages and one which stood out to me is that of viewing 'language as a thought shaper':

<blockquote>
Language as thought shaper: to induce a paradigm shift in how one should structure software (changing the "path of least resistance").
</blockquote>

<blockquote>
To quote <a href="http://www.cs.yale.edu/quotes.html">Alan Perlis</a>: "a language that doesn't affect the way you think about programming, is not worth knowing."

The goal of a thought shaper language is to change the way a programmer thinks about structuring his or her program.
</blockquote>

I've been rewriting part of the current system that I'm working on in Clojure in my spare time to see how the design would differ and it's interesting to see that it's quite different.

The part of the system I'm working on needs to extract a bunch of XML files from ZIP files and then import those into the database.

From a high level the problem can be described as follows:

<ul>
<li>Get all files in specified directory</li>
<li>Find only the ZIP files</li>
<li>Find the XML files in those ZIP files</li>
<li>Categorise the XML files depending on whether we can import them</li>
<li>Add an additional section to good files to allow for easier database indexing</li>
<li>Import the new version of the files into the database</li>
</ul>	

Clojure encourages a design based around processing lists and this problem seems to fit that paradigm very neatly.

We can make use of the <cite><a href="http://clojuredocs.org/clojure_core/clojure.core/-%3E%3E">->></a></cite> macro to chain together a bunch of functions originally acting on the specified directory to allow us to achieve this.

At the moment this is what the entry point of the code looks like:


~~~lisp

(defn parse-directory [dir]                                                                                                                                                                           
  (->> (all-files-in dir)                                                                                         
       (filter #(.. (canonical-path %1) (endsWith ".zip")))                                                                                                                                                                 
       (mapcat (fn [file] (extract file)))                                                                         
       (filter (fn [entry] (. (entry :name) (endsWith ".xml"))))                                                                                                                                                 
       (map #(categorise %))))
~~~

The design of the Scala code is a bit different even though the language constructs exist to make a similar design possible.

The following are some of the classes involved:

<ul>
<li>ImportManager - finds the XML files in the ZIP files, delegates to DocumentMatcher</li>
<li>DeliveryManager - gets all the ZIP files from specified directory</li>
<li>DocumentMatcher - checks if XML document matches any validation rules and wraps in appropriate object</li>
<li>ValidDocument/InvalidDocument - wrap the XML document and upload to database in the case of the former</li>
<li>ValidationRule - checks if the document can be imported into the system</li>
</ul>

It was interesting to me that when I read the Scala code the problem appeared quite complicated whereas in Clojure it's easier to see the outline of what the program does.

I think is because we're trying to shoe horn a <a href="http://eaipatterns.com/PipesAndFilters.html">pipes and filters</a> problems into objects which leaves us with a design that feels quite unnatural.

I originally learnt this design style while playing around with F# a couple of years ago and it seems to work reasonably well in most functional languages.
