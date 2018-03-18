+++
draft = false
date="2013-01-27 02:10:10"
title="Python/numpy: Selecting specific column in 2D array"
tag=['python']
category=['Python']
+++

<p>I've been playing around with <a href="http://www.numpy.org/">numpy</a> this evening in an attempt to improve the performance of a <a href="http://en.wikipedia.org/wiki/Travelling_salesman_problem">Travelling Salesman Problem implementation</a> and I wanted to get every value in a specific column of a 2D array.</p>


<p>The array looked something like this:</p>



~~~python

>>> x = arange(20).reshape(4,5)
>>> x
array([[ 0,  1,  2,  3,  4],
       [ 5,  6,  7,  8,  9],
       [10, 11, 12, 13, 14],
       [15, 16, 17, 18, 19]])
~~~

<p>I wanted to get the values for the 2nd column of each row which would return an array containing 1, 6, 11 and 16.</p>


<p>For some reason I was expecting it to be quite complicated but in fact we can do this by <a href="http://stackoverflow.com/questions/2111163/selecting-specific-column-in-each-row-from-array">using matrix style syntax</a> like so:</p>



~~~python

>>> x[:, 1]
array([ 1,  6, 11, 16])
~~~

<p>Here we are first saying that we want to return all the rows by specifying ':'  and then the '1' indicates that we only want to return the column with index 1.</p>


<p>If we wanted to return a specific row as well then we'd specify a value before the comma and it'd be a standard 2D array value lookup:</p>



~~~python

>> x[2,1]
11
~~~

<p>or</p>



~~~python

>> x[2][1]
11
~~~
