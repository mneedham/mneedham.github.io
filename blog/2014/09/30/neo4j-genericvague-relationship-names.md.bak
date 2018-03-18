+++
draft = false
date="2014-09-30 16:47:29"
title="Neo4j: Generic/Vague relationship names"
tag=['neo4j']
category=['neo4j']
+++

<p>An approach to modelling that I often see while working with Neo4j users is creating very generic relationships (e.g. HAS, CONTAINS, IS) and filtering on a relationship property or on a property/label at the end node.</p>


<p>Intuitively this doesn't seem to make best use of the graph model as it means that you have to evaluate many relationships and nodes that you're not interested in.

<p>However, I've never actually tested the performance differences between the approaches so I thought I'd try it out.</p>


<p>I created 4 different databases which had one node with 60,000 outgoing relationships - 10,000 which we wanted to retrieve and 50,000 that were irrelevant.</p>


<p>I modelled the 'relationship' in 4 different ways...</p>


<ul>
	<li>Using a specific relationship type<br />
        (node)-[:HAS_ADDRESS]->(address)</li>
	<li>Using a generic relationship type and then filtering by end node label<br />(node)-[:HAS]->(address:Address)</li>
	<li>Using a generic relationship type and then filtering by relationship property<br />(node)-[:HAS {type: "address"}]->(address)</li>
	<li>Using a generic relationship type and then filtering by end node property<br />(node)-[:HAS]->(address {type: "address"})</li>
</ul>

<p>...and then measured how long it took to retrieve the 'has address' relationships.</p>


<p>The <a href="https://gist.github.com/mneedham/a35f146dbe09266d574d">code is on github</a> if you want to take a look.</p>


<p>Although it's obviously not as precise as a <a href="http://openjdk.java.net/projects/code-tools/jmh/">JMH</a> micro benchmark I think it's good enough to get a feel for the difference between the approaches.</p>


<p>I ran a query against each database 100 times and then took the 50th, 75th and 99th percentiles (times are in ms):</p>



~~~text

Using a generic relationship type and then filtering by end node label
50%ile: 6.0    75%ile: 6.0    99%ile: 402.60999999999825

Using a generic relationship type and then filtering by relationship property
50%ile: 21.0   75%ile: 22.0   99%ile: 504.85999999999785

Using a generic relationship type and then filtering by end node label
50%ile: 4.0    75%ile: 4.0    99%ile: 145.65999999999931

Using a specific relationship type
50%ile: 0.0    75%ile: 1.0    99%ile: 25.749999999999872
~~~

<p>We can drill further into why there's a difference in the times for each of the approaches by profiling the equivalent cypher query. We'll start with the one which uses a specific relationship name</p>


<cite>Using a specific relationship type</cite>

~~~cypher

neo4j-sh (?)$ profile match (n) where id(n) = 0 match (n)-[:HAS_ADDRESS]->() return count(n);
+----------+
| count(n) |
+----------+
| 10000    |
+----------+
1 row

ColumnFilter
  |
  +EagerAggregation
    |
    +SimplePatternMatcher
      |
      +NodeByIdOrEmpty

+----------------------+-------+--------+-----------------------------+-----------------------+
|             Operator |  Rows | DbHits |                 Identifiers |                 Other |
+----------------------+-------+--------+-----------------------------+-----------------------+
|         ColumnFilter |     1 |      0 |                             | keep columns count(n) |
|     EagerAggregation |     1 |      0 |                             |                       |
| SimplePatternMatcher | 10000 |  10000 | n,   UNNAMED53,   UNNAMED35 |                       |
|      NodeByIdOrEmpty |     1 |      1 |                        n, n |          {  AUTOINT0} |
+----------------------+-------+--------+-----------------------------+-----------------------+

Total database accesses: 10001
~~~

<p>Here we can see that there were 10,002 database accesses in order to get a count of our 10,000 HAS_ADDRESS relationships. We get a database access each time we load a node, relationship or property.</p>


<p>By contrast the other approaches have to load in a lot more data only to then filter it out:</p>


