+++
draft = false
date="2014-04-19 19:51:58"
title="Neo4j 2.0.1: Cypher - Concatenating an empty collection / Type mismatch: expected Integer, Collection&lt;Integer&gt; or Collection&lt;Collection&lt;Integer&gt;&gt; but was Collection&lt;Any&gt;"
tag=['neo4j']
category=['neo4j']
+++

<p>Last weekend I was playing around with some collections using Neo4j's Cypher query language and I wanted to concatenate two collections.</p>


<p>This was easy enough when both collections contained values...</p>



~~~cypher

$ RETURN [1,2,3,4] + [5,6,7];
==> +---------------------+
==> | [1,2,3,4] + [5,6,7] |
==> +---------------------+
==> | [1,2,3,4,5,6,7]     |
==> +---------------------+
==> 1 row
~~~

<p>...but I ended up with the following exception when I tried to concatenate with an empty collection:</p>



~~~cypher

$ RETURN [1,2,3,4] + [];
==> SyntaxException: Type mismatch: expected Integer, Collection<Integer> or Collection<Collection<Integer>> but was Collection<Any> (line 1, column 20)
==> "RETURN [1,2,3,4] + []"
==>                     ^
~~~

<p>I figured there was probably some strange type coercion going on for the empty collection and came up with the following work around using the <cite><a href="http://docs.neo4j.org/chunked/stable/query-functions-collection.html#functions-range">RANGE</a></cite> function:</p>



~~~cypher

$ RETURN [1,2,3,4] + RANGE(0,-1);
==> +-------------------------+
==> | [1,2,3,4] + RANGE(0,-1) |
==> +-------------------------+
==> | [1,2,3,4]               |
==> +-------------------------+
==> 1 row
~~~

<p>While writing this up I decided to check if it behaved the same way in the <a href="http://blog.neo4j.org/2014/04/neo4j-202-maintenance-release.html">recently released 2.0.2</a> and was pleasantly surprised to see that the work around is no longer necessary:</p>



~~~cypher

$ RETURN [1,2,3,4] + [];
==> +----------------+
==> | [1,2,3,4] + [] |
==> +----------------+
==> | [1,2,3,4]      |
==> +----------------+
==> 1 row
~~~

<p>So if you're seeing the same issue get yourself upgraded!</p>

