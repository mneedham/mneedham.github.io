+++
draft = false
date="2017-12-01 22:09:17"
title="Neo4j: Cypher - Property values can only be of primitive types or arrays thereof."
tag=['neo4j', 'cypher']
category=['neo4j']
+++

<p>
I ran into an interesting <a href="https://neo4j.com/developer/cypher-query-language/">Cypher</a> error message earlier this week while trying to create an array property on a node which I thought I'd share.
</p>


<p>
This was the Cypher query I wrote:
</p>



~~~cypher

CREATE (:Person {id: [1, "mark", 2.0]})
~~~

<p>which results in this error:</p>



~~~cypher

Neo.ClientError.Statement.TypeError
Property values can only be of primitive types or arrays thereof.
~~~

<p>
We actually are storing an array of primitives but we have a mix of different types which isn't allowed. Let's try coercing all the values to strings:
</p>



~~~cypher

CREATE (:Person {id: [value in [1, "mark", 2.0] | toString(value)]})

Added 1 label, created 1 node, set 1 property, completed after 4 ms.
~~~

<p>Success!
</p>

