+++
draft = false
date="2013-03-20 02:54:43"
title="neo4j/cypher: WITH, COLLECT & EXTRACT"
tag=['neo4j', 'cypher']
category=['neo4j']
+++

<p>As I <a href="http://www.markhneedham.com/blog/2013/03/20/neo4jcypher-getting-the-hang-of-the-with-statement/">mentioned in my last post</a> I'm trying to get the hang of the <cite><a href="http://docs.neo4j.org/chunked/milestone/query-with.html">WITH</a></cite> statement in neo4j's <a href="http://docs.neo4j.org/chunked/milestone/cypher-query-lang.html">cypher</a> query language and I found another application when trying to work out which opponents teams played on certain days.</p>


<p>I started out with a query which grouped the data set by day and showed the opponents that were played on that day:</p>
 


~~~cypher

START team = node:teams('name:"Manchester United"')
MATCH team-[h:home_team|away_team]-game-[:on_day]-day
RETURN DISTINCT day.name, COLLECT(TRIM(REPLACE(REPLACE(game.name, "Manchester United", ""), "vs", "")))
~~~


~~~text

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| day.name    | opponents                                                                                                                                                                                                                       |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| "Sunday"    | ["Liverpool","Everton","Southampton","Liverpool","Newcastle United","Chelsea","Manchester City","Swansea City","Tottenham Hotspur"]                                                                                             |
| "Wednesday" | ["Southampton","West Ham United","Newcastle United"]                                                                                                                                                                            |
| "Monday"    | ["Everton"]                                                                                                                                                                                                                     |
| "Saturday"  | ["Reading","Fulham","Wigan Athletic","Tottenham Hotspur","Stoke City","Arsenal","Queens Park Rangers","Sunderland","West Bromwich Albion","Norwich City","Reading","Aston Villa","Norwich City","Fulham","Queens Park Rangers"] |
| "Tuesday"   | ["Wigan Athletic"]                                                                                                                                                                                                              |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
5 rows
~~~

<p>The way we've got the opponents is a bit of a hack - the name of the two teams is in the 'name' property of a game node and we've removed 'Manchester United' and the word 'vs' to get the opponent's name.</p>


<p>I thought it'd be cool if we could separate the games on each day based on whether Manchester United were playing at home or away.</p>


<p>With <a href="https://groups.google.com/forum/?fromgroups=#!topic/neo4j/D4M1gXKwQ3U">a lot of help from Wes Freeman</a> we ended up with the following query which does the job:</p>



~~~cypher

START team = node:teams('name:"Manchester United"')
MATCH team-[h:home_team|away_team]-game-[:on_day]-day 
WITH day.name as d, game, team, h 
MATCH team-[:home_team|away_team]-game-[:home_team|away_team]-opp 
WITH d, COLLECT([type(h),opp.name]) AS games 
RETURN d, 
  EXTRACT(c in FILTER(x in games: HEAD(x) = "home_team") : HEAD(TAIL(c))) AS home,   
  EXTRACT(c in FILTER(x in games: HEAD(x) = "away_team") : HEAD(TAIL(c))) AS away
~~~

<p>We use a similar approach with COLLECT as in the <a href="http://www.markhneedham.com/blog/2013/03/20/neo4jcypher-getting-the-hang-of-the-with-statement/">previous post</a> whereby we have a collection of tuples describing whether Manchester United were at home or not and who they were playing.</p>


<p>A neat thing that Wes pointed out is that since there are only 2 teams per game we're able to get the opponent node easily because it's the only other node that can match the 'home_team|away_team" relationship since we've already matched our team.</p>


<p>If we run the query just up to the last WITH we get the following result:</p>



~~~text

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| d           | games                                                                                                                                                                                                                                                                                                                                                                                                                                             |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| "Sunday"    | [["home_team","Liverpool"],["home_team","Everton"],["away_team","Southampton"],["away_team","Liverpool"],["away_team","Newcastle United"],["away_team","Chelsea"],["away_team","Manchester City"],["away_team","Swansea City"],["away_team","Tottenham Hotspur"]]                                                                                                                                                                                 |
| "Wednesday" | [["home_team","Southampton"],["home_team","West Ham United"],["home_team","Newcastle United"]]                                                                                                                                                                                                                                                                                                                                                    |
| "Monday"    | [["away_team","Everton"]]                                                                                                                                                                                                                                                                                                                                                                                                                         |
| "Saturday"  | [["home_team","Reading"],["home_team","Fulham"],["home_team","Wigan Athletic"],["home_team","Tottenham Hotspur"],["home_team","Stoke City"],["home_team","Arsenal"],["home_team","Queens Park Rangers"],["home_team","Sunderland"],["home_team","West Bromwich Albion"],["home_team","Norwich City"],["away_team","Reading"],["away_team","Aston Villa"],["away_team","Norwich City"],["away_team","Fulham"],["away_team","Queens Park Rangers"]] |
| "Tuesday"   | [["away_team","Wigan Athletic"]]                                                                                                                                                                                                                                                                                                                                                                                                                  |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
5 rows
~~~

