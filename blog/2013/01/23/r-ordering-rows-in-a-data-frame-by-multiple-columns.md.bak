+++
draft = false
date="2013-01-23 23:09:28"
title="R: Ordering rows in a data frame by multiple columns"
tag=['r-2']
category=['R']
+++

<p>In one of the assignments of <a href="https://www.coursera.org/course/compdata">Computing for Data Analysis</a> we needed to sort a data frame based on the values in  two of the columns and then return the top value.</p>


<p>The initial data frame looked a bit like this:</p>



~~~r

> names <- c("paul", "mark", "dave", "will", "john")
> values <- c(1,4,1,2,1)
> smallData <- data.frame(name = names, value = values)
> smallData
  name value
1 paul     1
2 mark     4
3 dave     1
4 will     2
5 john     1
~~~

<p>I want to be able to <a href="http://stackoverflow.com/questions/1296646/how-to-sort-a-dataframe-by-columns-in-r">sort the data frame by value and name both in ascending order</a> so the final result should look like this:</p>



~~~text

  name value
3 dave     1
5 john     1
1 paul     1
4 will     2
2 mark     4
~~~

<p>To do that we can use the <cite><a href="http://stat.ethz.ch/R-manual/R-patched/library/base/html/order.html">order</a></cite> function which will tell us the indices of the vector in sorted order.</p>


<p>e.g. in our case</p>



~~~r

> order(c(1,4,1,2,1))
[1] 1 3 5 4 2
~~~

<p>If we pass a collection of indices to the extract operation it'll reorder the rows. e.g.</p>



~~~r

> smallData[c(5,4,3,2,1),]
  name value
5 john     1
4 will     2
3 dave     1
2 mark     4
1 paul     1
~~~

<p>In our case we wire everything together like this to sort by the second column (value):</p>



~~~r

> smallData[order(smallData[,2]),]
  name value
1 paul     1
3 dave     1
5 john     1
4 will     2
2 mark     4
~~~

<p>It's a reasonably small tweak to get it to sort first by the second column and then by the first (name) which is what we want:</p>



~~~r

> smallData[order(smallData[,2], smallData[,1]),]
  name value
3 dave     1
5 john     1
1 paul     1
4 will     2
2 mark     4
~~~

<p>If we wanted to use the column names instead of indices we'd do the following:</p>



~~~r

> smallData[order(smallData$value, smallData$name),]
  name value
3 dave     1
5 john     1
1 paul     1
4 will     2
2 mark     4
~~~

<p>We could also rewrite it using the <cite>with</cite> function if we want to reduce the code further:</p>



~~~r

> smallData[with(smallData, order(value, name)),]
  name value
3 dave     1
5 john     1
1 paul     1
4 will     2
2 mark     4
~~~

<p>As I understand it, when we use <cite>with</cite> we put <cite>smallData</cite> into the environment and evaluate the second argument to <cite>with</cite> with respect to that so in this case it allows us to refer to the column names of <cite>smallData</cite>.
