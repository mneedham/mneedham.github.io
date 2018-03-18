+++
draft = false
date="2014-12-08 19:02:46"
title="R: dplyr - mutate with strptime (incompatible size/wrong result size)"
tag=['r-2', 'rstats']
category=['R']
+++

<p>Having worked out <a href="http://www.markhneedham.com/blog/2014/12/07/r-string-to-date-or-na/">how to translate a string into a date or NA if it wasn't the appropriate format</a> the next thing I wanted to do was store the result of the transformation in my data frame.
</p>


<p>I started off with this:</p>



~~~r

data = data.frame(x = c("2014-01-01", "2014-02-01", "foo"))
> data
           x
1 2014-01-01
2 2014-02-01
3        foo
~~~

<p>And when I tried to do the date translation ran into the following error:</p>



~~~r

> data %>% mutate(y = strptime(x, "%Y-%m-%d"))
Error: wrong result size (11), expected 3 or 1
~~~

<p>As I understand it this error is telling us that we are trying to put a value into the data frame which represents 11 rows rather than 3 rows or 1 row.</p>


<p>
It turns out that <a href="https://github.com/hadley/dplyr/issues/179">storing POSIXlts in a data frame isn't such a good idea!</a> In this case we can use the <cite>as.character</cite> function to create a character vector which can be stored in the data frame:</a>
</p>



~~~r

> data %>% mutate(y = strptime(x, "%Y-%m-%d") %>% as.character())
           x          y
1 2014-01-01 2014-01-01
2 2014-02-01 2014-02-01
3        foo       <NA>
~~~

<p>We can then get rid of the NA row by using the <cite>is.na</cite> function:</p>



~~~r

> data %>% mutate(y = strptime(x, "%Y-%m-%d") %>% as.character()) %>% filter(!is.na(y))
           x          y
1 2014-01-01 2014-01-01
2 2014-02-01 2014-02-01
~~~

<p>And a final tweak so that we have 100% pipelining goodness:</p>



~~~r

> data %>% 
    mutate(y = x %>% strptime("%Y-%m-%d") %>% as.character()) %>%
    filter(!is.na(y))
           x          y
1 2014-01-01 2014-01-01
2 2014-02-01 2014-02-01
~~~
