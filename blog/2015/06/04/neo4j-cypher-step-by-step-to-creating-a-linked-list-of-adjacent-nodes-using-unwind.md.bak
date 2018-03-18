+++
draft = false
date="2015-06-04 22:17:34"
title="Neo4j: Cypher - Step by step to creating a linked list of adjacent nodes using UNWIND"
tag=['neo4j']
category=['neo4j']
+++

<p>
In late 2013 I wrote a post showing <a href="http://www.markhneedham.com/blog/2013/11/22/neo4j-cypher-creating-relationships-between-nodes-from-adjacent-rows-in-a-query/">how to create a linked list connecting different football seasons together</a> using Neo4j's Cypher query language, a post I've frequently copy & pasted from!
</p>


<p>
Now 18 months later, and using Neo4j 2.2 rather than 2.0, we can actually solve this problem in what I believe is a more intuitive way using the <cite><a href="http://neo4j.com/docs/stable/query-unwind.html">UNWIND</a></cite> function. Credit for the idea goes to <a href="https://twitter.com/mesirii">Michael</a>, I'm just the messenger.
</p>


<p>To recap, we had a collection of football seasons and we wanted to connect adjacent seasons to each other to allow easy querying between seasons. The following is the code we used:</p>



~~~cypher

CREATE (:Season {name: "2013/2014", timestamp: 1375315200})
CREATE (:Season {name: "2012/2013", timestamp: 1343779200})
CREATE (:Season {name: "2011/2012", timestamp: 1312156800})
CREATE (:Season {name: "2010/2011", timestamp: 1280620800})
CREATE (:Season {name: "2009/2010", timestamp: 1249084800})
~~~


~~~cypher

MATCH (s:Season)
WITH s
ORDER BY s.timestamp
WITH COLLECT(s) AS seasons
 
FOREACH(i in RANGE(0, length(seasons)-2) | 
    FOREACH(si in [seasons[i]] | 
        FOREACH(si2 in [seasons[i+1]] | 
            MERGE (si)-[:NEXT]->(si2))))
~~~

<p>Our goal is to replace those 3 <cite>FOREACH</cite> loops with something a bit easier to understand. To start with, let's run the first part of the query to get some intuition of what we're trying to do:</p>



~~~cypher

MATCH (s:Season)
WITH s
ORDER BY s.timestamp
RETURN COLLECT(s) AS seasons

==> +-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
==> | seasons                                                                                                                                                                                                                                                     |
==> +-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
==> | [Node[1973]{timestamp:1249084800,name:"2009/2010"},Node[1972]{timestamp:1280620800,name:"2010/2011"},Node[1971]{timestamp:1312156800,name:"2011/2012"},Node[1970]{timestamp:1343779200,name:"2012/2013"},Node[1969]{timestamp:1375315200,name:"2013/2014"}] |
==> +-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
~~~

<p>
So at this point we've got all the seasons in an array going from 2009/2010 up to 2013/2014. We want to create a 'NEXT' relationship between 2009/2010 -> 2010/2011, 2010/2011 -> 2011/2012 and so on.
</p>


<p>
To achieve this we need to get the adjacent seasons split into two columns, like so:
</p>



~~~text

2009/2010	2010/2011
2010/2011	2011/2012
2011/2012	2012/2013
2012/2013	2013/2014
~~~

<p>If we can get the data into that format then we can apply a <cite>MERGE</cite> between the two fields to create the 'NEXT' relationship. So how do we do that?</p>


<p>
If we were in Python we'd be calling for the zip function which we could apply like this:
</p>



~~~python

>>> seasons = ["2009/2010", "2010/2011", "2011/2012", "2012/2013", "2013/2014"]

>>> zip(seasons, seasons[1:])
[('2009/2010', '2010/2011'), ('2010/2011', '2011/2012'), ('2011/2012', '2012/2013'), ('2012/2013', '2013/2014')]
~~~

<p>Unfortunately we don't have an equivalent function in Cypher but we can achieve the same outcome by creating 2 columns with adjacent integer values. The <cite>RANGE</cite> and <cite>UNWIND</cite> functions are our friends here:
</p>



~~~cypher

return RANGE(0,4)

==> +-------------+
==> | RANGE(0,4)  |
==> +-------------+
==> | [0,1,2,3,4] |
==> +-------------+
~~~


~~~cypher

UNWIND RANGE(0,4) as idx 
RETURN idx, idx +1;

==> +--------------+
==> | idx | idx +1 |
==> +--------------+
==> | 0   | 1      |
==> | 1   | 2      |
==> | 2   | 3      |
==> | 3   | 4      |
==> | 4   | 5      |
==> +--------------+
==> 5 rows
~~~

<p>Now all we need to do is plug this code into our original query where 'idx' and 'idx + 1' represent indexes into the array of seasons. We use a range which stops 1 element early since there isn't anywhere to connect our last season to:
</p>



~~~cypher

MATCH (s:Season)
WITH s
ORDER BY s.timestamp
WITH COLLECT(s) AS seasons
UNWIND RANGE(0,LENGTH(seasons) - 2) as idx 
RETURN seasons[idx], seasons[idx+1]

==> +-------------------------------------------------------------------------------------------------------+
==> | seasons[idx]                                      | seasons[idx+1]                                    |
==> +-------------------------------------------------------------------------------------------------------+
==> | Node[1973]{timestamp:1249084800,name:"2009/2010"} | Node[1972]{timestamp:1280620800,name:"2010/2011"} |
==> | Node[1972]{timestamp:1280620800,name:"2010/2011"} | Node[1971]{timestamp:1312156800,name:"2011/2012"} |
==> | Node[1971]{timestamp:1312156800,name:"2011/2012"} | Node[1970]{timestamp:1343779200,name:"2012/2013"} |
==> | Node[1970]{timestamp:1343779200,name:"2012/2013"} | Node[1969]{timestamp:1375315200,name:"2013/2014"} |
==> +-------------------------------------------------------------------------------------------------------+
==> 4 rows
~~~

<p>Now we've got all the adjacent seasons lined up we complete the query with a call to <cite>MERGE</cite>:</p>



~~~cypher

MATCH (s:Season)
WITH s
ORDER BY s.timestamp
WITH COLLECT(s) AS seasons
UNWIND RANGE(0,LENGTH(seasons) - 2) as idx 
WITH seasons[idx] AS s1, seasons[idx+1] AS s2
MERGE (s1)-[:NEXT]->(s2)

==> +-------------------+
==> | No data returned. |
==> +-------------------+
==> Relationships created: 4
~~~

<p>And we're done. Hopefully I can remember this approach more than I did the initial one!</p>

