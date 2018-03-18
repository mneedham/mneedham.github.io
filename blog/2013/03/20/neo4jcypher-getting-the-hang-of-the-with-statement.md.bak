+++
draft = false
date="2013-03-20 00:25:00"
title="neo4j/cypher: Getting the hang of the WITH statement"
tag=['neo4j', 'cypher']
category=['neo4j']
+++

<p>I wrote a post a few weeks ago <a href="http://www.markhneedham.com/blog/2013/02/24/neo4jcypher-combining-count-and-collect-in-one-query/">showing an example of a cypher query which made use of the  WITH statement</a> but I still don't completely understand how it works so I thought I'd write some more queries that use it.</p>


<p>I wanted to find out whether Luis Suárez has a better scoring record depending on which day a match is played on.</p>


<p>We start out by finding all the matches that he's played in and which days those matches were on:</p>



~~~cypher

START player = node:players('name:"Luis Suárez"')
MATCH game-[:in]-stats-[:played]-player, game-[:on_day]-day
RETURN day.name, game.name
~~~


~~~text

+---------------------------------------------------+
| day.name    | game.name                           |
+---------------------------------------------------+
| "Saturday"  | "Liverpool vs Southampton"          |
| "Saturday"  | "Southampton vs Liverpool"          |
| "Saturday"  | "Liverpool vs Reading"              |
| "Saturday"  | "West Bromwich Albion vs Liverpool" |
...
+---------------------------------------------------+
29 rows
~~~

<p>We can then group those matches by day to find out how many games he played in on a particular day:</p>



~~~cypher

START player = node:players('name:"Luis Suárez"')
MATCH game-[:in]-stats-[:played]-player, game-[:on_day]-day
RETURN day.name, COUNT(game.name)
~~~


~~~text

+--------------------------------+
| day.name    | COUNT(game.name) |
+--------------------------------+
| "Sunday"    | 13               |
| "Wednesday" | 4                |
| "Monday"    | 1                |
| "Saturday"  | 11               |
+--------------------------------+
4 rows
~~~

<p>Now we want to find out which days the games that Suarez scored in were on so we start out by returning each day that Suarez played in a match and then return a collection containing information about the games he played on that day and whether he scored:</p>



~~~cypher

START player = node:players('name:"Luis Suárez"')
MATCH game-[:in]-stats-[:played]-player-[r?:scored_in]-game-[:on_day]-day
RETURN day, COLLECT(DISTINCT([type(r), game.name])) AS games
~~~


~~~text

+----------------------------------------------------------------------------------------+
| day.name    | games                                                                    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
+----------------------------------------------------------------------------------------+
| "Sunday"    | [["scored_in","Liverpool vs Manchester City"]…]                          |
| "Wednesday" | [[<null>,"Tottenham Hotspur vs Liverpool"],[<null>,"Stoke City vs Liverpool"]...]    |                                                                                                                                                                                                                                                                                                                                                                                          
| "Monday"    | [[<null>,"Liverpool vs West Bromwich Albion"]]                                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
| "Saturday"  | [[<null>,"Liverpool vs Southampton"]…]                                         |                                                         
+----------------------------------------------------------------------------------------+
4 rows
~~~

<p>This query has got a little bit more complicated than our previous ones because we wanted to return all the days that Suarez played matches on even if he didn't score on that day.</p>


<p>The only interesting thing in the first couple of lines is that we match the 'scored_in' relationship <a href="http://www.markhneedham.com/blog/2012/06/24/neo4j-handling-optional-relationships/">optionally</a> so that we can handle the situation where Suarez didn't score while still returning a row.</p>


<p>On the third line we return the day and then we get a collection of tuples of the 'scored_in' relationship and the corresponding game.</p>


<p>We use <cite>DISTINCT</cite> on this line to take care of the situation where Suarez scored multiple times in the same match. We're working out the number of games that Suarez scored in so counting multiple goals in the same match would ruin that count.</p>


<p>We then need to tweak that query slightly to get a count of the matches that Suarez scored in rather than just returning them. We end up with the following:</p>



~~~cypher

START player = node:players('name:"Luis Suárez"')
MATCH game-[:in]-stats-[:played]-player-[r?:scored_in]-game-[:on_day]-day
WITH day, COLLECT(DISTINCT([type(r), game.name])) AS games
RETURN day.name, REDUCE(totalGames = 0, game in FILTER(x in games : head(x) = "scored_in"): totalGames + 1) AS gamesScoredIn
~~~


~~~text

+-----------------------------+
| day.name    | gamesScoredIn |
+-----------------------------+
| "Wednesday" | 2             |
| "Saturday"  | 6             |
| "Sunday"    | 7             |
| "Monday"    | 0             |
+-----------------------------+
4 rows
~~~

<p>We start off by <a href="http://docs.neo4j.org/chunked/milestone/query-function.html#functions-filter">filtering</a> the games so that we only keep the ones that Suarez scored in. We then run a <a href="http://docs.neo4j.org/chunked/milestone/query-function.html#functions-reduce"><cite>REDUCE</cite></a> over the resulting collection which just adds 1 to an accumulator for each record in the collection.</p>


<p>Now that we've got that the next step is to combine our games played and games scored in queries together so that we can see what % of games Suarez scores in on each day.</p>


<p>We end up with the following:</p>



~~~cypher

START player = node:players('name:"Luis Suárez"')
MATCH game-[:in]-stats-[:played]-player, game-[:on_day]-day

WITH player, day, COUNT(game) AS playedGames
MATCH game-[:in]-stats-[:played]-player-[r?:scored_in]-game-[:on_day]-day

WITH day, COLLECT(DISTINCT([type(r), game.name])) AS games, playedGames
WITH day, REDUCE(totalGames = 0, game in FILTER(x in games : head(x) = "scored_in"): totalGames + 1) AS scoredGames, playedGames
RETURN day.name, playedGames, scoredGames, (scoredGames*1.0/playedGames*1.0) * 100 AS percentage
~~~


~~~text

+-------------------------------------------------------------+
| day.name    | playedGames | scoredGames | percentage        |
+-------------------------------------------------------------+
| "Saturday"  | 11          | 6           | 54.54545454545454 |
| "Monday"    | 1           | 0           | 0.0               |
| "Wednesday" | 4           | 2           | 50.0              |
| "Sunday"    | 13          | 7           | 53.84615384615385 |
+-------------------------------------------------------------+
4 rows
~~~

<p>One thing I kept getting confused about here is that we need to pass everything that we want to eventually return in each WITH statement otherwise it won't be available to us at the end.</p>


<p>If we're going to do multiple MATCH statements we need to pass the starting node in the preceding WITH statement which in this case means that we need to pass the player variable along.</p>


<p>Other than that this query is the amalgamation of the previous two except we've added some arithmetic on the final line to work out the % of matches that Suarez scores in. I had to multiply each number by 1.0 to force float based arithmetic rather than integer based.</p>
  

<p>In answer to our initial question it doesn't seem to matter which day a match is played on, Suarez scores in approximately every other game.</p>

