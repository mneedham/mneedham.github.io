+++
draft = false
date="2012-03-23 23:54:42"
title="Oracle Spatial: Querying by a point/latitude/longitude"
tag=['oracle', 'spatial']
category=['Software Development']
+++

We're using Oracle Spatial on the application I'm working on and while most of the time any spatial queries we make are done from Java code we wanted to be able to run them directly from SQL as well to verify the code was working correctly.

We normally end up forgetting how to construct a query so I thought I'd document it.

Assuming we have a table <cite>table_with_shape</cite> which has a column <cite>shape</cite> which is a polygon, if we want to check whether a lat/long value interacts with that shape we can do that with the following query:


~~~text

SELECT *
FROM table_with_shape tws
WHERE 
SDO_ANYINTERACT(tws.shape, SDO_GEOMETRY(2001, 8307, SDO_POINT_TYPE(<LongValueHere>, <LatValueHere>, NULL), NULL, NULL) ) = 'TRUE' 
~~~

The first parameter to <cite>SDO_GEOMETRY</cite> <a href="http://docs.oracle.com/cd/B19306_01/appdev.102/b14255/sdo_objrelschema.htm#i1004087">defines the type of geometry</a> which in this case is a point. 

The second parameter is the coordinate system which is 8307 since we're using the 'WGS 84 longitude/latitude' system.

The third parameter is our point and the rest of the parameters aren't interesting here so we pass null for them.
