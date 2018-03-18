+++
draft = false
date="2013-02-24 19:19:59"
title="neo4j/cypher: Combining COUNT and COLLECT in one query"
tag=['neo4j', 'cypher']
category=['neo4j']
+++

<p>In my <a href="http://www.markhneedham.com/blog/2013/02/19/neo4jcypher-using-a-where-clause-to-filter-paths/">continued</a> <a href="http://www.markhneedham.com/blog/2013/02/17/neo4jcypher-sql-style-group-by-functionality/">playing around</a> with football data I wanted to write a cypher query against neo4j which would show me which teams had missed the most penalties this season and who missed them.</p>


<p>I started off with a query that returned all the penalties that have been missed this season and the games those misses happened in:</p>



~~~text

START player = node:players('name:*')
MATCH player-[:missed_penalty_in]-game, 
      player-[:played|subbed_on]-stats-[:in]-game,
      stats-[:for]-team,
      game-[:home_team]-home,
      game-[:away_team]-away
RETURN player.name, team.name, home.name, away.name
~~~


~~~text

+-------------------------------------------------------------------------------------------------+
| player.name          | team.name              | home.name              | away.name              |
+-------------------------------------------------------------------------------------------------+
| "Papiss Demba Cisse" | "Newcastle United"     | "Newcastle United"     | "Norwich City"         |
| "Wayne Rooney"       | "Manchester United"    | "Manchester United"    | "Arsenal"              |
| "Mikel Arteta"       | "Arsenal"              | "Arsenal"              | "Fulham"               |
| "David Silva"        | "Manchester City"      | "Manchester City"      | "Southampton"          |
| "Frank Lampard"      | "Chelsea"              | "Manchester City"      | "Chelsea"              |
| "Adel Taarabt"       | "Queens Park Rangers"  | "Queens Park Rangers"  | "Norwich City"         |
| "Javier Hernández"   | "Manchester United"    | "Manchester United"    | "Wigan Athletic"       |
| "Robin Van Persie"   | "Manchester United"    | "Southampton"          | "Manchester United"    |
| "Jonathan Walters"   | "Stoke City"           | "Fulham"               | "Stoke City"           |
| "Shane Long"         | "West Bromwich Albion" | "West Bromwich Albion" | "Liverpool"            |
| "Steven Gerrard"     | "Liverpool"            | "Liverpool"            | "West Bromwich Albion" |
| "Lucas Piazon"       | "Chelsea"              | "Chelsea"              | "Aston Villa"          |
+-------------------------------------------------------------------------------------------------+
12 rows
~~~

<p>(there should actually be another penalty miss for Jonathan Walters against Chelsea but for some reason the data source has missed it off!</p>


<p>I then grouped the penalty misses by team so that I'd have one row for each team and a collection showing the people who'd missed.</p>


<p>We can use the <cite><a href="http://docs.neo4j.org/chunked/milestone/query-aggregation.html#aggregation-collect">COLLECT</a></cite> function to do the latter:</p>



~~~text

START player = node:players('name:*')
MATCH player-[:missed_penalty_in]-game, 
      player-[:played|subbed_on]-stats-[:in]-game,
      stats-[:for]-team
RETURN DISTINCT team.name, COLLECT(player.name) AS players
~~~


~~~text

+---------------------------------------------------------------------------------+
| team.name              | players                                                |
+---------------------------------------------------------------------------------+
| "Newcastle United"     | ["Papiss Demba Cisse"]                                 |
| "Manchester United"    | ["Wayne Rooney","Javier Hernández","Robin Van Persie"] |
| "Stoke City"           | ["Jonathan Walters"]                                   |
| "West Bromwich Albion" | ["Shane Long"]                                         |
| "Chelsea"              | ["Frank Lampard","Lucas Piazon"]                       |
| "Arsenal"              | ["Mikel Arteta"]                                       |
| "Manchester City"      | ["David Silva"]                                        |
| "Liverpool"            | ["Steven Gerrard"]                                     |
| "Queens Park Rangers"  | ["Adel Taarabt"]                                       |
+---------------------------------------------------------------------------------+
9 rows
~~~

<p>I wanted to order the teams by the number of penalties they'd missed so Manchester United would be first in the table in this case and initially tried to order the results by a count of players:</p>



~~~text

START player = node:players('name:*')
MATCH player-[:missed_penalty_in]-game, 
      player-[:played|subbed_on]-stats-[:in]-game,
      stats-[:for]-team
RETURN DISTINCT team.name, COLLECT(player.name) AS players
ORDER BY COUNT(player.name)
~~~

<p>which doesn't actually compile:</p>



~~~text

SyntaxException: Aggregation expressions must be listed in the RETURN clause to be used in ORDER BY
~~~

<p>I tried a few other variations such as the following:</p>



~~~text

START player = node:players('name:*')
MATCH player-[:missed_penalty_in]-game, 
      player-[:played|subbed_on]-stats-[:in]-game,
      stats-[:for]-team
RETURN DISTINCT team.name, COUNT(player.name) AS numberOfPlayers, 
       COLLECT(player.name) AS players
ORDER BY numberOfPlayers DESC
~~~

<p>which again doesn't compile:</p>



~~~text

SyntaxException: Aggregation expressions must be listed in the RETURN clause to be used in ORDER BY
~~~

<p>I eventually found <a href="http://stackoverflow.com/questions/12269009/returning-two-aggregates-in-a-single-cypher-query?rq=1">a post by Andres</a> where he explains that you need to split the query into two and make use of <cite><a href="http://docs.neo4j.org/chunked/milestone/query-with.html">WITH</a></cite> if you want to make use of two aggregation expressions.</p>


<p>I ended up with the following query which does the job:</p>



~~~text

START player = node:players('name:*')
MATCH player-[:missed_penalty_in]-game, 
      player-[:played|subbed_on]-stats-[:in]-game,
      stats-[:for]-team
WITH DISTINCT team, COLLECT(player.name) AS players

MATCH player-[:missed_penalty_in]-game, 
      player-[:played|subbed_on]-stats-[:in]-game,
      stats-[:for]-team
WITH DISTINCT team, COUNT(player) AS numberOfPlayers, players

RETURN team.name, players
ORDER BY numberOfPlayers DESC
~~~


~~~text

+---------------------------------------------------------------------------------+
| team.name              | players                                                |
+---------------------------------------------------------------------------------+
| "Manchester United"    | ["Wayne Rooney","Javier Hernández","Robin Van Persie"] |
| "Chelsea"              | ["Frank Lampard","Lucas Piazon"]                       |
| "Liverpool"            | ["Steven Gerrard"]                                     |
| "Manchester City"      | ["David Silva"]                                        |
| "Newcastle United"     | ["Papiss Demba Cisse"]                                 |
| "Queens Park Rangers"  | ["Adel Taarabt"]                                       |
| "Stoke City"           | ["Jonathan Walters"]                                   |
| "Arsenal"              | ["Mikel Arteta"]                                       |
| "West Bromwich Albion" | ["Shane Long"]                                         |
+---------------------------------------------------------------------------------+
9 rows
~~~
