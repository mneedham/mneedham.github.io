+++
draft = false
date="2014-12-28 04:28:25"
title="Neo4j 2.1.6 - Cypher: FOREACH slowness"
tag=['neo4j', 'cypher']
category=['neo4j']
+++

<p>
A common problem that people have when using Neo4j for social network applications is updating a person with their newly imported friends.
</p>


<p>
We'll have an array of friends that we want to connect to a single Person node. Assuming the following schema...</p>
 


~~~cypher

$ schema
Indexes
  ON :Person(id) ONLINE

No constraints
~~~

<p>...a simplified version would look like this:
</p>



~~~cypher

WITH range (2,1002) AS friends
MERGE (p:Person {id: 1})

FOREACH(f IN friends |
  MERGE (friend:Person {id: f})
  MERGE (friend)-[:FRIENDS]->p);
~~~

<p>
If we execute that on an empty database we'll see something like this:
</p>



~~~text

+-------------------+
| No data returned. |
+-------------------+
Nodes created: 1002
Relationships created: 1001
Properties set: 1002
Labels added: 1002
19173 ms
~~~

<p>
This took much longer than we'd expect so let's have a look at the PROFILE output:
</p>



~~~text

EmptyResult
  |
  +UpdateGraph(0)
    |
    +Eager
      |
      +UpdateGraph(1)
        |
        +Extract
          |
          +Null

+----------------+------+---------+-------------+--------------------------------------+
|       Operator | Rows |  DbHits | Identifiers |                                Other |
+----------------+------+---------+-------------+--------------------------------------+
|    EmptyResult |    0 |       0 |             |                                      |
| UpdateGraph(0) |    1 | 3015012 |             |                              Foreach |
|          Eager |    1 |       0 |             |                                      |
| UpdateGraph(1) |    1 |       5 |        p, p | MergeNode; {  AUTOINT2}; :Person(id) |
|        Extract |    1 |       0 |             |                              friends |
|           Null |    ? |       ? |             |                                      |
+----------------+------+---------+-------------+--------------------------------------+
~~~

<p>
The <cite>DbHits</cite> value on the 2nd row seems suspiciously high suggesting that FOREACH might not be making use of the <cite>Person#id</cite> index and is instead scanning all <cite>Person</cite> nodes each time.
</p>


<p>
I'm not sure how to drill into that further but an alternative approach is to try out the same query but using UNWIND instead and checking the profile output of that:
</p>



~~~cypher

WITH range (2,1002) AS friends
MERGE (p:Person {id: 1})
WITH p, friends
UNWIND friends AS f
MERGE (friend:Person {id: f})
MERGE (friend)-[:FRIENDS]->p;
~~~


~~~text

+-------------------+
| No data returned. |
+-------------------+
Nodes created: 1002
Relationships created: 1001
Properties set: 1002
Labels added: 1002
343 ms
~~~


~~~text

EmptyResult
  |
  +UpdateGraph(0)
    |
    +Eager(0)
      |
      +UpdateGraph(1)
        |
        +UNWIND
          |
          +Eager(1)
            |
            +UpdateGraph(2)
              |
              +Extract
                |
                +Null

+----------------+------+--------+-------------------------+--------------------------------------+
|       Operator | Rows | DbHits |             Identifiers |                                Other |
+----------------+------+--------+-------------------------+--------------------------------------+
|    EmptyResult |    0 |      0 |                         |                                      |
| UpdateGraph(0) | 1001 |      0 | friend, p,   UNNAMED136 |                         MergePattern |
|       Eager(0) | 1001 |      0 |                         |                                      |
| UpdateGraph(1) | 1001 |   5005 |          friend, friend |            MergeNode; f; :Person(id) |
|         UNWIND | 1001 |      0 |                         |                                      |
|       Eager(1) |    1 |      0 |                         |                                      |
| UpdateGraph(2) |    1 |      5 |                    p, p | MergeNode; {  AUTOINT2}; :Person(id) |
|        Extract |    1 |      0 |                         |                              friends |
|           Null |    ? |      ? |                         |                                      |
+----------------+------+--------+-------------------------+--------------------------------------+
~~~

<p>
That's much quicker and doesn't touch as many nodes as FOREACH was. I expect the index issue will be sorted out in future but until then UNWIND is our friend.
</p>

