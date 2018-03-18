+++
draft = false
date="2014-07-07 06:07:29"
title="R/plyr: ddply - Error in vector(type, length) : vector: cannot make a vector of mode 'closure'."
tag=['r-2']
category=['R']
+++

<p>In my continued playing around with plyr's <a href="http://www.inside-r.org/packages/cran/plyr/docs/ddply">ddply</a> function I was trying to group a data frame by one of its columns and return a count of the number of rows with specific values and ran into a strange (to me) error message.</p>


<p>I had a data frame:</p>



~~~r

n = c(2, 3, 5) 
s = c("aa", "bb", "cc") 
b = c(TRUE, FALSE, TRUE) 
df = data.frame(n, s, b) 
~~~

<p>And wanted to group and count on column 'b' so I'd get back a count of 2 for TRUE and 1 for FALSE. I wrote this code:</p>



~~~r

ddply(df, "b", function(x) { 
  countr <- length(x$n) 
  data.frame(count = count) 
})
~~~

<p>which when evaluated gave the following error:</p>



~~~r

Error in vector(type, length) : 
  vector: cannot make a vector of mode 'closure'.
~~~

<p>It took me quite a while to realise that I'd just made a typo in assigned the count to a variable called 'countr' instead of 'count'.</p>
 

<p>As a result of that typo I think the R compiler was trying to find a variable called 'count' somwhere else in the lexical scope but was unable to. If I'd defined the variable 'count' outside the call to ddply function then my typo wouldn't have resulted in an error but rather an unexpected resulte.g.</p>



~~~r

> count = 10
~~~


~~~r

> ddply(df, "b", function(x) { 
+   countr <- length(x$n) 
+   data.frame(count = count) 
+ })
      b count
1 FALSE     4
2  TRUE     4
~~~

<p>Once I spotted the typo and fixed it things worked as expected:</p>



~~~r

> ddply(df, "b", function(x) { 
+   count <- length(x$n) 
+   data.frame(count = count) 
+ })
~~~


~~~r

      b count
1 FALSE     1
2  TRUE     2
~~~
