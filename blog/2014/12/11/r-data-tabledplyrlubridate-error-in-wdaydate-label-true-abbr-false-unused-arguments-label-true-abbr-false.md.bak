+++
draft = false
date="2014-12-11 19:03:06"
title="R: data.table/dplyr/lubridate - Error in wday(date, label = TRUE, abbr = FALSE) :  unused arguments (label = TRUE, abbr = FALSE)"
tag=['r-2', 'rstats']
category=['R']
+++

<p>
I spent a couple of hours playing around with <a href="http://cran.r-project.org/web/packages/data.table/index.html">data.table</a> this evening and tried changing some code written using a data frame to use a data table instead.
</p>


<p>
I started off by building a data frame which contains all the weekends between 2010 and 2015...
</p>



~~~r

> library(lubridate)

> library(dplyr)

> dates = data.frame(date = seq( dmy("01-01-2010"), to=dmy("01-01-2015"), by="day" ))

> dates = dates %>% filter(wday(date, label = TRUE, abbr = FALSE) %in% c("Saturday", "Sunday"))
~~~

<p>...which works fine:</p>



~~~r

> dates %>% head()
         date
1: 2010-01-02
2: 2010-01-03
3: 2010-01-09
4: 2010-01-10
5: 2010-01-16
6: 2010-01-17
~~~

<p>
I then tried to change the code to use a data table instead which led to the following error:
</p>



~~~r

> library(data.table)

> dates = data.table(date = seq( dmy("01-01-2010"), to=dmy("01-01-2015"), by="day" ))

> dates = dates %>% filter(wday(date, label = TRUE, abbr = FALSE) %in% c("Saturday", "Sunday"))
Error in wday(date, label = TRUE, abbr = FALSE) : 
  unused arguments (label = TRUE, abbr = FALSE)
~~~

<p>
I wasn't sure what was going on so I went back to the data frame version to check if that still worked...
</p>



~~~r

> dates = data.frame(date = seq( dmy("01-01-2010"), to=dmy("01-01-2015"), by="day" ))

> dates = dates %>% filter(wday(date, label = TRUE, abbr = FALSE) %in% c("Saturday", "Sunday"))
Error in wday(c(1262304000, 1262390400, 1262476800, 1262563200, 1262649600,  : 
  unused arguments (label = TRUE, abbr = FALSE)
~~~

<p>
...except it now didn't work either! I decided to check what <cite>wday</cite> was referring to...
</p>


<blockquote>
Help on topic 'wday' was found in the following packages:

Integer based date class
(in package data.table in library /Library/Frameworks/R.framework/Versions/3.1/Resources/library)
Get/set days component of a date-time.
(in package lubridate in library /Library/Frameworks/R.framework/Versions/3.1/Resources/library)
</blockquote>

<p>
...and realised that data.table has its own wday function - I'd been caught out by R's global scoping of all the things!
</p>


<p>
We can probably work around that by the order in which we require the various libraries but for now I'm just prefixing the call to wday and all is well:
</p>



~~~r

dates = dates %>% filter(lubridate::wday(date, label = TRUE, abbr = FALSE) %in% c("Saturday", "Sunday"))
~~~
