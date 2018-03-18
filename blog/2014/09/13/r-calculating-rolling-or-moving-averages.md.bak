+++
draft = false
date="2014-09-13 08:15:26"
title="R: Calculating rolling or moving averages"
tag=['r-2', 'rstats']
category=['R']
+++

<p>I've been playing around with some time series data in R and since there's a bit of variation between consecutive points I wanted to smooth the data out by calculating the moving average.</p>


<p>I struggled to find an in built function to do this but came across <a href="http://druedin.com/2012/08/11/moving-averages-in-r/">Didier Ruedin's blog post</a> which described the following function to do the job:</p>



~~~r

mav <- function(x,n=5){filter(x,rep(1/n,n), sides=2)}
~~~

<p>I tried plugging in some numbers to understand how it works:</p>



~~~r

> mav(c(4,5,4,6), 3)
Time Series:
Start = 1 
End = 4 
Frequency = 1 
[1]       NA 4.333333 5.000000       NA
~~~

<p>Here I was trying to do a rolling average which took into account the last 3 numbers so I expected to get just two numbers back - 4.333333 and 5 - and if there were going to be NA values I thought they'd be at the beginning of the sequence.</p>


<p>In fact it turns out this is what the 'sides' parameter controls:</p>



~~~text

sides	
for convolution filters only. If sides = 1 the filter coefficients are for past values only; if sides = 2 they 
are centred around lag 0. In this case the length of the filter should be odd, but if it is even, more of the 
filter is forward in time than backward.
~~~

<p>So in our 'mav' function the rolling average looks both sides of the current value rather than just at past values. We can tweak that to get the behaviour we want:</p>



~~~r

mav <- function(x,n=5){filter(x,rep(1/n,n), sides=1)}
~~~


~~~r

> mav(c(4,5,4,6), 3)
Time Series:
Start = 1 
End = 4 
Frequency = 1 
[1]       NA       NA 4.333333 5.000000
~~~

<p>The NA values are annoying for any plotting we want to do so let's get rid of them:</p>



~~~r

> na.omit(mav(c(4,5,4,6), 3))
Time Series:
Start = 3 
End = 4 
Frequency = 1 
[1] 4.333333 5.000000
~~~

<p>Having got to this point I noticed that Didier had referenced the <a href="http://cran.r-project.org/web/packages/zoo/index.html">zoo</a> package in the comments and it has a built in function to take care of all this:</p>



~~~r

> library(zoo)
> rollmean(c(4,5,4,6), 3)
[1] 4.333333 5.000000
~~~

<p>I also realised I can list all the functions in a package with the 'ls' function so I'll be scanning zoo's list of functions next time I need to do something time series related - there'll probably already be a function for it!</p>



~~~r

> ls("package:zoo")
  [1] "as.Date"              "as.Date.numeric"      "as.Date.ts"          
  [4] "as.Date.yearmon"      "as.Date.yearqtr"      "as.yearmon"          
  [7] "as.yearmon.default"   "as.yearqtr"           "as.yearqtr.default"  
 [10] "as.zoo"               "as.zoo.default"       "as.zooreg"           
 [13] "as.zooreg.default"    "autoplot.zoo"         "cbind.zoo"           
 [16] "coredata"             "coredata.default"     "coredata<-"          
 [19] "facet_free"           "format.yearqtr"       "fortify.zoo"         
 [22] "frequency<-"          "ifelse.zoo"           "index"               
 [25] "index<-"              "index2char"           "is.regular"          
 [28] "is.zoo"               "make.par.list"        "MATCH"               
 [31] "MATCH.default"        "MATCH.times"          "median.zoo"          
 [34] "merge.zoo"            "na.aggregate"         "na.aggregate.default"
 [37] "na.approx"            "na.approx.default"    "na.fill"             
 [40] "na.fill.default"      "na.locf"              "na.locf.default"     
 [43] "na.spline"            "na.spline.default"    "na.StructTS"         
 [46] "na.trim"              "na.trim.default"      "na.trim.ts"          
 [49] "ORDER"                "ORDER.default"        "panel.lines.its"     
 [52] "panel.lines.tis"      "panel.lines.ts"       "panel.lines.zoo"     
 [55] "panel.plot.custom"    "panel.plot.default"   "panel.points.its"    
 [58] "panel.points.tis"     "panel.points.ts"      "panel.points.zoo"    
 [61] "panel.polygon.its"    "panel.polygon.tis"    "panel.polygon.ts"    
 [64] "panel.polygon.zoo"    "panel.rect.its"       "panel.rect.tis"      
 [67] "panel.rect.ts"        "panel.rect.zoo"       "panel.segments.its"  
 [70] "panel.segments.tis"   "panel.segments.ts"    "panel.segments.zoo"  
 [73] "panel.text.its"       "panel.text.tis"       "panel.text.ts"       
 [76] "panel.text.zoo"       "plot.zoo"             "quantile.zoo"        
 [79] "rbind.zoo"            "read.zoo"             "rev.zoo"             
 [82] "rollapply"            "rollapplyr"           "rollmax"             
 [85] "rollmax.default"      "rollmaxr"             "rollmean"            
 [88] "rollmean.default"     "rollmeanr"            "rollmedian"          
 [91] "rollmedian.default"   "rollmedianr"          "rollsum"             
 [94] "rollsum.default"      "rollsumr"             "scale_x_yearmon"     
 [97] "scale_x_yearqtr"      "scale_y_yearmon"      "scale_y_yearqtr"     
[100] "Sys.yearmon"          "Sys.yearqtr"          "time<-"              
[103] "write.zoo"            "xblocks"              "xblocks.default"     
[106] "xtfrm.zoo"            "yearmon"              "yearmon_trans"       
[109] "yearqtr"              "yearqtr_trans"        "zoo"                 
[112] "zooreg"  
~~~
