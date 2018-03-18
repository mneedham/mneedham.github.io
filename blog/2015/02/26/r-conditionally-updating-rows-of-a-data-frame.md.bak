+++
draft = false
date="2015-02-26 00:45:42"
title="R: Conditionally updating rows of a data frame"
tag=['r-2']
category=['R']
+++

<p>
In a blog post I wrote a couple of days ago about <a href="http://www.markhneedham.com/blog/2015/02/24/r-cohort-analysis-of-neo4j-meetup-members/">cohort analysis</a> I had to assign a monthNumber to each row in a data frame and started out with the following code:
</p>



~~~r

library(zoo)
library(dplyr)

monthNumber = function(cohort, date) {
  cohortAsDate = as.yearmon(cohort)
  dateAsDate = as.yearmon(date)
    
  if(cohortAsDate > dateAsDate) {
    "NA"
  } else {
    paste(round((dateAsDate - cohortAsDate) * 12), sep="")
  }
}

cohortAttendance %>% 
  group_by(row_number()) %>% 
  mutate(monthNumber = monthNumber(cohort, date)) %>%
  filter(monthNumber != "NA") %>%
  filter(monthNumber != "0") %>% 
  mutate(monthNumber = as.numeric(monthNumber)) %>% 
  arrange(monthNumber)
~~~

<p>If we time this function using <cite>system.time</cite> we'll see that it's not very snappy:</p>



~~~r

system.time(cohortAttendance %>% 
  group_by(row_number()) %>% 
  mutate(monthNumber = monthNumber(cohort, date)) %>%
  filter(monthNumber != "NA") %>%
  filter(monthNumber != "0") %>% 
  mutate(monthNumber = as.numeric(monthNumber)) %>% 
  arrange(monthNumber))

   user  system elapsed 
  1.968   0.019   2.016 
~~~

<p>
The reason for the poor performance is that we process each row of the data table individually due to the call to <cite>group_by</cite> on the second line. One way we can refactor the code is to use the <cite>ifelse</cite> which can process multiple rows at a time:
</p>



~~~r

system.time(
cohortAttendance %>% 
  mutate(monthNumber = ifelse(as.yearmon(cohort) > as.yearmon(date), 
                              paste((round(as.yearmon(date) - as.yearmon(cohort))*12), sep=""), 
                              NA)))
   user  system elapsed 
  0.026   0.000   0.026 
~~~

<p>
<a href="https://twitter.com/tonkouts">Antonios</a> suggested another approach which involves first setting every row to 'NA' and then <a href="http://stackoverflow.com/questions/8214303/conditional-replacement-of-values-in-a-data-frame">selectively updating the appropriate rows</a>. I ended up with the following code:
</p>



~~~r

cohortAttendance$monthNumber = NA

cohortAttendance$monthNumber[as.yearmon(cohortAttendance$cohort) > as.yearmon(cohortAttendance$date)] = paste((round(as.yearmon(cohortAttendance$date) - as.yearmon(cohortAttendance$cohort))*12), sep="")
~~~

<p>Let's measure that:</p>



~~~r

system.time(paste((round(as.yearmon(cohortAttendance$date) - as.yearmon(cohortAttendance$cohort))*12), sep=""))
   user  system elapsed 
  0.013   0.000   0.013 
~~~

<p>Both approaches are much quicker than my original version although this one seems to be marginally quicker than the ifelse approach.</p>


<p>Note to future Mark: try to avoid grouping by row number - there's usually a better and faster solution!
</p>

