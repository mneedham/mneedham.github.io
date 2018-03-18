+++
draft = false
date="2014-08-11 16:47:35"
title="R: Grouping by two variables"
tag=['r-2']
category=['R']
+++

<p>In my continued playing around with R and meetup data I wanted to group a data table by two variables - day and event - so I could see the most popular day of the week for meetups and which events we'd held on those days.</p>


<p>I started off with the following data table:</p>



~~~r

> head(eventsOf2014, 20)
      eventTime                                              event.name rsvps            datetime       day monthYear
16 1.393351e+12                                         Intro to Graphs    38 2014-02-25 18:00:00   Tuesday   02-2014
17 1.403635e+12                                         Intro to Graphs    44 2014-06-24 18:30:00   Tuesday   06-2014
19 1.404844e+12                                         Intro to Graphs    38 2014-07-08 18:30:00   Tuesday   07-2014
28 1.398796e+12                                         Intro to Graphs    45 2014-04-29 18:30:00   Tuesday   04-2014
31 1.395772e+12                                         Intro to Graphs    56 2014-03-25 18:30:00   Tuesday   03-2014
41 1.406054e+12                                         Intro to Graphs    12 2014-07-22 18:30:00   Tuesday   07-2014
49 1.395167e+12                                         Intro to Graphs    45 2014-03-18 18:30:00   Tuesday   03-2014
50 1.401907e+12                                         Intro to Graphs    35 2014-06-04 18:30:00 Wednesday   06-2014
51 1.400006e+12                                         Intro to Graphs    31 2014-05-13 18:30:00   Tuesday   05-2014
54 1.392142e+12                                         Intro to Graphs    35 2014-02-11 18:00:00   Tuesday   02-2014
59 1.400611e+12                                         Intro to Graphs    53 2014-05-20 18:30:00   Tuesday   05-2014
61 1.390932e+12                                         Intro to Graphs    22 2014-01-28 18:00:00   Tuesday   01-2014
70 1.397587e+12                                         Intro to Graphs    47 2014-04-15 18:30:00   Tuesday   04-2014
7  1.402425e+12       Hands On Intro to Cypher - Neo4j's Query Language    38 2014-06-10 18:30:00   Tuesday   06-2014
25 1.397155e+12       Hands On Intro to Cypher - Neo4j's Query Language    28 2014-04-10 18:30:00  Thursday   04-2014
44 1.404326e+12       Hands On Intro to Cypher - Neo4j's Query Language    43 2014-07-02 18:30:00 Wednesday   07-2014
46 1.398364e+12       Hands On Intro to Cypher - Neo4j's Query Language    30 2014-04-24 18:30:00  Thursday   04-2014
65 1.400783e+12       Hands On Intro to Cypher - Neo4j's Query Language    26 2014-05-22 18:30:00  Thursday   05-2014
5  1.403203e+12 Hands on build your first Neo4j app for Java developers    34 2014-06-19 18:30:00  Thursday   06-2014
34 1.399574e+12 Hands on build your first Neo4j app for Java developers    28 2014-05-08 18:30:00  Thursday   05-2014
~~~

<p>I was able to work out the average number of RSVPs per day with the following code using plyr:                                                                                                                                                                                                                  </p>



~~~r

> ddply(eventsOf2014, .(day=format(datetime, "%A")), summarise, 
        count=length(datetime),
        rsvps=sum(rsvps),
        rsvpsPerEvent = rsvps / count)

        day count rsvps rsvpsPerEvent
1  Thursday     5   146      29.20000
2   Tuesday    13   504      38.76923
3 Wednesday     2    78      39.00000
~~~

<p>The next step was to show the names of events that happened on those days next to the row for that day. To do this we can make use of the <a href="http://stat.ethz.ch/R-manual/R-patched/library/base/html/paste.html">paste</a> function like so:</p>



~~~r

> ddply(eventsOf2014, .(day=format(datetime, "%A")), summarise, 
        events = paste(unique(event.name), collapse = ","),
        count=length(datetime),
        rsvps=sum(rsvps),
        rsvpsPerEvent = rsvps / count)

        day                                                                                                    events count rsvps rsvpsPerEvent
1  Thursday Hands On Intro to Cypher - Neo4j's Query Language,Hands on build your first Neo4j app for Java developers     5   146      29.20000
2   Tuesday                                         Intro to Graphs,Hands On Intro to Cypher - Neo4j's Query Language    13   504      38.76923
3 Wednesday                                         Intro to Graphs,Hands On Intro to Cypher - Neo4j's Query Language     2    78      39.00000
~~~

<p>If we wanted to drill down further and see the number of RSVPs per day per event type then we could instead group by the day and event name:</p>



~~~r

> ddply(eventsOf2014, .(day=format(datetime, "%A"), event.name), summarise, 
        count=length(datetime),
        rsvps=sum(rsvps),
        rsvpsPerEvent = rsvps / count)

        day                                              event.name count rsvps rsvpsPerEvent
1  Thursday Hands on build your first Neo4j app for Java developers     2    62      31.00000
2  Thursday       Hands On Intro to Cypher - Neo4j's Query Language     3    84      28.00000
3   Tuesday       Hands On Intro to Cypher - Neo4j's Query Language     1    38      38.00000
4   Tuesday                                         Intro to Graphs    12   466      38.83333
5 Wednesday       Hands On Intro to Cypher - Neo4j's Query Language     1    43      43.00000
6 Wednesday                                         Intro to Graphs     1    35      35.00000
~~~

<p>There are too few data points for some of those to make any decisions but as we gather more data hopefully we'll see if there's a trend for people to come to events on certain days or not.</p>

