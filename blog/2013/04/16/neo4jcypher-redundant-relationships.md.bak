+++
draft = false
date="2013-04-16 21:41:58"
title="neo4j/cypher: Redundant relationships"
tag=['neo4j', 'cypher']
category=['neo4j']
+++

<p>Last week I was writing a query to find the top scorers in the Premier League so far this season alongside the number of games they've played in which initially read like this:</p>



~~~text

START player = node:players('name:*')
MATCH player-[:started|as_sub]-playedLike-[:in]-game-[r?:scored_in]-player
WITH player, COUNT(DISTINCT game) AS games, COLLECT(r) AS allGoals
RETURN player.name, games, LENGTH(allGoals) AS goals
ORDER BY goals DESC
LIMIT 5
~~~


~~~text

+------------------------------------+
| player.name        | games | goals |
+------------------------------------+
| "Luis Suárez"      | 30    | 22    |
| "Robin Van Persie" | 30    | 19    |
| "Gareth Bale"      | 27    | 17    |
| "Michu"            | 29    | 16    |
| "Demba Ba"         | 28    | 15    |
+------------------------------------+
5 rows
1 ms
~~~

<p>I modelled whether a player started a game or came on as a substitute with separate relationship types 'started' and 'as_sub' but in this query we're not interested in that, we just want to know whether they played.</p>


<p>In the world of relational database design we tend to try and avoid redundancy but <a href="http://www.markhneedham.com/blog/2012/07/21/neo4j-embracing-the-sub-graph/">with graphs this isn't such a big deal</a> so I thought I may as well add a 'played' relationship whenever a 'as_sub' or 'started' one was being created.</p>


<p>We can then simplify the above query to read like this:</p>



~~~cypher

START player = node:players('name:*')
MATCH player-[:played]-playedLike-[:in]-game-[r?:scored_in]-player
WITH player, COUNT(DISTINCT game) AS games, COLLECT(r) AS allGoals
RETURN player.name, games, LENGTH(allGoals) AS goals
ORDER BY goals DESC
LIMIT 5
~~~


~~~text

+------------------------------------+
| player.name        | games | goals |
+------------------------------------+
| "Luis Suárez"      | 30    | 22    |
| "Robin Van Persie" | 30    | 19    |
| "Gareth Bale"      | 27    | 17    |
| "Michu"            | 29    | 16    |
| "Demba Ba"         | 28    | 15    |
+------------------------------------+
5 rows
0 ms
~~~

<p>When I'm querying I often forget that I modelled starting/substitute separately and think the data has screwed up and it's always because I've forgotten to include the 'as_sub' relationship.</p>


<p>Having the 'played' relationship means that no longer happens which is cool.</p>


<p>I have a reasonably small data set so I haven't seen any performance problems from creating this redundancy.</p>
 

<p>However, since the maximum number of relationships going out from a player would be unlikely to be more than 1000s I don't think it will become one either.</p>


<p>As always I'd be interested in thoughts from others who have come across similar problems or can see something that I've missed.</p>

