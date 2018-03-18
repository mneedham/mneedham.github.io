+++
draft = false
date="2014-07-16 05:04:46"
title="R: Apply a custom function across multiple lists"
tag=['r-2']
category=['R']
+++

<p>In my continued playing around with <a href="http://www.r-project.org/">R</a> I wanted to map a custom function over two lists comparing each item with its corresponding items.</p>


<p>If we just want to use a built in function such as subtraction between two lists it's quite easy to do:</p>



~~~r

> c(10,9,8,7,6,5,4,3,2,1) - c(5,4,3,4,3,2,2,1,2,1)
 [1] 5 5 5 3 3 3 2 2 0 0
~~~

<p>I wanted to do a slight variation on that where instead of returning the difference I wanted to return a text value representing the difference e.g. '5 or more', '3 to 5' etc.</p>


<p>I spent a long time trying to figure out how to do that before finding <a href="http://nsaunders.wordpress.com/2010/08/20/a-brief-introduction-to-apply-in-r/">an excellent blog post which describes all the different 'apply' functions available in R</a>. </p>


<p>As far as I understand 'apply' is the equivalent of 'map' in Clojure or other functional languages.</p>


<p>In this case we want the <cite><a href="http://stat.ethz.ch/R-manual/R-patched/library/base/html/mapply.html">mapply</a></cite> variant which we can use like so:</p>



~~~r

> mapply(function(x, y) { 
    if((x-y) >= 5) {
        "5 or more"
    } else if((x-y) >= 3) {
        "3 to 5"
    } else {
        "less than 5"
    }    
  }, c(10,9,8,7,6,5,4,3,2,1),c(5,4,3,4,3,2,2,1,2,1))
 [1] "5 or more"   "5 or more"   "5 or more"   "3 to 5"      "3 to 5"      "3 to 5"      "less than 5"
 [8] "less than 5" "less than 5" "less than 5"
~~~

<p>We could then pull that out into a function if we wanted:</p>



~~~r

summarisedDifference <- function(one, two) {
  mapply(function(x, y) { 
    if((x-y) >= 5) {
      "5 or more"
    } else if((x-y) >= 3) {
      "3 to 5"
    } else {
      "less than 5"
    }    
  }, one, two)
}
~~~

<p>which we could call like so:</p>



~~~r

> summarisedDifference(c(10,9,8,7,6,5,4,3,2,1),c(5,4,3,4,3,2,2,1,2,1))
 [1] "5 or more"   "5 or more"   "5 or more"   "3 to 5"      "3 to 5"      "3 to 5"      "less than 5"
 [8] "less than 5" "less than 5" "less than 5"
~~~

<p>I also wanted to be able to compare a list of items to a single item which was much easier than I expected:</p>



~~~r

> summarisedDifference(c(10,9,8,7,6,5,4,3,2,1), 1)
 [1] "5 or more"   "5 or more"   "5 or more"   "5 or more"   "5 or more"   "3 to 5"      "3 to 5"     
 [8] "less than 5" "less than 5" "less than 5"
~~~

<p>If we wanted to get a summary of the differences between the lists we could plug them into ddply like so:</p>



~~~r

> library(plyr)
> df = data.frame(x=c(10,9,8,7,6,5,4,3,2,1), y=c(5,4,3,4,3,2,2,1,2,1))
> ddply(df, .(difference=summarisedDifference(x,y)), summarise, count=length(x))
   difference count
1      3 to 5     3
2   5 or more     3
3 less than 5     4
~~~
