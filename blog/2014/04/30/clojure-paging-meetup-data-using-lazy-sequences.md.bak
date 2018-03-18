+++
draft = false
date="2014-04-30 00:20:46"
title="Clojure: Paging meetup data using lazy sequences"
tag=['clojure']
category=['Clojure']
+++

<p>
I've been playing around with the <a href="http://www.meetup.com/meetup_api/">meetup API</a> to do some analysis on the <a href="http://www.meetup.com/graphdb-london/">Neo4j London meetup</a> and one thing I wanted to do was download all the members of the group.
</p>


<p>A feature of the meetup API is that each end point will only allow you to return a maximum of 200 records so I needed to make use of offsets and paging to retrieve everybody.</p>


<p>
It seemed like a good chance to use some lazy sequences to keep track of the offsets and then stop making calls to the API once I wasn't retrieving any more results.
</p>


<p>I wrote the following functions to take care of that bit:</p>



~~~lisp

(defn unchunk [s]
  (when (seq s)
    (lazy-seq
      (cons (first s)
            (unchunk (next s))))))

(defn offsets []
  (unchunk (range)))


(defn get-all [api-fn]
  (flatten
   (take-while seq
               (map #(api-fn {:perpage 200 :offset % :orderby "name"}) (offsets)))))
~~~

<p>I previously wrote about the <a href="http://www.markhneedham.com/blog/2014/04/06/clojure-not-so-lazy-sequences-a-k-a-chunking-behaviour/">chunking behaviour of lazy collections</a> which meant that I ended up with a minimum of 32 calls to each URI which wasn't what I had in mind!</p>


<p>To get all the members in the group I wrote the following function which is passed to <cite>get-all</cite>:</p>



~~~lisp

(:require [clj-http.client :as client])

(defn members
  [{perpage :perpage offset :offset orderby :orderby}]
  (->> (client/get
        (str "https://api.meetup.com/2/members?page=" perpage
             "&offset=" offset
             "&orderby=" orderby
             "&group_urlname=" MEETUP_NAME
             "&key=" MEETUP_KEY)
        {:as :json})
       :body :results))
~~~

<p>So to get all the members we'd do this:</p>



~~~lisp

(defn all-members []
  (get-all members))
~~~

<p>I'm told that using lazy collections when side effects are involved is a bad idea - presumably because the calls to the API might never end - but since I only run it manually I can just kill the process if anything goes wrong.</p>


<p>I'd be interested in how others would go about solving this problem - <a href="https://github.com/clojure/core.async">core.async</a> was suggested but that seems to result in much more / more complicated code than this version.</p>


<p>The <a href="https://github.com/mneedham/neo4j-meetup/blob/master/src/neo4j_meetup/core.clj#L58">code is on github</a> if you want to take a look.</p>

