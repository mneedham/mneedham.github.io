+++
draft = false
date="2014-12-13 20:38:22"
title="R: Time to/from the weekend"
tag=['r-2', 'rstats']
category=['R']
+++

<p>
In my last post I showed some examples using <a href="http://www.markhneedham.com/blog/2014/12/13/r-numeric-representation-of-date-time/">R's lubridate</a> package and another problem it made really easy to solve was working out how close a particular date time was to the weekend.
</p>


<p>
I wanted to write a function which would return the previous Sunday or upcoming Saturday depending on which was closer.</p>
  

<p>lubridate's <cite>floor_date</cite> and <cite>ceiling_date</cite> functions make this quite simple. </p>


<p>e.g. if we want to round the 18th December down to the beginning of the week and up to the beginning of the next week we could do the following:
</p>



~~~r

> library(lubridate)
> floor_date(ymd("2014-12-18"), "week")
[1] "2014-12-14 UTC"

> ceiling_date(ymd("2014-12-18"), "week")
[1] "2014-12-21 UTC"
~~~

<p>
For the date in the future we actually want to grab the Saturday rather than the Sunday so we'll subtract one day from that:
</p>



~~~r

> ceiling_date(ymd("2014-12-18"), "week") - days(1)
[1] "2014-12-20 UTC"
~~~

<p>
Now let's put that together into a function which finds the closest weekend for a given date:
</p>



~~~r

findClosestWeekendDay = function(dateToLookup) {
  before = floor_date(dateToLookup, "week") + hours(23) + minutes(59) + seconds(59)
  after  = ceiling_date(dateToLookup, "week") - days(1)
  if((dateToLookup - before) < (after - dateToLookup)) {
    before  
  } else {
    after  
  }
}

> findClosestWeekendDay(ymd_hms("2014-12-13 13:33:29"))
[1] "2014-12-13 UTC"

> findClosestWeekendDay(ymd_hms("2014-12-14 18:33:29"))
[1] "2014-12-14 23:59:59 UTC"

> findClosestWeekendDay(ymd_hms("2014-12-15 18:33:29"))
[1] "2014-12-14 23:59:59 UTC"

> findClosestWeekendDay(ymd_hms("2014-12-17 11:33:29"))
[1] "2014-12-14 23:59:59 UTC"

> findClosestWeekendDay(ymd_hms("2014-12-17 13:33:29"))
[1] "2014-12-20 UTC"

> findClosestWeekendDay(ymd_hms("2014-12-19 13:33:29"))
[1] "2014-12-20 UTC"
~~~

<p>
I've set the Sunday date at 23:59:59 so that I can use this date in the next step where we want to calculate how how many hours it is from the current date to the nearest weekend.
</p>


<p>I ended up with this function:</p>



~~~r

distanceFromWeekend = function(dateToLookup) {
  before = floor_date(dateToLookup, "week") + hours(23) + minutes(59) + seconds(59)
  after  = ceiling_date(dateToLookup, "week") - days(1)
  timeToBefore = dateToLookup - before
  timeToAfter = after - dateToLookup
  
  if(timeToBefore < 0 || timeToAfter < 0) {
    0  
  } else {
    if(timeToBefore < timeToAfter) {
      timeToBefore / dhours(1)
    } else {
      timeToAfter / dhours(1)
    }
  }
}

> distanceFromWeekend(ymd_hms("2014-12-13 13:33:29"))
[1] 0

> distanceFromWeekend(ymd_hms("2014-12-14 18:33:29"))
[1] 0

> distanceFromWeekend(ymd_hms("2014-12-15 18:33:29"))
[1] 18.55833

> distanceFromWeekend(ymd_hms("2014-12-17 11:33:29"))
[1] 59.55833

> distanceFromWeekend(ymd_hms("2014-12-17 13:33:29"))
[1] 58.44194

> distanceFromWeekend(ymd_hms("2014-12-19 13:33:29"))
[1] 10.44194
~~~

<p>
While this works it's quite slow when you run it over a data frame which contains a lot of rows.</p>
 

<p>There must be a clever R way of doing the same thing (perhaps using matrices) which I haven't figured out yet so if you know how to speed it up do let me know.
</p>

