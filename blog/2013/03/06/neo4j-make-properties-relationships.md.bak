+++
draft = false
date="2013-03-06 00:59:36"
title="neo4j: Make properties relationships"
tag=['neo4j', 'cypher']
category=['neo4j']
+++

<p>I spent some of the weekend working my way through <a href="https://twitter.com/jimwebber">Jim</a>, <a href="https://twitter.com/iansrobinson">Ian</a> & <a href="https://twitter.com/emileifrem">Emil</a>'s book '<a href="http://graphdatabases.com/">Graph Databases</a>' and one of the things that they emphasise is that graphs allow us to <strong>make relationships first class citizens in our model</strong>.</p>


<p>Looking back on a couple of the graphs that I modelled last year I realise that I didn't quite get this and although the graphs I modelled had some relationships a lot of the time I was defining things as properties on nodes.</p>


<p>While it's fine to do this I think we lose some of the power of a graph and it's not necessarily obvious what we've lost until we model a property as a relationship and see what possibilities open up.</p>


<p>For example in my football graph I wanted to record the date of matches and initially stored this as a property on the match before realising that modelling it as a relationship which might open up some interesting queries.</p>


<p>I created this relationship between a match and the month that the match took place in:</p>



~~~text

MATCH-[:in_month]->MONTH
~~~

<p>As a result of having this relationship I can now really easily find out which matches Gareth Bale played in September for example:</p>



~~~cypher

START player = node:players('name:"Gareth Bale"'), month=node:months('name:September')
MATCH player-[:played_in]-game
WHERE game-[:in_month]-month
RETURN game.name, game.home_goals + "-" +game.away_goals AS score, game.date
~~~


~~~text

+----------------------------------------------------------------------------------+
| game.name                                  | score | game.date                   |
+----------------------------------------------------------------------------------+
| "Reading vs Tottenham Hotspur"             | "1-3" | "2012-09-16 16:00:00 +0100" |
| "Tottenham Hotspur vs Norwich City"        | "1-1" | "2012-09-01 15:00:00 +0100" |
| "Tottenham Hotspur vs Queens Park Rangers" | "2-1" | "2012-09-23 16:00:00 +0100" |
| "Manchester United vs Tottenham Hotspur"   | "2-3" | "2012-09-29 17:30:00 +0100" |
+----------------------------------------------------------------------------------+
~~~

<p>Or we could find all the matches in December where one of the teams won by more than 2 goals:</p>



~~~cypher

START month=node:months('name:December')
MATCH month-[:in_month]-game
WHERE ABS(game.home_goals - game.away_goals) > 2
RETURN game.name, game.home_goals + "-" +game.away_goals AS score, game.date
~~~


~~~text

+----------------------------------------------------------------------------+
| game.name                            | score | game.date                   |
+----------------------------------------------------------------------------+
| "Sunderland vs Reading"              | "3-0" | "2012-12-11 19:45:00 +0000" |
| "Reading vs Arsenal"                 | "2-5" | "2012-12-17 20:00:00 +0000" |
| "Newcastle United vs Wigan Athletic" | "3-0" | "2012-12-03 20:00:00 +0000" |
| "Fulham vs Tottenham Hotspur"        | "0-3" | "2012-12-01 15:00:00 +0000" |
| "Liverpool vs Fulham"                | "4-0" | "2012-12-22 17:30:00 +0000" |
| "Chelsea vs Aston Villa"             | "8-0" | "2012-12-23 16:00:00 +0000" |
| "Aston Villa vs Tottenham Hotspur"   | "0-4" | "2012-12-26 17:30:00 +0000" |
| "Aston Villa vs Wigan Athletic"      | "0-3" | "2012-12-29 15:00:00 +0000" |
| "Arsenal vs Newcastle United"        | "7-3" | "2012-12-29 17:30:00 +0000" |
| "Queens Park Rangers vs Liverpool"   | "0-3" | "2012-12-30 16:00:00 +0000" |
+----------------------------------------------------------------------------+
~~~

<p>There are certainly other things that we can find out now that we've got this relationship from months to matches explicit but it's not only dates where this idea comes in useful.</p>


<p>I already had players modelled in the data set but I thought it'd be interesting to find out more about the data set based on where players came from.</p>


<p>I therefore added the following relationships:</p>



~~~text

PLAYER-[:comes_from]->COUNTRY-[:is_in]->CONTINENT
~~~

<p>We can now find the top scorers in the Premiership (accurate until before last weekend) who come from South America for example:</p>



~~~cypher

START continent = node:continents('name:"South America"')
MATCH continent-[:is_in]-country-[:comes_from]-player-[:played|subbed_on]-stats-[:in]-game
WHERE player-[:scored_in]-game
RETURN player.name, country.name, player.team, SUM(stats.goals) AS goals
ORDER BY goals DESC
LIMIT 5
~~~


~~~text

+--------------------------------------------------------------+
| player.name       | country.name | player.team       | goals |
+--------------------------------------------------------------+
| "Luis Suárez"     | "Uruguay"    | "Liverpool"       | 18    |
| "Sergio Agüero"   | "Argentina"  | "Manchester City" | 9     |
| "Carlos Tevez"    | "Argentina"  | "Manchester City" | 8     |
| "Franco Di Santo" | "Argentina"  | "Wigan Athletic"  | 5     |
| "Ramires"         | "Brazil"     | "Chelsea"         | 4     |
+--------------------------------------------------------------+
~~~

<p>Or we could find out how many goals have been scored by players from each continent:</p>



~~~cypher

START continent = node:continents('name:*')
MATCH continent-[:is_in]-country-[:comes_from]-player-[:played|subbed_on]-stats-[:in]-game
WHERE player-[:scored_in]-game
RETURN continent.name, SUM(stats.goals) AS goals
ORDER BY goals DESC
~~~


~~~text

+-------------------------+
| continent.name  | goals |
+-------------------------+
| "Europe"        | 569   |
| "Africa"        | 73    |
| "South America" | 62    |
| "North America" | 22    |
| "Asia"          | 3     |
| "Oceania"       | 3     |
+-------------------------+
~~~

<p>I don't think every property needs to be a relationship but it can certainly be useful to think about doing so because it does allow you to think of interesting queries that you may not have previously thought about.</p>


<p>As an aside I'm working on putting this data set somewhere so people can play around with cypher queries on it so if you'd be interested let me know.</p>

