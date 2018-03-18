+++
draft = false
date="2013-01-27 02:21:39"
title="Python/numpy: Selecting values by multiple indices"
tag=['python', 'numpy']
category=['Python']
+++

<p>As I <a href="http://www.markhneedham.com/blog/2013/01/27/pythonnumpy-selecting-specific-column-in-2d-array/">mentioned in my previous post</a> I've been playing around with <a href="http://www.numpy.org/">numpy</a> and I wanted to get the values of a collection of different indices in a 2D array.</p>


<p>If we had a 2D array that looked like this:</p>



~~~python

>>> x = arange(20).reshape(4,5)
>>> x
array([[ 0,  1,  2,  3,  4],
       [ 5,  6,  7,  8,  9],
       [10, 11, 12, 13, 14],
       [15, 16, 17, 18, 19]])
~~~

<p>I knew that it was possible to retrieve the first 3 rows by using the following code:</p>



~~~python

>>> x[0:3]
array([[ 0,  1,  2,  3,  4],
       [ 5,  6,  7,  8,  9],
       [10, 11, 12, 13, 14]])
~~~

<p>What I wanted to do, however, was retrieve the 1st, 3rd and 4th rows which we can do by passing a collection to the array lookup function:</p>



~~~python

>>> x[[0,2,3]]
array([[ 0,  1,  2,  3,  4],
       [10, 11, 12, 13, 14],
       [15, 16, 17, 18, 19]])
~~~

<p>My collection of indices was actually in a tuple so I needed to use the <cite><a href="http://docs.python.org/2/library/functions.html#list">list</a></cite> function to convert it to the appropriate data structure first:</p>



~~~python

>>> x[list((0,2,3))]
array([[ 0,  1,  2,  3,  4],
       [10, 11, 12, 13, 14],
       [15, 16, 17, 18, 19]])
~~~

<p>Pretty neat!</p>

