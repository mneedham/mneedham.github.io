+++
draft = false
date="2013-03-24 13:00:29"
title="neo4j/cypher: CypherTypeException: Failed merging Number with Relationship"
tag=['neo4j', 'cypher']
category=['neo4j']
+++

<p>The latest thing that I added to my football graph was the matches that are shown on TV as I have the belief that players who score on televised games get more attention than players who score in other games.</p>


<p>I thought it'd be interesting to work out who the top scorers are on each of these game types.</p>


<p>I added the following relationship type to allow me to do this:</p>



~~~text

game-[:on_tv]-channel
~~~

<p>I then wrote a query to get a list of all the players along with a collection of the games they played in and whether or not this game was televised:</p>



~~~cypher

START player=node:players('name:*')
MATCH player-[:played|subbed_on]-stats-[:in]-game-[t?:on_tv]-channel
RETURN player.name, COLLECT([stats.goals, t]) AS games
LIMIT 10
~~~

<p>Unfortunately when I ran this query I ended up with the following exception:</p>



~~~text

CypherTypeException: Failed merging Number with Relationship
~~~

<p>From some previous conversations with <a href="http://wes.skeweredrook.com/">Wes</a> I'd noticed that this exception didn't seem to happen with the <a href="http://blog.neo4j.org/2013/03/neo4j-19m05-released-wrapping-up.html">1.9.M05</a> release but I was using <a href="http://blog.neo4j.org/2013/01/neo4j-milestone-19m04-released.html">1.9.M04</a>.</p>


<p>Just to see what happened I tried returning the type of the relationship in the collection literal rather than the relationship and that worked:</p>



~~~cypher

START player=node:players('name:*')
MATCH player-[:played|subbed_on]-stats-[:in]-game-[t?:on_tv]-channel
RETURN player.name, COLLECT([stats.goals, TYPE(t)]) AS games
LIMIT 10
~~~


~~~text

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| player.name          | games                                                                                                                                                                                                                                                                             |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| "Djibril Cissé"      | [[0,<null>],[1,"on_tv"],[0,<null>],[0,<null>],[0,"on_tv"],[0,<null>],[0,<null>],[0,<null>],[0,<null>],[0,<null>],[1,<null>],[0,"on_tv"],[0,"on_tv"],[0,<null>],[0,<null>],[0,"on_tv"],[0,<null>],[1,<null>]]                                                                      |
| "Markus Rosenberg"   | [[0,<null>],[0,<null>],[0,<null>],[0,<null>],[0,<null>],[0,<null>],[0,<null>],[0,<null>],[0,<null>],[0,<null>],[0,<null>],[0,"on_tv"],[0,"on_tv"],[0,<null>],[0,"on_tv"],[0,<null>]]                                                                                              |
| "Gabriel Agbonlahor" | [[0,"on_tv"],[1,<null>],[0,"on_tv"],[0,<null>],[0,<null>],[0,"on_tv"],[1,<null>],[0,"on_tv"],[0,<null>],[0,"on_tv"],[0,<null>],[0,<null>],[1,"on_tv"],[1,<null>],[0,<null>],[0,"on_tv"],[1,<null>],[0,<null>],[0,<null>],[0,<null>],[0,<null>]]                                   |
| "Shaun Derry"        | [[0,<null>],[0,<null>],[0,<null>],[0,"on_tv"],[0,<null>],[0,<null>],[0,"on_tv"],[0,<null>],[0,<null>],[0,<null>],[0,<null>],[0,<null>],[0,<null>],[0,"on_tv"]]                                                                                                                    |
| "Marouane Fellaini"  | [[0,<null>],[0,"on_tv"],[0,<null>],[1,<null>],[1,"on_tv"],[1,<null>],[0,<null>],[0,"on_tv"],[1,"on_tv"],[0,<null>],[0,"on_tv"],[2,<null>],[1,<null>],[1,<null>],[1,<null>],[0,<null>],[0,<null>],[0,"on_tv"],[0,<null>],[0,<null>],[2,<null>],[0,"on_tv"],[0,<null>],[0,"on_tv"]] |
| "Jermaine Jenas"     | [[0,<null>],[1,<null>],[0,<null>],[0,<null>],[0,"on_tv"],[0,<null>],[1,<null>]]                                                                                                                                                                                                   |
| "Sean Morrison"      | [[0,<null>],[0,"on_tv"],[0,<null>],[0,<null>],[1,<null>],[0,"on_tv"],[1,"on_tv"],[0,<null>],[0,"on_tv"]]                                                                                                                                                                          |
| "Claudio Yacob"      | [[0,"on_tv"],[0,<null>],[0,<null>],[0,<null>],[0,<null>],[0,<null>],[0,"on_tv"],[0,<null>],[0,<null>],[0,<null>],[0,<null>],[0,"on_tv"],[0,<null>],[0,<null>],[0,"on_tv"],[0,"on_tv"],[0,"on_tv"],[0,<null>],[0,<null>],[0,<null>],[0,<null>],[0,<null>]]                         |
| "Michael Owen"       | [[0,<null>],[0,<null>],[0,<null>],[0,<null>],[1,<null>],[0,<null>]]                                                                                                                                                                                                               |
| "Tony Hibbert"       | [[0,"on_tv"],[0,"on_tv"],[0,<null>],[0,<null>],[0,<null>]]                                                                                                                                                                                                                        |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
10 rows
~~~

