+++
draft = false
date="2013-02-03 10:40:48"
title="R: Mapping over a list of lists"
tag=['r-2']
category=['R']
+++

<p>As part of the coursera <a href="https://class.coursera.org/dataanalysis-001/class/index">Data Analysis</a> course I had the following code to download and then read in a file:</p>



~~~r

> file <- "https://dl.dropbox.com/u/7710864/data/csv_hid/ss06hid.csv"
> download.file(file, destfile="americancommunity.csv", method="curl")
> acomm <- read.csv("americancommunity.csv")
~~~

<p>We then had to filter the data based on the values in a couple of columns and work out how many rows were returned in each case:</p>



~~~r

> one <- acomm[acomm$RMS == 4 & !is.na(acomm$RMS) 
               & acomm$BDS == 3 & !is.na(acomm$BDS), c("RMS")]
> one
  [1] 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4
...
[137] 4 4 4 4 4 4 4 4 4 4 4 4
> two <- acomm[acomm$RMS == 5 & !is.na(acomm$RMS) 
               & acomm$BDS == 2 & !is.na(acomm$BDS), c("RMS")]
> two
  [1] 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
...
[375] 5 5 5 5 5 5 5 5 5 5 5 5

> three <- acomm[acomm$RMS == 7 & !is.na(acomm$RMS) 
                 & acomm$BDS == 2 & !is.na(acomm$BDS), c("RMS")]
> three
 [1] 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7
[36] 7 7 7 7 7 7 7 7 7 7 7 7 7 7

~~~

<p>So I needed to know how many values were in the variables <cite>one</cite>, <cite>two</cite> and <cite>three</cite>.</p>


<p>I thought I could probably put those lists into another list and then use <cite><a href="http://www.math.montana.edu/Rweb/Rhelp/apply.html">apply</a></cite> or one of its variants to get the length of each one. 

<p>I usually use the <cite><a href="http://www.math.montana.edu/Rweb/Rhelp/c.html">c</a></cite> function to help me create lists but it's not helpful in this case as it creates one massive vector with all the values concatenated together:</p>


<p>Calling apply doesn't have the intended outcome:</p>



~~~r

> lapply(c(one, two, three), length)
...
[[582]]
[1] 1

[[583]]
[1] 1
~~~

<p>Instead what we need is the <cite><a href="http://www.math.montana.edu/Rweb/Rhelp/list.html">list</a></cite> function:</p>



~~~r

> lapply(list(one, two, three), length)
[[1]]
[1] 148

[[2]]
[1] 386

[[3]]
[1] 49
~~~

<p>Et voila!</p>


<p>The <a href="https://github.com/mneedham/dataanalysis2/blob/master/week2.R">code is on github</a> as usual.</p>

