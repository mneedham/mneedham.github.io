+++
draft = false
date="2013-05-19 22:15:06"
title="neo4j/cypher: Keep longest path when finding taxonomy"
tag=['neo4j', 'cypher']
category=['neo4j']
+++

<p>I've been playing around with modelling a product taxonomy and one thing that I wanted to do was find out the full path where a product sits under the tree.</p>


<p>I created a <a href="http://console.neo4j.org/?id=62rmy2">simple data set</a> to show the problem:</p>



~~~cypher

CREATE (cat { name: "Cat" })
CREATE (subcat1 { name: "SubCat1" })
CREATE (subcat2 { name: "SubCat2" })
CREATE (subsubcat1 { name: "SubSubCat1" })
CREATE (product1 { name: "Product1" })
CREATE (cat)-[:CHILD]-subcat1-[:CHILD]-subsubcat1
CREATE (product1)-[:HAS_CATEGORY]-(subsubcat1)
~~~

<p>I wanted to write a query which would return 'product1' and the tree 'Cat -> SubCat1 -> SubSubCat1' and initially wrote the following query:</p>



~~~cypher

START product=node:node_auto_index(name="Product1") 
MATCH product-[:HAS_CATEGORY]-category, taxonomy=category<-[:CHILD*1..]-parent 
RETURN product, EXTRACT(n IN NODES(taxonomy): n.name)
~~~

<p>which returns:</p>



~~~text

==> +--------------------------------------------------------------------+
==> | product                    | EXTRACT(n IN NODES(taxonomy): n.name) |
==> +--------------------------------------------------------------------+
==> | Node[888]{name:"Product1"} | ["SubSubCat1","SubCat1"]              |
==> | Node[888]{name:"Product1"} | ["SubSubCat1","SubCat1","Cat"]        |
==> +--------------------------------------------------------------------+
==> 2 rows
~~~

<p>I didn't want to return the first row since that isn't the full tree and <a href="https://twitter.com/andres_taylor">Andres</a> suggested that looking for nodes which didn't have any incoming children would help me do that:</p>



~~~cypher

START product=node:node_auto_index(name="Product1") 
MATCH product-[:HAS_CATEGORY]-category, 
      taxonomy=category<-[:CHILD*1..]-parent 
WHERE NOT parent<-[:CHILD]-() 
RETURN product, EXTRACT(n IN NODES(taxonomy): n.name)
~~~


~~~text

==> +--------------------------------------------------------------------+
==> | product                    | EXTRACT(n IN NODES(taxonomy): n.name) |
==> +--------------------------------------------------------------------+
==> | Node[888]{name:"Product1"} | ["SubSubCat1","SubCat1","Cat"]        |
==> +--------------------------------------------------------------------+
==> 1 row
~~~

<p>If we want to reverse the taxonomy so it's in the right order we can follow <a href="http://stackoverflow.com/questions/13024098/how-to-get-a-null-value-when-using-the-head-function-with-an-empty-list">Wes Freeman's advice from the following Stack Overflow thread</a>:</p>



~~~cypher

START product=node:node_auto_index(name="Product1") 
MATCH product-[:HAS_CATEGORY]-category, taxonomy=category<-[:CHILD*1..]-parent 
WHERE NOT parent<-[:CHILD]-() 
RETURN product, 
       REDUCE(acc=[], cat IN EXTRACT(n IN NODES(taxonomy): n.name): cat + acc) AS taxonomy
~~~


~~~text

==> +-------------------------------------------------------------+
==> | product                    | taxonomy                       |
==> +-------------------------------------------------------------+
==> | Node[888]{name:"Product1"} | ["Cat","SubCat1","SubSubCat1"] |
==> +-------------------------------------------------------------+
==> 1 row
~~~
