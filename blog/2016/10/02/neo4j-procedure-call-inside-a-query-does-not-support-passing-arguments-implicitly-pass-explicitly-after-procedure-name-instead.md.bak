+++
draft = false
date="2016-10-02 10:13:26"
title="Neo4j: Procedure call inside a query does not support passing arguments implicitly (pass explicitly after procedure name instead)"
tag=['neo4j', 'cypher']
category=['neo4j']
+++

<p>
A couple of days I was trying to write a Cypher query to filter the labels in my database.
</p>


<p>I started with the following procedure call to get the list of all the labels:</p>



~~~cypher

CALL db.labels
~~~


~~~text

╒══════════╕
│label     │
╞══════════╡
│Airport   │
├──────────┤
│Flight    │
├──────────┤
│Airline   │
├──────────┤
│Movie     │
├──────────┤
│AirportDay│
├──────────┤
│Person    │
├──────────┤
│Engineer  │
└──────────┘
~~~

<p>I was only interested in labels that contained the letter 'a' so I tweaked the query to filter the output of the procedure:
</p>



~~~cypher

CALL db.labels
YIELD label 
WITH label WHERE tolower(label) contains "a"
RETURN label
~~~

<p>Unfortunately that didn't work as I expected:</p>



~~~text

Procedure call inside a query does not support passing arguments implicitly (pass explicitly after procedure name instead) (line 1, column 9 (offset: 8))
"CALL db.labels"
         ^
~~~

<p>
The mistake I made was calling the procedure implicitly without using parentheses. If you want to do any post processing on the output of a procedure you need to call it explicitly otherwise Cypher gets very confused. 
</p>


<p>If we add back the parentheses it's much happier:</p>



~~~cypher

CALL db.labels()
YIELD label 
WITH label WHERE tolower(label) contains "a"
RETURN label
~~~


~~~text

╒══════════╕
│label     │
╞══════════╡
│Airport   │
├──────────┤
│Airline   │
├──────────┤
│AirportDay│
└──────────┘
~~~ 

<p>
It stumped me for a while until I figured out what the error message meant! I think I'll just use explicit parentheses all the time from now on to save me running into this one again.
</p>

