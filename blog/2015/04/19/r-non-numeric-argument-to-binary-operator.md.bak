+++
draft = false
date="2015-04-19 23:08:45"
title="R: non-numeric argument to binary operator"
tag=['r-2']
category=['R']
+++

<p>When debugging R code, given my Java background, I often find myself trying to print out the state of variables along with an appropriate piece of text like this:
</p>



~~~r

names = c(1,2,3,4,5,6)
> print("names: " + names)
Error in "names: " + names : non-numeric argument to binary operator
~~~

<p>
We might try this next:
</p>



~~~r

> print("names: ", names)
[1] "names: "
~~~

<p>
which doesn't actually print the <cite>names</cite> variable - only the first argument to the print function is printed.
</p>


<p>
We'll find more success with the <cite><a href="https://stat.ethz.ch/R-manual/R-devel/library/base/html/paste.html">paste</a></cite> function:
</p>



~~~r

> print(paste("names: ", names))
[1] "names:  1" "names:  2" "names:  3" "names:  4" "names:  5" "names:  6"
~~~

<p>
This is an improvement but it repeats the 'names:' prefix multiple times which isn't what we want. Introducing the <cite><a href="https://stat.ethz.ch/R-manual/R-devel/library/base/html/toString.html">toString</a></cite> function gets us over the line:
</p>



~~~r

> print(paste("names: ", toString(names)))
[1] "names:  1, 2, 3, 4, 5, 6"
~~~
