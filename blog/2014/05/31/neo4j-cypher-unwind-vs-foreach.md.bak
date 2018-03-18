+++
draft = false
date="2014-05-31 14:19:25"
title="Neo4j: Cypher - UNWIND vs FOREACH"
tag=['neo4j', 'cypher']
category=['neo4j']
+++

<p>I've written a <a href="http://www.markhneedham.com/blog/2014/05/20/neo4j-2-0-creating-adjacency-matrices/">couple of</a> <a href="http://www.markhneedham.com/blog/2014/05/25/neo4j-2-1-passing-around-node-ids-vs-unwind/">posts</a> about the new <a href="http://docs.neo4j.org/chunked/milestone/query-unwind.html">UNWIND</a> clause in Neo4j's cypher query language but I forgot about my favourite use of UNWIND, which is to get rid of some uses of <a href="http://docs.neo4j.org/chunked/stable/query-foreach.html">FOREACH</a> from our queries.</p>


<p>Let's say we've <a href="http://www.markhneedham.com/blog/2014/04/19/neo4j-cypher-creating-a-time-tree-down-to-the-day/">created a timetree up front</a> and now have a series of events coming in that we want to create in the database and attach to the appropriate part of the timetree.</p>


<p>Before UNWIND existed we might try to write the following query using FOREACH:</p>



~~~cypher

WITH [{name: "Event 1", timetree: {day: 1, month: 1, year: 2014}}, 
      {name: "Event 2", timetree: {day: 2, month: 1, year: 2014}}] AS events
FOREACH (event IN events | 
  CREATE (e:Event {name: event.name})
  MATCH (year:Year {year: event.timetree.year }), 
        (year)-[:HAS_MONTH]->(month {month: event.timetree.month }),
        (month)-[:HAS_DAY]->(day {day: event.timetree.day })
  CREATE (e)-[:HAPPENED_ON]->(day))
~~~

<p>Unfortunately we can't use MATCH inside a FOREACH statement so we'll get the following error:</p>



~~~cypher

Invalid use of MATCH inside FOREACH (line 5, column 3)
"  MATCH (year:Year {year: event.timetree.year }), "
   ^
Neo.ClientError.Statement.InvalidSyntax
~~~

<p>We can work around this by using MERGE instead in the knowledge that it's never going to create anything because the timetree already exists:</p>



~~~cypher

WITH [{name: "Event 1", timetree: {day: 1, month: 1, year: 2014}}, 
      {name: "Event 2", timetree: {day: 2, month: 1, year: 2014}}] AS events
FOREACH (event IN events | 
  CREATE (e:Event {name: event.name})
  MERGE (year:Year {year: event.timetree.year })
  MERGE (year)-[:HAS_MONTH]->(month {month: event.timetree.month })
  MERGE (month)-[:HAS_DAY]->(day {day: event.timetree.day })
  CREATE (e)-[:HAPPENED_ON]->(day))
~~~

<p>If we replace the FOREACH with UNWIND we'd get the following:</p>



~~~cypher

WITH [{name: "Event 1", timetree: {day: 1, month: 1, year: 2014}}, 
      {name: "Event 2", timetree: {day: 2, month: 1, year: 2014}}] AS events
UNWIND events AS event
CREATE (e:Event {name: event.name})
WITH e, event.timetree AS timetree
MATCH (year:Year {year: timetree.year }), 
      (year)-[:HAS_MONTH]->(month {month: timetree.month }),
      (month)-[:HAS_DAY]->(day {day: timetree.day })
CREATE (e)-[:HAPPENED_ON]->(day)
~~~

<p>Although the lines of code has slightly increased the query is now correct and we won't accidentally correct new parts of our time tree.<p> 

<p>We could also pass on the event that we created to the next part of the query which wouldn't be the case when using FOREACH.</p>

