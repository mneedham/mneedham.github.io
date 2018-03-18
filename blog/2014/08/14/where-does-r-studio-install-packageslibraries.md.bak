+++
draft = false
date="2014-08-14 10:24:52"
title="Where does r studio install packages/libraries?"
tag=['r-2']
category=['R']
+++

<p>As a newbie to R I wanted to look at the source code of some of the libraries/packages that I'd installed via R Studio which I initially struggled to do as I wasn't sure where the packages had been installed.</p>


<p>I eventually came across <a href="http://stackoverflow.com/questions/15170399/changing-r-default-library-path-using-libpaths-in-rprofile-site-fails-to-work">a StackOverflow post</a> which described the <cite><a href="http://stat.ethz.ch/R-manual/R-devel/library/base/html/libPaths.html">.libPaths</a></cite> function which tells us where that is:</p>



~~~r

> .libPaths()
[1] "/Library/Frameworks/R.framework/Versions/3.1/Resources/library"
~~~

<p>If we want to see which libraries are installed we can use the <cite><a href="http://stat.ethz.ch/R-manual/R-devel/library/base/html/list.files.html">list.files</a></cite> function:</p>



~~~r

> list.files("/Library/Frameworks/R.framework/Versions/3.1/Resources/library")
 [1] "alr3"         "assertthat"   "base"         "bitops"       "boot"         "brew"        
 [7] "car"          "class"        "cluster"      "codetools"    "colorspace"   "compiler"    
[13] "data.table"   "datasets"     "devtools"     "dichromat"    "digest"       "dplyr"       
[19] "evaluate"     "foreign"      "formatR"      "Formula"      "gclus"        "ggplot2"     
[25] "graphics"     "grDevices"    "grid"         "gridExtra"    "gtable"       "hflights"    
[31] "highr"        "Hmisc"        "httr"         "KernSmooth"   "knitr"        "labeling"    
[37] "Lahman"       "lattice"      "latticeExtra" "magrittr"     "manipulate"   "markdown"    
[43] "MASS"         "Matrix"       "memoise"      "methods"      "mgcv"         "mime"        
[49] "munsell"      "nlme"         "nnet"         "openintro"    "parallel"     "plotrix"     
[55] "plyr"         "proto"        "RColorBrewer" "Rcpp"         "RCurl"        "reshape2"    
[61] "RJSONIO"      "RNeo4j"       "Rook"         "rpart"        "rstudio"      "scales"      
[67] "seriation"    "spatial"      "splines"      "stats"        "stats4"       "stringr"     
[73] "survival"     "swirl"        "tcltk"        "testthat"     "tools"        "translations"
[79] "TSP"          "utils"        "whisker"      "xts"          "yaml"         "zoo" 
~~~

<p>We can then drill into those directories to find the appropriate file - in this case I wanted to look at one of the <a href="http://cran.r-project.org/web/packages/Rook/Rook.pdf">Rook</a> examples:</p>



~~~text

$ cat /Library/Frameworks/R.framework/Versions/3.1/Resources/library/Rook/exampleApps/helloworld.R
app <- function(env){
    req <- Rook::Request$new(env)
    res <- Rook::Response$new()
    friend <- 'World'
    if (!is.null(req$GET()[['friend']]))
	friend <- req$GET()[['friend']]
    res$write(paste('<h1>Hello',friend,'</h1>\n'))
    res$write('What is your name?\n')
    res$write('<form method="GET">\n')
    res$write('<input type="text" name="friend">\n')
    res$write('<input type="submit" name="Submit">\n</form>\n<br>')
    res$finish()
}
~~~
