+++
draft = false
date="2014-12-22 11:46:25"
title="R: Vectorising all the things"
tag=['r-2', 'rstats']
category=['R']
+++

<p>After my last post about <a href="http://www.markhneedham.com/blog/2014/12/13/r-time-tofrom-the-weekend/">finding the distance a date/time is from the weekend</a> Hadley Wickham suggested I could improve the function by vectorising it...</p>


<blockquote class="twitter-tweet" lang="en"><p><a href="https://twitter.com/markhneedham">@markhneedham</a> vectorise with pmin(pmax(dateToLookup - before, 0), pmax(after - dateToLookup, 0)) / dhours(1)</p>
&mdash; Hadley Wickham (@hadleywickham) <a href="https://twitter.com/hadleywickham/status/544122663573000192">December 14, 2014</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

<p>...so I thought I'd try and vectorise some of the other functions I've written recently and show the two versions.</p>


<p>I found the following articles useful for explaining vectorisation and why you might want to do it:</p>


<ul>
<li>
	<a href="http://www.noamross.net/blog/2014/4/16/vectorization-in-r--why.html">Vectorisation in R: Why?</a>
</li>
<li>
<a href="http://www.burns-stat.com/pages/Tutor/R_inferno.pdf">Chapters 3 and 4 of R Inferno</a>
</li>
<li>
<a href="http://nesterko.com/blog/2011/04/29/drastic-r-speed-ups-via-vectorization-and-bug-fixes/">Drastic R speed ups via vectorisation and bug fixes</a>
</li>
</ul>

<p>
Let's get started.
</p>


<h3>
Distance from the weekend
</h3>

<p>
We want to find out how many hours away from the weekend i.e. nearest Saturday/Sunday a particular date/time is. We'll be using the following libraries and set of date/times:
</p>



~~~r

library(dplyr)
library(lubridate)
library(geosphere)
options("scipen"=100, "digits"=4)

times = ymd_hms("2002-01-01 17:00:00") + c(0:99) * hours(1)
data = data.frame(time = times)
~~~


~~~r

> data %>% head()
                 time
1 2002-01-01 17:00:00
2 2002-01-01 18:00:00
3 2002-01-01 19:00:00
4 2002-01-01 20:00:00
5 2002-01-01 21:00:00
6 2002-01-01 22:00:00
~~~

<p>Let's have a look at the non vectorised version first:</p>



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
~~~

<p>Now let's run it against our data frame:</p>



~~~r

> system.time(
    data %>% mutate(ind = row_number()) %>% group_by(ind) %>% mutate(dist = distanceFromWeekend(time))  
    )
   user  system elapsed 
  1.837   0.020   1.884 
~~~

<p>And now for Hadley's vectorised version:</p>



~~~r

distanceFromWeekendVectorised = function(dateToLookup) {
  before = floor_date(dateToLookup, "week") + hours(23) + minutes(59) + seconds(59)
  after  = ceiling_date(dateToLookup, "week") - days(1)
  pmin(pmax(dateToLookup - before, 0), pmax(after - dateToLookup, 0)) / dhours(1)
}

> system.time(data %>% mutate(dist = distanceFromWeekendVectorised(time)))
   user  system elapsed 
  0.020   0.001   0.023 
~~~

<h3>
Extracting start date
</h3>

<p>
My next example was from <a href="http://www.markhneedham.com/blog/2014/12/09/r-cleaning-up-plotting-google-trends-data/">cleaning up Google Trends data</a> and extracting the start date from a cell inside a CSV file.
</p>


<p>
We'll use this data frame:
</p>



~~~r

googleTrends = read.csv("/Users/markneedham/Downloads/report.csv", row.names=NULL)
names(googleTrends) = c("week", "score")
~~~


~~~r

> googleTrends %>% head(10)
                        week score
1  Worldwide; 2004 - present      
2         Interest over time      
3                       Week neo4j
4    2004-01-04 - 2004-01-10     0
5    2004-01-11 - 2004-01-17     0
6    2004-01-18 - 2004-01-24     0
7    2004-01-25 - 2004-01-31     0
8    2004-02-01 - 2004-02-07     0
9    2004-02-08 - 2004-02-14     0
10   2004-02-15 - 2004-02-21     0
~~~

<p>The non vectorised version looked like this:</p>



~~~r

> system.time(
    googleTrends %>% 
      mutate(ind = row_number()) %>% 
      group_by(ind) %>%
      mutate(dates = strsplit(week, " - "),
             start = dates[[1]][1] %>% strptime("%Y-%m-%d") %>% as.character())
    )
   user  system elapsed 
  0.215   0.000   0.214
~~~

<p>
In this case it's actually not possible to vectorise the code using the <cite><a href="http://stackoverflow.com/questions/3054612/r-strsplit-and-vectorization">strsplit</a></cite> so we need to use something else. <a href="https://twitter.com/tonkouts">Antonios</a> showed me how to do so using <cite>substr</cite>:
</p>



~~~r

> system.time(googleTrends %>% mutate(start = substr(week, 1, 10) %>% ymd()))
   user  system elapsed 
  0.018   0.000   0.017 
~~~

<h3>
Calculating haversine distance
</h3>

<p>I wanted to work out the great circular distance from a collection of venues to a centre point in London. I started out with this data frame:</p>



~~~r

centre = c(-0.129581, 51.516578)
venues = read.csv("/tmp/venues.csv")

> venues %>% head()
                       venue   lat      lon
1              Skills Matter 51.52 -0.09911
2                   Skinkers 51.50 -0.08387
3          Theodore Bullfrog 51.51 -0.12375
4 The Skills Matter eXchange 51.52 -0.09923
5               The Guardian 51.53 -0.12234
6            White Bear Yard 51.52 -0.10980
~~~

