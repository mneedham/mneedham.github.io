+++
draft = false
date="2014-12-13 19:58:13"
title="R: Numeric representation of date time"
tag=['r-2', 'rstats']
category=['R']
+++

<p>
I've been playing around with date times in R recently and I wanted to derive a numeric representation for a given value to make it easier to see the correlation between time and another variable.
</p>


<p>
e.g. December 13th 2014 17:30 should return 17.5 since it's 17.5 hours since midnight.
</p>


<p>
Using the standard R libraries we would write the following code:
</p>



~~~r

> december13 = as.POSIXlt("2014-12-13 17:30:00")
> as.numeric(december13 - trunc(december13, "day"), units="hours")
[1] 17.5
~~~

<p>
That works pretty well but <a href="https://twitter.com/tonkouts">Antonios</a> recently introduced me to the <a href="http://cran.r-project.org/web/packages/lubridate/index.html">lubridate</a> so I thought I'd give that a try as well.
</p>


<p>The first nice thing about lubridate is that we can use the date we created earlier and call the <cite>floor_date</cite> function rather than <cite>truncate</cite>:</p>



~~~r

> (december13 - floor_date(december13, "day"))
Time difference of 17.5 hours
~~~

<p>That gives us back a <cite>difftime</cite>...</p>



~~~r

> class((december13 - floor_date(december13, "day")))
[1] "difftime"
~~~

<p>...which we can divide by different units to get the granularity we want:</p>



~~~r

> diff = (december13 - floor_date(december13, "day"))
> diff / dhours(1)
[1] 17.5

> diff / ddays(1)
[1] 0.7291667

> diff / dminutes(1)
[1] 1050
~~~

<p>
Pretty neat!</p>
 

<p>lubridate also has some nice functions for creating dates/date times. e.g.</p>

</p>



~~~r

> ymd_hms("2014-12-13 17:00:00")
[1] "2014-12-13 17:00:00 UTC"

> ymd_hm("2014-12-13 17:00")
[1] "2014-12-13 17:00:00 UTC"

> ymd_h("2014-12-13 17")
[1] "2014-12-13 17:00:00 UTC"

> ymd("2014-12-13")
[1] "2014-12-13 UTC"
~~~

<p>And if you want a different time zone that's pretty easy too:</p>



~~~r

> with_tz(ymd("2014-12-13"), "GMT")
[1] "2014-12-13 GMT"
~~~
