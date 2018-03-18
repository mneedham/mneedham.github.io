+++
draft = false
date="2014-04-13 17:40:05"
title="Neo4j 2.0.0: Query not prepared correctly / Type mismatch: expected Map"
tag=['neo4j']
category=['neo4j']
+++

<p>I was playing around with Neo4j's Cypher last weekend and found myself accidentally running some queries against an earlier version of the Neo4j 2.0 series (2.0.0).</p>


<p>My first query started with a map and I wanted to create a person from an identifier inside the map:</p>



~~~cypher

WITH {person: {id: 1}} AS params
MERGE (p:Person {id: params.person.id})
RETURN p
~~~

<p>When I ran the query I got this error:</p>



~~~text

==> SyntaxException: Type mismatch: expected Map but was Boolean, Number, String or Collection<Any> (line 1, column 62)
==> "WITH {person: {id: 1}} AS params MERGE (p:Person {id: params.person.id}) RETURN p"
~~~

<p>If we try the same query in 2.0.1 it works as we'd expect:</p>



~~~text

==> +---------------+
==> | p             |
==> +---------------+
==> | Node[1]{id:} |
==> +---------------+
==> 1 row
==> Nodes created: 1
==> Properties set: 1
==> Labels added: 1
==> 47 ms
~~~

<p>My next query was the following which links topics of interest to a person:</p>



~~~cypher

WITH {topics: [{name: "Java"}, {name: "Neo4j"}]} AS params
MERGE (p:Person {id: 2})
FOREACH(t IN params.topics | 
  MERGE (topic:Topic {name: t.name})
  MERGE (p)-[:INTERESTED_IN]->(topic)
)
RETURN p
~~~

<p>In 2.0.0 that query fails like so:</p>



~~~text

==> InternalException: Query not prepared correctly!
~~~

<p>but if we try it in 2.0.1 we'll see that it works as well:</p>



~~~text

==> +---------------+
==> | p             |
==> +---------------+
==> | Node[4]{id:2} |
==> +---------------+
==> 1 row
==> Nodes created: 1
==> Relationships created: 2
==> Properties set: 1
==> Labels added: 1
==> 53 ms
~~~

<p>So if you're seeing either of those errors then <a href="http://www.neo4j.org/download">get yourself upgraded</a> to 2.0.1 as well!</p>

