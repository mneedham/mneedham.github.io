+++
draft = false
date="2014-09-26 20:46:50"
title="Neo4j: COLLECTing multiple values (Too many parameters for function 'collect')"
tag=['neo4j']
category=['neo4j']
+++

<p>One of my favourite functions in Neo4j's cypher query language is COLLECT which allows us to group items into an array for later consumption.</p>


<p>However, I've noticed that people sometimes have trouble working out how to collect multiple items with COLLECT and struggle to find a way to do so.</p>


<p>Consider the following data set:</p>



~~~cypher

create (p:Person {name: "Mark"})
create (e1:Event {name: "Event1", timestamp: 1234})
create (e2:Event {name: "Event2", timestamp: 4567})

create (p)-[:EVENT]->(e1)
create (p)-[:EVENT]->(e2)
~~~

<p>If we wanted to return each person along with a collection of the event names they'd participated in we could write the following:</p>



~~~cypher

$ MATCH (p:Person)-[:EVENT]->(e)
> RETURN p, COLLECT(e.name);
+--------------------------------------------+
| p                    | COLLECT(e.name)     |
+--------------------------------------------+
| Node[0]{name:"Mark"} | ["Event1","Event2"] |
+--------------------------------------------+
1 row
~~~

<p>That works nicely, but what about if we want to collect the event name and the timestamp but don't want to return the entire event node?</p>
 

<p>An approach I've seen a few people try during workshops is the following:</p>



~~~cypher

MATCH (p:Person)-[:EVENT]->(e)
RETURN p, COLLECT(e.name, e.timestamp)
~~~

<p>Unfortunately this doesn't compile:</p>



~~~text

SyntaxException: Too many parameters for function 'collect' (line 2, column 11)
"RETURN p, COLLECT(e.name, e.timestamp)"
           ^
~~~

<p>As the error message suggests, the COLLECT function only takes one argument so we need to find another way to solve our problem.<p>

<p>One way is to put the two values into a literal array which will result in an array of arrays as our return result:</p>



~~~cypher

$ MATCH (p:Person)-[:EVENT]->(e)
> RETURN p, COLLECT([e.name, e.timestamp]);
+----------------------------------------------------------+
| p                    | COLLECT([e.name, e.timestamp])    |
+----------------------------------------------------------+
| Node[0]{name:"Mark"} | [["Event1",1234],["Event2",4567]] |
+----------------------------------------------------------+
1 row
~~~

<p>The annoying thing about this approach is that as you add more items you'll forget in which position you've put each bit of data so I think a preferable approach is to collect a map of items instead:</p>



~~~cypher

$ MATCH (p:Person)-[:EVENT]->(e)
> RETURN p, COLLECT({eventName: e.name, eventTimestamp: e.timestamp});
+--------------------------------------------------------------------------------------------------------------------------+
| p                    | COLLECT({eventName: e.name, eventTimestamp: e.timestamp})                                         |
+--------------------------------------------------------------------------------------------------------------------------+
| Node[0]{name:"Mark"} | [{eventName -> "Event1", eventTimestamp -> 1234},{eventName -> "Event2", eventTimestamp -> 4567}] |
+--------------------------------------------------------------------------------------------------------------------------+
1 row
~~~

<p>During the <a href="http://www.meetup.com/graphdb-london/events/194308602/">Clojure Neo4j Hackathon</a> that we ran earlier this week this proved to be a particularly pleasing approach as we could easily destructure the collection of maps in our Clojure code.</p>

