+++
draft = false
date="2014-07-02 06:30:50"
title="R/plyr: ddply - Renaming the grouping/generated column when grouping by date"
tag=['r-2']
category=['R']
+++

<p>On <a href="https://twitter.com/_nicolemargaret">Nicole's</a> recommendation I've been having a look at R's <a href="http://cran.r-project.org/web/packages/plyr/index.html">plyr</a> package to see if I could simplify my <a href="http://www.markhneedham.com/blog/2014/06/30/neo4jr-grouping-meetup-members-by-join-timestamp/">meetup analysis</a> and I started by translating my code that grouped meetup join dates by day of the week.</p>


<p>To refresh, the code without plyr looked like this:</p>



~~~r

library(Rneo4j)
timestampToDate <- function(x) as.POSIXct(x / 1000, origin="1970-01-01")

query = "MATCH (:Person)-[:HAS_MEETUP_PROFILE]->()-[:HAS_MEMBERSHIP]->(membership)-[:OF_GROUP]->(g:Group {name: \"Neo4j - London User Group\"})
         RETURN membership.joined AS joinDate"
meetupMembers = cypher(graph, query)
meetupMembers$joined <- timestampToDate(meetupMembers$joinDate)

dd = aggregate(meetupMembers$joined, by=list(format(meetupMembers$joined, "%A")), function(x) length(x))
colnames(dd) = c("dayOfWeek", "count")
~~~

<p>which returns the following:</p>



~~~r

> dd
  dayOfWeek count
1    Friday   135
2    Monday   287
3  Saturday    80
4    Sunday   102
5  Thursday   187
6   Tuesday   286
7 Wednesday   211
~~~

<p>We need to use <a href="http://seananderson.ca/courses/12-plyr/plyr_2012.pdf">plyr's</a> ddply function which takes a data frame and transforms it into another one.</p>


<p>To refresh, this is what the initial data frame looks like:</p>



~~~r

> meetupMembers[1:10,]
       joinDate              joined
1  1.376572e+12 2013-08-15 14:13:40
2  1.379491e+12 2013-09-18 08:55:11
3  1.349454e+12 2012-10-05 17:28:04
4  1.383127e+12 2013-10-30 09:59:03
5  1.372239e+12 2013-06-26 10:27:40
6  1.330295e+12 2012-02-26 22:27:00
7  1.379676e+12 2013-09-20 12:22:39
8  1.398462e+12 2014-04-25 22:41:19
9  1.331734e+12 2012-03-14 14:11:43
10 1.396874e+12 2014-04-07 13:32:26
~~~

<p>Most of the examples of using ddply show how to group by a specific 'column' e.g. joined but I want to group by part of the value in that column and eventually <a href="http://stackoverflow.com/questions/18110110/r-ddply-function-applied-to-certain-months-obtained-from-date-field">came across an example</a> which showed how to do it:</p>



~~~r

> ddply(meetupMembers, .(format(joined, "%A")), function(x) {
    count <- length(x$joined)
    data.frame(count = count)
  })
  format(joined, "%A") count
1               Friday   135
2               Monday   287
3             Saturday    80
4               Sunday   102
5             Thursday   187
6              Tuesday   286
7            Wednesday   211
~~~

<p>Unfortunately the generated column heading  for the group by key isn't very readable and it took me way longer than it should have to work out how to name it as I wanted! This is how you do it:</p>



~~~r

> ddply(meetupMembers, .(dayOfWeek=format(joined, "%A")), function(x) {
    count <- length(x$joined)
    data.frame(count = count)
  })
  dayOfWeek count
1    Friday   135
2    Monday   287
3  Saturday    80
4    Sunday   102
5  Thursday   187
6   Tuesday   286
7 Wednesday   211
~~~

<p>If we want to sort that in descending order by 'count' we can <a href="http://stackoverflow.com/questions/5839265/r-plyr-ordering-results-from-ddply">wrap that ddply in another one</a>:</p>



~~~r

> ddply(ddply(meetupMembers, .(dayOfWeek=format(joined, "%A")), function(x) {
    count <- length(x$joined)
    data.frame(count = count)
  }), .(count = count* -1))
  dayOfWeek count
1    Monday   287
2   Tuesday   286
3 Wednesday   211
4  Thursday   187
5    Friday   135
6    Sunday   102
7  Saturday    80
~~~

<p>From reading a bit about ddply I gather that its slower than using some other approaches e.g. <a href="http://cran.r-project.org/web/packages/data.table/index.html">data.table</a> but I'm not dealing with much data so it's not an issue yet.</p>


<p>Once I got the hang of how it worked ddply was quite nice to work with so I think I'll have a go at translating some of my other code to use it now.</p>

