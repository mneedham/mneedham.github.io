+++
draft = false
date="2012-09-30 19:47:32"
title="neo4j: Handling SUM's scientific notation"
tag=['neo4j', 'cypher']
category=['neo4j']
+++

In some of the recent work I've been doing with neo4j the queries I've written have been summing up the values from multiple nodes and after a certain number is reached the value returned used scientific notation.

For example in a cypher query like this:


~~~text

START category = node:categories('category_id:1') 
MATCH p = category-[:has_child*1..5]->subCategory-[:has_product]->product-[:sold]->sales 
RETURN EXTRACT(n in NODES(p) : n.category_id?),subCategory.category_id, SUM(sales.sales)
~~~

I might get a result set like this:


~~~text

+------------------------------------------------------------------------------------------------+
| EXTRACT(n in NODES(p) : n.category_id?)        | subCategory.category_id  | SUM(sales.sales)   |
+------------------------------------------------------------------------------------------------+
| ["246","254","255","3279",<null>,<null>]       | "3279"                   | 3.07213e07         |
| ["246","3649","3650","4362",<null>,<null>]     | "4362"                   | 1.023412e06        |
| ["246","287","291","308",<null>,<null>]        | "308"                    | 504712.5999448135  |
+------------------------------------------------------------------------------------------------+
~~~

I wanted to be able to add the first two rows together but still have them return separately which meant I needed to convert the values into decimal notation in order to do so.

I came across <a href="http://stackoverflow.com/questions/8586357/how-to-convert-a-scientific-notation-string-to-decimal-notation">a Stack Overflow thread explaining how to do it in Ruby</a>:


~~~ruby

> "%f" % "3.07213e07"
=> "30721300.000000"
~~~

or


~~~ruby

> "3.07213e07".to_f
=> 30721300.0
~~~

If we want to <a href="http://www.coderanch.com/t/417237/java/java/format-scientific-notation-double-non">do the same thing in Java</a> it'd read like this:


~~~java

double d = Double.parseDouble("3.07213e07");
NumberFormat formatter = new DecimalFormat("###.#####");
String f = formatter.format(d);
System.out.println(f);
// returns 30721300
~~~

I couldn't see a way to make the SUM function return in decimal notation but it'd be neat if there was a way to. 

For now we have to apply some formatting on the result if we want to do any calculations with it.
