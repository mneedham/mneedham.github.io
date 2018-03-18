+++
draft = false
date="2014-05-20 23:14:07"
title="Neo4j 2.1: Creating adjacency matrices"
tag=['neo4j', 'cypher']
category=['neo4j']
+++

<p>About 9 months ago I wrote a blog post showing how to <a href="http://www.markhneedham.com/blog/2013/08/11/neo4j-extracting-a-subgraph-as-an-adjacency-matrix-and-calculating-eigenvector-centrality-with-jblas/">export an adjacency matrix</a> from a Neo4j 1.9 database using the cypher query language and I thought it deserves an update to use 2.0 syntax.</p>


<p>I've been spending some of my free time working on <a href="https://github.com/mneedham/neo4j-meetup">an application that runs on top of meetup.com's API</a> and one of the queries I wanted to write was to find the common members between 2 meetup groups.</p>


<p>The first part of this query is a cartesian product of the groups we want to consider which will give us the combinations of pairs of groups:</p>



~~~cypher

MATCH (g1:Group), (g2:Group)
RETURN g1.name, g2.name
LIMIT 10
~~~


~~~bash

+-------------------------------------------------------------------------------------+
| g1.name                           | g2.name                                         |
+-------------------------------------------------------------------------------------+
| "London ElasticSearch User Group" | "London ElasticSearch User Group"               |
| "London ElasticSearch User Group" | "Big Data / Data Science / Data Analytics Jobs" |
| "London ElasticSearch User Group" | "eXist User Group London"                       |
| "London ElasticSearch User Group" | "Couchbase London"                              |
| "London ElasticSearch User Group" | "Big Data Developers in London"                 |
| "London ElasticSearch User Group" | "HBase London Meetup"                           |
| "London ElasticSearch User Group" | "Marklogic Financial Services Community"        |
| "London ElasticSearch User Group" | "GridGain London"                               |
| "London ElasticSearch User Group" | "MEAN Stack"                                    |
| "London ElasticSearch User Group" | "Hazelcast User Group London (HUGL)"            |
...
+-------------------------------------------------------------------------------------+
~~~

<p>Our next step is to write a pattern which checks for common members between each pair of groups. We end up with the following:</p>



~~~cypher

MATCH (g1:Group), (g2:Group)
OPTIONAL MATCH (g1)<-[:MEMBER_OF]-()-[:MEMBER_OF]->(g2)
RETURN g1.name, g2.name, COUNT(*) AS overlap
~~~


~~~bash

+----------------------------------------------------------------------------------------------+
| g1.name                     | g2.name                                              | overlap |
+----------------------------------------------------------------------------------------------+
| "eXist User Group London"   | "Women in Data"                                      | 1       |
| "Hive London"               | "Big Data Developers in London"                      | 47      |
| "Neo4j - London User Group" | "London ElasticSearch User Group"                    | 80      |
| "MEAN Stack"                | "The London Distributed Graph Database Meetup Group" | 1       |
| "HBase London Meetup"       | "Big Data London"                                    | 92      |
| "London MongoDB User Group" | "Big Data Developers in London"                      | 63      |
| "Big Data London"           | "Hive London"                                        | 195     |
| "HBase London Meetup"       | "Cassandra London"                                   | 58      |
| "Big Data London"           | "Neo4j - London User Group"                          | 330     |
| "Cassandra London"          | "Oracle Big Data 4 the Enterprise"                   | 50      |
...
+----------------------------------------------------------------------------------------------+
~~~

<p>The next step is to sort the rows so that we can create an array of values for each group in our next step. We therefore sort by group1 and then by group2:</p>



~~~cypher

MATCH (g1:Group), (g2:Group)
OPTIONAL MATCH (g1)<-[:MEMBER_OF]-()-[:MEMBER_OF]->(g2)
RETURN g1.name, g2.name, COUNT(*) AS overlap
ORDER BY g1.name, g2.name
~~~


~~~bash