<p>We then use the <a href="http://docs.neo4j.org/chunked/milestone/query-function.html#functions-filter">FILTER</a> function to choose either the opponents Manchester United played at home or away and then we use the <a href="http://docs.neo4j.org/chunked/milestone/query-function.html#functions-extract">EXTRACT</a> function to get the opponent from the tuple:</p>



~~~text

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| d           | home                                                                                                                                                      |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| "Sunday"    | ["Liverpool","Everton"]                                                                                                                                   |
| "Wednesday" | ["Southampton","West Ham United","Newcastle United"]                                                                                                      |
| "Monday"    | []                                                                                                                                                        |
| "Saturday"  | ["Reading","Fulham","Wigan Athletic","Tottenham Hotspur","Stoke City","Arsenal","Queens Park Rangers","Sunderland","West Bromwich Albion","Norwich City"] |
| "Tuesday"   | []                                                                                                                                                        |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
5 rows

+-----------------------------------------------------------------------------------------------------------------------------+
| d           | away                                                                                                          |
+-----------------------------------------------------------------------------------------------------------------------------+
| "Sunday"    | ["Southampton","Liverpool","Newcastle United","Chelsea","Manchester City","Swansea City","Tottenham Hotspur"] |
| "Wednesday" | []                                                                                                            |
| "Monday"    | ["Everton"]                                                                                                   |
| "Saturday"  | ["Reading","Aston Villa","Norwich City","Fulham","Queens Park Rangers"]                                       |
| "Tuesday"   | ["Wigan Athletic"]                                                                                            |
+-----------------------------------------------------------------------------------------------------------------------------+
5 rows
~~~

<p><em>(I ran the query twice alternating between the last two lines so that it's readable here. In actual fact the away teams would be in a column next to the home teams)</em></p>


<p>I thought it was quite interesting how many games Manchester United play away on a Sunday - I think all of those games were probably televised so I thought they'd be more evenly split between home and away matches. Adding televised matches is perhaps <a href="http://www.markhneedham.com/blog/2012/07/21/neo4j-embracing-the-sub-graph/">another layer to add to the graph</a>.</p>


<p>It's probably more useful to summarise how many games were played on each day at home and away rather than who they're against and we can use the <cite>REDUCE</cite> function to do this:</p>



~~~cypher

START team = node:teams('name:"Manchester United"')
MATCH team-[h:home_team|away_team]-game-[:on_day]-day 
WITH day.name as dayName, game, team, h 
MATCH team-[:home_team|away_team]-game-[:home_team|away_team]-opp 
WITH dayName, COLLECT([type(h),opp.name]) AS games 
RETURN dayName, 
  REDUCE(homeGames=0, game in EXTRACT(c in FILTER(x in games: head(x) = "home_team") : HEAD(TAIL(c))) : homeGames + 1) as home,   
  REDUCE(awayGames=0, game in EXTRACT(c in FILTER(x in games: head(x) = "away_team") : HEAD(TAIL(c))) : awayGames + 1) as away,
  REDUCE(totalGames=0, game in games : totalGames + 1) as total
~~~


~~~text

+-----------------------------------+
| dayName     | home | away | total |
+-----------------------------------+
| "Sunday"    | 2    | 7    | 9     |
| "Wednesday" | 3    | 0    | 3     |
| "Monday"    | 0    | 1    | 1     |
| "Saturday"  | 10   | 5    | 15    |
| "Tuesday"   | 0    | 1    | 1     |
+-----------------------------------+
5 rows
~~~

<p>An alternative way of writing the initial query would be the following which Michael Hunger suggested on the thread:</p>



~~~cypher

START team = node:teams('name:"Manchester United"')
MATCH p=team-[:home_team|away_team]-game-[:home_team|away_team]-(), game-[:on_day]-day
WITH day.name as dayName, COLLECT([LAST(p), HEAD(RELS(p))]) AS opponents
WITH dayName,  
  EXTRACT(y in FILTER(x in opponents: TYPE(HEAD(TAIL(x))) = "home_team") : HEAD(y)) AS home,
  EXTRACT(y in FILTER(x in opponents : TYPE(HEAD(TAIL(x))) = "away_team") : HEAD(y)) AS away
RETURN dayName, 
  EXTRACT(team in home: team.name) AS homeOpponents,
  EXTRACT(team in away: team.name) AS awayOpponents
ORDER BY dayName
~~~

<p>Here we take a slightly different approach where we make use of functions that we can apply to a matching path. We create a collection of tuples where <cite>LAST(p)</cite> matches the opponent node and <cite>HEAD(RELS(p))</cite> matches the 'home_team' or 'away_team' relationship accordingly.</p>


<p>We then filter the collection to find the times that we played at home and away. This is done by taking the second value from the tuple and then calling <cite>TYPE</cite> on it which either returns 'home_team' or 'away_team'. We then extract the first value from the tuple which is the opponent node.</p>


<p>In the last part of the query we extract the name from the opponent nodes.</p>

