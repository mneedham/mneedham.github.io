+++
draft = false
date="2010-09-29 03:28:40"
title="Ruby: Intersection/Difference/Concatenation with collections"
tag=['ruby']
category=['Ruby']
+++

We came across a couple of situations yesterday where we wanted to perform operations on two different arrays.

My immediate thought was that there should be some methods available similar to what we have in C# which <a href="http://skillsmatter.com/podcast/open-source-dot-net/mike-wagg-mark-needham-functional-and-oo-approaches-to-c-sharp-programming">Mike Wagg and I spoke about in our talk about using functional programming techniques in C#</a>.

I was expecting to find methods with names indicating the operation they perform but in actual fact <a href="http://ruby-doc.org/core/classes/Array.html#M002209">the methods are more like operators</a> which makes for code that reads really well.

<h3>Intersection</h3>

This is useful when we have two collections and want to find the elements that exist in both of them.

In the world of C# we have an 'Intersect' method available as part of the LINQ library:


~~~csharp

var collection1 = new int[] { 1,2,3,4 };
var collection2 = new int[] { 1,2,5,6 };
collection1.Intersect(collection2);
~~~

In Ruby we have the '&' method:


~~~ruby

ruby-1.8.7-p299 > [1,2,3,4]  & [1,2,5,6]
 => [1, 2] 
~~~

<h3>Difference</h3>

This is useful when we have two collections and want to find items which are in one collection and not in the other.

In C# we can use the 'Except' method...


~~~csharp

var collection1 = new int[] { 1,2,3,4 };
var collection2 = new int[] { 1,2 };
collection1.Except(collection2);
~~~

...whereas in Ruby we have the '-' method:


~~~ruby

ruby-1.8.7-p299 > [1,2,3,4]  - [1,2]
 => [3, 4] 
~~~

<h3>Concatenation</h3>

This is useful when we have two collections and want to join the two collections together.

In C# we'd use the 'Union' method..


~~~csharp

var collection1 = new int[] { 1,2,3 };
var collection2 = new int[] { 4,5,6 };
collection1.Union(collection2);
~~~

..and in Ruby we have the '+' method:


~~~ruby

ruby-1.8.7-p299 > [1,2,3]  + [4,5,6]
 => [1, 2, 3, 4, 5, 6] 
~~~

These methods and others on array are  <a href="http://ruby-doc.org/core/classes/Array.html#M002209">well documented on ruby-doc.org</a> 

