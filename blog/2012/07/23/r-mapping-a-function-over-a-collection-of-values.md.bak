+++
draft = false
date="2012-07-23 23:25:00"
title="R: Mapping a function over a collection of values"
tag=['r-2']
category=['R']
+++

I spent a bit of Sunday playing around with R and one thing I wanted to do was map a function over a collection of values and transform each value slightly. 

I loaded my data set using the 'Import Dataset' option in <a href="http://rstudio.org/">R Studio</a> (suggested to me by <a href="https://twitter.com/roryoung">Rob</a>) which gets converted to the following function call:


~~~r

> data <-  read.csv("~/data.csv", header=T, encoding="ISO-8859")
> data
  Column1 InterestingColumn
1    Mark             12.50
2    Dave            100.00
3    John          1,231.00
~~~

<em>data.csv</em>

~~~text

Column1, InterestingColumn
Mark, 12.50
Dave, 100.00 
John, 1,231.00
~~~

<cite>data</cite> is a table with the type '3 obs. of 2 variables' in R Studio.

I was only interested in the values in the 2nd column so I selected those like this:


~~~r

> data$InterestingColumn
[1]  12.50     100.00    1,231.00
Levels:  1,231.00  100.00  12.50
~~~

I wanted to apply a function over each of the numbers and return a new list containing those transformations. 

I initially had a look at doing this with a for loop but it didn't turn out to be as easy as I'd expected and I eventually came across the <cite><a href="http://stat.ethz.ch/R-manual/R-patched/library/base/html/lapply.html">lapply</a></cite> function which allows you to apply a function over a list or vector.


~~~r

> values <- data$InterestingColumn
> lapply(values, function(x) 5000 - as.numeric(gsub("\\s|,","", x)))
[[1]]
[1] 4987.5

[[2]]
[1] 4900

[[3]]
[1] 3769
~~~

We define a function which subtracts the value in the column from 5000 since the CSV file contained derived values and I was interested in the original value.

In order to do that subtraction I needed to cast the value from the CSV file to be numeric which first involved stripping out any spaces or commas using <a href="http://stackoverflow.com/questions/5992082/how-to-remove-all-whitespace-from-a-string-in-r">gsub</a> and then casting the string using as.numeric.

If we want to have a table structure then we can use the 'by' function to do a similar thing:


~~~r

> as.table(by(data$InterestingColumn, data$Column1, function(x) 5000 - as.numeric(gsub("\\s|,","", x))))
data$Column1
  Dave   John   Mark 
4900.0 3769.0 4987.5 
~~~

I don't know enough R to know how to keep the data in exactly the same structure as we got it so if anyone can point me in the right direction that'd be cool.
