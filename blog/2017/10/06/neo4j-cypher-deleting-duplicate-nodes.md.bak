+++
draft = false
date="2017-10-06 16:13:33"
title="Neo4j: Cypher - Deleting duplicate nodes"
tag=['neo4j', 'cypher']
category=['neo4j']
description="Sometimes we might accidentally create duplicate nodes in our Neo4j graph database. In this post I show how to remove them with a simple Cypher query."
+++

<p>
I had a problem on a graph I was working on recently where I'd managed to create duplicate nodes because I hadn't applied any <a href="http://neo4j.com/docs/developer-manual/current/cypher/schema/constraints/">unique constraints</a>.
</p>


<p>
I wanted to remove the duplicates, and came across <a href="https://gist.github.com/jruts/fe782ff2531d509784a24b655ad8ae76">Jimmy Ruts' excellent post</a> which shows some ways to do this.
</p>


<p>
Let's first create a graph with some duplicate nodes to play with:
</p>



~~~cypher

UNWIND range(0, 100) AS id
CREATE (p1:Person {id: toInteger(rand() * id)})
MERGE (p2:Person {id: toInteger(rand() * id)})
MERGE (p3:Person {id: toInteger(rand() * id)})
MERGE (p4:Person {id: toInteger(rand() * id)})
CREATE (p1)-[:KNOWS]->(p2)
CREATE (p1)-[:KNOWS]->(p3)
CREATE (p1)-[:KNOWS]->(p4)

Added 173 labels, created 173 nodes, set 173 properties, created 5829 relationships, completed after 408 ms.
~~~

<p>
How do we find the duplicate nodes?
</p>



~~~cypher

MATCH (p:Person)
WITH p.id as id, collect(p) AS nodes 
WHERE size(nodes) >  1
RETURN [ n in nodes | n.id] AS ids, size(nodes)
ORDER BY size(nodes) DESC
LIMIT 10

╒══════════════════════╤═════════════╕
│"ids"                 │"size(nodes)"│
╞══════════════════════╪═════════════╡
│[1,1,1,1,1,1,1,1]     │8            │
├──────────────────────┼─────────────┤
│[0,0,0,0,0,0,0,0]     │8            │
├──────────────────────┼─────────────┤
│[17,17,17,17,17,17,17]│7            │
├──────────────────────┼─────────────┤
│[4,4,4,4,4,4,4]       │7            │
├──────────────────────┼─────────────┤
│[2,2,2,2,2,2]         │6            │
├──────────────────────┼─────────────┤
│[5,5,5,5,5,5]         │6            │
├──────────────────────┼─────────────┤
│[19,19,19,19,19,19]   │6            │
├──────────────────────┼─────────────┤
│[11,11,11,11,11]      │5            │
├──────────────────────┼─────────────┤
│[25,25,25,25,25]      │5            │
├──────────────────────┼─────────────┤
│[43,43,43,43,43]      │5            │
└──────────────────────┴─────────────┘
~~~

<p>
Let's zoom in on all the people with 'id:1' and work out how many relationships they have. Our plan is keep the node that has the most connections and get rid of the others.
</p>



~~~cypher

MATCH (p:Person)
WITH p.id as id, collect(p) AS nodes 
WHERE size(nodes) >  1
WITH nodes ORDER BY size(nodes) DESC
LIMIT 1
UNWIND nodes AS n 
RETURN n.id, id(n) AS internalId, size((n)--()) AS rels
ORDER BY rels DESC

╒══════╤════════════╤══════╕
│"n.id"│"internalId"│"rels"│
╞══════╪════════════╪══════╡
│1     │175         │1284  │
├──────┼────────────┼──────┤
│1     │184         │721   │
├──────┼────────────┼──────┤
│1     │180         │580   │
├──────┼────────────┼──────┤
│1     │2           │391   │
├──────┼────────────┼──────┤
│1     │195         │361   │
├──────┼────────────┼──────┤
│1     │199         │352   │
├──────┼────────────┼──────┤
│1     │302         │5     │
├──────┼────────────┼──────┤
│1     │306         │1     │
└──────┴────────────┴──────┘
~~~

<p>
So in this example we want to keep the node that has 210 relationships and delete the rest.
</p>


<p>
To make things easy we need the node with the highest cardinality to be first or last in our list. We can ensure that's the case by ordering the nodes before we group them.
</p>



~~~cypher

MATCH (p:Person)
WITH p 
ORDER BY p.id, size((p)--()) DESC
WITH p.id as id, collect(p) AS nodes 
WHERE size(nodes) >  1
RETURN [ n in nodes | {id: n.id,rels: size((n)--()) } ] AS ids, size(nodes)
ORDER BY size(nodes) DESC
LIMIT 10

