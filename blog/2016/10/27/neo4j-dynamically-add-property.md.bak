+++
draft = false
date="2016-10-27 05:29:30"
title="Neo4j: Dynamically add property/Set dynamic property"
tag=['neo4j']
category=['neo4j']
+++

<p>
I've been playing around with a dataset which has the timetable for the national rail in the UK and they give you departure and arrival times of each train in a textual format.
</p>


<p>For example, the node to represent a stop could be created like this:</p>



~~~cypher

CREATE (stop:Stop {arrival: "0802", departure: "0803H"})
~~~

<p>
That time format isn't particular amenable to querying so I wanted to add another property which indicated the number of seconds since the start of the day.
</p>


<p>So we want to add 'arrivalSecondsSinceStartOfDay' and 'departureSecondsSinceStartOfDay' properties to our node. I wrote the following query to calculate the values for those properties.
</p>



~~~cypher

MATCH (stop:Stop)
UNWIND ["arrival", "departure"] AS key

WITH key,
     toInteger(substring(stop[key], 0, 2)) AS hours,          
     toInteger(substring(stop[key], 2, 2)) AS minutes,
     CASE WHEN substring(stop[key], 4,1) = "H" THEN 30 ELSE 0 END AS seconds

WITH key, (hours * 60 * 60) + (minutes * 60) + seconds AS secondsSinceStartOfDay

RETURN key + "SecondsSinceStartOfDay" AS newKey, secondsSinceStartOfDay
~~~


~~~text

╒═══════════════════════════════╤══════════════════════╕
│newKey                         │secondsSinceStartOfDay│
╞═══════════════════════════════╪══════════════════════╡
│arrivalSecondsSinceStartOfDay  │28920                 │
├───────────────────────────────┼──────────────────────┤
│departureSecondsSinceStartOfDay│29010                 │
└───────────────────────────────┴──────────────────────┘
~~~

<p>
Now we're ready to set those properties on the 'stop' node. 
</p>



~~~cypher

MATCH (stop:Stop2)
UNWIND ["arrival", "departure"] AS key

WITH stop,
     key,
     toInteger(substring(stop[key], 0, 2)) AS hours,          
     toInteger(substring(stop[key], 2, 2)) AS minutes,
     CASE WHEN substring(stop[key], 4,1) = "H" THEN 30 ELSE 0 END AS seconds

WITH stop, key, (hours * 60 * 60) + (minutes * 60) + seconds AS secondsSinceStartOfDay
WITH stop, key + "SecondsSinceStartOfDay" AS newKey, secondsSinceStartOfDay
SET stop[newKey] = secondsSinceStartOfDay
~~~


~~~text

Invalid input '[': expected an identifier character, whitespace, '{', node labels, a property map, a relationship pattern, '.', '(', '=' or "+=" (line 12, column 9 (offset: 447))
"SET stop[newKey] = secondsSinceStartOfDay"
         ^
~~~

<p>Hmmm that didn't work as expected! It doesn't look like we can set dynamic properties using Cypher just yet.
</p>


<p>
Luckily my colleague Michael Hunger and the Neo4j community have been curating the <a href="https://neo4j-contrib.github.io/neo4j-apoc-procedures/">APOC procedures library</a> and it has just the procedure to help us out.
</p>


<p>
You'll need to <a href="https://github.com/neo4j-contrib/neo4j-apoc-procedures/releases">download the jar</a> for your version of Neo4j and then place it in the <cite>plugins</cite> directory. I'm using Neo4j 3.1 Beta1 so this is what it looks like for me:
</p>



~~~bash

$ tree neo4j-enterprise-3.1.0-BETA1/plugins/

neo4j-enterprise-3.1.0-BETA1/plugins/
└── apoc-3.1.0.1-all.jar

0 directories, 1 file
~~~

<p>
After you've done that you'll need to restart Neo4j so that it can pick up the new procedures that we've added. Once you've done that execute the following query to check they've installed correctly:
</p>



~~~cypher

call dbms.procedures()
YIELD name 
WITH name 
WHERE name STARTS WITH "apoc"
RETURN COUNT(*)
~~~


~~~text

╒════════╕
│COUNT(*)│
╞════════╡
│183     │
└────────┘
~~~

<p>We're now ready to dynamically set properties in the graph. The procedure that we'll use is <cite>apoc.create.setProperty</cite> and it's easy to update our query to use it:</p>



~~~cypher

MATCH (stop:Stop)
UNWIND ["arrival", "departure"] AS key

WITH stop,
     key,
     toInteger(substring(stop[key], 0, 2)) AS hours,          
     toInteger(substring(stop[key], 2, 2)) AS minutes,
     CASE WHEN substring(stop[key], 4,1) = "H" THEN 30 ELSE 0 END AS seconds

WITH stop, key, (hours * 60 * 60) + (minutes * 60) + seconds AS secondsSinceStartOfDay
WITH stop, key + "SecondsSinceStartOfDay" AS newKey, secondsSinceStartOfDay
CALL apoc.create.setProperty(stop, newKey, secondsSinceStartOfDay) 
~~~


~~~text

Query cannot conclude with CALL (must be RETURN or an update clause) (line 12, column 1 (offset: 439))
"CALL apoc.create.setProperty(stop, newKey, secondsSinceStartOfDay)"
 ^
~~~

<p>Oops I spoke too soon! We need to yield the return column of the procedure and return it or just return a count to work around this:</p>



~~~cypher

MATCH (stop:Stop)
UNWIND ["arrival", "departure"] AS key

WITH stop,
     key,
     toInteger(substring(stop[key], 0, 2)) AS hours,          
     toInteger(substring(stop[key], 2, 2)) AS minutes,
     CASE WHEN substring(stop[key], 4,1) = "H" THEN 30 ELSE 0 END AS seconds

WITH stop, key, (hours * 60 * 60) + (minutes * 60) + seconds AS secondsSinceStartOfDay
WITH stop, key + "SecondsSinceStartOfDay" AS newKey, secondsSinceStartOfDay
CALL apoc.create.setProperty(stop, newKey, secondsSinceStartOfDay) 
YIELD node
RETURN COUNT(*)
~~~


~~~text

╒════════╕
│COUNT(*)│
╞════════╡
│2       │
└────────┘
~~~

<p>And that's it, we can now dynamically set properties in our queries.</p>

