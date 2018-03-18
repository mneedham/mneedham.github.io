+++
draft = false
date="2017-11-06 16:17:35"
title="Neo4j Browser: Expected entity id to be an integral value"
tag=['javascript', 'neo4j', 'neo4j-browser']
category=['neo4j']
description="Learn how to handle the 'Expected entity id to be an integral value' error that you get if you pass in 32 bit integer values as params to a query."
+++

<p>
I came across an interesting error while writing a Cypher query that used parameters in the Neo4j browser which I thought I should document for future me. 
</p>


<p>
We'll start with a graph that has 1,000 people:
</p>



~~~cypher

unwind range(0,1000) AS id
create (:Person {id: id})
~~~

<p>
Now we'll try and retrieve some of those people via a parameter lookup:
</p>



~~~cypher

:param ids: [0]
~~~



~~~cypher

match (p:Person) where p.id in {ids}
return p

╒════════╕
│"p"     │
╞════════╡
│{"id":0}│
└────────┘
~~~

<p>
All good so far. Now what about if we try and look them up by their internal node id instead:
</p>



~~~cypher

match (p:Person) where id(p) in {ids}
return p

Neo.ClientError.Statement.TypeError
Expected entity id to be an integral value
~~~

<p>
Hmm, that was unexpected. It turns out that to get this query to work we need to cast each of the integer values in the <cite>{ids}</cite> array to a 64 bit integer using the <cite><a href="https://neo4j.com/docs/developer-manual/current/cypher/functions/scalar/#functions-tointeger">toInteger</a></cite> function:</p>



~~~cypher

match (p:Person) where id(p) in [id in {ids} | toInteger(id)]
return p

╒════════╕
│"p"     │
╞════════╡
│{"id":0}│
└────────┘
~~~

<p>
Success!
</p>

