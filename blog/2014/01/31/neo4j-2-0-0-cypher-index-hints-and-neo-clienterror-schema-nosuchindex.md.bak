+++
draft = false
date="2014-01-31 07:14:53"
title="Neo4j 2.0.0: Cypher - Index Hints and Neo.ClientError.Schema.NoSuchIndex"
tag=['neo4j', 'cypher']
category=['neo4j']
+++

<p>One of the features added into the more recent versions of Neo4j's cypher query language is the ability to <a href="http://docs.neo4j.org/chunked/stable/query-using.html">tell Cypher which index you'd like to use in your queries</a>.</p>


<p>We'll use the football dataset, so let's start by creating an index on the 'name' property of nodes labelled 'Player':</p>



~~~cypher

CREATE INDEX ON :Player(name)
~~~

<p>Let's say we want to write a query to find 'Wayne Rooney' while explicitly using this index. We might start with the following query:</p>



~~~cypher

MATCH p
USING INDEX p:Player(name)
WHERE p.name = "Wayne Rooney"
RETURN p
~~~

<p>If we run that we'll see this error:</p>



~~~text

Cannot use index hint in this context. The label and property comparison must be specified on a non-optional node
Label: `Player`
Property name: `name`
Neo.ClientError.Schema.NoSuchIndex
~~~

<p>We need to specify the label on the node in the 'MATCH' part of the query for our hint to work e.g.</p>



~~~cypher

MATCH (p:Player)
USING INDEX p:Player(name)
WHERE p.name = "Wayne Rooney"
RETURN p
~~~

<p>Now we might decide that we want to find 'Wayne Rooney' or 'Robin Van Persie' so we change our query slightly:</p>



~~~cypher

MATCH (p:Player)
USING INDEX p:Player(name)
WHERE p.name = "Wayne Rooney" OR p.name = "Robin Van Persie"
RETURN p
~~~

<p>But this one fails too!</p>



~~~cypher

Cannot use index hint in this context. The label and property comparison must be specified on a non-optional node
Label: `Player`
Property name: `name`
Neo.ClientError.Schema.NoSuchIndex
~~~

<p>The problem here is that when you use 'OR' it's currently not using an index but rather a label scan so the hint to use the index doesn't make sense to Cypher.</p>


<p>The final way I've seen people get confused using index hints is when matching node properties inline e.g.</p>



~~~cypher

MATCH (p:Player {name: "Wayne Rooney"})
USING INDEX p:Player(name)
RETURN p
~~~

<p>If we run that we'll be back in the land of exceptions:</p>



~~~text

Cannot use index hint in this context. The label and property comparison must be specified on a non-optional node
Label: `Player`
Property name: `name`
Neo.ClientError.Schema.NoSuchIndex
~~~

<p>We can work around that by pulling out the inline matching of the 'name' property":</p>



~~~cypher

MATCH (p:Player)
USING INDEX p:Player(name)
WHERE p.name = "Wayne Rooney"
RETURN p
~~~