<p>My non vectorised version looked like this:</p>



~~~r

> system.time(venues %>% 
    mutate(distanceFromCentre = by(venues, 1:nrow(venues), function(row) { distHaversine(c(row$lon, row$lat), centre)  }))
    )
   user  system elapsed 
  0.034   0.000   0.033 
~~~

<p>
It's pretty quick but we can do better - the <cite>distHaversine</cite> function allows us to calculate multiple distances if the first argument ot it is a matrix of lon/lat values rather than a vector: 
</p>



~~~r

> system.time(
    venues %>% mutate(distanceFromCentre = distHaversine(cbind(venues$lon, venues$lat), centre))
    )
   user  system elapsed 
  0.001   0.000   0.001 
~~~

<h3>One I can't figure out...</h3>

<p>
And finally I have a function which I can't figure out how to vectorise but maybe someone with more R skillz than me can?
</p>



<p>
I have a data frame containing the <a href="https://gist.github.com/mneedham/6ec5651f0402fd4ca22e">cumulative member counts of various NoSQL London groups</a>:
</p>



~~~r

cumulativeMeetupMembers = read.csv("/tmp/cumulativeMeetupMembers.csv")
> cumulativeMeetupMembers %>% sample_n(10)
                               g.name dayMonthYear    n
4734            Hadoop Users Group UK   2013-10-26 1144
4668            Hadoop Users Group UK   2013-08-03  979
4936            Hadoop Users Group UK   2014-07-31 1644
5150                      Hive London   2012-10-15  109
8020        Neo4j - London User Group   2014-03-15  826
7666        Neo4j - London User Group   2012-08-06   78
1030                  Big Data London   2013-03-01 1416
6500        London MongoDB User Group   2013-09-21  952
8290 Oracle Big Data 4 the Enterprise   2012-06-04   61
2584              Data Science London   2012-03-20  285
~~~

<p>
And I want to find out the number of members for a group on a specific date. e.g. given the following data...
</p>



~~~r

> cumulativeMeetupMembers %>% head(10)
                                          g.name dayMonthYear  n
1  Big Data / Data Science / Data Analytics Jobs   2013-01-29  1
2  Big Data / Data Science / Data Analytics Jobs   2013-02-06 15
3  Big Data / Data Science / Data Analytics Jobs   2013-02-07 28
4  Big Data / Data Science / Data Analytics Jobs   2013-02-10 31
5  Big Data / Data Science / Data Analytics Jobs   2013-02-18 33
6  Big Data / Data Science / Data Analytics Jobs   2013-03-27 38
7  Big Data / Data Science / Data Analytics Jobs   2013-04-16 41
8  Big Data / Data Science / Data Analytics Jobs   2013-07-17 53
9  Big Data / Data Science / Data Analytics Jobs   2013-08-28 58
10 Big Data / Data Science / Data Analytics Jobs   2013-11-11 63
~~~

<p>...the number of members for the 'Big Data / Data Science / Data Analytics Jobs' group on the 10th November 2013 should be 58.</p>


<p>
I created this data frame of groups and random dates:
</p>



~~~R

dates = ymd("2014-09-01") + c(0:9) * weeks(1)
groups = cumulativeMeetupMembers %>% distinct(g.name) %>% select(g.name)

groupsOnDate = merge(dates, groups)
names(groupsOnDate) = c('date', 'name')

> groupsOnDate %>% sample_n(10)
          date                                            name
156 2014-10-06                                 GridGain London
153 2014-09-15                                 GridGain London
70  2014-11-03                                Couchbase London
185 2014-09-29                           Hadoop Users Group UK
105 2014-09-29                             Data Science London
137 2014-10-13            Equal Experts Technical Meetup Group
360 2014-11-03                        Scale Warriors of London
82  2014-09-08 Data Science & Business Analytics London Meetup
233 2014-09-15                 London ElasticSearch User Group
84  2014-09-22 Data Science & Business Analytics London Meetup
~~~

<p>The non vectorised version looks like this:</p>



~~~r

memberCount = function(meetupMembers) {
  function(groupName, date) {
    (meetupMembers %>% 
       filter(g.name == groupName & dayMonthYear < date) %>% do(tail(., 1)))$n    
  }  
} 

findMemberCount = memberCount(cumulativeMeetupMembers)

> system.time(groupsOnDate %>% mutate(groupMembers = by(groupsOnDate, 1:nrow(groupsOnDate), function(row) { 
          findMemberCount(row$name, as.character(row$date))
        }) %>% 
        cbind() %>% 
        as.vector() ))
   user  system elapsed 
  2.259   0.005   2.269 
~~~

<p>The output looks like this:</p>



~~~R

          date                                     name groupMembers
116 2014-10-06                      DeNormalised London          157
322 2014-09-08                 OpenCredo Tech Workshops            7
71  2014-09-01                  Data Enthusiasts London             
233 2014-09-15          London ElasticSearch User Group          614
171 2014-09-01 HPC & GPU Supercomputing Group of London           80
109 2014-10-27                      Data Science London         3632
20  2014-11-03            Big Data Developers in London          708
42  2014-09-08              Big Data Week London Meetup           96
127 2014-10-13          Enterprise Search London Meetup          575
409 2014-10-27                            Women in Data          548
~~~

<p>I've tried many different approaches but haven't been able to come up with a version that lets me pass in all the rows to <cite>memberCount</cite> and calculate the count for each row in one go.</p>


<p>Any ideas/advice/hints welcome!</p>

