+++
draft = false
date="2013-09-22 21:23:25"
title="Clojure/Emacs/nrepl: Ctrl X + Ctrl E leads to 'FileNotFoundException Could not locate […] on classpath'"
tag=['clojure', 'nrepl']
category=['Clojure']
+++

<p>I've been playing around with Clojure using <a href="http://www.gnu.org/software/emacs/">Emacs</a> and <a href="https://github.com/clojure/tools.nrepl">nrepl</a> recently and my normal work flow is to write some code in Emacs and then have it evaluated in nrepl by typing <cite>Ctrl X + Ctrl E</cite> at the end of the function.</p>


<p>I tried this once recently and got the following exception instead of a successful evaluation:</p>



~~~text

FileNotFoundException Could not locate ranking_algorithms/ranking__init.class or ranking_algorithms/ranking.clj on classpath: clojure.lang.RT.load (RT.java:432)
~~~

<p>I was a bit surprised because I had nrepl running already (via <cite>(Meta + X) + Enter + nrepl-jack-in</cite>) and I'd only ever seen that exception refer to dependencies which weren't in my project.clj file at the time I launched nrepl.</p>


<p>I eventually came across <a href="http://stackoverflow.com/questions/15511840/emacs-clojure-compiling-error">this StackOverflow post</a> which suggested that you either launch nrepl using leiningen and then connect to it from Emacs or have your project.clj open when running <cite>(Meta + X) + Enter +  nrepl-jack-in</cite>.</p>


<p>To launch nrepl from leiningen we'd run the following command from the terminal:</p>



~~~bash

$ lein repl
nREPL server started on port 52265
REPL-y 0.1.0-beta10
Clojure 1.4.0
    Exit: Control+D or (exit) or (quit)
Commands: (user/help)
    Docs: (doc function-name-here)
          (find-doc "part-of-name-here")
  Source: (source function-name-here)
          (user/sourcery function-name-here)
 Javadoc: (javadoc java-object-or-class-here)
Examples from clojuredocs.org: [clojuredocs or cdoc]
          (user/clojuredocs name-here)
          (user/clojuredocs "ns-here" "name-here")
~~~

<p>We can then connect to that nrepl server from Emacs by typing <cite>(Meta + X) + Enter + nrepl</cite> which seems to work quite nicely.</p>


<p>To check the <cite>nrepl-jack-in</cite> approach works when we've got project.clj open we need to first kill the existing server by typing <cite>(Meta + X) + Enter + nrepl-quit</cite>.</p>
 

<p>Now if we type <cite>(Meta + X) + Enter + nrepl-jack-in</cite> our functions are evaluated correctly and all is well with the world again.</p>