╒══════════════════════════════════════════════════════════════════════╤═════════════╕
│"ids"                                                                 │"size(nodes)"│
╞══════════════════════════════════════════════════════════════════════╪═════════════╡
│[{"id":1,"rels":1284},{"id":1,"rels":721},{"id":1,"rels":580},{"id":1,│8            │
│"rels":391},{"id":1,"rels":361},{"id":1,"rels":352},{"id":1,"rels":5},│             │
│{"id":1,"rels":1}]                                                    │             │
├──────────────────────────────────────────────────────────────────────┼─────────────┤
│[{"id":0,"rels":2064},{"id":0,"rels":2059},{"id":0,"rels":1297},{"id":│8            │
│0,"rels":1124},{"id":0,"rels":995},{"id":0,"rels":928},{"id":0,"rels":│             │
│730},{"id":0,"rels":702}]                                             │             │
├──────────────────────────────────────────────────────────────────────┼─────────────┤
│[{"id":17,"rels":153},{"id":17,"rels":105},{"id":17,"rels":81},{"id":1│7            │
│7,"rels":31},{"id":17,"rels":15},{"id":17,"rels":14},{"id":17,"rels":1│             │
│}]                                                                    │             │
├──────────────────────────────────────────────────────────────────────┼─────────────┤
│[{"id":4,"rels":394},{"id":4,"rels":320},{"id":4,"rels":250},{"id":4,"│7            │
│rels":201},{"id":4,"rels":162},{"id":4,"rels":162},{"id":4,"rels":14}]│             │
├──────────────────────────────────────────────────────────────────────┼─────────────┤
│[{"id":2,"rels":514},{"id":2,"rels":329},{"id":2,"rels":318},{"id":2,"│6            │
│rels":241},{"id":2,"rels":240},{"id":2,"rels":2}]                     │             │
├──────────────────────────────────────────────────────────────────────┼─────────────┤
│[{"id":5,"rels":487},{"id":5,"rels":378},{"id":5,"rels":242},{"id":5,"│6            │
│rels":181},{"id":5,"rels":158},{"id":5,"rels":8}]                     │             │
├──────────────────────────────────────────────────────────────────────┼─────────────┤
│[{"id":19,"rels":153},{"id":19,"rels":120},{"id":19,"rels":84},{"id":1│6            │
│9,"rels":53},{"id":19,"rels":45},{"id":19,"rels":1}]                  │             │
├──────────────────────────────────────────────────────────────────────┼─────────────┤
│[{"id":11,"rels":222},{"id":11,"rels":192},{"id":11,"rels":172},{"id":│5            │
│11,"rels":152},{"id":11,"rels":89}]                                   │             │
├──────────────────────────────────────────────────────────────────────┼─────────────┤
│[{"id":25,"rels":133},{"id":25,"rels":107},{"id":25,"rels":98},{"id":2│5            │
│5,"rels":15},{"id":25,"rels":2}]                                      │             │
├──────────────────────────────────────────────────────────────────────┼─────────────┤
│[{"id":43,"rels":92},{"id":43,"rels":85},{"id":43,"rels":9},{"id":43,"│5            │
│rels":5},{"id":43,"rels":1}]                                          │             │
└──────────────────────────────────────────────────────────────────────┴─────────────┘───────────────────────────────────────────────────────┴─────────────┘
~~~

<p>
Now it's time to delete the duplicates:
</p>



~~~cypher

MATCH (p:Person)
WITH p 
ORDER BY p.id, size((p)--()) DESC
WITH p.id as id, collect(p) AS nodes 
WHERE size(nodes) >  1
UNWIND nodes[1..] AS n
DETACH DELETE n

Deleted 143 nodes, deleted 13806 relationships, completed after 29 ms.
~~~

<p>
Now if we run our duplicate query:
</p>



~~~cypher

MATCH (p:Person)
WITH p.id as id, collect(p) AS nodes 
WHERE size(nodes) >  1
RETURN [ n in nodes | n.id] AS ids, size(nodes)
ORDER BY size(nodes) DESC
LIMIT 10

(no changes, no records)
~~~

<p>
What about if we remove the WHERE clause?
</p>



~~~cypher

MATCH (p:Person)
WITH p.id as id, collect(p) AS nodes 
RETURN [ n in nodes | n.id] AS ids, size(nodes)
ORDER BY size(nodes) DESC
LIMIT 10

╒═════╤═════════════╕
│"ids"│"size(nodes)"│
╞═════╪═════════════╡
│[23] │1            │
├─────┼─────────────┤
│[86] │1            │
├─────┼─────────────┤
│[77] │1            │
├─────┼─────────────┤
│[59] │1            │
├─────┼─────────────┤
│[50] │1            │
├─────┼─────────────┤
│[32] │1            │
├─────┼─────────────┤
│[41] │1            │
├─────┼─────────────┤
│[53] │1            │
├─────┼─────────────┤
│[44] │1            │
├─────┼─────────────┤
│[8]  │1            │
└─────┴─────────────┘
~~~

<p>Hoorah, no more duplicates! Finally, let's check that we kept the node we expected to keep. We expect it to have an 'internalId' of 175:</p>



~~~cypher

MATCH (p:Person {id: 1})
RETURN size((p)--()), id(p) AS internalId

╒═══════════════╤════════════╕
│"size((p)--())"│"internalId"│
╞═══════════════╪════════════╡
│242            │175         │
└───────────────┴────────────┘
~~~

<p>
Which it does! There are many fewer relationships than we had before because a lot of those relationships were to duplicate nodes that we've now deleted.
</p>


<p>
If we want to go a step further we could 'merge' the duplicate node's relationships onto the nodes that we did keep, but that's for another post!
</p>