<cite>Using a generic relationship type and then filtering by end node label</cite>

~~~cypher

neo4j-sh (?)$ profile match (n) where id(n) = 0 match (n)-[:HAS]->(:Address) return count(n);
+----------+
| count(n) |
+----------+
| 10000    |
+----------+
1 row

ColumnFilter
  |
  +EagerAggregation
    |
    +Filter
      |
      +SimplePatternMatcher
        |
        +NodeByIdOrEmpty

+----------------------+-------+--------+-----------------------------+----------------------------------+
|             Operator |  Rows | DbHits |                 Identifiers |                            Other |
+----------------------+-------+--------+-----------------------------+----------------------------------+
|         ColumnFilter |     1 |      0 |                             |            keep columns count(n) |
|     EagerAggregation |     1 |      0 |                             |                                  |
|               Filter | 10000 |  10000 |                             | hasLabel(  UNNAMED45:Address(0)) |
| SimplePatternMatcher | 10000 |  60000 | n,   UNNAMED45,   UNNAMED35 |                                  |
|      NodeByIdOrEmpty |     1 |      1 |                        n, n |                     {  AUTOINT0} |
+----------------------+-------+--------+-----------------------------+----------------------------------+

Total database accesses: 70001
~~~

<cite>Using a generic relationship type and then filtering by relationship property</cite>

~~~cypher

neo4j-sh (?)$ profile match (n) where id(n) = 0 match (n)-[:HAS {type: "address"}]->() return count(n);
+----------+
| count(n) |
+----------+
| 10000    |
+----------+
1 row

ColumnFilter
  |
  +EagerAggregation
    |
    +Filter
      |
      +SimplePatternMatcher
        |
        +NodeByIdOrEmpty

+----------------------+-------+--------+-----------------------------+--------------------------------------------------+
|             Operator |  Rows | DbHits |                 Identifiers |                                            Other |
+----------------------+-------+--------+-----------------------------+--------------------------------------------------+
|         ColumnFilter |     1 |      0 |                             |                            keep columns count(n) |
|     EagerAggregation |     1 |      0 |                             |                                                  |
|               Filter | 10000 |  20000 |                             | Property(  UNNAMED35,type(0)) == {  AUTOSTRING1} |
| SimplePatternMatcher | 10000 | 120000 | n,   UNNAMED63,   UNNAMED35 |                                                  |
|      NodeByIdOrEmpty |     1 |      1 |                        n, n |                                     {  AUTOINT0} |
+----------------------+-------+--------+-----------------------------+--------------------------------------------------+

Total database accesses: 140001
~~~

<cite>Using a generic relationship type and then filtering by end node property</cite>

~~~cypher

neo4j-sh (?)$ profile match (n) where id(n) = 0 match (n)-[:HAS]->({type: "address"}) return count(n);
+----------+
| count(n) |
+----------+
| 10000    |
+----------+
1 row

ColumnFilter
  |
  +EagerAggregation
    |
    +Filter
      |
      +SimplePatternMatcher
        |
        +NodeByIdOrEmpty

+----------------------+-------+--------+-----------------------------+--------------------------------------------------+
|             Operator |  Rows | DbHits |                 Identifiers |                                            Other |
+----------------------+-------+--------+-----------------------------+--------------------------------------------------+
|         ColumnFilter |     1 |      0 |                             |                            keep columns count(n) |
|     EagerAggregation |     1 |      0 |                             |                                                  |
|               Filter | 10000 |  20000 |                             | Property(  UNNAMED45,type(0)) == {  AUTOSTRING1} |
| SimplePatternMatcher | 10000 | 120000 | n,   UNNAMED45,   UNNAMED35 |                                                  |
|      NodeByIdOrEmpty |     1 |      1 |                        n, n |                                     {  AUTOINT0} |
+----------------------+-------+--------+-----------------------------+--------------------------------------------------+

Total database accesses: 140001
~~~

<p>So in summary...specific relationships #ftw!</p>

