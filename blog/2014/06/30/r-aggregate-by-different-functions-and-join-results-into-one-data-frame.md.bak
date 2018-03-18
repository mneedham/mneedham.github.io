+++
draft = false
date="2014-06-30 22:47:44"
title="R: Aggregate by different functions and join results into one data frame"
tag=['r-2']
category=['R']
+++

<p>In continuing <a href="http://www.markhneedham.com/blog/2014/06/30/neo4jr-grouping-meetup-members-by-join-timestamp/">my</a> <a href="http://www.markhneedham.com/blog/2014/06/30/r-order-by-data-frame-column-and-take-top-10-rows/">analysis</a> of the London Neo4j meetup group using R I wanted to see which days of the week we organise meetups and how many people RSVP affirmatively by the day.</p>


<p>I started out with this query which returns each event and the number of 'yes' RSVPS:</p>



~~~r

library(Rneo4j)
timestampToDate <- function(x) as.POSIXct(x / 1000, origin="1970-01-01")

query = "MATCH (g:Group {name: \"Neo4j - London User Group\"})-[:HOSTED_EVENT]->(event)<-[:TO]-({response: 'yes'})<-[:RSVPD]-()
         WHERE (event.time + event.utc_offset) < timestamp()
         RETURN event.time + event.utc_offset AS eventTime, COUNT(*) AS rsvps"
events = cypher(graph, query)
events$datetime <- timestampToDate(events$eventTime)
~~~


~~~r

      eventTime rsvps            datetime
1  1.314815e+12     3 2011-08-31 19:30:00
2  1.337798e+12    13 2012-05-23 19:30:00
3  1.383070e+12    29 2013-10-29 18:00:00
4  1.362474e+12     5 2013-03-05 09:00:00
5  1.369852e+12    66 2013-05-29 19:30:00
6  1.385572e+12    67 2013-11-27 17:00:00
7  1.392142e+12    35 2014-02-11 18:00:00
8  1.364321e+12    23 2013-03-26 18:00:00
9  1.372183e+12    22 2013-06-25 19:00:00
10 1.401300e+12    60 2014-05-28 19:00:00
~~~

<p>I wanted to get a data frame which had these columns:</p>



~~~bash

Day of Week | RSVPs | Number of Events
~~~

<p>Getting the number of events for a given day was quite easy as I could use the groupBy function I wrote last time:</p>



~~~r

groupBy = function(dates, format) {
  dd = aggregate(dates, by=list(format(dates, format)), function(x) length(x))
  colnames(dd) = c("key", "count")
  dd
}

> groupBy(events$datetime, "%A")
        key count
1  Thursday     9
2   Tuesday    24
3 Wednesday    35
~~~

<p>The next step is to get the sum of RSVPs by the day which we can get with the following code:</p>



~~~r

dd = aggregate(events$rsvps, by=list(format(events$datetime, "%A")), FUN=sum)
colnames(dd) = c("key", "count")
~~~

<p>The difference between this and our previous use of the aggregate function is that we're passing in the number of RSVPs for each event and then grouping by the day and <a href="http://stackoverflow.com/questions/1660124/how-to-group-columns-by-sum-in-r">summing up the values for each day</a> rather than counting how many occurrences there are.</p>


<p>If we evaluate 'dd' we get the following:</p>



~~~r

> dd
        key count
1  Thursday   194
2   Tuesday   740
3 Wednesday  1467
~~~

<p>We now have two data tables with a very similar shape and it turns out there's a function called <a href="http://stat.ethz.ch/R-manual/R-devel/library/base/html/merge.html">merge</a> which makes it very easy to convert these two data frames into a single one:</p>



~~~r

x = merge(groupBy(events$datetime, "%A"), dd, by = "key")
colnames(x) = c("day", "events", "rsvps")
~~~


~~~r

> x
        day events rsvps
1  Thursday      9   194
2   Tuesday     24   740
3 Wednesday     35  1467
~~~

<p>We could now choose to order our new data frame by number of events descending:</p>



~~~r

> x[order(-x$events),]
        day events rsvps
3 Wednesday     35  1467
2   Tuesday     24   740
1  Thursday      9   194
~~~

<p>We might also add an extra column to calculate the average number of RSVPs per day:</p>



~~~r

> x$rsvpsPerEvent = x$rsvps / x$events
> x
        day events rsvps rsvpsPerEvent
1  Thursday      9   194      21.55556
2   Tuesday     24   740      30.83333
3 Wednesday     35  1467      41.91429
~~~

<p>I'm still getting the hang of it but already it seems like the combination of <a href="https://github.com/nicolewhite/Rneo4j">R and Neo4j</a> allows us to quickly get insights into our data and I've barely scratched the surface!</p>