+-------------------------------------------------------------------------------------------------------------+
| g1.name                                         | g2.name                                         | overlap |
+-------------------------------------------------------------------------------------------------------------+
| "Big Data / Data Science / Data Analytics Jobs" | "Big Data / Data Science / Data Analytics Jobs" | 1       |
| "Big Data / Data Science / Data Analytics Jobs" | "Big Data Developers in London"                 | 17      |
| "Big Data / Data Science / Data Analytics Jobs" | "Big Data Jobs in London"                       | 20      |
| "Big Data / Data Science / Data Analytics Jobs" | "Big Data London"                               | 37      |
| "Big Data / Data Science / Data Analytics Jobs" | "Cassandra London"                              | 16      |
| "Big Data / Data Science / Data Analytics Jobs" | "Couchbase London"                              | 3       |
| "Big Data / Data Science / Data Analytics Jobs" | "Data Science London"                           | 49      |
| "Big Data / Data Science / Data Analytics Jobs" | "DeNormalised London"                           | 3       |
| "Big Data / Data Science / Data Analytics Jobs" | "Enterprise Search London Meetup"               | 2       |
| "Big Data / Data Science / Data Analytics Jobs" | "GridGain London"                               | 1       |
...
+-------------------------------------------------------------------------------------------------------------+
~~~

<p>One strange thing we see here is that there is an overlap of 1 between 'Big Data / Data Science / Data Analytics Jobs' and itself which is 'wrong' as the query doesn't actually return any overlapping members. However, since we used 'OPTIONAL MATCH' we would still have got 1 row back for that pair of groups with a 'null' value. Let's fix that:</p>



~~~cypher

MATCH (g1:Group), (g2:Group)
OPTIONAL MATCH path = (g1)<-[:MEMBER_OF]-()-[:MEMBER_OF]->(g2)

WITH g1, g2, CASE WHEN path is null THEN 0 ELSE COUNT(path) END AS overlap
RETURN g1.name, g2.name, overlap
ORDER BY g1.name, g2.name
LIMIT 10
~~~


~~~bash

+-------------------------------------------------------------------------------------------------------------+
| g1.name                                         | g2.name                                         | overlap |
+-------------------------------------------------------------------------------------------------------------+
| "Big Data / Data Science / Data Analytics Jobs" | "Big Data / Data Science / Data Analytics Jobs" | 0       |
| "Big Data / Data Science / Data Analytics Jobs" | "Big Data Developers in London"                 | 17      |
| "Big Data / Data Science / Data Analytics Jobs" | "Big Data Jobs in London"                       | 20      |
| "Big Data / Data Science / Data Analytics Jobs" | "Big Data London"                               | 37      |
| "Big Data / Data Science / Data Analytics Jobs" | "Cassandra London"                              | 16      |
| "Big Data / Data Science / Data Analytics Jobs" | "Couchbase London"                              | 3       |
| "Big Data / Data Science / Data Analytics Jobs" | "Data Science London"                           | 49      |
| "Big Data / Data Science / Data Analytics Jobs" | "DeNormalised London"                           | 3       |
| "Big Data / Data Science / Data Analytics Jobs" | "Enterprise Search London Meetup"               | 2       |
| "Big Data / Data Science / Data Analytics Jobs" | "GridGain London"                               | 0       |
...
+-------------------------------------------------------------------------------------------------------------+
~~~

<p>We'll see that there is no overlap with 'GridGain London' either which we didn't know before. We've been able to do this by using <a href="http://docs.neo4j.org/chunked/milestone/syntax-simple-case.html">CASE</a> and checking whether or not the OPTIONAL MATCH came up with a path or not.</p>


<p>Our next step is to group the data returned so that we have one row for each meetup group which contains an array showing the overlap with all the other groups:</p>



~~~cypher

MATCH (g1:Group), (g2:Group)
OPTIONAL MATCH path = (g1)<-[:MEMBER_OF]-()-[:MEMBER_OF]->(g2)

WITH g1, g2, CASE WHEN path is null THEN 0 ELSE COUNT(path) END AS overlap
ORDER BY g1.name, g2.name
RETURN g1.name, COLLECT(overlap)
ORDER BY g1.name
~~~


