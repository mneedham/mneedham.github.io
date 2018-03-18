+++
draft = false
date="2016-10-30 22:12:50"
title="Neo4j: Create dynamic relationship type"
tag=['neo4j']
category=['neo4j']
+++

<p>
One of the things I've often found frustrating when importing data using Cypher, Neo4j's query language, is that it's quite difficult to create dynamic relationship types.
</p>


<p>Say we have a CSV file structured like this:</p>



~~~cypher

load csv with headers from "file:///people.csv" AS row
RETURN row
~~~


~~~text

╒═══════════════════════════════════════════════════════╕
│row                                                    │
╞═══════════════════════════════════════════════════════╡
│{node1: Mark, node2: Reshmee, relationship: MARRIED_TO}│
├───────────────────────────────────────────────────────┤
│{node1: Mark, node2: Alistair, relationship: FRIENDS}  │
└───────────────────────────────────────────────────────┘
~~~

<p>We want to create nodes with the relationship type specified in the file. Unfortunately, in Cypher we can't pass in relationship types so we have to resort to the FOREACH hack to create our relationships:</p>



~~~cypher

load csv with headers from "file:///people.csv" AS row
MERGE (p1:Person {name: row.node1})
MERGE (p2:Person {name: row.node2})

FOREACH(ignoreMe IN CASE WHEN row.relationship = "MARRIED_TO" THEN [1] ELSE [] END |
 MERGE (p1)-[:MARRIED_TO]->(p2))

FOREACH(ignoreMe IN CASE WHEN row.relationship = "FRIENDS" THEN [1] ELSE [] END |
 MERGE (p1)-[:FRIENDS]->(p2))
~~~

<p>This works, but:</p>


<ol>
<li>Looks horrendous</li>
<li>Doesn't scale particularly well when we have multiple relationship types to deal with</li>
</ol>

<p>
As <a href="http://www.markhneedham.com/blog/2016/10/27/neo4j-dynamically-add-property/">in my last post</a> the <a href="https://neo4j-contrib.github.io/neo4j-apoc-procedures/">APOC library</a> comes to the rescue again, this time in the form of the <cite>apoc.create.relationship</cite> procedure.
</p>


<p>This procedure allows us to change our initial query to read like this:</p>



~~~cypher

load csv with headers from "file:///people.csv" AS row
MERGE (p1:Person {name: row.node1})
MERGE (p2:Person {name: row.node2})

WITH p1, p2, row
CALL apoc.create.relationship(p1, row.relationship, {}, p2) YIELD rel
RETURN rel
~~~

<p>
Much better!
</p>