<p>The final query ends up looking like this out of interest:</p>



~~~cypher

START player=node:players('name:*')
MATCH player-[:played|subbed_on]-stats-[:in]-game-[t?:on_tv]-channel
WITH COLLECT([stats.goals, TYPE(t)]) AS games, player
RETURN player.name,
       REDUCE(goals = 0, h IN FILTER(g IN games : HEAD(TAIL(g)) IS NULL): goals + HEAD(h)) AS nonTvGoals,
       REDUCE(goals = 0, h IN FILTER(g IN games : HEAD(TAIL(g)) <> NULL): goals + HEAD(h)) AS tvGoals,
       REDUCE(goals = 0, h in games : goals + HEAD(h)) AS totalGoals
ORDER BY tvGoals DESC
LIMIT 10
~~~


~~~text

+--------------------------------------------------------+
| player.name        | nonTvGoals | tvGoals | totalGoals |
+--------------------------------------------------------+
| "Gareth Bale"      | 4          | 12      | 16         |
| "Robin Van Persie" | 8          | 11      | 19         |
| "Luis Suárez"      | 12         | 10      | 22         |
| "Theo Walcott"     | 3          | 8       | 11         |
| "Demba Ba"         | 7          | 8       | 15         |
| "Santi Cazorla"    | 4          | 7       | 11         |
| "Carlos Tevez"     | 3          | 6       | 9          |
| "Edin Dzeko"       | 6          | 6       | 12         |
| "Wayne Rooney"     | 6          | 6       | 12         |
| "Juan Mata"        | 4          | 6       | 10         |
+--------------------------------------------------------+
10 rows
~~~

<p>So as we can see Gareth Bale pretty much only scores when TV cameras are about!</p>


<p>I was intrigued what had changed between 1.9.M04 and 1.9.M05 so I spent a few hours this morning browsing  the <a href="https://github.com/neo4j/neo4j/tree/master/community/cypher">cypher part of the code base</a> and not really getting anywhere for the most part.</p>


<p>I thought that there had probably been a change around the way that <a href="https://github.com/neo4j/neo4j/blob/master/community/cypher/src/main/scala/org/neo4j/cypher/internal/parser/v1_9/Expressions.scala#L86">collection literals</a> were handled but a quick scan of git log suggested there hadn't been any changes:</p>



~~~text

$ git log -- community/cypher/src/main/scala/org/neo4j/cypher/internal/parser/v1_9
commit 7311bbe33bc06b346e60e12a4eee2a7173cbd317
Author: Andres Taylor <andres@neotechnology.com>
Date:   Tue Mar 19 06:42:49 2013 +0100

    Handles single node patterns in MATCH

commit c9f580456572d3d267a15dc88b35e07fd450cf93
Author: Stefan Plantikow <stefan.plantikow@googlemail.com>
Date:   Fri Jan 11 21:27:55 2013 +0100

    scala 2.10 support: Kills type erasure warnings with a few casts and cleans up a bit
...
~~~

<p>1.9.M04 was released on January 22nd and 1.9.M05 on March 6th and the only commit in this part of the code base in that time didn't touch the bit of code I'd been looking at.</p>


<p>Interestingly I couldn't find anywhere in the code base which had the string 'Failed merging' so I thought I'd do a <a href="http://stackoverflow.com/questions/4468361/search-all-of-git-history-for-string">quick scan of the diffs</a> to see if this had been deleted:</p>



~~~text

$ git log -S"Failed merging"
commit b6501aac03cf70419e94b4cfc160695e4950914a
Author: Andres Taylor <andres@neotechnology.com>
Date:   Sat Feb 16 19:30:00 2013 +0100

    Changed how Cypher merges types
~~~

<p>So in fact <a href="https://github.com/neo4j/neo4j/commit/b6501aac03cf70419e94b4cfc160695e4950914a">there was a commit</a> which changed the way that the collection type was determined so that rather than throwing an exception for clashing types a parent type would be used instead.</p>


<p>In any case this merging problem doesn't exist in 1.9.M05 and I've switched my graph to use that version of neo4j so I won't be see in this exception anymore!</p>

