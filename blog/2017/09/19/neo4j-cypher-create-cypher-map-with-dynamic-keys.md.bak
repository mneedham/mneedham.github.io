+++
draft = false
date="2017-09-19 19:30:09"
title="Neo4j: Cypher - Create Cypher map with dynamic keys"
tag=['neo4j', 'cypher', 'apoc']
category=['neo4j']
description="Learn how to create maps with dynamic keys using Neo4j's Cypher query language and the APOC procedure library."
+++

<p>
I was recently trying to create a map in a Cypher query but wanted to have dynamic keys in that map. I started off with this query:
</p>



~~~cypher

WITH "a" as dynamicKey, "b" as dynamicValue
RETURN { dynamicKey: dynamicValue } AS map


╒══════════════════╕
│"map"             │
╞══════════════════╡
│{"dynamicKey":"b"}│
└──────────────────┘
~~~

<p>
Not quite what we want! We want <cite>dynamicKey</cite> to be evaluated rather than treated as a literal. As usual, <a href="https://github.com/neo4j-contrib/neo4j-apoc-procedures">APOC</a> comes to the rescue!
</p>


<p>
In fact APOC has several functions that will help us out here. Let's take a look at them:
</p>



~~~cypher

CALL dbms.functions() yield name, description
WHERE name STARTS WITH "apoc.map.from"
RETURN name, description

╒═════════════════════╤═════════════════════════════════════════════════════╕
│"name"               │"description"                                        │
╞═════════════════════╪═════════════════════════════════════════════════════╡
│"apoc.map.fromLists" │"apoc.map.fromLists([keys],[values])"                │
├─────────────────────┼─────────────────────────────────────────────────────┤
│"apoc.map.fromNodes" │"apoc.map.fromNodes(label, property)"                │
├─────────────────────┼─────────────────────────────────────────────────────┤
│"apoc.map.fromPairs" │"apoc.map.fromPairs([[key,value],[key2,value2],...])"│
├─────────────────────┼─────────────────────────────────────────────────────┤
│"apoc.map.fromValues"│"apoc.map.fromValues([key1,value1,key2,value2,...])" │
└─────────────────────┴─────────────────────────────────────────────────────┘
~~~

<p>
So we can generate a map like this:
</p>



~~~cypher

WITH "a" as dynamicKey, "b" as dynamicValue
RETURN apoc.map.fromValues([dynamicKey, dynamicValue]) AS map

╒═════════╕
│"map"    │
╞═════════╡
│{"a":"b"}│
└─────────┘
~~~

<p>
or like this:
</p>



~~~cypher

WITH "a" as dynamicKey, "b" as dynamicValue
RETURN apoc.map.fromLists([dynamicKey], [dynamicValue]) AS map

╒═════════╕
│"map"    │
╞═════════╡
│{"a":"b"}│
└─────────┘
~~~

<p>
or even like this:
</p>



~~~cypher

WITH "a" as dynamicKey, "b" as dynamicValue
RETURN apoc.map.fromPairs([[dynamicKey, dynamicValue]]) AS map

╒═════════╕
│"map"    │
╞═════════╡
│{"a":"b"}│
└─────────┘
~~~
