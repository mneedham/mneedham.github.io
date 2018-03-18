+++
draft = false
date="2015-06-28 22:30:08"
title="R: dplyr - Update rows with earlier/previous rows values"
tag=['r-2']
category=['R']
+++

<p>Recently I had a data frame which contained a column which had mostly empty values:
</p>



~~~r

> data.frame(col1 = c(1,2,3,4,5), col2  = c("a", NA, NA , "b", NA))
  col1 col2
1    1    a
2    2 <NA>
3    3 <NA>
4    4    b
5    5 <NA>
~~~

<p>
I wanted to fill in the NA values with the last non NA value from that column. So I want the data frame to look like this:
</p>



~~~text

1    1    a
2    2    a
3    3    a
4    4    b
5    5    b
~~~

<p>
I spent ages searching around before I <a href="http://stackoverflow.com/questions/27207162/fill-in-na-based-on-the-last-non-na-value-for-each-group-in-r">came across the <cite>na.locf</cite> function in the zoo library</a> which does the job:
</p>



~~~r

library(zoo)
library(dplyr)

> data.frame(col1 = c(1,2,3,4,5), col2  = c("a", NA, NA , "b", NA)) %>% 
    do(na.locf(.))
  col1 col2
1    1    a
2    2    a
3    3    a
4    4    b
5    5    b
~~~

<p>
This will fill in the missing values for every column, so if we had a third column with missing values it would populate those too:
</p>



~~~r

> data.frame(col1 = c(1,2,3,4,5), col2  = c("a", NA, NA , "b", NA), col3 = c("A", NA, "B", NA, NA)) %>% 
    do(na.locf(.))

  col1 col2 col3
1    1    a    A
2    2    a    A
3    3    a    B
4    4    b    B
5    5    b    B
~~~

<p>If we only want to populate 'col2' and leave 'col3' as it is we can apply the function specifically to that column:
</p>



~~~r

> data.frame(col1 = c(1,2,3,4,5), col2  = c("a", NA, NA , "b", NA), col3 = c("A", NA, "B", NA, NA)) %>% 
    mutate(col2 = na.locf(col2))
  col1 col2 col3
1    1    a    A
2    2    a <NA>
3    3    a    B
4    4    b <NA>
5    5    b <NA>
~~~

<p>
It's quite a neat function and certainly comes in helpful when cleaning up data sets which don't tend to be as uniform as you'd hope!
</p>

