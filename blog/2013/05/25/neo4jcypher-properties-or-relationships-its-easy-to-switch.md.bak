+++
draft = false
date="2013-05-25 12:21:55"
title="neo4j/cypher: Properties or relationships? It's easy to switch"
tag=['neo4j', 'cypher']
category=['neo4j']
+++

<p>I've written previously about how I've <a href="http://www.markhneedham.com/blog/2013/03/06/neo4j-make-properties-relationships/">converted properties on nodes into relationships</a> and over the past week there was an <a href="https://groups.google.com/forum/?fromgroups#!topic/neo4j/Uk5KV9kfFzk">interesting discussion on the neo4j mailing list about where each is appropriate</a>.</p>


<p><a href="https://twitter.com/jimwebber">Jim</a> gives quite a neat summary of the difference between the two on the thread:</p>


<blockquote>
Properties are the data that an entity like a node [or relationship] holds. Relationships simply form the semantic glue (type, direction, cardinality) between nodes.
</blockquote>

<p>To add to that, if you find yourself using a property to help narrow down a traversal then it's worth checking whether you'd be better off modelling it as a relationship.</p>


<p>The neat thing is that it's reasonably easy to change your mind at a later stage and convert a property into a relationship or vice versa.</p>


<p>For example let's say we're modelling some products for a shop. We might start with the following cypher code to create them:</p>



~~~cypher

CREATE (frenchConnection { name: "French Connection" })
CREATE  (dress1 { name: "Halter Dress", colour: "Blue"})-[:BRAND]-(frenchConnection)
CREATE  (dress2 { name: "Another Dress", colour: "Yellow"})-[:BRAND]-(frenchConnection)
CREATE  (dress3 { name: "Different Dress", colour: "Blue"})-[:BRAND]-(frenchConnection)
RETURN dress1, dress2, dress3
~~~


~~~text

==> +--------------------------------------------------------------------------------------------------------------------------------------------+
==> | dress1                                     | dress2                                        | dress3                                        |
==> +--------------------------------------------------------------------------------------------------------------------------------------------+
==> | Node[2]{name:"Halter Dress",colour:"Blue"} | Node[3]{name:"Another Dress",colour:"Yellow"} | Node[4]{name:"Different Dress",colour:"Blue"} |
==> +--------------------------------------------------------------------------------------------------------------------------------------------+
==> 1 row
==> Nodes created: 4
==> Relationships created: 3
==> Properties set: 7
==> 179 ms
~~~

<p>If we want to find all the French connection clothing which is blue we could write the following query:</p>



~~~cypher

START brand = node:node_auto_index(name="French Connection") 
MATCH brand<-[:BRAND]-product 
WHERE product.colour = "Blue"
RETURN brand, product
~~~


~~~text

==> +-----------------------------------------------------------------------------------+
==> | brand                             | product                                       |
==> +-----------------------------------------------------------------------------------+
==> | Node[1]{name:"French Connection"} | Node[2]{name:"Halter Dress",colour:"Blue"}    |
==> | Node[1]{name:"French Connection"} | Node[3]{name:"Another Dress",colour:"Yellow"} |
==> | Node[1]{name:"French Connection"} | Node[4]{name:"Different Dress",colour:"Blue"} |
==> +-----------------------------------------------------------------------------------+
==> 3 rows
==> 69 ms
~~~

<p>Since our query doesn't return many records it's not a problem that we have to look up the 'colour' property for every product but with a bigger data set the query would slow down considerably. We might therefore decide to create a 'COLOUR' relationship.</p>


<p>One way to do that would be by running the same cypher query as before except we also create a relationship to a colour node:</p>



~~~cypher

CREATE (blue { name: "Blue"})
~~~


~~~cypher

START brand = node:node_auto_index(name="French Connection"), 
      blue = node:node_auto_index(name="Blue")
MATCH brand<-[:BRAND]-product 
WHERE product.colour = "Blue"

CREATE UNIQUE product-[:COLOUR]->blue
RETURN brand, product
~~~

<p>Our query to find the blue French Connection products would now look like this:</p>



~~~cypher

START brand = node:node_auto_index(name="French Connection"), 
      blue = node:node_auto_index(name="Blue") 
MATCH brand<-[:BRAND]-product-[:COLOUR]->blue 
RETURN brand, product
~~~


~~~text

==> +-----------------------------------------------------------------------------------+
==> | brand                             | product                                       |
==> +-----------------------------------------------------------------------------------+
==> | Node[1]{name:"French Connection"} | Node[2]{name:"Halter Dress",colour:"Blue"}    |
==> | Node[1]{name:"French Connection"} | Node[4]{name:"Different Dress",colour:"Blue"} |
==> +-----------------------------------------------------------------------------------+
==> 2 rows
==> 3 ms
~~~

<p>We can do it the other way around as well i.e. we can search for relationships and then set properties on nodes.</p>
 

<p>For example let's say we want to mark the blue French connection clothing as being on sale but we weren't interested in searching specifically for on sale items:</p>



~~~cypher

START brand = node:node_auto_index(name="French Connection"), 
      blue = node:node_auto_index(name="Blue") 
MATCH brand<-[:BRAND]-product-[:COLOUR]->blue 
SET product.state = "OnSale"
RETURN brand, product
~~~

<p>If we now repeat our previous query we'll see that property on the products:</p>



~~~cypher

START brand = node:node_auto_index(name="French Connection"), 
      blue = node:node_auto_index(name="Blue") 
MATCH brand<-[:BRAND]-product-[:COLOUR]->blue 
RETURN brand, product
~~~


~~~text

==> +--------------------------------------------------------------------------------------------------+
==> | brand                             | product                                                      |
==> +--------------------------------------------------------------------------------------------------+
==> | Node[1]{name:"French Connection"} | Node[2]{name:"Halter Dress",colour:"Blue",state:"OnSale"}    |
==> | Node[1]{name:"French Connection"} | Node[4]{name:"Different Dress",colour:"Blue",state:"OnSale"} |
==> +--------------------------------------------------------------------------------------------------+
==> 2 rows
==> 2 ms
~~~


<p>All the queries used in this post are on available as a <a href="https://gist.github.com/mneedham/5648898">gist</a> if you're interesting in playing around with it further. You can read more about <a href="http://docs.neo4j.org/chunked/stable/query-write.html">cypher write syntax on the documentation pages</a>.</p>

