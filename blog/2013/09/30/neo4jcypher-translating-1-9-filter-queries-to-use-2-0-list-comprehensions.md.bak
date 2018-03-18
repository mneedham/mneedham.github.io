+++
draft = false
date="2013-09-30 21:34:01"
title="neo4j/cypher: Translating 1.9 FILTER queries to use 2.0 list comprehensions"
tag=['neo4j', 'cypher']
category=['neo4j']
+++

<p>I was looking back over some cypher queries I'd written earlier in the year against my football data set to find some examples of where <a href="http://docs.neo4j.org/chunked/milestone/syntax-collections.html#_list_comprehension">list comprehensions</a> could be useful and I came across this query which is used to work out which teams were the most badly behaved in terms of accumulating red and yellow cards:</p>



~~~cypher

START team = node:teams('name:*') 
MATCH team<-[:for]-like_this<-[:started|as_sub]-player-[r?:sent_off_in|booked_in]->game<-[:in]-like_this 
WITH team, COLLECT(r) AS cards
WITH team, 
     FILTER(x IN cards: TYPE(x) = "sent_off_in") AS reds, 
     FILTER(x IN cards: TYPE(x) = "booked_in") AS yellows
RETURN team.name, LENGTH(reds) AS redCards, LENGTH(yellows) AS yellowCards
ORDER BY (yellowCards*1 + redCards*3) DESC
~~~

<p>We start by getting all the teams, work out which players played in that game, then work out who got booked or sent off before separating the yellow/red cards into their own respective collections. Finally we assign 3 points for a red card and 1 point for a yellow card and order the teams based on that.</p>



~~~bash

==> +-------------------------------------------------+
==> | team.name              | redCards | yellowCards |
==> +-------------------------------------------------+
==> | "Stoke City"           | 4        | 81          |
==> | "Newcastle United"     | 4        | 74          |
==> | "Aston Villa"          | 3        | 74          |
==> | "West Ham United"      | 1        | 74          |
==> | "West Bromwich Albion" | 4        | 63          |
==> | "Sunderland"           | 3        | 63          |
==> | "Wigan Athletic"       | 2        | 66          |
==> | "Manchester City"      | 3        | 62          |
==> | "Everton"              | 3        | 62          |
==> | "Queens Park Rangers"  | 3        | 60          |
==> | "Swansea City"         | 2        | 59          |
==> | "Norwich City"         | 1        | 60          |
==> | "Chelsea"              | 3        | 53          |
==> | "Liverpool"            | 2        | 54          |
==> | "Manchester United"    | 1        | 57          |
==> | "Tottenham Hotspur"    | 2        | 54          |
==> | "Arsenal"              | 5        | 44          |
==> | "Fulham"               | 3        | 48          |
==> | "Southampton"          | 2        | 44          |
==> | "Reading"              | 1        | 45          |
==> +-------------------------------------------------+
==> 20 rows
~~~

<p>Unfortunately if we run that query on a 2.0.0-M05 neo4j database we'll get the following error:</p>



~~~bash

==> SyntaxException: Invalid input '(': expected an identifier character, whitespace, NodeLabel, '.', '[', node labels, "=~", IN, IS, '*', '/', '%', '^', '+', '-', '<', '>', "<=", ">=", '=', "<>", "!=", AND, XOR, OR, WHERE, ')' or ',' (line 1, column 207)
==> "START team = node:teams('name:*')  MATCH team<-[:for]-like_this<-[:started|as_sub]-player-[r?:sent_off_in|booked_in]->game<-[:in]-like_this  WITH team, COLLECT(r) AS cards WITH team, FILTER(x IN cards: TYPE(x) = "sent_off_in") AS reds, FILTER(x IN cards: TYPE(x) = "booked_in") AS yellows RETURN team.name, LENGTH(reds) AS redCards, LENGTH(yellows) AS yellowCards ORDER BY (yellowCards*1 + redCards*3) DESC"
==>
~~~

<p>The syntax when using the <cite>FILTER</cite> function has changed a bit so we need to use a <cite>WHERE</cite> clause rather than a ':':</p>



~~~cypher

