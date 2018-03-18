+++
draft = false
date="2015-07-12 09:53:04"
title="R: I write more in the last week of the month, or do I?"
tag=['r-2']
category=['R']
+++

<p>
I've been writing on this blog for almost 7 years and have always believed that I write more frequently towards the end of a month. Now that I've got all the data I thought it'd be interesting to test that belief.
</p>


<p>
I started with a data frame containing each post and its publication date and added an extra column which works out how many weeks from the end of the month that post was written:
</p>



~~~r

> df %>% sample_n(5)
                                                               title                date
946  Python: Equivalent to flatMap for flattening an array of arrays 2015-03-23 00:45:00
175                                         Ruby: Hash default value 2010-10-16 14:02:37
375               Java/Scala: Runtime.exec hanging/in 'pipe_w' state 2011-11-20 20:20:08
1319                            Coding Dojo #18: Groovy Bowling Game 2009-06-26 08:15:23
381                   Continuous Delivery: Removing manual scenarios 2011-12-05 23:13:34

calculate_start_of_week = function(week, year) {
  date <- ymd(paste(year, 1, 1, sep="-"))
  week(date) = week
  return(date)
}

tidy_df  = df %>% 
  mutate(year = year(date), 
         week = week(date),
         week_in_month = ceiling(day(date) / 7),
         max_week = max(week_in_month), 
         weeks_from_end = max_week - week_in_month,
         start_of_week = calculate_start_of_week(week, year))

> tidy_df %>% select(date, weeks_from_end, start_of_week) %>% sample_n(5)

                    date weeks_from_end start_of_week
1023 2008-08-08 21:16:02              3    2008-08-05
800  2014-01-31 06:51:06              0    2014-01-29
859  2014-08-14 10:24:52              3    2014-08-13
107  2010-07-10 22:49:52              3    2010-07-09
386  2011-12-20 23:57:51              2    2011-12-17
~~~

<p>
Next I want to get a count of how many posts were published in a given week. The following code does that transformation for us:
</p>



~~~r

weeks_from_end_counts =  tidy_df %>%
  group_by(start_of_week, weeks_from_end) %>%
  summarise(count = n())

> weeks_from_end_counts
Source: local data frame [540 x 4]
Groups: start_of_week, weeks_from_end

   start_of_week weeks_from_end year count
1     2006-08-27              0 2006     1
2     2006-08-27              4 2006     3
3     2006-09-03              4 2006     1
4     2008-02-05              3 2008     2
5     2008-02-12              3 2008     2
6     2008-07-15              2 2008     1
7     2008-07-22              1 2008     1
8     2008-08-05              3 2008     8
9     2008-08-12              2 2008     5
10    2008-08-12              3 2008     9
..           ...            ...  ...   ...
~~~

<p>We group by both 'start_of_week' and 'weeks_from_end' because we could have posts published in the same week but different month and we want to capture that difference. Now we can run a correlation on the data frame to see if there's any relationship between 'count' and 'weeks_from_end':</p>



~~~r

> cor(weeks_from_end_counts %>% ungroup() %>% select(weeks_from_end, count))
               weeks_from_end       count
weeks_from_end     1.00000000 -0.08253569
count             -0.08253569  1.00000000
~~~

<p>
This suggests there's a slight negative correlation between the two variables i.e. 'count' decreases as 'weeks_from_end' increases. Let's plug the data frame into a linear model to see how good 'weeks_from_end' is as a predictor of 'count':
</p>



~~~r

> fit = lm(count ~ weeks_from_end, weeks_from_end_counts)

> summary(fit)

Call:
lm(formula = count ~ weeks_from_end, data = weeks_from_end_counts)

Residuals:
    Min      1Q  Median      3Q     Max 
-2.0000 -1.5758 -0.5758  1.1060  8.0000 

Coefficients:
               Estimate Std. Error t value Pr(>|t|)    
(Intercept)     3.00000    0.13764  21.795   <2e-16 ***
weeks_from_end -0.10605    0.05521  -1.921   0.0553 .  
---
Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

Residual standard error: 1.698 on 538 degrees of freedom
Multiple R-squared:  0.006812,	Adjusted R-squared:  0.004966 
F-statistic:  3.69 on 1 and 538 DF,  p-value: 0.05527
~~~

<p>
We see a similar result here. The effect of 'weeks_from_end' is worth 0.1 posts per week with a p value of 0.0553 so it's on the border line of being significant.</p>


<p>We also have a very low 'R squared' value which suggests the 'weeks_from_end' isn't explaining much of the variation in the data which makes sense given that we didn't see much of a correlation.
</p>


<p>
If we charged on and wanted to predict the number of posts likely to be published in a given week we could run the predict function like this:
</p>



~~~r

> predict(fit, data.frame(weeks_from_end=c(1,2,3,4,5)))
       1        2        3        4        5 
2.893952 2.787905 2.681859 2.575812 2.469766
~~~

<p>
Obviously it's a bit flawed since we could plug in any numeric value we want, even ones that don't make any sense, and it'd still come back with a prediction:
</p>



~~~r

> predict(fit, data.frame(weeks_from_end=c(30 ,-10)))
        1         2 
-0.181394  4.060462 
~~~

<p>
I think we'd probably protect against that with a function wrapping our call to predict that doesn't allow 'weeks_from_end' to be greater than 5 or less than 0.
</p>


<p>
So far it looks like my belief is incorrect! I'm a bit dubious about my calculation of 'weeks_from_end' though - it's not completely capturing what I want since in some months the last week only contains a couple of days.
</p>


<p>Next I'm going to explore whether it makes any difference if I calculate that value by counting the number of days back from the last day of the month rather than using week number.</p>

