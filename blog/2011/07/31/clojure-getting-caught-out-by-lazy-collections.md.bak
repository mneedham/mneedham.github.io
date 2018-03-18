+++
draft = false
date="2011-07-31 21:40:35"
title="Clojure: Getting caught out by lazy collections"
tag=['clojure']
category=['Clojure']
+++

Most of the work that I've done with Clojure has involved running a bunch of functions directly in the REPL or through Leiningen's <cite>run</cite> target which led to me getting caught out when I created a JAR and tried to run that.

As I <a href="http://www.markhneedham.com/blog/2011/07/10/clojure-language-as-thought-shaper/">mentioned a few weeks ago</a> I've been rewriting part of our system in Clojure to see how the design would differ and a couple of levels down the Clojure version comprises of applying a map function over a collection of documents.

The code in question originally looked like this:


~~~lisp

(ns aim.main (:gen-class))

(defn import-zip-file [zipFile working-dir]
  (let [xml-files (filter xml-file? (unzip zipFile working-dir))]
    (map import-document xml-files)))

(defn -main [& args]
  (import-zip-file "our/file.zip", "/tmp/unzip/to/here"))
~~~

Which led to absolutely nothing happening when run like this!


~~~text

$ lein uberjar && java -jar my-project-0.1.0-standalone.jar 
~~~

I originally assumed that I had something wrong in the code but my colleague Uday reminded me that collections in Clojure are lazily evaluated and there was nothing in the code that would force the evaluation of ours.

In this situation we had to wrap the <cite>map</cite> with a <cite><a href="http://clojure.github.com/clojure/clojure.core-api.html#clojure.core/doall">doall</a></cite> in order to force evaluation of the collection:


~~~lisp

(ns aim.main (:gen-class))

(defn import-zip-file [zip-file working-dir]
  (let [xml-files (filter xml-file? (unzip zip-file working-dir))]
    (doall (map import-document xml-files))))

(defn -main [& args]
  (import-zip-file "our/file.zip", "/tmp/unzip/to/here"))
~~~

When we run the code in the REPL or through 'lein run' the code is being eagerly evaluated as far as I understand it which is why we see a different behaviour than when we run it on its own.

I also got caught out on another occasion where I tried to pass around a collection of input streams which I'd retrieved from a zip file only to realise that when the code which used the input stream got evaluated the ZIP file was no longer around!
