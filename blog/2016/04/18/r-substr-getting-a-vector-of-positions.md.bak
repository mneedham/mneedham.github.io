+++
draft = false
date="2016-04-18 19:49:02"
title="R: substr - Getting a vector of positions"
tag=['r-2']
category=['R']
+++

<p>
I recently found myself writing an R script to extract parts of a string based on a beginning and end index which is reasonably easy using the <cite><a href="https://stat.ethz.ch/R-manual/R-devel/library/base/html/substr.html">substr</a></cite> function:
</p>



~~~r

> substr("mark loves graphs", 0, 4)
[1] "mark"
~~~

<p>
But what if we have a vector of start and end positions?
</p>



~~~r

> substr("mark loves graphs", c(0, 6), c(4, 10))
[1] "mark"
~~~

<p>Hmmm that didn't work as I expected! It turns out we actually need to use the <cite><a href="https://stat.ethz.ch/R-manual/R-devel/library/base/html/substr.html">substring</a></cite> function instead which wasn't initially obvious to me on reading the documentation:</p>



~~~r

> substring("mark loves graphs", c(0, 6, 12), c(4, 10, 17))
[1] "mark"   "loves"  "graphs"
~~~

<p>
Easy when you know how!
</p>

