+++
draft = false
date="2014-06-30 21:44:14"
title="R: Order by data frame column and take top 10 rows"
tag=['r-2']
category=['R']
+++

<p>I've been doing some <a href="http://www.markhneedham.com/blog/2014/06/30/neo4jr-grouping-meetup-members-by-join-timestamp/">ad-hoc analysis of the Neo4j London meetup group using R and Neo4j</a> and having worked out how to group by certain keys the next step was to order the rows of the data frame.</p>


<p>I wanted to drill into the days on which people join the group and see whether they join it at a specific time of day. My feeling was that most people would join on a Monday morning.</p>


<p>The first step was to run the query using <a href="https://github.com/nicolewhite/Rneo4j">RNeo4j</a> and then group by day and <a href="http://stat.ethz.ch/R-manual/R-devel/library/base/html/as.POSIXlt.html">hour</a>:</p>



~~~r

library(Rneo4j)

query = "MATCH (:Person)-[:HAS_MEETUP_PROFILE]->()-[:HAS_MEMBERSHIP]->(membership)-[:OF_GROUP]->(g:Group {name: \"Neo4j - London User Group\"})
         RETURN membership.joined AS joinDate"

timestampToDate <- function(x) as.POSIXct(x / 1000, origin="1970-01-01")

meetupMembers = cypher(graph, query)
meetupMembers$joined <- timestampToDate(meetupMembers$joinDate)

groupBy = function(dates, format) {
  dd = aggregate(dates, by= list(format(dates, format)), function(x) length(x))
  colnames(dd) = c("key", "count")
  dd
}

byDayTime = groupBy(meetupMembers$joined, "%A %H:00")
~~~

<p>This returned quite a few rows so we'll just display a subset of them:</p>



~~~r

> byDayTime[12:25,]
            key count
12 Friday 14:00    12
13 Friday 15:00     8
14 Friday 16:00    11
15 Friday 17:00    10
16 Friday 18:00     3
17 Friday 19:00     1
18 Friday 20:00     3
19 Friday 21:00     4
20 Friday 22:00     7
21 Friday 23:00     2
22 Monday 00:00     3
23 Monday 01:00     1
24 Monday 03:00     1
25 Monday 05:00     3
~~~

<p>The next step was to order by the 'count' column which wasn't too difficult:</p>



~~~r

> byDayTime[order(byDayTime$count),][1:10,]
              key count
2    Friday 03:00     1
3    Friday 04:00     1
4    Friday 05:00     1
5    Friday 07:00     1
17   Friday 19:00     1
23   Monday 01:00     1
24   Monday 03:00     1
46 Saturday 03:00     1
66   Sunday 06:00     1
67   Sunday 07:00     1
~~~

<p>If we run the order function on its own we'll see that it returns the order in which the current rows in the data frame should appear:</p>



~~~r

> order(byDayTime$count)
  [1]   2   3   4   5  17  23  24  46  66  67 109 128 129   1  21  44  47  48  81  86  87  88 108 130  16  18  22  25  45  53  64  71  75 107  19  26  49  51  55  56  58  59  61
 [44]  65  68  77  79  85 106 110 143  50  52  54  82  84 101 127 146  27  57  60  62  63  69  70  73  99 103 126 145   6  20  76  83  89 105 122 131 144   7  13  40  43  72  80
 [87] 102  39  78 100 132 147  15  94 121 123 142  14  42  74 104 137 140  12  38  92  93 111 124   8   9  11  90  96 125 139  10  32  34  36  95  97  98  28 135 136  33  35 112
[130] 113 116 134  91 141  41 115 120 133  37 119 138  31 117 118  30 114  29
~~~

<p>The first 4 rows in our sorted data frame will be rows 2-5 from the initial data frame, which are:</p>



~~~r

           key count
2 Friday 03:00     1
3 Friday 04:00     1
4 Friday 05:00     1
5 Friday 07:00     1
~~~

<p>So that makes sense! In our case we want to <a href="http://www.statmethods.net/management/sorting.html">sort in descending order</a> which we can do by prefixing the sorting variable with a minus sign:</p>



~~~r

> byDayTime[order(-byDayTime$count),][1:10,]
                key count
29     Monday 09:00    34
30     Monday 10:00    28
114   Tuesday 11:00    28
31     Monday 11:00    27
117   Tuesday 14:00    27
118   Tuesday 15:00    27
138 Wednesday 14:00    23
119   Tuesday 16:00    22
37     Monday 17:00    21
115   Tuesday 12:00    20
~~~

<p>As expected Monday morning makes a strong showing although Tuesday afternoon is also popular which is unexpected. We'll need to do some more investigation to figure out what's going on there.</p>

