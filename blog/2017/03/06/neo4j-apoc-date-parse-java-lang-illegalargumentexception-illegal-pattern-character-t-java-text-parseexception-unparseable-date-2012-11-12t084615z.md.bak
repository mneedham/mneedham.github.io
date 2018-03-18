+++
draft = false
date="2017-03-06 20:52:01"
title="Neo4j: apoc.date.parse - java.lang.IllegalArgumentException: Illegal pattern character 'T' / java.text.ParseException: Unparseable date: \"2012-11-12T08:46:15Z\""
tag=['neo4j']
category=['neo4j']
+++

<p>
I often find myself wanting to convert date strings into Unix timestamps using <a href="https://github.com/neo4j-contrib/neo4j-apoc-procedures">Neo4j's APOC library</a> and unfortunately some sources don't use the format that <a href="https://neo4j-contrib.github.io/neo4j-apoc-procedures/#_date_time_support"><cite>apoc.date.parse</cite></a> expects.
</p>


<p>e.g.</p>



~~~cypher

return apoc.date.parse("2012-11-12T08:46:15Z",'s') 
AS ts

Failed to invoke function `apoc.date.parse`: 
Caused by: java.lang.IllegalArgumentException: java.text.ParseException: Unparseable date: "2012-11-12T08:46:15Z"
~~~

<p>We need to define the format explicitly so the <a href="https://docs.oracle.com/javase/7/docs/api/java/text/SimpleDateFormat.html">SimpleDataFormat</a> documentation comes in handy. I tried the following:
</p>



~~~cypher

return apoc.date.parse("2012-11-12T08:46:15Z",'s',"yyyy-MM-ddTHH:mm:ssZ") 
AS ts

Failed to invoke function `apoc.date.parse`: 
Caused by: java.lang.IllegalArgumentException: Illegal pattern character 'T'
~~~

<p>
Hmmm, we need to quote the 'T' character - we can't just include it in the pattern. Let's try again:
</p>



~~~cypher

return  apoc.date.parse("2012-11-12T08:46:15Z",'s',"yyyy-MM-dd'T'HH:mm:ssZ") 
AS ts

Failed to invoke function `apoc.date.parse`: 
Caused by: java.lang.IllegalArgumentException: java.text.ParseException: Unparseable date: "2012-11-12T08:46:15Z"
~~~

<p>The problem now is that we haven't quoted the 'Z' but the error doesn't indicate that - not sure why!</p>


<p>We can either quote the 'Z':</p>



~~~cypher

return  apoc.date.parse("2012-11-12T08:46:15Z",'s',"yyyy-MM-dd'T'HH:mm:ss'Z'") 
AS ts

╒══════════╕
│"ts"      │
╞══════════╡
│1352709975│
└──────────┘
~~~

<p>
Or we can match the timezone using 'XXX':

</p>



~~~cypher

return  apoc.date.parse("2012-11-12T08:46:15Z",'s',"yyyy-MM-dd'T'HH:mm:ssXXX") 
AS ts

╒══════════╕
│"ts"      │
╞══════════╡
│1352709975│
└──────────┘
~~~