START team = node:teams('name:*') 
MATCH team<-[:for]-like_this<-[:started|as_sub]-player-[r?:sent_off_in|booked_in]->game<-[:in]-like_this 
WITH team, COLLECT(r) AS cards
WITH team, 
     FILTER(x IN cards WHERE TYPE(x) = "sent_off_in") AS reds, 
     FILTER(x IN cards WHERE TYPE(x) = "booked_in") AS yellows
RETURN team.name, LENGTH(reds) AS redCards, LENGTH(yellows) AS yellowCards
ORDER BY (yellowCards*1 + redCards*3) DESC
~~~

<p>However, as I hinted at the beginning of this post, we can also translate the query to make use of the new for comprehensions. I ended up with the following:</p>



~~~cypher

START team = node:teams('name:*') 
MATCH team<-[:for]-like_this<-[:started|as_sub]-player-[r?:sent_off_in|booked_in]->game<-[:in]-like_this 
WITH team, COLLECT(r) AS cards
WITH team, 
     [card IN cards WHERE TYPE(card) = "sent_off_in"] as reds, 
     [card in cards WHERE TYPE(card) = "booked_in"] as yellows
RETURN team.name, LENGTH(reds) AS redCards, LENGTH(yellows) AS yellowCards
ORDER BY (yellowCards*1 + redCards*3) DESC
~~~

<p>The syntax is similar to <a href="http://www.pythonforbeginners.com/lists/list-comprehensions-in-python/">Python's list comprehesions</a> and there are a <a href="http://docs.neo4j.org/chunked/milestone/syntax-collections.html#_list_comprehension">collection of examples on the manual</a> that you can follow.</p>


<p>A query I wanted to write in May, but had to park until list comprehensions were implemented, is the following one which finds the top 5 scorers for each month and returns their goal tally as well:</p>



~~~cypher

START month = node:months('name:*')
MATCH month-[:in_month]-game-[:scored_in]-player
WITH month, player, COUNT(game) AS games
ORDER BY games DESC
WITH month, 
     [x IN COLLECT([player.name, games])[0..5] | x[0]] AS players,
     [x IN COLLECT([player.name, games])[0..5] | x[1]] AS goals
ORDER BY month.position
RETURN month.name, players, goals
~~~

<p>My previous attempt was littered with calls to <cite>HEAD</cite> and <cite>TAIL</cite> but this version is much more concise. This is what it returns:</p>



~~~bash

==> +--------------------------------------------------------------------------------------------------------------------+
==> | month.name  | players                                                                                | goals       |
==> +--------------------------------------------------------------------------------------------------------------------+
==> | "August"    | ["Michu","Nathan Dyer","Fernando Torres","Mladen Petric","Damien Duff"]                | [3,2,2,2,2] |
==> | "September" | ["Demba Ba","Steven Fletcher","Peter Crouch","Robin Van Persie","Luis Suárez"]         | [5,5,4,4,4] |
==> | "October"   | ["Juan Mata","Wayne Rooney","Jose Fonte","Michu","Grant Holt"]                         | [3,2,2,2,2] |
==> | "November"  | ["Marouane Fellaini","Luis Suárez","Gareth Bale","Sergio Agüero","Olivier Giroud"]     | [4,4,3,3,3] |
==> | "December"  | ["Demba Ba","Wayne Rooney","Robin Van Persie","Michu","Theo Walcott"]                  | [5,5,5,5,4] |
==> | "January"   | ["Adam Le Fondre","Luis Suárez","Robin Van Persie","Frank Lampard","Leighton Baines"]  | [5,4,4,3,3] |
==> | "February"  | ["Gareth Bale","Romelu Lukaku","Moussa Sissoko","Christian Benteke","Santi Cazorla"]   | [5,3,3,3,3] |
==> | "March"     | ["Luis Suárez","Jan Vertonghen","Christian Benteke","Shinji Kagawa","Stewart Downing"] | [4,3,3,3,2] |
==> | "April"     | ["Robin Van Persie","Christian Benteke","Daniel Sturridge","Oscar","Andrew Carroll"]   | [6,4,3,2,2] |
==> | "May"       | ["Grant Holt","Romelu Lukaku","Daniel Sturridge","Kevin Nolan","Theo Walcott"]         | [3,3,3,3,2] |
==> +--------------------------------------------------------------------------------------------------------------------+
==> 10 rows
~~~

<p>If you like cypher and haven't played around with list comprehensions yet I'd recommend it - this syntax will help a great deal in reducing the complexity of some queries.</p>

