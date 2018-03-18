+++
draft = false
date="2016-01-17 12:19:35"
title="Neo4j: Cypher - avoid duplicate calls to NOT patterns"
tag=['neo4j']
category=['neo4j']
+++

<p>
I've been reacquainting myself with the <a href="https://github.com/neo4j-meetups/modeling-worked-example">meetup.com dataset</a> ahead of <a href="http://www.meetup.com/graphdb-london/">Wednesday's meetup in London</a> and wanted to write a collaborative filtering type query to work out which groups people in my groups were in.
</p>


<p>This started simple enough:</p>



~~~cypher

MATCH (member:Member {name: "Mark Needham"})-[:MEMBER_OF]->(group:Group)<-[:MEMBER_OF]-(other:Member)-[:MEMBER_OF]->(otherGroup:Group)
RETURN otherGroup, COUNT(*) AS commonMembers
ORDER BY commonMembers DESC
LIMIT 5
~~~

<p>And doesn't take too long to run:</p>



~~~text

Cypher version: CYPHER 2.3, planner: COST. 1084378 total db hits in 1103 ms.
~~~

<p>However, it was showing up several groups that I'm already a member of so I added in a "WHERE NOT" clause to sort that out:</p>



~~~cypher

MATCH (member:Member {name: "Mark Needham"})-[:MEMBER_OF]->(group:Group)<-[:MEMBER_OF]-(other:Member)-[:MEMBER_OF]->(otherGroup:Group)
WHERE NOT (member)-[:MEMBER_OF]->(otherGroup)
RETURN otherGroup, COUNT(*) AS commonMembers
ORDER BY commonMembers DESC
LIMIT 5
~~~

<p>Unfortunately when I ran this the amount of db hits increased by 14x and it now took 3x as long to run:</p>



~~~text

Cypher version: CYPHER 2.3, planner: COST. 14061442 total db hits in 3364 ms.
~~~

<P>
The problem is that we're making lots of duplicate calls to <cite>NOT (member)-[:MEMBER_OF]->(otherGroup)</cite> because each group shows up lots of times.</p>
 

<p>This is the 'reduce cardinality of work in progress' tip from <a href="http://neo4j.com/blog/neo4j-2-2-query-tuning/">Michael Hunger's blog post</a>:
</p>


<blockquote>
Bonus Query Tuning Tip: Reduce Cardinality of Work in Progress

When following longer paths, you’ll encounter duplicates. If you’re not interested in <strong>all the possible paths</strong> – but just distinct information from stages of the path – make sure that you eagerly eliminate duplicates, so that later matches don’t have to be executed many multiple times.
</blockquote>

<p>
We can reduce the WIP in our query by doing the counting of common members first and then filtering out the groups we're already a member of:</p>



~~~cypher

MATCH (member:Member {name: "Mark Needham"})-[:MEMBER_OF]->(group:Group)<-[:MEMBER_OF]-(other:Member)-[:MEMBER_OF]->(otherGroup:Group)
WITH otherGroup, member, COUNT(*) AS commonMembers
WHERE NOT (member)-[:MEMBER_OF]->(otherGroup)
RETURN otherGroup, commonMembers
ORDER BY commonMembers DESC
LIMIT 5
~~~

<p>This gets us back down to something closer to the running time/db hits of our initial query:</p>



~~~text

Cypher version: CYPHER 2.3, planner: COST. 1097114 total db hits in 1004 ms.
~~~
