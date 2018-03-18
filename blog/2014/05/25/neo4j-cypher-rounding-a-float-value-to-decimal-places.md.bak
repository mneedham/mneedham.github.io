+++
draft = false
date="2014-05-25 22:17:35"
title="Neo4j: Cypher - Rounding a float value to decimal places"
tag=['neo4j', 'cypher']
category=['neo4j']
+++

<p>About 6 months ago <a href="http://www.jacqui.tk/">Jacqui Read</a> created a github issue explaining how she wanted to <a href="https://github.com/neo4j/neo4j/issues/1580">round a float value to a number of decimal places</a> but was unable to do so due to the <cite><a href="http://docs.neo4j.org/chunked/stable/query-functions-mathematical.html#functions-round">round</a></cite> function not taking the appropriate parameter.</p>


<p>I found myself wanting to do the same thing last week where I initially had the following value:</p>



~~~cypher

RETURN toFloat("12.336666") AS value
~~~

<p>I wanted to round that to 2 decimal places and <a href="https://twitter.com/wefreema">Wes</a> suggested multiplying the value before using ROUND and then dividing afterwards to achieve that.</p>


<p>For two decimal places we need to multiply and divide by 100:</p>



~~~cypher

WITH toFloat("12.336666") AS value
RETURN round(100 * value) / 100 AS value
~~~


~~~bash

12.34
~~~

<p><a href="https://twitter.com/mesirii">Michael</a> suggested abstracting the number of decimal places like so:</p>



~~~cypher

WITH 2 as precision
WITH toFloat("12.336666") AS value, 10^precision AS factor
RETURN round(factor * value)/factor AS value
~~~

<p>If we want to round to 4 decimal places we can easily change that:</p>



~~~cypher

WITH 4 as precision
WITH toFloat("12.336666") AS value, 10^precision AS factor
RETURN round(factor * value)/factor AS value
~~~


~~~bash

12.3367
~~~

<p>The code is <a href="http://gist.neo4j.org/?0e68a1c6922c04b53af0">available as a graph gist</a> too if you want to play around with it. And you may as well check out the <a href="https://github.com/neo4j-contrib/graphgist/wiki">other gists</a> while you're at it - enjoy!</p>

