+++
draft = false
date="2014-12-07 19:29:01"
title="R: String to Date or NA"
tag=['r-2', 'rstats']
category=['R']
+++

<p>I've been trying to clean up a CSV file which contains some rows with dates and some not - I only want to keep the cells which do have dates so I've been trying to work out how to do that.</p>


<p>My first thought was that I'd try and find a function which would convert the contents of the cell into a date if it was in date format and NA if not. I could then filter out the NA values using the <cite><a href="http://www.statmethods.net/input/missingdata.html">is.na</a></cite> function.</p>


<p>I started out with the <cite><a href="http://www.statmethods.net/input/dates.html">as.Date</a></cite> function...</p>




~~~r

> as.Date("2014-01-01")
[1] "2014-01-01"

> as.Date("foo")
Error in charToDate(x) : 
  character string is not in a standard unambiguous format
~~~

<p>...but that throws an error if we have a non date value so it's not so useful in this case.</p>


<p>Instead we can make use of the <cite><a href="http://stackoverflow.com/questions/14755425/what-are-the-standard-unambiguous-date-formats">strptime</a></cite> function which does exactly what we want:</p>



~~~r

> strptime("2014-01-01", "%Y-%m-%d")
[1] "2014-01-01 GMT"

> strptime("foo", "%Y-%m-%d")
[1] NA
~~~

<p>We can then feed those values into <cite>is.na</cite>..
</p>



~~~r

> strptime("2014-01-01", "%Y-%m-%d") %>% is.na()
[1] FALSE

> strptime("foo", "%Y-%m-%d") %>% is.na()
[1] TRUE
~~~

<p>...and we have exactly the behaviour we were looking for.</p>