~~~bash

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| g1.name                                                     | COLLECT(overlap)                                                                                                    |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| "Big Data / Data Science / Data Analytics Jobs"             | [0,17,20,37,16,3,49,3,2,0,6,4,28,2,11,0,3,4,5,13,4,1,4,0,2,0,20,1,5,5,0,5,4,4,1]                                    |
| "Big Data Developers in London"                             | [17,0,48,231,67,18,228,18,17,0,38,10,150,12,47,4,24,18,31,63,36,11,20,7,7,1,88,2,38,10,0,33,11,26,3]                |
| "Big Data Jobs in London"                                   | [20,48,0,189,70,16,168,19,7,0,21,10,128,9,51,4,24,14,23,69,13,5,20,5,7,2,69,1,34,12,0,10,10,19,4]                   |
| "Big Data London"                                           | [37,231,189,0,417,49,1128,94,89,0,92,31,738,39,195,20,116,93,124,328,98,44,81,20,36,10,330,2,122,79,2,74,45,107,11] |
| "Cassandra London"                                          | [16,67,70,417,0,36,276,63,40,1,58,13,292,34,104,9,72,55,71,195,58,23,64,9,10,2,174,4,50,65,2,21,23,19,4]            |
| "Couchbase London"                                          | [3,18,16,49,36,0,42,8,6,1,19,6,56,7,20,2,16,11,24,51,21,10,22,12,7,1,43,2,12,9,1,6,5,9,2]                           |
| "Data Science London"                                       | [49,228,168,1128,276,42,0,93,83,2,71,32,611,24,174,17,63,83,120,268,82,36,60,21,22,3,363,3,88,65,0,98,45,141,9]     |
| "DeNormalised London"                                       | [3,18,19,94,63,8,93,0,5,1,17,5,75,6,39,3,20,34,16,53,16,7,27,1,6,2,55,1,20,17,0,3,17,7,3]                           |
| "Enterprise Search London Meetup"                           | [2,17,7,89,40,6,83,5,0,0,9,0,64,4,22,2,6,8,75,44,12,5,11,3,17,2,48,0,9,19,0,7,9,6,0]                                |
| "GridGain London"                                           | [0,0,0,0,1,1,2,1,0,0,0,1,1,3,1,0,0,0,0,1,1,0,0,0,0,0,2,0,0,0,0,0,0,0,0]                                             |
| "HBase London Meetup"                                       | [6,38,21,92,58,19,71,17,9,0,0,3,94,15,37,3,17,9,30,38,22,6,12,5,5,1,51,2,24,9,0,9,10,4,4]                           |
| "HPC & GPU Supercomputing Group of London"                  | [4,10,10,31,13,6,32,5,0,1,3,0,25,4,6,1,6,4,4,8,2,1,4,0,0,0,16,0,3,4,0,2,3,1,1]                                      |
| "Hadoop Users Group UK"                                     | [28,150,128,738,292,56,611,75,64,1,94,25,0,29,214,9,81,67,113,272,75,28,72,13,28,4,259,3,101,60,4,38,39,48,11]      |
| "Hazelcast User Group London (HUGL)"                        | [2,12,9,39,34,7,24,6,4,3,15,4,29,0,6,1,6,5,5,20,14,2,10,2,1,1,27,0,3,2,1,5,2,0,1]                                   |
| "Hive London"                                               | [11,47,51,195,104,20,174,39,22,1,37,6,214,6,0,2,22,31,40,75,23,13,26,4,9,1,80,2,39,27,1,12,18,13,1]                 |
| "London Actionable Behavioral Analytics for Web and Mobile" | [0,4,4,20,9,2,17,3,2,0,3,1,9,1,2,0,1,0,2,8,4,1,1,1,0,1,7,0,2,0,0,8,1,2,1]                                           |
| "London Cloud Computing / NoSQL"                            | [3,24,24,116,72,16,63,20,6,0,17,6,81,6,22,1,0,11,15,52,21,7,27,3,7,1,39,0,15,21,4,2,2,9,5]                          |
| "London Data Bar"                                           | [4,18,14,93,55,11,83,34,8,0,9,4,67,5,31,0,11,0,13,58,12,4,22,3,1,0,44,4,19,7,0,5,8,8,0]                             |
| "London ElasticSearch User Group"                           | [5,31,23,124,71,24,120,16,75,0,30,4,113,5,40,2,15,13,0,80,22,9,32,9,6,0,80,1,20,33,1,6,9,11,2]                      |
| "London MongoDB User Group"                                 | [13,63,69,328,195,51,268,53,44,1,38,8,272,20,75,8,52,58,80,0,56,32,64,62,21,4,211,5,52,71,3,17,22,22,5]             |
| "London NoSQL"                                              | [4,36,13,98,58,21,82,16,12,1,22,2,75,14,23,4,21,12,22,56,0,16,24,20,8,2,69,1,12,13,0,18,8,6,3]                      |
| "London PostgreSQL Meetup Group"                            | [1,11,5,44,23,10,36,7,5,0,6,1,28,2,13,1,7,4,9,32,16,0,12,2,5,1,29,1,10,10,0,3,2,7,0]                                |
| "London Riak Meetup"                                        | [4,20,20,81,64,22,60,27,11,0,12,4,72,10,26,1,27,22,32,64,24,12,0,5,7,1,63,2,9,24,1,9,12,4,3]                        |
| "MEAN Stack"                                                | [0,7,5,20,9,12,21,1,3,0,5,0,13,2,4,1,3,3,9,62,20,2,5,0,1,0,27,1,1,4,1,6,1,3,1]                                      |
| "MarkLogic User Group London"                               | [2,7,7,36,10,7,22,6,17,0,5,0,28,1,9,0,7,1,6,21,8,5,7,1,0,16,22,1,8,6,0,0,5,5,13]                                    |
| "Marklogic Financial Services Community"                    | [0,1,2,10,2,1,3,2,2,0,1,0,4,1,1,1,1,0,0,4,2,1,1,0,16,0,6,0,1,1,0,1,1,1,4]                                           |
| "Neo4j - London User Group"                                 | [20,88,69,330,174,43,363,55,48,2,51,16,259,27,80,7,39,44,80,211,69,29,63,27,22,6,0,5,40,43,3,36,44,58,11]           |
| "OpenCredo Tech Workshops"                                  | [1,2,1,2,4,2,3,1,0,0,2,0,3,0,2,0,0,4,1,5,1,1,2,1,1,0,5,0,2,1,0,0,1,1,0]                                             |
| "Oracle Big Data 4 the Enterprise"                          | [5,38,34,122,50,12,88,20,9,0,24,3,101,3,39,2,15,19,20,52,12,10,9,1,8,1,40,2,0,10,0,2,7,9,4]                         |
| "Redis London"                                              | [5,10,12,79,65,9,65,17,19,0,9,4,60,2,27,0,21,7,33,71,13,10,24,4,6,1,43,1,10,0,0,2,7,2,1]                            |
| "The Apache Jmeter London Group"                            | [0,0,0,2,2,1,0,0,0,0,0,0,4,1,1,0,4,0,1,3,0,0,1,1,0,0,3,0,0,0,0,1,0,0,0]                                             |
| "The Data Scientist - UK"                                   | [5,33,10,74,21,6,98,3,7,0,9,2,38,5,12,8,2,5,6,17,18,3,9,6,0,1,36,0,2,2,1,0,2,12,1]                                  |
| "The London Distributed Graph Database Meetup Group"        | [4,11,10,45,23,5,45,17,9,0,10,3,39,2,18,1,2,8,9,22,8,2,12,1,5,1,44,1,7,7,0,2,0,9,1]                                 |
| "Women in Data"                                             | [4,26,19,107,19,9,141,7,6,0,4,1,48,0,13,2,9,8,11,22,6,7,4,3,5,1,58,1,9,2,0,12,9,0,1]                                |
| "eXist User Group London"                                   | [1,3,4,11,4,2,9,3,0,0,4,1,11,1,1,1,5,0,2,5,3,0,3,1,13,4,11,0,4,1,0,1,1,1,0]                                         |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
~~~

