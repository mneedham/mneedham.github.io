+++
draft = false
date="2014-06-17 23:41:35"
title="Neo4j: LOAD CSV - Handling conditionals"
tag=['neo4j', 'cypher']
category=['neo4j']
+++

<p>While <a href="http://worldcup.neo4j.org/extending-the-world-cup-graph-domain-model/">building up the Neo4j World Cup Graph</a> I've been making use of the <cite><a href="http://neo4j.com/blog/neo4j-2-1-graph-etl">LOAD CSV</a></cite> function  and I frequently found myself needing to do different things depending on the value in one of the columns.</p>


<p>For example I have <a href="https://raw.githubusercontent.com/mneedham/neo4j-worldcup/master/data/import/events.csv">one CSV file</a> which contains the different events that can happen in a football match:</p>



~~~bash

match_id,player,player_id,time,type
"1012","Antonin Panenka","174835",21,"penalty"
"1012","Faisal Al Dakhil","2204",57,"goal"
"102","Roger Milla","79318",106,"goal"
"102","Roger Milla","79318",108,"goal"
"102","Bernardo Redin","44555",115,"goal"
"102","Andre Kana-biyik","174649",44,"yellow"
~~~

<p>If the <cite>type</cite> is 'penalty', 'owngoal' or 'goal' then I want to create a SCORED_GOAL relationship whereas if it's  'yellow', 'yellowred' or 'red' then I want to create a RECEIVED_CARD relationship instead.</p>


<p>I learnt - from reading <a href="https://github.com/cleishm/opendisclosure/blob/master/neo4j/import.cyp#L31">a cypher script written by Chris Leishman</a> - that we can make FOREACH mimic a conditional by creating a collection with one item in to represent 'true' and an empty collection to represent 'false'.</p>
 

<p>In this case we'd end up with something like this to handle the case where a row represents a goal:</p>



~~~cypher

LOAD CSV WITH HEADERS FROM "https://raw.githubusercontent.com/mneedham/neo4j-worldcup/master/data/import/events.csv" AS csvLine

// removed for conciseness

// goals
FOREACH(n IN (CASE WHEN csvLine.type IN ["penalty", "goal", "owngoal"] THEN [1] else [] END) |
  FOREACH(t IN CASE WHEN team = home THEN [home] ELSE [away] END |
    MERGE (stats)-[:SCORED_GOAL]->(penalty:Goal {time: csvLine.time, type: csvLine.type})
  )		
)
~~~

<p>And equally when we want to process a row that represents a card we'd have this:</p>



~~~cypher

// cards
FOREACH(n IN (CASE WHEN csvLine.type IN ["yellow", "red", "yellowred"] THEN [1] else [] END) |
  FOREACH(t IN CASE WHEN team = home THEN [home] ELSE [away] END |
    MERGE (stats)-[:RECEIVED_CARD]->(card {time: csvLine.time, type: csvLine.type})
  )		
)
~~~

<p>And if we put everything together we get this:</p>



~~~cypher

USING PERIODIC COMMIT 1000
LOAD CSV WITH HEADERS FROM "https://raw.githubusercontent.com/mneedham/neo4j-worldcup/master/data/import/events.csv" AS csvLine

MATCH (home)<-[:HOME_TEAM]-(match:Match {id: csvLine.match_id})-[:AWAY_TEAM]->(away)

MATCH (player:Player {id: csvLine.player_id})-[:IN_SQUAD]->(squad)<-[:NAMED_SQUAD]-(team)
MATCH (player)-[:STARTED|:SUBSTITUTE]->(stats)-[:IN_MATCH]->(match)

// goals
FOREACH(n IN (CASE WHEN csvLine.type IN ["penalty", "goal", "owngoal"] THEN [1] else [] END) |
  FOREACH(t IN CASE WHEN team = home THEN [home] ELSE [away] END |
    MERGE (stats)-[:SCORED_GOAL]->(penalty:Goal {time: csvLine.time, type: csvLine.type})
  )		
)

// cards
FOREACH(n IN (CASE WHEN csvLine.type IN ["yellow", "red", "yellowred"] THEN [1] else [] END) |
  FOREACH(t IN CASE WHEN team = home THEN [home] ELSE [away] END |
    MERGE (stats)-[:RECEIVED_CARD]->(card {time: csvLine.time, type: csvLine.type})
  )		
)
;
~~~

<p>You can have a look at the <a href="https://github.com/mneedham/neo4j-worldcup/blob/master/data/import/loadEvents.cyp">code on github</a> or <a href="https://github.com/mneedham/neo4j-worldcup#importing-into-neo4j">follow the instructions to get all the World Cup graph into your own local Neo4j</a>.</p>


<p>Feedback welcome as always.</p>

