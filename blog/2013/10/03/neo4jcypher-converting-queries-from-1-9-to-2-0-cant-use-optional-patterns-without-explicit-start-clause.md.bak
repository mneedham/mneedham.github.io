+++
draft = false
date="2013-10-03 16:16:02"
title="neo4j/cypher: Converting queries from 1.9 to 2.0 -  'Can't use optional patterns without explicit START clause'"
tag=['neo4j', 'cypher']
category=['neo4j']
+++

<p>I've been playing around with the most recent Neo4j 2.0 milestone release - <a href="http://blog.neo4j.org/2013/09/neo4j-200m05-released.html">2.0.0-M05</a> - and one of the first things I did was translate the queries from my football data set which were written against Neo4j 1.9.</p>


<p>The following query calculates the number of goals scored by players in matches that were shown on television, not on television and in total.</p>



~~~cypher

START player=node:players('name:*')
MATCH player-[:played|subbed_on]->stats-[:in]->game-[t?:on_tv]->channel
WITH COLLECT([stats.goals, TYPE(t)]) AS games, player
RETURN player.name,
       REDUCE(goals = 0, g' IN FILTER(g IN games WHERE HEAD(TAIL(g)) IS NULL)| goals + HEAD(g')) AS nonTvGoals,
       REDUCE(goals = 0, g' IN FILTER(g IN games WHERE HEAD(TAIL(g)) <> NULL)| goals + HEAD(g')) AS tvGoals,
       REDUCE(goals = 0, g' in games | goals + HEAD(g')) AS totalGoals
ORDER BY tvGoals DESC
LIMIT 10
~~~

<p>We use a legacy index to get all of the players, find the games they participated in, check if those games were on television and then group by player to work out whether the goals were scored in televised games.</p>


<p>When we evaluate that query we get the following result:</p>



~~~bash

==> +--------------------------------------------------------+
==> | player.name        | nonTvGoals | tvGoals | totalGoals |
==> +--------------------------------------------------------+
==> | "Robin Van Persie" | 11         | 15      | 26         |
==> | "Gareth Bale"      | 8          | 13      | 21         |
==> | "Luis Suárez"      | 12         | 11      | 23         |
==> | "Theo Walcott"     | 5          | 9       | 14         |
==> | "Demba Ba"         | 7          | 8       | 15         |
==> | "Edin Dzeko"       | 7          | 7       | 14         |
==> | "Santi Cazorla"    | 5          | 7       | 12         |
==> | "Juan Mata"        | 6          | 6       | 12         |
==> | "Steven Gerrard"   | 3          | 6       | 9          |
==> | "Carlos Tevez"     | 5          | 6       | 11         |
==> +--------------------------------------------------------+
==> 10 rows
~~~

<p>The first step was to get rid of the legacy index and replace it with a <a href="http://jexp.de/blog/2013/04/cool-first-neo4j-2-0-milestone-now-with-labels-and-real-indexes/">label based one</a>. I created a label 'Player' for this purpose:</p>



~~~cypher

START player = node:players('name:*') SET player :Player RETURN player
CREATE INDEX on :Player(name) 
~~~

<p>Then I got rid of the legacy index lookup and replaced it with a label based one:</p>



~~~cypher

MATCH (player:Player)-[:played|subbed_on]->stats-[:in]->game-[t?:on_tv]->channel
WITH COLLECT([stats.goals, TYPE(t)]) AS games, player
RETURN player.name,
       REDUCE(goals = 0, g' IN FILTER(g IN games WHERE HEAD(TAIL(g)) IS NULL)| goals + HEAD(g')) AS nonTvGoals,
       REDUCE(goals = 0, g' IN FILTER(g IN games WHERE HEAD(TAIL(g)) <> NULL)| goals + HEAD(g')) AS tvGoals,
       REDUCE(goals = 0, g' in games | goals + HEAD(g')) AS totalGoals
ORDER BY tvGoals DESC
LIMIT 10
~~~

<p>Unfortunately you can't use optional relationships like this:</p>



~~~cypher

