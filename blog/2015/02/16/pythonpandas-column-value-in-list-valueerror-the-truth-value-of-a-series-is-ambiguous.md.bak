+++
draft = false
date="2015-02-16 21:39:16"
title="Python/pandas: Column value in list (ValueError: The truth value of a Series is ambiguous.)"
tag=['python']
category=['Python']
+++

<p>I've been using Python's <a href="http://pandas.pydata.org/">pandas</a> library while exploring some CSV files and although for the most part I've found it intuitive to use, I had trouble filtering a data frame based on checking whether a column value was in a list.
</p>


<p>A subset of one of the CSV files I've been working with looks like this:</p>



~~~python

$ cat foo.csv
"Foo"
1
2
3
4
5
6
7
8
9
10
~~~

<p>Loading it into a pandas data frame is reasonably simple:</p>



~~~python

import pandas as pd
df = pd.read_csv('foo.csv', index_col=False, header=0)
>>> df
   Foo
0    1
1    2
2    3
3    4
4    5
5    6
6    7
7    8
8    9
9   10
~~~

<p>
If we want to find the rows which have a value of 1 we'd write the following:
</p>



~~~python

>>> df[df["Foo"] == 1]
   Foo
0    1
~~~

<p>
Finding the rows with a value less than 7 is as you'd expect too:
</p>



~~~python

>>> df[df["Foo"] < 7]
   Foo
0    1
1    2
2    3
3    4
4    5
5    6
~~~

<p>Next I wanted to filter out the rows containing odd numbers which I initially tried to do like this:</p>



~~~python

odds = [i for i in range(1,10) if i % 2 <> 0]
>>> odds
[1, 3, 5, 7, 9]

>>> df[df["Foo"] in odds]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/markneedham/projects/neo4j-himym/himym/lib/python2.7/site-packages/pandas/core/generic.py", line 698, in __nonzero__
    .format(self.__class__.__name__))
ValueError: The truth value of a Series is ambiguous. Use a.empty, a.bool(), a.item(), a.any() or a.all().
~~~

<p>Unfortunately that doesn't work and I couldn't get any of the suggestions from the error message to work either. Luckily pandas has a special <cite><a href="http://pandas.pydata.org/pandas-docs/dev/generated/pandas.DataFrame.isin.html">isin</a></cite> function for this use case which we can call like this:
</p>



~~~python

>>> df[df["Foo"].isin(odds)]
   Foo
0    1
2    3
4    5
6    7
8    9
~~~

<p>
Much better!
</p>

