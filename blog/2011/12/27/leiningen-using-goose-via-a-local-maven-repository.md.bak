+++
draft = false
date="2011-12-27 12:48:17"
title="Leiningen: Using goose via a local Maven repository"
tag=['clojure', 'goose', 'leiningen']
category=['Clojure']
+++

I've been playing around a little bit with <a href="https://github.com/jiminoc/goose">goose</a> - a HTML content/article extractor - originally in Java but later in clojure where I needed to work out how to include goose and all its dependencies via <a href="https://github.com/technomancy/leiningen">Leiningen</a>.

goose isn't included in a Maven repository so I needed to create a local repository, something which I've got stuck on in the past.

Luckily <a href="http://www.pgrs.net/2011/10/30/using-local-jars-with-leiningen/">Paul Gross has written a cool blog post</a> explaining how his team got past this problem.

Following the instructions from Paul's post this is how I got goose playing nicely with clojure:

Inside my clojure project:

~~~text

/Users/mneedham/github/android/text-extraction $ mkdir maven_repository
~~~

I then ran the following command from where I had goose checked out on my machine:


~~~text

mvn install:install-file -Dfile=target/goose-2.1.6.jar -DartifactId=goose -Dversion=2.1.6 -DgroupId=goose -Dpackaging=jar -DlocalRepositoryPath=/Users/mneedham/github/android/text-extraction/maven_repository -DpomFile=pom.xml 
~~~

I added the repository and goose dependency to my project.clj file which now looks like this:


~~~text

(defproject textextraction "0.1.0"
  :description "Extract text from urls"
  :dependencies [[org.clojure/clojure "1.2.0"],
		 [org.clojure/clojure-contrib "1.2.0"],
		 [ring/ring-jetty-adapter "0.3.11"],
         [compojure "0.6.4"]
         [goose "2.1.6"]]
  :dev-dependencies [[swank-clojure "1.2.1"]]
  :repositories {"local" ~(str (.toURI (java.io.File. "maven_repository")))}
  :main textextraction.main)
~~~

I then run:


~~~text

/Users/mneedham/github/android/text-extraction $ lein run
~~~

And goose and all its dependencies are included in the 'lib' directory.
