+++
draft = false
date="2013-01-23 22:34:01"
title="R: Filter a data frame based on values in two columns"
tag=['r-2']
category=['R']
+++

<p>In the most recent assignment of the <a href="https://www.coursera.org/course/compdata">Computing for Data Analysis</a> course we had to filter a data frame which contained N/A values in two columns to only return rows which had no N/A's.</p>


<p>I started with a data frame that looked like this:</p>



~~~r

> data <- read.csv("specdata/002.csv") 
> # we'll just use a few rows to make it easier to see what's going on
> data[2494:2500,]
           Date sulfate nitrate ID
2494 2007-10-30    3.25   0.902  2
2495 2007-10-31      NA      NA  2
2496 2007-11-01      NA      NA  2
2497 2007-11-02    6.56   1.270  2
2498 2007-11-03      NA      NA  2
2499 2007-11-04      NA      NA  2
2500 2007-11-05    6.10   0.772  2
~~~

<p>We want to only return the rows which have a value in both the 'sulfate' and the 'nitrate' columns.</p>


<p>I initially tried to use the <cite><a href="http://www.r-bloggers.com/filtering-a-list-with-the-filter-higher-order-function/">Filter</a></cite> function but wasn't very successful:</p>



~~~r

> smallData <- data[2494:2500,]
> Filter(function(x) !is.na(x$sulfate), smallData)
Error in x$sulfate : $ operator is invalid for atomic vectors
~~~

<p>I'm not sure that <cite>Filter</cite> is designed to filter data frames - it seems more appropriate for lists or vectors - so I ended up filtering the data frame using what I think is called an extract operation:</p>



~~~r

> smallData[!is.na(smallData$sulfate) & !is.na(smallData$nitrate),]
           Date sulfate nitrate ID
2494 2007-10-30    3.25   0.902  2
2497 2007-11-02    6.56   1.270  2
2500 2007-11-05    6.10   0.772  2
~~~

<p>The code inside the square brackets returns a collection indicating whether or not we should return each row:</p>



~~~r

> !is.na(smallData$sulfate) & !is.na(smallData$nitrate)
[1]  TRUE FALSE FALSE  TRUE FALSE FALSE  TRUE
~~~

<p>which is equivalent to doing this:</p>



~~~r

> smallData[c(TRUE, FALSE, FALSE, TRUE, FALSE, FALSE, TRUE),]
           Date sulfate nitrate ID
2494 2007-10-30    3.25   0.902  2
2497 2007-11-02    6.56   1.270  2
2500 2007-11-05    6.10   0.772  2
~~~

<p>We put a comma after the list of true/false values to indicate that we want to return all the columns otherwise we'd get this error:</p>



~~~r

> smallData[c(TRUE, FALSE, FALSE, TRUE, FALSE, FALSE, TRUE)]
Error in `[.data.frame`(smallData, c(TRUE, FALSE, FALSE, TRUE, FALSE,  : 
  undefined columns selected
~~~

<p>We could filter the columns as well if we wanted to:</p>



~~~r

> smallData[c(TRUE, FALSE, FALSE, TRUE, FALSE, FALSE, TRUE), c(1,2)]
           Date sulfate
2494 2007-10-30    3.25
2497 2007-11-02    6.56
2500 2007-11-05    6.10
~~~

<p>As is no doubt obvious, I don't know much R so if there's a better way to do anything please let me know.</p>


<p>The <a href="https://github.com/mneedham/dataanalysis/blob/master/week2/complete.R">full code is on github</a> if you're interested in seeing it in context.</p>

