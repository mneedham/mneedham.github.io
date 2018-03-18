+++
draft = false
date="2012-09-09 22:29:33"
title="neo4j/cypher: CREATE UNIQUE - \"SyntaxException: string matching regex `$' expected but `p' found\""
tag=['neo4j', 'cypher']
category=['neo4j']
+++

I've been playing around with the mutating cypher syntax of neo4j which allows you to make changes to the graph as well as query it, a feature introduced into cypher in May in <a href="http://blog.neo4j.org/2012/05/neo4j-18m01-release-vindeln-vy.html">release 1.8 M01</a>.

I was trying to make use of the '<a href="http://docs.neo4j.org/chunked/milestone/query-create-unique.html">CREATE UNIQUE</a>' syntax which allows you to create nodes/relationships if they're missing but won't do anything if they already exists.

I had something like the following:


~~~text

START product1=node:products('product_id:1')
CREATE UNIQUE product1-[:sold]->(sales200010 {type:"product_sales", value: 1, name: "Oct 2000 Sales"})
~~~

So I already have a product indexed with a 'product_id' of 1 and I wanted to create a relationship to a node defining the sales for that product.

When I tried to execute that query I was ending up with the following error:


~~~text

SyntaxException: string matching regex `$' expected but `p' found

Think we should have better error message here? Help us by sending this query to cypher@neo4j.org.

Thank you, the Neo4j Team.
~~~

I was a bit puzzled as to why that wouldn't work but eventually I read the <a href="http://blog.neo4j.org/2012/08/neo4j-18m07-sharing-is-caring.html">release notes for 1.8 M07</a> where I learnt that in earlier versions of neo4j 'CREATE UNIQUE' had actually been known as 'RELATE' instead.

Since I'm using 1.8 M06 at the moment I just needed to change 'CREATE UNIQUE' to 'RELATE' but <a href="http://neo4j.org/download-thanks/?edition=community&release=1.8.RC1&platform=unix">RC1 is now available</a> so I'll soon switch to that and go back to 'CREATE UNIQUE' again.
