+++
draft = false
date="2014-11-08 22:29:01"
title="R: dplyr - Group by field dynamically ('regroup' is deprecated / no applicable method for 'as.lazy' applied to an object of class \"list\" )"
tag=['r-2']
category=['R']
+++

<p>A few months ago I wrote a blog <a href="http://www.markhneedham.com/blog/2014/08/29/r-dplyr-group_by-dynamic-or-programmatic-field-variable-error-index-out-of-bounds/">explaining how to dynamically/programatically group a data frame by a field using dplyr</a> but that approach has been deprecated in the latest version.</p>


<p>To recap, the original function looked like this:</p>



~~~r

library(dplyr)

groupBy = function(df, field) {
  df %.% regroup(list(field)) %.% summarise(n = n())
}
~~~

<p>And if we execute that with a sample data frame we'll see the following:</p>



~~~r

> data = data.frame(
      letter = sample(LETTERS, 50000, replace = TRUE),
      number = sample (1:10, 50000, replace = TRUE)
  )

> groupBy(data, 'letter') %>% head(5)
Source: local data frame [5 x 2]

  letter    n
1      A 1951
2      B 1903
3      C 1954
4      D 1923
5      E 1886
Warning messages:
1: %.% is deprecated. Please use %>% 
2: %.% is deprecated. Please use %>% 
3: 'regroup' is deprecated.
Use 'group_by_' instead.
See help("Deprecated") 
~~~

<p>I replaced each of the deprecated operators and ended up with this function:</p>



~~~r

groupBy = function(df, field) {
  df %>% group_by_(list(field)) %>% summarise(n = n())
}
~~~

<p>Now if we run that:</p>



~~~r

> groupBy(data, 'letter') %>% head(5)
Error in UseMethod("as.lazy") : 
  no applicable method for 'as.lazy' applied to an object of class "list"
~~~

<p>It turns out the 'group_by_' function doesn't want to receive a list of fields so let's remove the call to <cite>list</cite>:</p>



~~~r

groupBy = function(df, field) {
  df %>% group_by_(field) %>% summarise(n = n())
}
~~~

<p>And now if we run that:</p>



~~~r

> groupBy(data, 'letter') %>% head(5)
Source: local data frame [5 x 2]

  letter    n
1      A 1951
2      B 1903
3      C 1954
4      D 1923
5      E 1886
~~~

<p>Good times! We get the correct result and no deprecation messages.</p>


<p>If we want to group by multiple fields we can just pass in the field names like so:</p>



~~~r

groupBy = function(df, field1, field2) {
  df %>% group_by_(field1, field2) %>% summarise(n = n())
}
~~~


~~~r

> groupBy(data, 'letter', 'number') %>% head(5)
Source: local data frame [5 x 3]
Groups: letter

  letter number   n
1      A      1 200
2      A      2 218
3      A      3 205
4      A      4 176
5      A      5 203
~~~

<p>Or with this simpler version:</p>



~~~r

groupBy = function(df, ...) {
  df %>% group_by_(...) %>% summarise(n = n())
}
~~~


~~~r

> groupBy(data, 'letter', 'number') %>% head(5)
Source: local data frame [5 x 3]
Groups: letter

  letter number   n
1      A      1 200
2      A      2 218
3      A      3 205
4      A      4 176
5      A      5 203
~~~

<p>I realised that we can actually just use the <cite>group_by</cite> itself and pass in the field names without quotes, something I couldn't get to work in earlier versions:</p>



~~~r

groupBy = function(df, ...) {
  df %>% group_by(...) %>% summarise(n = n())
}
~~~


~~~r

> groupBy(data, letter, number) %>% head(5)
Source: local data frame [5 x 3]
Groups: letter

  letter number   n
1      A      1 200
2      A      2 218
3      A      3 205
4      A      4 176
5      A      5 203
~~~

<p>We could even get a bit of pipelining going on if we fancied it:</p>



~~~r

> data %>% groupBy(letter, number) %>% head(5)
Source: local data frame [5 x 3]
Groups: letter

  letter number   n
1      A      1 200
2      A      2 218
3      A      3 205
4      A      4 176
5      A      5 203
~~~

<p>And <a href="http://blog.rstudio.org/2014/10/13/dplyr-0-3-2/">as of dplyr 0.3</a> we can simplify our groupBy function to make use of the new <cite>count</cite> function which combines <cite>group_by</cite> and <cite>summarise</cite>:</p>



~~~r

groupBy = function(df, ...) {
  df %>% count(...)
}
~~~


~~~r

> data %>% groupBy(letter, number) %>% head(5)
Source: local data frame [5 x 3]
Groups: letter

  letter number   n
1      A      1 200
2      A      2 218
3      A      3 205
4      A      4 176
5      A      5 203
~~~
