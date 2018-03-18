+++
draft = false
date="2014-08-29 09:13:00"
title="R: dplyr - group_by dynamic or programmatic field / variable (Error: index out of bounds)"
tag=['r-2']
category=['R']
+++

<p>In my <a href="http://www.markhneedham.com/blog/2014/08/29/r-grouping-by-week-month-quarter/">last blog post</a> I showed how to group timestamp based data by week, month and quarter and by the end we had the following code samples using <a href="http://cran.r-project.org/web/packages/dplyr/index.html">dplyr</a> and <a href="http://cran.r-project.org/web/packages/zoo/index.html">zoo</a>:</p>



~~~r

library(RNeo4j)
library(zoo)

timestampToDate <- function(x) as.POSIXct(x / 1000, origin="1970-01-01", tz = "GMT")

query = "MATCH (:Person)-[:HAS_MEETUP_PROFILE]->()-[:HAS_MEMBERSHIP]->(membership)-[:OF_GROUP]->(g:Group {name: \"Neo4j - London User Group\"})
         RETURN membership.joined AS joinTimestamp"
meetupMembers = cypher(graph, query)

meetupMembers$joinDate <- timestampToDate(meetupMembers$joinTimestamp)
meetupMembers$monthYear <- as.Date(as.yearmon(meetupMembers$joinDate))
meetupMembers$quarterYear <- as.Date(as.yearqtr(meetupMembers$joinDate))

meetupMembers %.% group_by(week) %.% summarise(n = n())
meetupMembers %.% group_by(monthYear) %.% summarise(n = n())
meetupMembers %.% group_by(quarterYear) %.% summarise(n = n())
~~~

<p>As you can see there's quite a bit of duplication going on - the only thing that changes in the last 3 lines is the name of the field that we want to group by. </p>


<p>I wanted to pull this code out into a function and my first attempt was this:</p>



~~~r

groupMembersBy = function(field) {
  meetupMembers %.% group_by(field) %.% summarise(n = n())
}
~~~

<p>And now if we try to group by week:</p>



~~~r

> groupMembersBy("week")
 Show Traceback
 
 Rerun with Debug
 Error: index out of bounds 
~~~

<p>It turns out if we want to do this then <a href="http://stackoverflow.com/questions/21815060/dplyr-how-to-use-group-by-inside-a-function">we actually want the <cite>regroup</cite> function rather than <cite>group_by</cite></a>:</p>



~~~r

groupMembersBy = function(field) {
  meetupMembers %.% regroup(list(field)) %.% summarise(n = n())
}
~~~

<p>And now if we group by week:</p>



~~~r

> head(groupMembersBy("week"), 20)
Source: local data frame [20 x 2]

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

<p>Much better!</p>

