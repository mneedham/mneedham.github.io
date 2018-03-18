+++
draft = false
date="2014-08-29 00:25:33"
title="R: Grouping by week, month, quarter"
tag=['r-2']
category=['R']
+++

<p>In my continued playing around with R and <a href="https://github.com/mneedham/neo4j-meetup">meetup data</a> I wanted to have a look at when people joined the London Neo4j group based on week, month or quarter of the year to see when they were most likely to do so.</p>


<p>I started with the following query to get back the join timestamps:</p>



~~~r

library(RNeo4j)
query = "MATCH (:Person)-[:HAS_MEETUP_PROFILE]->()-[:HAS_MEMBERSHIP]->(membership)-[:OF_GROUP]->(g:Group {name: \"Neo4j - London User Group\"})
         RETURN membership.joined AS joinTimestamp"
meetupMembers = cypher(graph, query)

> head(meetupMembers)
      joinTimestamp
1 1.376572e+12
2 1.379491e+12
3 1.349454e+12
4 1.383127e+12
5 1.372239e+12
6 1.330295e+12
~~~

<p>The first step was to get <cite>joinDate</cite> into a nicer format that we can use in R more easily:</p>



~~~r

timestampToDate <- function(x) as.POSIXct(x / 1000, origin="1970-01-01", tz = "GMT")
meetupMembers$joinDate <- timestampToDate(meetupMembers$joinTimestamp)

> head(meetupMembers)
  joinTimestamp            joinDate
1  1.376572e+12 2013-08-15 13:13:40
2  1.379491e+12 2013-09-18 07:55:11
3  1.349454e+12 2012-10-05 16:28:04
4  1.383127e+12 2013-10-30 09:59:03
5  1.372239e+12 2013-06-26 09:27:40
6  1.330295e+12 2012-02-26 22:27:00
~~~

<p>Much better!</p>


<p>I started off with grouping by month and quarter and <a href="http://stackoverflow.com/questions/6242955/converting-year-and-month-to-a-date-in-r">came across</a> the excellent <a href="http://cran.r-project.org/web/packages/zoo/index.html">zoo</a> library which makes it really easy to transform dates:</p>



~~~r

library(zoo)
meetupMembers$monthYear <- as.Date(as.yearmon(meetupMembers$joinDate))
meetupMembers$quarterYear <- as.Date(as.yearqtr(meetupMembers$joinDate))

> head(meetupMembers)
  joinTimestamp            joinDate  monthYear quarterYear
1  1.376572e+12 2013-08-15 13:13:40 2013-08-01  2013-07-01
2  1.379491e+12 2013-09-18 07:55:11 2013-09-01  2013-07-01
3  1.349454e+12 2012-10-05 16:28:04 2012-10-01  2012-10-01
4  1.383127e+12 2013-10-30 09:59:03 2013-10-01  2013-10-01
5  1.372239e+12 2013-06-26 09:27:40 2013-06-01  2013-04-01
6  1.330295e+12 2012-02-26 22:27:00 2012-02-01  2012-01-01
~~~

<p>The next step was to create a new data frame which grouped the data by those fields. I've been learning <a href="http://blog.rstudio.org/2014/01/17/introducing-dplyr/">dplyr</a> as part of <a href="https://www.udacity.com/course/ud651">Udacity's EDA course</a> so I thought I'd try and use that:</p>



~~~r

> head(meetupMembers %.% group_by(monthYear) %.% summarise(n = n()), 20)

    monthYear  n
1  2011-06-01 13
2  2011-07-01  4
3  2011-08-01  1
4  2011-10-01  1
5  2011-11-01  2
6  2012-01-01  4
7  2012-02-01  7
8  2012-03-01 11
9  2012-04-01  3
10 2012-05-01  9
11 2012-06-01  5
12 2012-07-01 16
13 2012-08-01 32
14 2012-09-01 14
15 2012-10-01 28
16 2012-11-01 31
17 2012-12-01  7
18 2013-01-01 52
19 2013-02-01 49
20 2013-03-01 22
~~~


~~~r

> head(meetupMembers %.% group_by(quarterYear) %.% summarise(n = n()), 20)

   quarterYear   n
1   2011-04-01  13
2   2011-07-01   5
3   2011-10-01   3
4   2012-01-01  22
5   2012-04-01  17
6   2012-07-01  62
7   2012-10-01  66
8   2013-01-01 123
9   2013-04-01 139
10  2013-07-01 117
11  2013-10-01  94
12  2014-01-01 266
13  2014-04-01 359
14  2014-07-01 216
~~~

<p>Grouping by week number is a bit trickier but we can do it with a <a href="http://stackoverflow.com/questions/11395927/how-to-subset-data-frame-by-weeks-and-then-sum">bit of transformation</a> on our initial timestamp:</p>



~~~r

meetupMembers$week <- as.Date("1970-01-01")+7*trunc((meetupMembers$joinTimestamp / 1000)/(3600*24*7))

> head(meetupMembers %.% group_by(week) %.% summarise(n = n()), 20)

         week n
1  2011-06-02 8
2  2011-06-09 4
3  2011-06-16 1
4  2011-06-30 2
5  2011-07-14 1
6  2011-07-21 1
7  2011-08-18 1
8  2011-10-13 1
9  2011-11-24 2
10 2012-01-05 1
11 2012-01-12 3
12 2012-02-09 1
13 2012-02-16 2
14 2012-02-23 4
15 2012-03-01 2
16 2012-03-08 3
17 2012-03-15 5
18 2012-03-29 1
19 2012-04-05 2
20 2012-04-19 1
~~~

<p>We can then plug that data frame into ggplot if we want to track membership sign up over time at different levels of granularity and create some bar charts of scatter plots depending on what we feel like!</p>

