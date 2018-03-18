+++
draft = false
date="2014-06-28 11:12:30"
title="Neo4j: Cypher - Finding movies by decade"
tag=['neo4j']
category=['neo4j']
+++

<p>I was recently asked how to find the <strong>number of movies produced per decade</strong> in the movie data set that comes with the Neo4j browser and can be imported with the following command:</p>



~~~bash

:play movies
~~~

<p>We want to get one row per decade and have a count alongside so the easiest way is to start with one decade and build from there.</p>



~~~cypher

MATCH (movie:Movie)
WHERE movie.released >= 1990 and movie.released <= 1999
RETURN 1990 + "-" + 1999 as years, count(movie) AS movies
ORDER BY years
~~~

<p>Note that we're doing a label scan of all nodes of type <cite>Movie</cite> as there are no indexes for range queries. In this case it's fine as we have few movies but If we had 100s of thousands of movies then we'd want to optimise the WHERE clause to make use of an <a href="http://docs.neo4j.org/chunked/stable/query-where.html#query-where-patterns">IN</a> which would then use any indexes.</p>


<p>If we run the query we get the following result:</p>



~~~bash

==> +----------------------+
==> | years       | movies |
==> +----------------------+
==> | "1990-1999" | 21     |
==> +----------------------+
==> 1 row
~~~

<p>Let's pull out the start and end years so they're explicitly named:</p>



~~~cypher

WITH 1990 AS startDecade, 1999 AS endDecade
MATCH (movie:Movie)
WHERE movie.released >= startDecade and movie.released <= endDecade
RETURN startDecade + "-" + endDecade as years, count(movie)
ORDER BY years
~~~

<p>Now we need to create a collection of start and end years so we can return more than one. We can use the <a href="http://docs.neo4j.org/chunked/stable/query-unwind.html">UNWIND</a> function to take a collection of decades and run them through the rest of the query:</p>



~~~cypher

UNWIND [{start: 1970, end: 1979}, {start: 1980, end: 1989}, {start: 1980, end: 1989}, {start: 1990, end: 1999}, {start: 2000, end: 2009}, {start: 2010, end: 2019}] AS row
WITH row.start AS startDecade, row.end AS endDecade
MATCH (movie:Movie)
WHERE movie.released >= startDecade and movie.released <= endDecade
RETURN startDecade + "-" + endDecade as years, count(movie)
ORDER BY years
~~~


~~~bash

==> +----------------------------+
==> | years       | count(movie) |
==> +----------------------------+
==> | "1970-1979" | 2            |
==> | "1980-1989" | 2            |
==> | "1990-1999" | 21           |
==> | "2000-2009" | 13           |
==> | "2010-2019" | 1            |
==> +----------------------------+
==> 5 rows
~~~

<p><a href="https://twitter.com/apcj">Alistair</a> pointed out that we can simplify this even further by using the <a href="http://docs.neo4j.org/chunked/stable/syntax-collections.html#_collections_in_general">RANGE</a> function:</p>



~~~cypher

UNWIND range(1970,2010,10) as startDecade
WITH startDecade, startDecade + 9 as endDecade
MATCH (movie:Movie)
WHERE movie.released >= startDecade and movie.released <= endDecade
RETURN startDecade + "-" + endDecade as years, count(movie)
ORDER BY years
~~~

<p>And here's a <a href="http://gist.neo4j.org/?84dd2c6729b08f674b3b">graph gist</a> for you to play with.</p>

