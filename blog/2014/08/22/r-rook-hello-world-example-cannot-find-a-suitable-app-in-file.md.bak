+++
draft = false
date="2014-08-22 11:05:54"
title="R: Rook - Hello world example - 'Cannot find a suitable app in file'"
tag=['r-2']
category=['R']
+++

<p>I've been playing around with the <a href="http://cran.r-project.org/web/packages/Rook/README.html">Rook</a> library and struggled a bit getting a basic Hello World application up and running so I thought I should document it for future me.</p>


<p>I wanted to spin up a web server using Rook and serve a page with the text 'Hello World'. I <a href="https://docs.google.com/presentation/d/1AT8nQo6jrZ9SwPgdwqkHZI_2SeqGQormy-EWWmm_rlk/edit#slide=id.i112">started with the following code</a>:</p>



~~~r

library(Rook)
s <- Rhttpd$new()

s$add(name='MyApp',app='helloworld.R')
s$start()
s$browse("MyApp")
~~~

<p>where <cite>helloWorld.R</cite> contained the following code:</p>



~~~r

function(env){ 
  list(
    status=200,
    headers = list(
      'Content-Type' = 'text/html'
    ),
    body = paste('<h1>Hello World!</h1>')
  )
}
~~~

<p>Unfortunately that failed on the 's$add' line with the following error message:</p>



~~~r

> s$add(name='MyApp',app='helloworld.R')
Error in .Object$initialize(...) : 
  Cannot find a suitable app in file helloworld.R
~~~

<p>I hadn't realised that you actually need to assign that function to a variable 'app' in order for it to be picked up:</p>



~~~r

app <- function(env){ 
  list(
    status=200,
    headers = list(
      'Content-Type' = 'text/html'
    ),
    body = paste('<h1>Hello World!</h1>')
  )
}
~~~

<p>Once I fixed that everything seemed to work as expected:s</p>



~~~r

> s
Server started on 127.0.0.1:27120
[1] MyApp http://127.0.0.1:27120/custom/MyApp

Call browse() with an index number or name to run an application.
~~~
