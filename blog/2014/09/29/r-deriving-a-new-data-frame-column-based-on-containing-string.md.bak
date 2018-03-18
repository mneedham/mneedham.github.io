+++
draft = false
date="2014-09-29 21:37:21"
title="R: Deriving a new data frame column based on containing string"
tag=['r-2', 'rstats']
category=['R']
+++

<p>I've been playing around with R data frames a bit more and one thing I wanted to do was derive a new column based on the text contained in the existing column.</p>


<p>I started with something like this:</p>



~~~r

> x = data.frame(name = c("Java Hackathon", "Intro to Graphs", "Hands on Cypher"))
> x
             name
1  Java Hackathon
2 Intro to Graphs
3 Hands on Cypher
~~~

<p>And I wanted to derive a new column based on whether or not the session was a practical one. The <a href="https://stat.ethz.ch/R-manual/R-devel/library/base/html/grep.html">grepl</a> function seemed to be the best tool for the job:</p>



~~~r

> grepl("Hackathon|Hands on|Hands On", x$name)
[1]  TRUE FALSE  TRUE
~~~

<p>We can then add a column to our data frame with that output:</p>



~~~r

x$practical = grepl("Hackathon|Hands on|Hands On", x$name)
~~~

<p>And we end up with the following:</p>



~~~r

> x
             name practical
1  Java Hackathon      TRUE
2 Intro to Graphs     FALSE
3 Hands on Cypher      TRUE
~~~

<p>Not too tricky but it took me a bit too long to figure it out so I thought I'd save future Mark some time!</p>

