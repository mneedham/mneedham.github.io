+++
draft = false
date="2013-03-31 21:08:22"
title="neo4j/cypher: Playing around with time"
tag=['neo4j', 'lucene']
category=['neo4j']
+++

<p>I've done a bit of modelling with years and months in neo4j graphs that I've worked on previously but I haven't ever done anything with time so I thought it'd be interesting to have a go with my football graph.</p>


<p>I came across <a href="http://stackoverflow.com/questions/9138857/in-neo4j-how-can-i-index-by-date-and-search-in-a-date-range">this StackOverflow post</a> on my travels which suggested that indexing nodes by time would be helpful and since I have a bunch of football matches with associated times I thought I'd try it out.</p>


<p>I created the key of the index by running code similar to the following:</p>



~~~ruby

> DateTime.now.strftime("%H%M")
=> "2200"
~~~

<p>We can then write a query to show all the games at a certain time of day:</p>



~~~cypher

START game=node:times('time:*')
RETURN game.time, COUNT(game)
ORDER BY game.time
~~~


~~~text

+-------------------------+
| game.time | COUNT(game) |
+-------------------------+
| 1245      | 21          |
| 1330      | 21          |
| 1500      | 163         |
| 1600      | 29          |
| 1730      | 22          |
| 1945      | 21          |
| 2000      | 19          |
+-------------------------+
7 rows
~~~

<p>To be fair any index that referenced all the matches would allow us to do this. e.g.</p>
 


~~~cypher

START game=node:matches('match_id:*')
RETURN game.time, COUNT(game)
ORDER BY game.time
~~~

<p>The time based indexing becomes more interesting when we use Lucene's <a href="http://lucene.apache.org/core/old_versioned_docs/versions/2_9_0/api/all/org/apache/lucene/search/NumericRangeQuery.html">numeric range query</a> syntax to only select matches which happened between certain times of day:</p>



~~~cypher

START game=node:times('time:[1600 TO 2000]')
RETURN game.time, COUNT(game)
ORDER BY game.time
~~~


~~~text

+-------------------------+
| game.time | COUNT(game) |
+-------------------------+
| 1600      | 29          |
| 1730      | 22          |
| 1945      | 21          |
| 2000      | 19          |
+-------------------------+
4 rows
~~~

<p>I couldn't see a way to set an open ended value either side of the 'TO' so if we want to do that we just need to set a really high maximum value or really low minimum value.</p>


<p>For example if we want to find all the evening matches we could use this query:</p>



~~~cypher

START game=node:times('time:[1730 TO 2359]')
RETURN game.time, COUNT(game)
ORDER BY game.time
~~~


~~~text

+-------------------------+
| game.time | COUNT(game) |
+-------------------------+
| 1730      | 22          |
| 1945      | 21          |
| 2000      | 19          |
+-------------------------+
3 rows
~~~

<p>I also indexed each match by its full timestamp so we could find all the evening games this year if we wanted as well:</p>



~~~ruby

> Time.new(2013,1,1).to_i
=> 1356998400
~~~


~~~cypher

START game=node:times('time:[1730 TO 2359] AND date: [1356998400 TO 9999999999]')
RETURN game.time, game.name, game.friendly_date
~~~


~~~text

+------------------------------------------------------------------------------------+
| game.time | game.name                                | game.friendly_date          |
+------------------------------------------------------------------------------------+
| 1730      | "Wigan Athletic vs Liverpool"            | "2013-03-02 17:30:00 +0000" |
| 2000      | "Aston Villa vs Manchester City"         | "2013-03-04 20:00:00 +0000" |
| 2000      | "West Ham United vs Tottenham Hotspur"   | "2013-02-25 20:00:00 +0000" |
| 2000      | "Liverpool vs West Bromwich Albion"      | "2013-02-11 20:00:00 +0000" |
| 1730      | "Fulham vs Manchester United"            | "2013-02-02 17:30:00 +0000" |
...
| 1945      | "Chelsea vs Southampton"                 | "2013-01-16 19:45:00 +0000" |
+------------------------------------------------------------------------------------+
25 rows
~~~
