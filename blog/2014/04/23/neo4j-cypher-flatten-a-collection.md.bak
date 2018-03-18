+++
draft = false
date="2014-04-23 22:02:19"
title="Neo4j: Cypher - Flatten a collection"
tag=['neo4j']
category=['neo4j']
+++

<p>Every now and then in Cypher land we'll end up with a collection of arrays, often created via the <a href="http://docs.neo4j.org/chunked/stable/query-aggregation.html#aggregation-collect">COLLECT</a> function, that we want to squash down into one array.</p>


<p>For example let's say we have the following array of arrays...</p>



~~~cypher

$ RETURN [[1,2,3], [4,5,6], [7,8,9]] AS result;
==> +---------------------------+
==> | result                    |
==> +---------------------------+
==> | [[1,2,3],[4,5,6],[7,8,9]] |
==> +---------------------------+
==> 1 row
~~~

<p>...and we want to return the array <cite>[1,2,3,4,5,6,7,8,9]</cite>. </p>


<p>Many programming languages have a 'flatten' function and although cypher doesn't we can make our own by using the <cite><a href="http://docs.neo4j.org/chunked/stable/query-functions-collection.html#functions-reduce">REDUCE</a></cite> function:</p>



~~~cypher

$ WITH  [[1,2,3], [4,5,6], [7,8,9]] AS result 
  RETURN REDUCE(output = [], r IN result | output + r) AS flat;
==> +---------------------+
==> | flat                |
==> +---------------------+
==> | [1,2,3,4,5,6,7,8,9] |
==> +---------------------+
==> 1 row
~~~

<p>Here we're passing the array 'output' over the collection and adding the individual arrays (<cite>[1,2,3]</cite>, <cite>[4,5,6]</cite> and <cite>[7,8,9]</cite>) to that array as we iterate over the collection.</p>


<p>If we're working with numbers in Neo4j 2.0.1 we'll get this type exception with this version of the code:</p>



~~~text

==> SyntaxException: Type mismatch: expected Any, Collection<Any> or Collection<Collection<Any>> but was Integer (line 1, column 148)
~~~

<p>We can easily work around that by coercing the type of 'output' like so:</p>



~~~cypher

WITH  [[1,2,3], [4,5,6], [7,8,9]] AS result 
RETURN REDUCE(output = range(0,-1), r IN result | output + r);
~~~

<p>Of course this is quite a simple example but we can handle more complicated scenarios as well by using nested calls to REDUCE. For example let's say we wanted to completely flatten this array:</p>



~~~cypher

$ RETURN [[1,2,3], [4], [5, [6, 7]], [8,9]] AS result;
==> +-------------------------------+
==> | result                        |
==> +-------------------------------+
==> | [[1,2,3],[4],[5,[6,7]],[8,9]] |
==> +-------------------------------+
==> 1 row
~~~

<p>We could write the following cypher code:</p>



~~~cypher

$ WITH  [[1,2,3], [4], [5, [6, 7]], [8,9]] AS result 
  RETURN REDUCE(output = [], r IN result | output + REDUCE(innerOutput = [], innerR in r | innerOutput + innerR)) AS flat;
==> +---------------------+
==> | flat                |
==> +---------------------+
==> | [1,2,3,4,5,6,7,8,9] |
==> +---------------------+
==> 1 row
~~~

<p>Here we have an outer REDUCE function which iterates over <cite>[1,2,3]</cite>, <cite>[4]</cite>, <cite>[5, [6,7]]</cite> and <cite>[8,9]</cite> and then an inner REDUCE function which iterates over those individual arrays.</p>


<p>If we had more nesting then we could just introduce another level of nesting!</p>

