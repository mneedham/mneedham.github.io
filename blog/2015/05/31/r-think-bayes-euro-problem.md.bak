+++
draft = false
date="2015-05-31 23:11:50"
title="R: Think Bayes Euro Problem"
tag=['r-2', 'rstats']
category=['R']
+++

<p>I've got back to working my way through <a href="http://www.greenteapress.com/thinkbayes/">Think Bayes</a> after a month's break and started out with the one euro coin problem in Chapter 4:
</p>


<blockquote>
A statistical statement appeared in “The Guardian" on Friday January 4, 2002:

When spun on edge 250 times, a Belgian one-euro coin came up heads 140 times and tails 110. ‘It looks very suspicious to me,’ said Barry Blight, a statistics lecturer at the London School of Economics. ‘If the coin were unbiased, the chance of getting a result as extreme as that would be less than 7%.’

But do these data give evidence that the coin is biased rather than fair?
</blockquote>

<p>
We're going to create a data frame with each row representing the probability that heads shows up that often. We need one row for each value between 0 (no heads) and 100 (all heads) and we'll start with the assumption that each value can be chosen equally (a uniform prior):
</p>



~~~r

library(dplyr)

values = seq(0, 100)
scores = rep(1.0 / length(values), length(values))  
df = data.frame(score = scores, value = values)

> df %>% sample_n(10)
         score value
60  0.00990099    59
101 0.00990099   100
10  0.00990099     9
41  0.00990099    40
2   0.00990099     1
83  0.00990099    82
44  0.00990099    43
97  0.00990099    96
100 0.00990099    99
12  0.00990099    11
~~~

<p>
Now we need to feed in our observations. We need to create a vector containing 140 heads and 110 tails. The 'rep' function comes in handy here:
</p>



~~~r

observations = c(rep("T", times = 110), rep("H", times = 140))
> observations
  [1] "T" "T" "T" "T" "T" "T" "T" "T" "T" "T" "T" "T" "T" "T" "T" "T" "T" "T" "T" "T" "T" "T" "T" "T" "T" "T" "T" "T"
 [29] "T" "T" "T" "T" "T" "T" "T" "T" "T" "T" "T" "T" "T" "T" "T" "T" "T" "T" "T" "T" "T" "T" "T" "T" "T" "T" "T" "T"
 [57] "T" "T" "T" "T" "T" "T" "T" "T" "T" "T" "T" "T" "T" "T" "T" "T" "T" "T" "T" "T" "T" "T" "T" "T" "T" "T" "T" "T"
 [85] "T" "T" "T" "T" "T" "T" "T" "T" "T" "T" "T" "T" "T" "T" "T" "T" "T" "T" "T" "T" "T" "T" "T" "T" "T" "T" "H" "H"
[113] "H" "H" "H" "H" "H" "H" "H" "H" "H" "H" "H" "H" "H" "H" "H" "H" "H" "H" "H" "H" "H" "H" "H" "H" "H" "H" "H" "H"
[141] "H" "H" "H" "H" "H" "H" "H" "H" "H" "H" "H" "H" "H" "H" "H" "H" "H" "H" "H" "H" "H" "H" "H" "H" "H" "H" "H" "H"
[169] "H" "H" "H" "H" "H" "H" "H" "H" "H" "H" "H" "H" "H" "H" "H" "H" "H" "H" "H" "H" "H" "H" "H" "H" "H" "H" "H" "H"
[197] "H" "H" "H" "H" "H" "H" "H" "H" "H" "H" "H" "H" "H" "H" "H" "H" "H" "H" "H" "H" "H" "H" "H" "H" "H" "H" "H" "H"
[225] "H" "H" "H" "H" "H" "H" "H" "H" "H" "H" "H" "H" "H" "H" "H" "H" "H" "H" "H" "H" "H" "H" "H" "H" "H" "H"
~~~

<p>Now we need to iterate over each of the observations and update our data frame appropriately.</p>



~~~r

for(observation in observations) {
  if(observation == "H") {
    df = df %>% mutate(score = score * (value / 100.0))
  } else {
    df = df %>% mutate(score = score * (1.0 - (value / 100.0)))
  }    
}

df = df %>% mutate(weighted = score / sum(score)) 
~~~

<p>
Now that we've done that we can calculate the maximum likelihood, mean, median and credible interval. We'll create a 'percentile' function to help us out:
</p>



~~~r

percentile = function(df, p) {
    df %>% filter(cumsum(weighted) > p) %>% head(1) %>% select(value) %>% as.numeric
}
~~~

<p>And now let's calculate the values:</p>



~~~r

# Maximum likelihood
> df %>% filter(weighted == max(weighted)) %>% select(value) %>% as.numeric
[1] 56

# Mean
> df %>% mutate(mean = value * weighted) %>% select(mean) %>% sum
[1] 55.95238

# Median
> percentile(df, 0.5)
[1] 56

# Credible Interval
percentage = 90
prob = (1 - percentage / 100.0) / 2

# lower
> percentile(df, prob)
[1] 51

# upper
> percentile(df, 1 - prob)
[1] 61
~~~

<p>
This all wraps up nicely into a function:
</p>



~~~r

euro = function(values, priors, observations) {
  df = data.frame(score = priors, value = values)
  
  for(observation in observations) {
    if(observation == "H") {
      df = df %>% mutate(score = score * (value / 100.0))
    } else {
      df = df %>% mutate(score = score * (1.0 - (value / 100.0)))
    }    
  }
  
  return(df %>% mutate(weighted = score / sum(score)))
}
~~~

<p>which we can call like so:</p>



~~~r

values = seq(0,100)
priors = rep(1.0 / length(values), length(values))
observations = c(rep("T", times = 110), rep("H", times = 140))
df = euro(values, priors, observations)
~~~

<P>The next part of the problem requires us to change the prior distribution to be more weighted to values close to 50%. We can tweak the parameters we pass into the function accordingly:</p>



~~~r

values = seq(0,100)
priors = sapply(values, function(x) ifelse(x < 50, x, 100 - x))
priors = priors / sum(priors)
observations = c(rep("T", times = 110), rep("H", times = 140))
df = euro(values, priors, observations)
~~~

<p>In fact even with the adjusted priors we still end up with the same posterior distribution:</p>



~~~r

> df %>% filter(weighted == max(weighted)) %>% select(value) %>% as.numeric
[1] 56

> df %>% mutate(mean = value * weighted) %>% select(mean) %>% sum
[1] 55.7435

> percentile(df, 0.5)
[1] 56

> percentile(df, 0.05)
[1] 51

> percentile(df, 0.95)
[1] 61
~~~

<p>The book describes this phenemenom as follows:</p>


<blockquote>
This is an example of swamping the priors: with enough data, people who start with different priors will tend to converge on the same posterior.
</blockquote>
