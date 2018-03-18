+++
draft = false
date="2018-03-14 16:53:33"
title="Neo4j: Cypher - Neo.ClientError.Statement.TypeError: Don't know how to add Double and String"
tag=['neo4j', 'cypher']
category=['neo4j']
+++

<p>
I recently upgraded a Neo4j backed application from Neo4j 3.2 to Neo4j 3.3 and came across an interesting change in behaviour around type coercion which led to my application throwing a bunch of errors.
</p>


<p>
In Neo4j 3.2 and earlier if you added a String to a Double it would coerce the Double to a String and concatenate the values. The following would therefore be valid Cypher:
</p>



~~~cypher

RETURN toFloat("1.0") + " Mark"

╒══════════╕
│"result"  │
╞══════════╡
│"1.0 Mark"│
└──────────┘
~~~

<p>
This behaviour has changed in the 3.3 series and will instead throw an exception:
</p>



~~~cypher

RETURN toFloat("1.0") + " Mark"

Neo.ClientError.Statement.TypeError: Don't know how to add `Double(1.000000e+00)` and `String(" Mark")`
~~~

<p>
We can workaround that by forcing our query to run in 3.2 mode:
</p>



~~~cypher

CYPHER 3.2
RETURN toFloat("1.0") + " Mark" AS result
~~~

<p>
or we can convert the Double to a String in our Cypher statement:
</p>



~~~cypher

RETURN toString(toFloat("1.0")) + " Mark" AS result
~~~
