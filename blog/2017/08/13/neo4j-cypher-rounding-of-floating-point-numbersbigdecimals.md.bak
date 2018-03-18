+++
draft = false
date="2017-08-13 07:23:46"
title="Neo4j: Cypher - Rounding of floating point numbers/BigDecimals"
tag=['neo4j', 'cypher', 'apoc']
category=['neo4j']
description="Learn how to deal with floating point arithmetic and rounding errors when working with Neo4j's Cypher query language. APOC comes to the rescue."
+++

<p>
I was doing some data cleaning a few days ago and wanting to multiply a value by 1 million. My <a href="https://neo4j.com/developer/cypher-query-language/">Cypher</a> code to do this looked like this:
</p>



~~~cypher

with "8.37" as rawNumeric 
RETURN toFloat(rawNumeric) * 1000000 AS numeric

╒═════════════════╕
│"numeric"        │
╞═════════════════╡
│8369999.999999999│
└─────────────────┘
~~~

<p>
Unfortunately that suffers from the classic rounding error when working with floating point numbers. I couldn't figure out a way to solve it using pure Cypher, but there tends to be an <a href="https://neo4j-contrib.github.io/neo4j-apoc-procedures/">APOC</a> function to solve every problem and <a href="https://neo4j-contrib.github.io/neo4j-apoc-procedures/index32.html#_handle_biginteger_and_bigdecimal">this was no exception</a>.
</p>


<p>I'm using Neo4j 3.2.3 so I downloaded the corresponding APOC jar and put it in a plugins directory:
</p>



~~~bash

$ ls -lh plugins/
total 3664
-rw-r--r--@ 1 markneedham  staff   1.8M  9 Aug 09:14 apoc-3.2.0.4-all.jar
~~~

<p>
I'm using Docker so I needed to tell that where my plugins folder lives:
</p>



~~~bash

$ docker run -v $PWD/plugins:/plugins \
    -p 7474:7474 \
    -p 7687:7687 \
    -e NEO4J_AUTH="none" \
    neo4j:3.2.3
~~~

<p>
Now we're reading to try out our new function:
</p>



~~~cypher

with "8.37" as rawNumeric 
RETURN apoc.number.exact.mul(rawNumeric,"1000000") AS apocConversion

╒════════════════╕
│"apocConversion"│
╞════════════════╡
│"8370000.00"    │
└────────────────┘
~~~

<p>
That almost does what we want, but the result is a string rather than numeric value. It's not too difficult to fix though:
</p>



~~~cypher

with "8.37" as rawNumeric 
RETURN toFloat(apoc.number.exact.mul(rawNumeric,"1000000")) AS apocConversion

╒════════════════╕
│"apocConversion"│
╞════════════════╡
│8370000         │
└────────────────┘
~~~

<p>
That's more like it!
</p>