<p>This query is reasonably easy to follow and our next step would be to plug the output of this query into a visualisation tool of some sort.</p>


<p>Sometimes we can't create the cartesian product as easily as we were able to here - all we needed to do was call MATCH with the same label twice.</p>


<p>We can create cartesian products in other scenarios as well. For example let's say we only want to compare the first 5 meetup groups ordered by name.</p>


<p>First we'll get the top 5 groups:


~~~cypher

MATCH (g:Group)
RETURN g.name
ORDER BY g.name
LIMIT 5
~~~


~~~bash

+-------------------------------------------------+
| g.name                                          |
+-------------------------------------------------+
| "Big Data / Data Science / Data Analytics Jobs" |
| "Big Data Developers in London"                 |
| "Big Data Jobs in London"                       |
| "Big Data London"                               |
| "Cassandra London"                              |
+-------------------------------------------------+
~~~

<p>Now let's get all the pairs of those groups:</p>



~~~cypher

MATCH (g:Group)
WITH g
ORDER BY g.name
LIMIT 5

WITH COLLECT(g) AS groups
UNWIND groups AS g1
UNWIND groups AS g2
RETURN g1.name, g2.name
ORDER BY g1.name, g2.name
~~~


~~~bash

+---------------------------------------------------------------------------------------------------+
| g1.name                                         | g2.name                                         |
+---------------------------------------------------------------------------------------------------+
| "Big Data / Data Science / Data Analytics Jobs" | "Big Data / Data Science / Data Analytics Jobs" |
| "Big Data / Data Science / Data Analytics Jobs" | "Big Data Developers in London"                 |
| "Big Data / Data Science / Data Analytics Jobs" | "Big Data Jobs in London"                       |
| "Big Data / Data Science / Data Analytics Jobs" | "Big Data London"                               |
| "Big Data / Data Science / Data Analytics Jobs" | "Cassandra London"                              |
| "Big Data Developers in London"                 | "Big Data / Data Science / Data Analytics Jobs" |
| "Big Data Developers in London"                 | "Big Data Developers in London"                 |
| "Big Data Developers in London"                 | "Big Data Jobs in London"                       |
| "Big Data Developers in London"                 | "Big Data London"                               |
| "Big Data Developers in London"                 | "Cassandra London"                              |
| "Big Data Jobs in London"                       | "Big Data / Data Science / Data Analytics Jobs" |
| "Big Data Jobs in London"                       | "Big Data Developers in London"                 |
| "Big Data Jobs in London"                       | "Big Data Jobs in London"                       |
| "Big Data Jobs in London"                       | "Big Data London"                               |
| "Big Data Jobs in London"                       | "Cassandra London"                              |
| "Big Data London"                               | "Big Data / Data Science / Data Analytics Jobs" |
| "Big Data London"                               | "Big Data Developers in London"                 |
| "Big Data London"                               | "Big Data Jobs in London"                       |
| "Big Data London"                               | "Big Data London"                               |
| "Big Data London"                               | "Cassandra London"                              |
| "Cassandra London"                              | "Big Data / Data Science / Data Analytics Jobs" |
| "Cassandra London"                              | "Big Data Developers in London"                 |
| "Cassandra London"                              | "Big Data Jobs in London"                       |
| "Cassandra London"                              | "Big Data London"                               |
| "Cassandra London"                              | "Cassandra London"                              |
+---------------------------------------------------------------------------------------------------+
~~~

