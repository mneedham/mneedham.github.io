+++
draft = false
date="2015-06-30 22:26:39"
title="R: write.csv - unimplemented type 'list' in 'EncodeElement'"
tag=['r-2']
category=['R']
+++

<p>
Everyone now and then I want to serialise an R data frame to a CSV file so I can easily load it up again if my R environment crashes without having to recalculate everything but recently ran into the following error:
</p>



~~~r

> write.csv(foo, "/tmp/foo.csv", row.names = FALSE)
Error in .External2(C_writetable, x, file, nrow(x), p, rnames, sep, eol,  : 
  unimplemented type 'list' in 'EncodeElement'
~~~

<p>If we take a closer look at the data frame in question it looks ok:</p>



~~~r

> foo
  col1 col2
1    1    a
2    2    b
3    3    c
~~~

<p>
However, one of the columns contains a list in each cell and we need to find out which one it is. I've found the quickest way is to run the <cite>typeof</cite> function over each column:
</p>



~~~r

> typeof(foo$col1)
[1] "double"

> typeof(foo$col2)
[1] "list"
~~~

<p>So 'col2' is the problem one which isn't surprising if you consider the way I created 'foo':</p>



~~~r

library(dplyr)
foo = data.frame(col1 = c(1,2,3)) %>% mutate(col2 = list("a", "b", "c"))
~~~

<p>
If we do have a list that we want to add to the data frame we need to convert it to a vector first so we don't run into this type of problem:
</p>



~~~R

foo = data.frame(col1 = c(1,2,3)) %>% mutate(col2 = list("a", "b", "c") %>% unlist())
~~~

<p>And now we can write to the CSV file:</p>



~~~r

write.csv(foo, "/tmp/foo.csv", row.names = FALSE)
~~~


~~~bash

$ cat /tmp/foo.csv
"col1","col2"
1,"a"
2,"b"
3,"c"
~~~

<p>
And that's it!
</p>

