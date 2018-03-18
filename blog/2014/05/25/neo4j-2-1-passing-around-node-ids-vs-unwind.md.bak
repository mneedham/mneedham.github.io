+++
draft = false
date="2014-05-25 10:48:39"
title="Neo4j 2.1:  Passing around node ids vs UNWIND"
tag=['neo4j', 'cypher']
category=['neo4j']
+++

<p>When Neo4j 2.1 is released we'll have the  <a href="http://docs.neo4j.org/chunked/milestone/query-unwind.html">UNWIND</a> clause which makes working with collections of things easier.</p>


<p>In my blog post about <a href="http://www.markhneedham.com/blog/2014/05/20/neo4j-2-0-creating-adjacency-matrices/">creating adjacency matrices</a> we wanted to show how many people were members of the first 5 meetup groups ordered alphabetically and then check how many were members of each of the other groups.</p>


<p>Without the UNWIND clause we'd have to do this:</p>



~~~cypher

MATCH (g:Group)
WITH g
ORDER BY g.name
LIMIT 5

WITH COLLECT(id(g)) AS groups

MATCH (g1) WHERE id(g1) IN groups
MATCH (g2) WHERE id(g2) IN groups

OPTIONAL MATCH path = (g1)<-[:MEMBER_OF]-()-[:MEMBER_OF]->(g2)
 
RETURN g1.name, g2.name, CASE WHEN path is null THEN 0 ELSE COUNT(path) END AS overlap
~~~

<p>Here we get the first 5 groups, put their IDs into a collection and then create a cartesian product of groups by doing back to back MATCH's with a node id lookup.</p>


<p>If instead of passing around node ids in 'groups' we pass around nodes and then used those in the MATCH step we'd end up doing a full node scan which becomes very slow as the store grows.</p>


<p>e.g. this version would be very slow</p>



~~~cypher

MATCH (g:Group)
WITH g
ORDER BY g.name
LIMIT 5

WITH COLLECT(g) AS groups

MATCH (g1) WHERE g1 IN groups
MATCH (g2) WHERE g2 IN groups

OPTIONAL MATCH path = (g1)<-[:MEMBER_OF]-()-[:MEMBER_OF]->(g2)
 
RETURN g1.name, g2.name, CASE WHEN path is null THEN 0 ELSE COUNT(path) END AS overlap
~~~

<p>This is the output from the original query:</p>



~~~bash

+-------------------------------------------------------------------------------------------------------------+
| g1.name                                         | g2.name                                         | overlap |
+-------------------------------------------------------------------------------------------------------------+
| "Big Data Developers in London"                 | "Big Data / Data Science / Data Analytics Jobs" | 17      |
| "Big Data Jobs in London"                       | "Big Data London"                               | 190     |
| "Big Data London"                               | "Big Data Developers in London"                 | 244     |
| "Cassandra London"                              | "Big Data / Data Science / Data Analytics Jobs" | 16      |
| "Big Data Jobs in London"                       | "Big Data Developers in London"                 | 52      |
| "Cassandra London"                              | "Cassandra London"                              | 0       |
| "Big Data London"                               | "Big Data / Data Science / Data Analytics Jobs" | 36      |
| "Big Data London"                               | "Cassandra London"                              | 422     |
| "Big Data Jobs in London"                       | "Big Data Jobs in London"                       | 0       |
| "Big Data / Data Science / Data Analytics Jobs" | "Big Data / Data Science / Data Analytics Jobs" | 0       |
| "Big Data Jobs in London"                       | "Cassandra London"                              | 74      |
| "Big Data Developers in London"                 | "Big Data London"                               | 244     |
| "Cassandra London"                              | "Big Data Jobs in London"                       | 74      |
| "Cassandra London"                              | "Big Data London"                               | 422     |
| "Big Data / Data Science / Data Analytics Jobs" | "Big Data London"                               | 36      |
| "Big Data Jobs in London"                       | "Big Data / Data Science / Data Analytics Jobs" | 20      |
| "Big Data Developers in London"                 | "Big Data Jobs in London"                       | 52      |
| "Cassandra London"                              | "Big Data Developers in London"                 | 69      |
| "Big Data / Data Science / Data Analytics Jobs" | "Big Data Jobs in London"                       | 20      |
| "Big Data Developers in London"                 | "Big Data Developers in London"                 | 0       |
| "Big Data Developers in London"                 | "Cassandra London"                              | 69      |
| "Big Data / Data Science / Data Analytics Jobs" | "Big Data Developers in London"                 | 17      |
| "Big Data London"                               | "Big Data Jobs in London"                       | 190     |
| "Big Data / Data Science / Data Analytics Jobs" | "Cassandra London"                              | 16      |
| "Big Data London"                               | "Big Data London"                               | 0       |
+-------------------------------------------------------------------------------------------------------------+
25 rows
~~~

<p>If we use UNWIND we don't need to pass around node ids anymore, instead we can collect up the nodes into a collection and then explode them out into a cartesian product:</p>



~~~cypher

MATCH (g:Group)
WITH g
ORDER BY g.name
LIMIT 5

WITH COLLECT(g) AS groups

UNWIND groups AS g1
UNWIND groups AS g2

OPTIONAL MATCH path = (g1)<-[:MEMBER_OF]-()-[:MEMBER_OF]->(g2)
 
RETURN g1.name, g2.name, CASE WHEN path is null THEN 0 ELSE COUNT(path) END AS overlap
~~~

<p>There's not significantly less code but I think the intent of the query is a bit clearer using UNWIND.</p>


<p>I'm looking forward to seeing the innovative uses of UNWIND people come up with once 2.1 is GA.
