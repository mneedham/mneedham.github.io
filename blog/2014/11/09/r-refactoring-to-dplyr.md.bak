+++
draft = false
date="2014-11-09 00:11:48"
title="R: Refactoring to dplyr"
tag=['r-2']
category=['R']
+++

<p>I've been looking back over some of the early code I wrote using R before I knew about the <a href="http://cran.r-project.org/web/packages/dplyr/vignettes/introduction.html">dplyr</a> library and thought it'd be an interesting exercise to refactor some of the snippets.</p>


<p>We'll use the following data frame for each of the examples:</p>



~~~r

library(dplyr)

data = data.frame(
  letter = sample(LETTERS, 50000, replace = TRUE),
  number = sample (1:10, 50000, replace = TRUE)
  )
~~~

<h3>Take {n} rows</h3> 


~~~r

> data[1:5,]
  letter number
1      R      7
2      Q      3
3      B      8
4      R      3
5      U      2
~~~

<p>becomes:</p>



~~~r

> data %>% head(5)
  letter number
1      R      7
2      Q      3
3      B      8
4      R      3
5      U      2
~~~

<h3>Order by numeric value descending</h3>


~~~r

> data[order(-(data$number)),][1:5,]
   letter number
14      H     10
17      G     10
63      L     10
66      W     10
73      R     10
~~~

<p>becomes:</p>



~~~r

> data %>% arrange(desc(number)) %>% head(5)
  letter number
1      H     10
2      G     10
3      L     10
4      W     10
5      R     10
~~~

<h3>Count number of items</h3>


~~~r

> length(data[,1])
[1] 50000
~~~

<p>becomes:</p>



~~~r

> data %>% count()
Source: local data frame [1 x 1]

      n
1 50000
~~~

<h3>Filter by column value</h3>


~~~r

> length(subset(data, number == 1)[, 1])
[1] 4928
~~~

<p>becomes:</p>



~~~r

> data %>% filter(number == 1) %>% count()
Source: local data frame [1 x 1]

     n
1 4928
~~~

<h3>Group by variable and count</h3>


~~~r

> aggregate(data, by= list(data$number), function(x) length(x))
   Group.1 letter number
1        1   4928   4928
2        2   5045   5045
3        3   5064   5064
4        4   4823   4823
5        5   5032   5032
6        6   5163   5163
7        7   4945   4945
8        8   5077   5077
9        9   5025   5025
10      10   4898   4898
~~~

<p>becomes:</p>



~~~r

> data %>% count(number)
Source: local data frame [10 x 2]

   number    n
1       1 4928
2       2 5045
3       3 5064
4       4 4823
5       5 5032
6       6 5163
7       7 4945
8       8 5077
9       9 5025
10     10 4898
~~~

<h3>Select a range of rows</h3>


~~~r

> data[4:5,]
  letter number
4      R      3
5      U      2
~~~

<p>becomes:</p>



~~~r

> data %>% slice(4:5)
  letter number
1      R      3
2      U      2
~~~

<p>There's certainly more code in some of the dplyr examples but I find it easier to remember how the dplyr code works when I come back to it and hence tend to favour that approach.</p>

