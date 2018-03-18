+++
draft = false
date="2013-11-01 20:41:18"
title="Neo4j: A first attempt at retail product substitution"
tag=['neo4j']
category=['neo4j']
+++

<p>One of the interesting problems in the world of online shopping from the perspective of the retailer is working out <strong>whether there is a suitable substitute product</strong> if an ordered item isn't currently in stock.</p>


<p>Since this problem brings together three types of data - order history, stock levels and products - it seems like it should be a nice fit for Neo4j so I 'graphed up' a quick example.</p>


<p>I wrote the following cypher to create some products, a person, a few orders and then the availability of those products in an imaginary store.</p>



~~~cypher

CREATE (bakedBeans :Category {name: "Baked Beans"} )
CREATE (fruit :Category {name: "Fruit"} )

CREATE (hbb :Product {name: "Heinz Baked Beans", type: "brand"} )
CREATE (bbb :Product {name: "Branstone Baked Beans", type: "brand"} )
CREATE (sbb :Product {name: "Sainsbury's Baked Beans", type: "own"} )
CREATE (apple :Product {name: "Bag of Apples"} )

CREATE UNIQUE (hbb)-[:HAS_CATEGORY]->(bakedBeans)
CREATE UNIQUE (bbb)-[:HAS_CATEGORY]->(bakedBeans)
CREATE UNIQUE (sbb)-[:HAS_CATEGORY]->(bakedBeans)

CREATE (southwark :Store {name: "Southwark"})

CREATE UNIQUE (southwark)-[:HAS_IN_STOCK {availability: 0}]->(hbb)
CREATE UNIQUE (southwark)-[:HAS_IN_STOCK {availability: 2}]->(bbb)
CREATE UNIQUE (southwark)-[:HAS_IN_STOCK {availability: 10}]->(sbb)
CREATE UNIQUE (southwark)-[:HAS_IN_STOCK {availability: 10}]->(apple)

CREATE (mark :Person {name: "Mark"})

CREATE (order1 :Order {id: 1, date: 1380884632})

CREATE UNIQUE (order1)-[:CONTAINS {count: 1}]->(hbb)
CREATE UNIQUE (order1)-[:CONTAINS {count: 5}]->(apple)
CREATE UNIQUE (mark)-[:PLACED_ORDER]->(order1)

CREATE (order2 :Order {id: 2, date: 1380885051})

CREATE UNIQUE (order2)-[:CONTAINS {count: 1}]->bbb
CREATE UNIQUE (mark)-[:PLACED_ORDER]->(order2)
~~~

<p>We may then have a new order which we're trying to fulfil and we want to check whether the products are in stock.</p>


<p>First we'll create the order:</p>



~~~cypher

// Create the order
CREATE (order3:Order {id: 3, date: 1380895051})

WITH order3

// Assign the order to Mark
MATCH (p:Person)
WHERE p.name = "Mark"
CREATE UNIQUE (p)-[:PLACED_ORDER]->(order3)

WITH order3

// Populate the order with some products
MATCH (p:Product)
WHERE p.name = "Heinz Baked Beans" 
CREATE UNIQUE (order3)-[:CONTAINS {count: 2}]->(p)

WITH order3

MATCH (p:Product)
WHERE p.name = "Bag of Apples"
CREATE UNIQUE (order3)-[:CONTAINS {count: 2}]->(p)
~~~

<p>Now let's check on the availability of each item in the order in a particular store:</p>



~~~cypher

// Find the products in the order
MATCH (o:Order)-[c:CONTAINS]->(product)
WHERE o.id = 3
WITH product, c.count AS count

// Check which items are out of stock in our store
MATCH (s:Store)-[inStock:HAS_IN_STOCK]->(product)
WHERE s.name = "Southwark"
RETURN product, inStock

==> +--------------------------------------------------------------------------------------------+
==> | product                                            | inStock                               |
==> +--------------------------------------------------------------------------------------------+
==> | Node[11444]{name:"Heinz Baked Beans",type:"brand"} | :HAS_IN_STOCK[60053]{availability:0}  |
==> | Node[11447]{name:"Bag of Apples"}                  | :HAS_IN_STOCK[60056]{availability:10} |
==> +--------------------------------------------------------------------------------------------+
~~~

