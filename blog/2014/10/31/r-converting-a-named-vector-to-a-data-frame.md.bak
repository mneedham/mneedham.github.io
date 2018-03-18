+++
draft = false
date="2014-10-31 23:47:26"
title="R: Converting a named vector to a data frame"
tag=['r-2']
category=['R']
+++

<p>I've been playing around with <a href="http://igraph.org/r/">igraph's</a> <a href="http://igraph.org/r/doc/page.rank.html">page rank</a> function to see who the most central nodes in the London NoSQL scene are and I wanted to put the result in a data frame to make the data easier to work with.</p>


<p>I started off with a data frame containing pairs of people and the number of events that they'd both RSVP'd 'yes' to:</p>



~~~r

> library(dplyr)
> data %>% arrange(desc(times)) %>% head(10)
       p.name     other.name times
1  Amit Nandi Anish Mohammed    51
2  Amit Nandi Enzo Martoglio    49
3       louis          zheng    46
4       louis     Raja Kolli    45
5  Raja Kolli Enzo Martoglio    43
6  Amit Nandi     Raja Kolli    42
7       zheng Anish Mohammed    42
8  Raja Kolli          Rohit    41
9  Amit Nandi          zheng    40
10      louis          Rohit    40
~~~

<p>I actually had ~ 900,000 such rows in the data frame:</p>



~~~r

> length(data[,1])
[1] 985664
~~~

<p>I ran page rank over the data set like so:</p>



~~~r

g = graph.data.frame(data, directed = F)
pr = page.rank(g)$vector
~~~

<p>If we evaluate <cite>pr</cite> we can see the person's name and their page rank:</p>



~~~r

> head(pr)
Ioanna Eirini          Mjay       Baktash      madhuban    Karl Prior   Keith Bolam 
    0.0002190     0.0001206     0.0001524     0.0008819     0.0001240     0.0005702 
~~~

<p>I initially tried to convert this to a data frame with the following code...</p>



~~~r

> head(data.frame(pr))
                     pr
Ioanna Eirini 0.0002190
Mjay          0.0001206
Baktash       0.0001524
madhuban      0.0008819
Karl Prior    0.0001240
Keith Bolam   0.0005702
~~~

<p>...which unfortunately didn't create a column for the person's name. </p>



~~~R

> colnames(data.frame(pr))
[1] "pr"
~~~

<p><a href="http://nicolewhite.github.io/">Nicole</a> pointed out that I actually had a <a href="http://www.r-tutor.com/r-introduction/vector/named-vector-members">named vector</a> and would need to explicitly extract the names from that vector into the data frame. I ended up with this:</p>



~~~r

> prDf = data.frame(name = names(pr), rank = pr)
> head(prDf)
                       name      rank
Ioanna Eirini Ioanna Eirini 0.0002190
Mjay                   Mjay 0.0001206
Baktash             Baktash 0.0001524
madhuban           madhuban 0.0008819
Karl Prior       Karl Prior 0.0001240
Keith Bolam     Keith Bolam 0.0005702
~~~

<p>We can now sort the data frame to find the most central people on the NoSQL London scene based on meetup attendance:</p>



~~~r

> data.frame(prDf) %>%
+   arrange(desc(pr)) %>%
+   head(10)
             name     rank
1           louis 0.001708
2       Kannappan 0.001657
3           zheng 0.001514
4    Peter Morgan 0.001492
5      Ricki Long 0.001437
6      Raja Kolli 0.001416
7      Amit Nandi 0.001411
8  Enzo Martoglio 0.001396
9           Chris 0.001327
10          Rohit 0.001305
~~~
