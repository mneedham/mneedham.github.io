+++
draft = false
date="2014-05-31 12:44:10"
title="Neo4j: Cypher - Neo.ClientError.Statement.ParameterMissing and neo4j-shell"
tag=['neo4j']
category=['neo4j']
+++

<p>Every now and then I get sent Neo4j cypher queries to look at and more often than not they're <a href="http://docs.neo4j.org/chunked/stable/cypher-parameters.html">parameterised</a> which means you can't easily run them in the <a href="http://neo4j.com/blog/neo4j-2-0-0-m06-introducing-neo4js-browser/">Neo4j browser</a>.</p>


<p>For example let's say we have a database which has a user called 'Mark':</p>



~~~cypher

CREATE (u:User {name: "Mark"})
~~~

<p>Now we write a query to find 'Mark' with the name parameterised so we can easily search for a different user in future:</p>



~~~cypher

MATCH (u:User {name: {name}}) RETURN u
~~~

<p>If we run that query in the Neo4j browser we'll get this error:</p>



~~~bash

Expected a parameter named name
Neo.ClientError.Statement.ParameterMissing
~~~

<p>If we try that in neo4j-shell we'll get the same exception to start with:</p>



~~~cypher

$ MATCH (u:User {name: {name}}) RETURN u;
ParameterNotFoundException: Expected a parameter named name
~~~

<p>However, as <a href="https://twitter.com/mesirii">Michael</a> pointed out to me, the neat thing about neo4j-shell is that we can define parameters by using the <cite>export</cite> command:</p>



~~~cypher

$ export name="Mark"
$ MATCH (u:User {name: {name}}) RETURN u;
+-------------------------+
| u                       |
+-------------------------+
| Node[1923]{name:"Mark"} |
+-------------------------+
1 row
~~~

<p><cite>export</cite> is a bit sensitive to spaces so it's best to keep them to a minimum. e.g. the following tries to create the variable 'name ' which is invalid:</p>



~~~bash

$ export name = "Mark"
name  is no valid variable name. May only contain alphanumeric characters and underscores.
~~~

<p>The variables we create in the shell don't have to only be primitives. We can create maps too:</p>



~~~bash

$ export params={ name: "Mark" }
$ MATCH (u:User {name: {params}.name}) RETURN u;
+-------------------------+
| u                       |
+-------------------------+
| Node[1923]{name:"Mark"} |
+-------------------------+
1 row
~~~

<p>A simple tip but one that saves me from having to rewrite queries all the time!</p>