PatternException: Can't use optional patterns without explicit START clause. Optional relationships: `t`
~~~

<p>A neat workaround which <a href="https://twitter.com/andres_taylor">Andres</a> showed me is to first match all of the players and then make them available using a <cite>WITH</cite> statement:</p>



~~~cypher

MATCH (player:Player)
WITH player
MATCH player-[:played|subbed_on]->stats-[:in]->game-[t?:on_tv]->channel
WITH COLLECT([stats.goals, TYPE(t)]) AS games, player
RETURN player.name,
       REDUCE(goals = 0, g' IN FILTER(g IN games WHERE HEAD(TAIL(g)) IS NULL)| goals + HEAD(g')) AS nonTvGoals,
       REDUCE(goals = 0, g' IN FILTER(g IN games WHERE HEAD(TAIL(g)) <> NULL)| goals + HEAD(g')) AS tvGoals,
       REDUCE(goals = 0, g' in games | goals + HEAD(g')) AS totalGoals
ORDER BY tvGoals DESC
LIMIT 10
~~~

<p>If we evaluate this query it returns us the same results as before. However, given that we now have <a href="http://docs.neo4j.org/chunked/2.0.0-M05/syntax-collections.html">better collection support</a> it seemed a shame to still use <cite>HEAD</cite> and <cite>TAIL</cite> so I replaced those with the following:</p>



~~~cypher

MATCH (player:Player)
WITH player
MATCH player-[:played|subbed_on]->stats-[:in]->game-[t?:on_tv]->channel
WITH COLLECT([stats.goals, TYPE(t)]) AS games, player
RETURN player.name,
       REDUCE(goals = 0, g' IN FILTER(g IN games WHERE g[1] IS NULL)| goals + g'[0]) AS nonTvGoals,
       REDUCE(goals = 0, g' IN FILTER(g IN games WHERE g[1] <> NULL)| goals + g'[0]) AS tvGoals,
       REDUCE(goals = 0, g' in games | goals + g'[0]) AS totalGoals
ORDER BY tvGoals DESC
LIMIT 10
~~~

<p>I didn't like those array indexes either and since we can now <a href="http://docs.neo4j.org/chunked/2.0.0-M05/syntax-collections.html#_literal_maps">create maps</a> I thought the query would be clearer if we created one on line 4 of the query rather than an array:</p>



~~~cypher

MATCH (player:Player)
WITH player
MATCH player-[:played|subbed_on]->stats-[:in]->game-[t?:on_tv]->channel
WITH COLLECT({goals: stats.goals, ontv: TYPE(t)}) AS games, player
RETURN player.name,
       REDUCE(goals = 0, g' IN FILTER(g IN games WHERE g.ontv IS NULL)| goals + g'.goals) AS nonTvGoals,
       REDUCE(goals = 0, g' IN FILTER(g IN games WHERE g.ontv <> NULL)| goals + g'.goals) AS tvGoals,
       REDUCE(goals = 0, g' in games | goals + g'.goals) AS totalGoals
ORDER BY tvGoals DESC
LIMIT 10
~~~

<p>The next tweak would be to remove the <cite>FILTER</cite> and replace that with a list comprehension:</p>



~~~cypher

MATCH (player:Player)
WITH player
MATCH player-[:played|subbed_on]->stats-[:in]->game-[t?:on_tv]->channel
WITH COLLECT({goals: stats.goals, ontv: TYPE(t)}) AS games, player
RETURN player.name,
       REDUCE(goals = 0, g' IN [g IN games WHERE g.ontv IS NULL] | goals + g'.goals) AS nonTvGoals,
       REDUCE(goals = 0, g' IN [g IN games WHERE g.ontv <> NULL] | goals + g'.goals) AS tvGoals,
       REDUCE(goals = 0, g' in games | goals + g'.goals) AS totalGoals
ORDER BY tvGoals DESC
LIMIT 10
~~~

<p>Although the query ends up being a couple of lines longer than its 1.9 cousin I think there's less noise and the intent is clearer.</p>