<p>Here we're making use of my current favourite function in cypher - <a href="http://docs.neo4j.org/chunked/milestone/query-unwind.html">UNWIND</a> - which allows you to take a collection of things and expand them out to have an individual row each.</p>


<p>It's currently only available in the latest RC of Neo4j 2.1 so we'll have to wait a little bit longer before using it in production!</p>


<p>We complete the query like so:</p>



~~~cypher

MATCH (g:Group)
WITH g
ORDER BY g.name
LIMIT 5

WITH COLLECT(g) AS groups
UNWIND groups AS g1
UNWIND groups AS g2
OPTIONAL MATCH path = (g1)<-[:MEMBER_OF]-()-[:MEMBER_OF]->(g2)

WITH g1, g2, CASE WHEN path is null THEN 0 ELSE COUNT(path) END AS overlap
ORDER BY g1.name, g2.name
RETURN g1.name, COLLECT(overlap)
ORDER BY g1.name
~~~


~~~bash

+----------------------------------------------------------------------+
| g1.name                                         | COLLECT(overlap)   |
+----------------------------------------------------------------------+
| "Big Data / Data Science / Data Analytics Jobs" | [0,17,20,37,16]    |
| "Big Data Developers in London"                 | [17,0,48,231,67]   |
| "Big Data Jobs in London"                       | [20,48,0,189,70]   |
| "Big Data London"                               | [37,231,189,0,417] |
| "Cassandra London"                              | [16,67,70,417,0]   |
+----------------------------------------------------------------------+
~~~

<p>And we're done!</p>

