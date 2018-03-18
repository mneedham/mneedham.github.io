+++
draft = false
date="2014-06-30 00:06:54"
title="Neo4j/R: Grouping meetup members by join timestamp"
tag=['neo4j', 'r-2']
category=['neo4j', 'R']
+++

<p>I wanted to do some ad-hoc analysis on the join date of members of the <a href="http://www.meetup.com/graphdb-london/">Neo4j London meetup group</a> and since cypher doesn't yet have functions for dealings with dates I thought I'd give R a try.</p>


<p>I started off by executing a cypher query which returned the join timestamp of all the group members using Nicole White's <a href="https://github.com/nicolewhite/Rneo4j">RNeo4j</a> package:</p>



~~~r

> library(Rneo4j)

> query = "match (:Person)-[:HAS_MEETUP_PROFILE]->()-[:HAS_MEMBERSHIP]->(membership)-[:OF_GROUP]->(g:Group {name: \"Neo4j - London User Group\"})
RETURN membership.joined AS joinDate"

> meetupMembers = cypher(graph, query)

> meetupMembers[1:5,]
[1] 1.389107e+12 1.376572e+12 1.379491e+12 1.349454e+12 1.383127e+12
~~~

<p>I realised that if I was going to do any date manipulation I'd need to translate the timestamp into an R friendly format so I wrote the following function to help me do that:</p>



~~~r

> timestampToDate <- function(x) as.POSIXct(x / 1000, origin="1970-01-01")
~~~

<p>I added another column to the data frame with this date representation:</p>



~~~r

> meetupMembers$joined <- timestampToDate(meetupMembers$joinDate)

> meetupMembers[1:5,]
      joinDate              joined
1 1.389107e+12 2014-01-07 15:08:40
2 1.376572e+12 2013-08-15 14:13:40
3 1.379491e+12 2013-09-18 08:55:11
4 1.349454e+12 2012-10-05 17:28:04
5 1.383127e+12 2013-10-30 09:59:03
~~~

<p>Next I wanted to group those timestamps by the combination of month + year for which the <a href="http://www.statmethods.net/management/aggregate.html">aggregate</a> and <a href="http://www.statmethods.net/input/dates.html">format</a> functions came in handy:</p>



~~~r

> dd = aggregate(meetupMembers$joined, by=list(format(meetupMembers$joined, "%m-%Y")), function(x) length(x))
> colnames(dd) = c("month", "count")
> dd
     month count
1  01-2012     4
2  01-2013    52
3  01-2014    88
4  02-2012     7
5  02-2013    52
6  02-2014    91
7  03-2012    12
8  03-2013    23
9  03-2014    93
10 04-2012     3
11 04-2013    34
12 04-2014   119
13 05-2012     9
14 05-2013    69
15 05-2014   102
16 06-2011    14
17 06-2012     5
18 06-2013    39
19 06-2014   114
20 07-2011     4
21 07-2012    16
22 07-2013    20
23 08-2011     2
24 08-2012    34
25 08-2013    50
26 09-2012    14
27 09-2013    52
28 10-2011     2
29 10-2012    29
30 10-2013    42
31 11-2011     2
32 11-2012    31
33 11-2013    34
34 12-2012     7
35 12-2013    19
~~~

<p>I wanted to be able to group by different date formats so I created the following function to make life easier:</p>



~~~r

groupBy = function(dates, format) {
  dd = aggregate(dates, by= list(format(dates, format)), function(x) length(x))
  colnames(dd) = c("key", "count")
  dd
}
~~~

<p>Now we can find the join dates grouped by year:</p>



~~~r

> groupBy(meetupMembers$joined, "%Y")
   key count
1 2011    24
2 2012   171
3 2013   486
4 2014   607
~~~

<p>or by day:</p>



~~~r

> groupBy(meetupMembers$joined, "%A")
        key count
1    Friday   135
2    Monday   287
3  Saturday    80
4    Sunday   102
5  Thursday   187
6   Tuesday   286
7 Wednesday   211
~~~

<p>or by month:</p>



~~~r

> groupBy(meetupMembers$joined, "%m")
   key count
1   01   144
2   02   150
3   03   128
4   04   156
5   05   180
6   06   172
7   07    40
8   08    86
9   09    66
10  10    73
11  11    67
12  12    26
~~~

<p>I found the 'by day' grouping interesting as I had the impression that the huge majority of people joined meetup groups on a Monday but the difference between Monday and Tuesday isn't significant. 60% of the joins happen between Monday and Wednesday.</p>


<p>The 'by month' grouping is a bit skewed by the fact we're only half way into 2014 and there have been a lot more people joining this year than in previous years.</p>
 

<p>If we <a href="https://stat.ethz.ch/pipermail/r-help/2012-July/319446.html">exclude this year</a> then the spread is more uniform with a slight dip in December:</p>



~~~r

> groupBy(meetupMembers$joined[format(meetupMembers$joined, "%Y") != 2014], "%m")
   key count
1   01    56
2   02    59
3   03    35
4   04    37
5   05    78
6   06    58
7   07    40
8   08    86
9   09    66
10  10    73
11  11    67
12  12    26
~~~

<p>Next up I think I need to get some charts going on and perhaps compare the distributions of join dates of various London meetup groups against each other.</p>


<p>I'm an absolute R newbie so if anything I've done is stupid and can be done better please let me know.</p>

