+++
draft = false
date="2015-07-30 06:23:03"
title="Neo4j: Cypher - Removing consecutive duplicates"
tag=['neo4j', 'cypher']
category=['neo4j']
+++

<p>
When writing Cypher queries I sometimes find myself wanting to remove consecutive duplicates in collections that I've joined together.
</p>


<p>e.g we might start with the following query where 1 and 7 appear consecutively:</p>



~~~cypher

RETURN [1,1,2,3,4,5,6,7,7,8] AS values

==> +-----------------------+
==> | values                |
==> +-----------------------+
==> | [1,1,2,3,4,5,6,7,7,8] |
==> +-----------------------+
==> 1 row
~~~

<p>
We want to end up with [1,2,3,4,5,6,7,8]. We can start by exploding our array and putting consecutive elements next to each other:
</p>



~~~cypher

WITH [1,1,2,3,4,5,6,7,7,8] AS values
UNWIND RANGE(0, LENGTH(values) - 2) AS idx
RETURN idx, idx+1, values[idx], values[idx+1]

==> +-------------------------------------------+
==> | idx | idx+1 | values[idx] | values[idx+1] |
==> +-------------------------------------------+
==> | 0   | 1     | 1           | 1             |
==> | 1   | 2     | 1           | 2             |
==> | 2   | 3     | 2           | 3             |
==> | 3   | 4     | 3           | 4             |
==> | 4   | 5     | 4           | 5             |
==> | 5   | 6     | 5           | 6             |
==> | 6   | 7     | 6           | 7             |
==> | 7   | 8     | 7           | 7             |
==> | 8   | 9     | 7           | 8             |
==> +-------------------------------------------+
==> 9 rows
~~~

<p>Next we can filter out rows which have the same values since that means they have consecutive duplicates:</p>



~~~cypher

WITH [1,1,2,3,4,5,6,7,7,8] AS values
UNWIND RANGE(0, LENGTH(values) - 2) AS idx
WITH values[idx] AS a, values[idx+1] AS b
WHERE a <> b
RETURN a,b

==> +-------+
==> | a | b |
==> +-------+
==> | 1 | 2 |
==> | 2 | 3 |
==> | 3 | 4 |
==> | 4 | 5 |
==> | 5 | 6 |
==> | 6 | 7 |
==> | 7 | 8 |
==> +-------+
==> 7 rows
~~~

<p>Now we need to join the collection back together again. Most of the values we want are in field 'b' but we also need to grab the first value from field 'a':</p>



~~~cypher

WITH [1,1,2,3,4,5,6,7,7,8] AS values
UNWIND RANGE(0, LENGTH(values) - 2) AS idx
WITH values[idx] AS a, values[idx+1] AS b
WHERE a <> b
RETURN COLLECT(a)[0] + COLLECT(b) AS noDuplicates

==> +-------------------+
==> | noDuplicates      |
==> +-------------------+
==> | [1,2,3,4,5,6,7,8] |
==> +-------------------+
==> 1 row
~~~

<p>What about if we have more than 2 duplicates in a row?</p>



~~~cypher

WITH [1,1,1,2,3,4,5,5,6,7,7,8] AS values
UNWIND RANGE(0, LENGTH(values) - 2) AS idx
WITH values[idx] AS a, values[idx+1] AS b
WHERE a <> b
RETURN COLLECT(a)[0] + COLLECT(b) AS noDuplicates

==> +-------------------+
==> | noDuplicates      |
==> +-------------------+
==> | [1,2,3,4,5,6,7,8] |
==> +-------------------+
==> 1 row
~~~

<p>Still happy, good times! Of course if we have a non consecutive duplicate that wouldn't be removed:</p>



~~~cypher

WITH [1,1,1,2,3,4,5,5,6,7,7,8,1] AS values
UNWIND RANGE(0, LENGTH(values) - 2) AS idx
WITH values[idx] AS a, values[idx+1] AS b
WHERE a <> b
RETURN COLLECT(a)[0] + COLLECT(b) AS noDuplicates

==> +---------------------+
==> | noDuplicates        |
==> +---------------------+
==> | [1,2,3,4,5,6,7,8,1] |
==> +---------------------+
==> 1 row
~~~
