+++
draft = false
date="2013-09-26 07:47:34"
title="Clojure: Writing JSON to a file/reading JSON from a file"
tag=['clojure']
category=['Clojure']
+++

<p>A few weeks ago I described how I'd <a href="http://www.markhneedham.com/blog/2013/08/26/clojureenlive-screen-scraping-a-html-file-from-disk/">scraped football matches using Clojure's Enlive</a>, and the next step after translating the HTML representation into a Clojure map was to save it as a JSON document.</p>


<p>I decided to follow a two step process to achieve this:</p>


<ul>
<li>Convert hash to JSON string</li>
<li>Write JSON string to file</li>
</ul>

<p>I imagine there's probably a way to convert the hash to a stream and pipe that into a file but my JSON document isn't very large so I think this way is ok for now.</p>


<p><cite><a href="https://github.com/clojure/data.json">data.json</a></cite> seems to be the way to go to convert a Hash to a JSON string and I had the following code:</p>



~~~lisp

> (require '[clojure.data.json :as json])
nil

> (json/write-str { :key1 "val1" :key2 "val2" })
"{\"key2\":\"val2\",\"key1\":\"val1\"}"
~~~

<p>The next step was to write that into a file and <a href="http://stackoverflow.com/questions/7756909/in-clojure-1-3-how-to-read-and-write-a-file">this StackOverflow post describes a couple of ways that we can do this</a>:</p>



~~~lisp

> (use 'clojure.java.io)
> (with-open [wrtr (writer "/tmp/test.json")]
    (.write wrtr (json/write-str {:key1 "val1" :key2 "val2"})))
~~~

<p>or</p>



~~~lisp

> (spit "/tmp/test.json" (json/write-str {:key1 "val1" :key2 "val2"}))
~~~

<p>Now I wanted to read the file back into a hash and I started with the following:</p>



~~~lisp

> (json/read-str (slurp "/tmp/test.json"))
{"key2" "val2", "key1" "val1"}
~~~

<p>That's not bad but I wanted the keys to be what I know as symbols (e.g. ':key1') from Ruby land. I re-learnt that this is called a keyword in Clojure.</p>


<p>Since I'm not very good at reading the documentation I wrote a function to convert all the keys in a map from strings to keywords:</p>



~~~lisp

> (defn string-keys-to-symbols [map]
    (reduce #(assoc %1 (-> (key %2) keyword) (val %2)) {} map))

> (string-keys-to-symbols (json/read-str (slurp "/tmp/test.json")))
{:key1 "val1", :key2 "val2"}
~~~

<p>What I should have done is pass the <cite><a href="http://clojuredocs.org/clojure_core/clojure.core/keyword">keyword</a></cite> function as an argument to <cite>read-str</cite> instead:</p>



~~~lisp

> (json/read-str (slurp "/tmp/test.json") :key-fn keyword)
{:key2 "val2", :key1 "val1"}
~~~

<p>Simple!</p>

