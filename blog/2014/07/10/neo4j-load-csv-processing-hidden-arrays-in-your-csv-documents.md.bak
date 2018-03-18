+++
draft = false
date="2014-07-10 14:54:25"
title="Neo4j: LOAD CSV - Processing hidden arrays in your CSV documents"
tag=['neo4j']
category=['neo4j']
+++

<p>I was recently asked how to process an 'array' of values inside a column in a CSV file using <a href="http://docs.neo4j.org/chunked/stable/query-load-csv.html">Neo4j's LOAD CSV</a> tool and although I initially thought this wouldn't be possible as every cell is treated as a String, <a href="https://twitter.com/mesirii">Michael</a> showed me a way of working around this which I thought was pretty neat.</p>


<p>
Let's say we have a CSV file representing people and their friends. It might look like this:
</p>



~~~bash

name,friends
"Mark","Michael,Peter"
"Michael","Peter,Kenny"
"Kenny","Anders,Michael"
~~~

<p>And what we want is to have the following nodes:</p>


<ul>
<li>Mark</li>
<li>Michael</li>
<li>Peter</li>
<li>Kenny</li>
<li>Anders</li>
</ul>

<p>And the following friends relationships:</p>


<ul>
<li>Mark -> Michael</li>
<li>Mark -> Peter</li>
<li>Michael -> Peter</li>
<li>Michael -> Kenny</li>
<li>Kenny -> Anders</li>
<li>Kenny -> Michael</li>
</ul>

<p>We'll start by loading the CSV file and returning each row:</p>



~~~cypher

$ load csv with headers from "file:/Users/markneedham/Desktop/friends.csv" AS row RETURN row;
+------------------------------------------------+
| row                                            |
+------------------------------------------------+
| {name -> "Mark", friends -> "Michael,Peter"}   |
| {name -> "Michael", friends -> "Peter,Kenny"}  |
| {name -> "Kenny", friends -> "Anders,Michael"} |
+------------------------------------------------+
3 rows
~~~

<p>As expected the 'friends' column is being treated as a String which means we can use the <a href="http://docs.neo4j.org/chunked/stable/query-functions-string.html#functions-split">split</a> function to get an array of people that we want to be friends with:</p>



~~~cypher

$ load csv with headers from "file:/Users/markneedham/Desktop/friends.csv" AS row RETURN row, split(row.friends, ",") AS friends;
+-----------------------------------------------------------------------+
| row                                            | friends              |
+-----------------------------------------------------------------------+
| {name -> "Mark", friends -> "Michael,Peter"}   | ["Michael","Peter"]  |
| {name -> "Michael", friends -> "Peter,Kenny"}  | ["Peter","Kenny"]    |
| {name -> "Kenny", friends -> "Anders,Michael"} | ["Anders","Michael"] |
+-----------------------------------------------------------------------+
3 rows
~~~

<p>Now that we've got them as an array we can use <a href="http://docs.neo4j.org/chunked/stable/query-unwind.html">UNWIND</a> to get pairs of friends that we want to create:</p>



~~~cypher

$ load csv with headers from "file:/Users/markneedham/Desktop/friends.csv" AS row 
  WITH row, split(row.friends, ",") AS friends 
  UNWIND friends AS friend 
  RETURN row.name, friend;
+-----------------------+
| row.name  | friend    |
+-----------------------+
| "Mark"    | "Michael" |
| "Mark"    | "Peter"   |
| "Michael" | "Peter"   |
| "Michael" | "Kenny"   |
| "Kenny"   | "Anders"  |
| "Kenny"   | "Michael" |
+-----------------------+
6 rows
~~~

<p>And now we'll introduce some <a href="http://docs.neo4j.org/chunked/stable/query-merge.html">MERGE</a> statements to create the appropriate nodes and relationships:</p>



~~~cypher

$ load csv with headers from "file:/Users/markneedham/Desktop/friends.csv" AS row 
  WITH row, split(row.friends, ",") AS friends 
  UNWIND friends AS friend  
  MERGE (p1:Person {name: row.name}) 
  MERGE (p2:Person {name: friend}) 
  MERGE (p1)-[:FRIENDS_WITH]->(p2);
+-------------------+
| No data returned. |
+-------------------+
Nodes created: 5
Relationships created: 6
Properties set: 5
Labels added: 5
373 ms
~~~

<p>And now if we query the database to get back all the nodes + relationships...</p>



~~~cypher

$ match (p1:Person)-[r]->(p2) RETURN p1,r, p2;
+------------------------------------------------------------------------+
| p1                      | r                  | p2                      |
+------------------------------------------------------------------------+
| Node[0]{name:"Mark"}    | :FRIENDS_WITH[0]{} | Node[1]{name:"Michael"} |
| Node[0]{name:"Mark"}    | :FRIENDS_WITH[1]{} | Node[2]{name:"Peter"}   |
| Node[1]{name:"Michael"} | :FRIENDS_WITH[2]{} | Node[2]{name:"Peter"}   |
| Node[1]{name:"Michael"} | :FRIENDS_WITH[3]{} | Node[3]{name:"Kenny"}   |
| Node[3]{name:"Kenny"}   | :FRIENDS_WITH[4]{} | Node[4]{name:"Anders"}  |
| Node[3]{name:"Kenny"}   | :FRIENDS_WITH[5]{} | Node[1]{name:"Michael"} |
+------------------------------------------------------------------------+
6 rows
~~~

<p>...you'll see that we have everything.</p>


<p>If instead of a comma separated list of people we have a literal array in the cell...</p>



~~~text

name,friends
"Mark", "[Michael,Peter]"
"Michael", "[Peter,Kenny]"
"Kenny", "[Anders,Michael]"
~~~

<p>...we'd need to tweak the part of the query which extracts our friends to strip off the first and last characters:</p>



~~~cypher

$ load csv with headers from "file:/Users/markneedham/Desktop/friendsa.csv" AS row 
  RETURN row, split(substring(row.friends, 1, length(row.friends) -2), ",") AS friends;
+-------------------------------------------------------------------------+
| row                                              | friends              |
+-------------------------------------------------------------------------+
| {name -> "Mark", friends -> "[Michael,Peter]"}   | ["Michael","Peter"]  |
| {name -> "Michael", friends -> "[Peter,Kenny]"}  | ["Peter","Kenny"]    |
| {name -> "Kenny", friends -> "[Anders,Michael]"} | ["Anders","Michael"] |
+-------------------------------------------------------------------------+
3 rows
~~~

<p>And then if we put the whole query together we end up with this:</p>



~~~cypher

$ load csv with headers from "file:/Users/markneedham/Desktop/friendsa.csv" AS row 
  WITH row, split(substring(row.friends, 1, length(row.friends) -2), ",") AS friends 
  UNWIND friends AS friend  
  MERGE (p1:Person {name: row.name}) 
  MERGE (p2:Person {name: friend}) 
  MERGE (p1)-[:FRIENDS_WITH]->(p2);;
+-------------------+
| No data returned. |
+-------------------+
Nodes created: 5
Relationships created: 6
Properties set: 5
Labels added: 5
~~~
