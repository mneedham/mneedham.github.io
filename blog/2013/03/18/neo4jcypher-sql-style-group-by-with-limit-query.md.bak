+++
draft = false
date="2013-03-18 23:19:36"
title="neo4j/cypher: SQL style GROUP BY WITH LIMIT query"
tag=['neo4j', 'cypher']
category=['neo4j']
+++

<p>A few weeks ago I wrote a blog post where I described how we could <a href="http://www.markhneedham.com/blog/2013/02/17/neo4jcypher-sql-style-group-by-functionality/">construct a SQL GROUP BY style query</a> in <a href="http://docs.neo4j.org/chunked/milestone/cypher-query-lang.html">cypher</a> and last week I wanted to write a similar query but with what I think would be a LIMIT clause in SQL.</p>


<p>I wanted to find the maximum number of goals that players had scored in a match for a specific team and started off with the following query to find all the matches that players had scored in:</p>



~~~cypher

START team = node:teams('name:"Manchester United"')
MATCH team-[:home_team|away_team]-game-[:scored_in]-player-[:played]-stats-[:for]-team, 
      stats-[:in]-game
RETURN DISTINCT player.name, stats.goals, game.name
~~~

<p>We find all the matches where Manchester United were playing and then get a list of the players who scored for them in those games:</p>



~~~text

+--------------------------------------------------------------------------------+
| player.name         | stats.goals | game.name                                  |
+--------------------------------------------------------------------------------+
| "Javier Hernández"  | 1           | "Manchester United vs Wigan Athletic"      |
| "Robin Van Persie"  | 1           | "Manchester United vs Sunderland"          |
| "Danny Welbeck"     | 1           | "Manchester United vs Stoke City"          |
| "Rafael"            | 1           | "Queens Park Rangers vs Manchester United" |
| "Wayne Rooney"      | 1           | "Manchester United vs Norwich City"        |
| "Shinji Kagawa"     | 1           | "Manchester United vs Fulham"              |
| "Shinji Kagawa"     | 3           | "Manchester United vs Norwich City"        |
...
+--------------------------------------------------------------------------------+
50 rows
~~~

<p>Our next step would be to only return the unique combinations of players and goals:</p>



~~~cypher

START team = node:teams('name:"Manchester United"')
MATCH team-[:home_team|away_team]-game-[:scored_in]-player-[:played]-stats-[:for]-team, 
      stats-[:in]-game
RETURN DISTINCT player.name, stats.goals
~~~


~~~text

+-----------------------------------+
| player.name         | stats.goals |
+-----------------------------------+
| "Nemanja Vidic"     | 1           |
| "Shinji Kagawa"     | 1           |
| "Danny Welbeck"     | 1           |
| "Darren Fletcher"   | 1           |
| "Wayne Rooney"      | 2           |
| "Javier Hernández"  | 1           |
| "Nani"              | 1           |
| "Tom Cleverley"     | 1           |
| "Robin Van Persie"  | 2           |
| "Shinji Kagawa"     | 3           |
...
| "Robin Van Persie"  | 3           |
+-----------------------------------+
21 rows
~~~

<p>Since we only want to return each player once along with their maximum value from the 'stats.goals' column all we have to do now is make use of the <cite><a href="http://docs.neo4j.org/chunked/milestone/query-aggregation.html#aggregation-max">MAX</a></cite> function:</p>



~~~cypher

START team = node:teams('name:"Manchester United"')
MATCH team-[:home_team|away_team]-game-[:scored_in]-player-[:played]-stats-[:for]-team, 
      stats-[:in]-game
RETURN DISTINCT player.name, MAX(stats.goals) AS goals
ORDER BY goals DESC
~~~


~~~text

+-----------------------------+
| player.name         | goals |
+-----------------------------+
| "Robin Van Persie"  | 3     |
| "Shinji Kagawa"     | 3     |
| "Javier Hernández"  | 2     |
| "Wayne Rooney"      | 2     |
| "Paul Scholes"      | 1     |
| "Ryan Giggs"        | 1     |
| "Tom Cleverley"     | 1     |
...
| "Rafael"            | 1     |
| "Darren Fletcher"   | 1     |
| "Nani"              | 1     |
+-----------------------------+
16 rows
~~~
