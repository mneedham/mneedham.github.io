+++
draft = false
date="2016-10-19 05:16:07"
title="Neo4j: Detecting rogue spaces in CSV headers with LOAD CSV"
tag=['neo4j']
category=['neo4j']
+++

<p>
Last week I was helping someone load the data from a CSV file into Neo4j and we were having trouble filtering out rows which contained a null value in one of the columns.
</p>


<p>
This is what the data looked like:
</p>



~~~cypher

load csv with headers from "file:///foo.csv" as row
RETURN row
~~~


~~~text

╒══════════════════════════════════╕
│row                               │
╞══════════════════════════════════╡
│{key1: a,  key2: (null),  key3: c}│
├──────────────────────────────────┤
│{key1: d,  key2: e,  key3: f}     │
└──────────────────────────────────┘
~~~

<p>
We'd like to filter out any rows which have 'key2' as null, so let's tweak our query to do that:
</p>



~~~cypher

load csv with headers from "file:///foo.csv" as row
WITH row WHERE NOT row.key2 is null
RETURN row
~~~


~~~text

(no rows)
~~~

<p>Hmmm that's odd, it's got rid of both rows. We'd expect to see the 2nd row since that doesn't have a null value.</p>


<p>
At this point we might suspect that what we're seeing on the screen isn't actually what the data looks like. Let's write the following query to check our header values:
</p>



~~~cypher

load csv with headers from "file:///foo.csv" as row
WITH row LIMIT 1
UNWIND keys(row) AS key
RETURN key, SIZE(key)
~~~


~~~text

╒═════╤═════════╕
│key  │SIZE(key)│
╞═════╪═════════╡
│key1 │4        │
├─────┼─────────┤
│ key2│5        │
├─────┼─────────┤
│ key3│5        │
└─────┴─────────┘
~~~

<p>
The second column tells us that there are some extra characters in the columns for 'key2' and 'key3' or rather ' key2' and ' key3'. In this case they are spaces, but it could easily be another character:
</p>



~~~cypher

load csv with headers from "file:///foo.csv" as row
WITH row LIMIT 1
UNWIND keys(row) AS key
RETURN key, replace(key, " ", "_SPACE_") AS spaces
~~~


~~~text

╒═════╤═══════════╕
│key  │spaces     │
╞═════╪═══════════╡
│key1 │key1       │
├─────┼───────────┤
│ key2│_SPACE_key2│
├─────┼───────────┤
│ key3│_SPACE_key3│
└─────┴───────────┘
~~~

<p>
If we clean up our CSV file and try again everything works as expected:
</p>



~~~cypher

load csv with headers from "file:///foo.csv" as row
WITH row LIMIT 1
UNWIND keys(row) AS key
RETURN key, SIZE(key)
~~~


~~~text

╒════╤═════════╕
│key │SIZE(key)│
╞════╪═════════╡
│key1│4        │
├────┼─────────┤
│key2│4        │
├────┼─────────┤
│key3│4        │
└────┴─────────┘
~~~


~~~cypher

load csv with headers from "file:///foo.csv" as row
WITH row WHERE NOT row.key2 is null
RETURN row
~~~


~~~text

╒═══════════════════════════╕
│row                        │
╞═══════════════════════════╡
│{key1: d, key2: e, key3: f}│
└───────────────────────────┘
~~~
