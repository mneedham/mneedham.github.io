+++
draft = false
date="2015-04-27 22:34:43"
title="R: dplyr - Error in (list: invalid subscript type 'double'"
tag=['r-2', 'rstats']
category=['R']
+++

<p>
In my continued playing around with R I wanted to find the minimum value for a specified percentile given a data frame representing a cumulative distribution function (CDF).</p>



<p>e.g. imagine we have the following CDF represented in a data frame:</p>



~~~r

library(dplyr)
df = data.frame(score = c(5,7,8,10,12,20), percentile = c(0.05,0.1,0.15,0.20,0.25,0.5))
~~~

<p>
and we want to find the minimum value for the 0.05 percentile. We can use the <cite>filter</cite> function to do so:
</p>




~~~r

> (df %>% filter(percentile > 0.05) %>% slice(1))$score
[1] 7
~~~

<p>
Things become more tricky if we want to return multiple percentiles in one go.</p>
 

<p>
My first thought was to create a data frame with one row for each target percentile and then pull in the appropriate row from our original data frame:
</p>



~~~r

targetPercentiles = c(0.05, 0.2)
percentilesDf = data.frame(targetPercentile = targetPercentiles)
> percentilesDf %>% 
    group_by(targetPercentile) %>%
    mutate(x = (df %>% filter(percentile > targetPercentile) %>% slice(1))$score)

Error in (list(score = c(5, 7, 8, 10, 12, 20), percentile = c(0.05, 0.1,  : 
  invalid subscript type 'double'
~~~

<p>
Unfortunately this didn't quite work as I expected - <a href="https://twitter.com/tonkouts">Antonios</a> pointed out that this is probably because we're mixing up two pipelines and dplyr can't figure out what we want to do.
</p>


<p>
Instead he suggested the following variant which uses the <cite><a href="https://github.com/hadley/dplyr#do">do</a></cite> function 
</p>



~~~r

df = data.frame(score = c(5,7,8,10,12,20), percentile = c(0.05,0.1,0.15,0.20,0.25,0.5))
targetPercentiles = c(0.05, 0.2)
 
> data.frame(targetPercentile = targetPercentiles) %>%
    group_by(targetPercentile) %>%
    do(df) %>% 
    filter(percentile > targetPercentile) %>% 
    slice(1) %>%
    select(targetPercentile, score)
Source: local data frame [2 x 2]
Groups: targetPercentile

  targetPercentile score
1             0.05     7
2             0.20    12
~~~

<p>We can then wrap this up in a function:</p>



~~~r

percentiles = function(df, targetPercentiles) {
  # make sure the percentiles are in order
  df = df %>% arrange(percentile)
  
  data.frame(targetPercentile = targetPercentiles) %>%
    group_by(targetPercentile) %>%
    do(df) %>% 
    filter(percentile > targetPercentile) %>% 
    slice(1) %>%
    select(targetPercentile, score)
}
~~~

<p>which we call like this:</p>



~~~r

df = data.frame(score = c(5,7,8,10,12,20), percentile = c(0.05,0.1,0.15,0.20,0.25,0.5))
> percentiles(df, c(0.08, 0.10, 0.50, 0.80))
Source: local data frame [2 x 2]
Groups: targetPercentile

  targetPercentile score
1             0.08     7
2             0.10     8
~~~

<p>
Note that we don't actually get any rows back for 0.50 or 0.80 since we don't have any entries greater than those percentiles. With a proper CDF we would though so the function does its job.
</p>

