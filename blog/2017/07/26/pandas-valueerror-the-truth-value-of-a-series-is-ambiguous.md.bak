+++
draft = false
date="2017-07-26 21:41:55"
title="Pandas: ValueError: The truth value of a Series is ambiguous."
tag=['python', 'pandas', 'data-science']
category=['Data Science']
description="In this post we look at how to work around the ValueError: The truth value of a Series is ambiguous when adding a new column to a DataFrame."
+++

<p>
I've been playing around with Kaggle in my spare time over the last few weeks and came across an unexpected behaviour when trying to add a column to a dataframe.
</p>


<p>
First let's get Panda's into our program scope:
</p>


<h3>Prerequisites</h3>


~~~python

import pandas as pd
~~~

<p>
Now we'll create a data frame to play with for the duration of this post:
</p>



~~~python

>>> df = pd.DataFrame({"a": [1,2,3,4,5], "b": [2,3,4,5,6]})
>>> df
   a  b
0  5  2
1  6  6
2  0  8
3  3  2
4  1  6
~~~

<p>
Let's say we want to create a new column which returns True if either of the numbers are odd. If not then it'll return False.
</p>
 

<p>
We'd expect to see a column full of True values so let's get started. 
</p>



~~~python

>>> divmod(df["a"], 2)[1] > 0
0     True
1    False
2     True
3    False
4     True
Name: a, dtype: bool

>>> divmod(df["b"], 2)[1] > 0
0    False
1     True
2    False
3     True
4    False
Name: b, dtype: bool
~~~

<p>
So far so good. Now let's combine those two calculations together and create a new column in our data frame:
</p>



~~~python

>>> df["anyOdd"] = (divmod(df["a"], 2)[1] > 0) or (divmod(df["b"], 2)[1] > 0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/markneedham/projects/kaggle/house-prices/a/lib/python3.6/site-packages/pandas/core/generic.py", line 953, in __nonzero__
    .format(self.__class__.__name__))
ValueError: The truth value of a Series is ambiguous. Use a.empty, a.bool(), a.item(), a.any() or a.all().
~~~

<p>
Hmmm, that was unexpected! Unfortunately Python's <cite>or</cite> and <cite>and</cite> statements <a href="https://stackoverflow.com/questions/36921951/truth-value-of-a-series-is-ambiguous-use-a-empty-a-bool-a-item-a-any-o">don't work very well against Panda's Series'</a>, so instead we need to use the bitwise or (|) and and (&). 
</p>


<p>
Let's update our example:
</p>



~~~python

>>> df["anyOdd"] = (divmod(df["a"], 2)[1] > 0) | (divmod(df["b"], 2)[1] > 0)
>>> df
   a  b  anyOdd
0  1  2    True
1  2  3    True
2  3  4    True
3  4  5    True
4  5  6    True
~~~

<p>
Much better. And what about if we wanted to check if both values are odd?
</p>



~~~python

>>> df["bothOdd"] = (divmod(df["a"], 2)[1] > 0) & (divmod(df["b"], 2)[1] > 0)
>>> df
   a  b  anyOdd  bothOdd
0  1  2    True    False
1  2  3    True    False
2  3  4    True    False
3  4  5    True    False
4  5  6    True    False
~~~

<p>
Works exactly as expected, hoorah!
</p>