<p>Now if we change that query to only return items which have less items in stock than we attempted to order we'll see that Heinz Baked Beans aren't available:</p>



~~~bash

// Find the products in the order
MATCH (o:Order)-[c:CONTAINS]->(product)
WHERE o.id = 3
WITH product, c.count AS count

// Check which items are out of stock in our store
MATCH (s:Store)-[inStock:HAS_IN_STOCK]->(product)
WHERE s.name = "Southwark" AND count > inStock.availability
RETURN product, inStock

==> +-------------------------------------------------------------------------------------------+
==> | product                                            | inStock                              |
==> +-------------------------------------------------------------------------------------------+
==> | Node[15281]{name:"Heinz Baked Beans",type:"brand"} | :HAS_IN_STOCK[86079]{availability:0} |
==> +-------------------------------------------------------------------------------------------+
~~~

<p></p>



~~~cypher

MATCH (p:Person)-[:PLACED_ORDER]->order-[c:CONTAINS]->product-[:HAS_CATEGORY]->category
WHERE p.name = "Mark" AND category.name = "Baked Beans" AND order.id <> 3
RETURN product.name, product.type, order.id

==> +---------------------------------------------------+
==> | product.name            | product.type | order.id |
==> +---------------------------------------------------+
==> | "Heinz Baked Beans"     | "brand"      | 1        |
==> | "Branstone Baked Beans" | "brand"      | 2        |
==> +---------------------------------------------------+
~~~

<p>Having identified Mark as a connoisseur of branded baked beans we might then run a query to check if there are any other branded baked beans available in that store:</p>



~~~cypher

MATCH (s:Store)-[inStock:HAS_IN_STOCK]->p-[:HAS_CATEGORY]->c
WHERE s.name = "Southwark" 
AND c.name = "Baked Beans" 
AND inStock.availability > 0 
AND p.type = "brand"
RETURN p.name, inStock.availability

==> +------------------------------------------------+
==> | p.name                  | inStock.availability |
==> +------------------------------------------------+
==> | "Branstone Baked Beans" | 2                    |
==> +------------------------------------------------+
~~~

<p>This is obviously an extremely naive approach so I went to twitter in the hope that I could find a more sophisticated approach:</p>


<blockquote class="twitter-tweet"><p>Are there any general algorithms for product similarity? e.g. based on category/description etc. Or is it very much domain specific?</p>
&mdash; Mark Needham (@markhneedham) <a href="https://twitter.com/markhneedham/statuses/394062759089803264">October 26, 2013</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

<p>Nicole White is currently playing around with <a href="http://en.wikipedia.org/wiki/Association_rule_learning">association rule mining</a> which sounds interesting.</p>


<blockquote class="twitter-tweet"><p><a href="https://twitter.com/markhneedham">@markhneedham</a> I&#39;m sure it can be! I&#39;m actually working on association rule mining in a <a href="https://twitter.com/search?q=%23neo4j&src=hash">#neo4j</a> db with purchases transaction data.</p>
&mdash; Nicole White (@_nicolemargaret) <a href="https://twitter.com/_nicolemargaret/statuses/395442129243103232">October 30, 2013</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

<p>It is described on its Wikipedia page like so:</p>


<blockquote>
Based on the concept of strong rules, Rakesh Agrawal et al.[2] introduced association rules for discovering regularities between products in large-scale transaction data recorded by point-of-sale (POS) systems in supermarkets.
</blockquote>

<p>Although it's not exactly the same as what I want to do I need to look into it more to see if some of the ideas can be applied.</p>


<p>I also learnt that the terminology for what I'm looking for is a '<a href="https://www.google.com/?q=similar+items+algorithm#q=similar+items+algorithm">similar items</a>' algorithm and I think what I'm looking to spike would be a <a href="http://en.wikipedia.org/wiki/Recommender_system#Hybrid_Recommender_Systems">hybrid recommender system</a> which combines content similarity and user's previous purchase history.</p>


<p>I've been looking around to see if there are any open or anonymised retail data sets to play around with but all I've come across is the '<a href="http://fimi.ua.ac.be/data/">Frequent Itemset Mining Dataset Repository</a>'. Unfortunately when I tried to open the files they seem to just contain random numbers so I must be doing something wrong.</p>


<p>If anyone knows of a retail data set I can play around with please point me in the right direction.</p>

