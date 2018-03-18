+++
draft = false
date="2014-08-22 12:51:36"
title="Neo4j: LOAD CSV - Handling empty columns"
tag=['neo4j']
category=['neo4j']
+++

<p>A common problem that people encounter when trying to import CSV files into Neo4j using Cypher's <a href="http://docs.neo4j.org/chunked/stable/cypherdoc-importing-csv-files-with-cypher.html">LOAD CSV</a> command is how to handle empty or 'null' entries in said files.</p>


<p>For example let's try and import the following file which has 3 columns, 1 populated, 2 empty:</p>



~~~text

$ cat /tmp/foo.csv
a,b,c
mark,,
~~~


~~~cypher

load csv with headers from "file:/tmp/foo.csv" as row
MERGE (p:Person {a: row.a})
SET p.b = row.b, p.c = row.c
RETURN p
~~~

<P>When we execute that query we'll see that our Person node has properties 'b' and 'c' with no value:</p>



~~~cypher

==> +-----------------------------+
==> | p                           |
==> +-----------------------------+
==> | Node[5]{a:"mark",b:"",c:""} |
==> +-----------------------------+
==> 1 row
==> Nodes created: 1
==> Properties set: 3
==> Labels added: 1
==> 26 ms
~~~

<p>That isn't what we want - we don't want those properties to be set unless they have a value.</p>


<p>TO achieve this we need to introduce a conditional when setting the 'b' and 'c' properties. We'll assume that 'a' is always present as that's the key for our Person nodes.</p>


<p>The following query will do what we want:</p>



~~~cypher

load csv with headers from "file:/tmp/foo.csv" as row
MERGE (p:Person {a: row.a})
FOREACH(ignoreMe IN CASE WHEN trim(row.b) <> "" THEN [1] ELSE [] END | SET p.b = row.b)
FOREACH(ignoreMe IN CASE WHEN trim(row.c) <> "" THEN [1] ELSE [] END | SET p.c = row.c)
RETURN p
~~~

<p>Since there's no if or else statements in cypher we create our own conditional statement by using FOREACH. If there's a value in the CSV column then we'll loop once and set the property and if not we won't loop at all and therefore no property will be set.</p>



~~~cypher

==> +-------------------+
==> | p                 |
==> +-------------------+
==> | Node[4]{a:"mark"} |
==> +-------------------+
==> 1 row
==> Nodes created: 1
==> Properties set: 1
==> Labels added: 1
~~~
