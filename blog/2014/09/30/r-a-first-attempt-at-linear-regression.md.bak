+++
draft = false
date="2014-09-30 22:20:05"
title="R: A first attempt at linear regression"
tag=['r-2', 'rstats']
category=['R']
+++

<p>I've been working through <a href="http://www.dataschool.io/15-hours-of-expert-machine-learning-videos/">the videos that accompany the Introduction to Statistical Learning with Applications in R</a> book and thought it'd be interesting to try out the linear regression algorithm against my <a href="https://github.com/mneedham/neo4j-meetup">meetup data set</a>.</p>


<p>I wanted to see how well a linear regression algorithm could predict how many people were likely to RSVP to a particular event. I started with the following code to build a data frame containing some potential predictors:</p>



~~~r

library(RNeo4j)
officeEventsQuery = "MATCH (g:Group {name: \"Neo4j - London User Group\"})-[:HOSTED_EVENT]->(event)<-[:TO]-({response: 'yes'})<-[:RSVPD]-(),
                           (event)-[:HELD_AT]->(venue)
                     WHERE (event.time + event.utc_offset) < timestamp() AND venue.name IN [\"Neo Technology\", \"OpenCredo\"]
                     RETURN event.time + event.utc_offset AS eventTime,event.announced_at AS announcedAt, event.name, COUNT(*) AS rsvps"

events = subset(cypher(graph, officeEventsQuery), !is.na(announcedAt))
events$eventTime <- timestampToDate(events$eventTime)
events$day <- format(events$eventTime, "%A")
events$monthYear <- format(events$eventTime, "%m-%Y")
events$month <- format(events$eventTime, "%m")
events$year <- format(events$eventTime, "%Y")
events$announcedAt<- timestampToDate(events$announcedAt)
events$timeDiff = as.numeric(events$eventTime - events$announcedAt, units = "days")
~~~

<p>If we preview 'events' it contains the following columns:</p>



~~~r

> head(events)
            eventTime         announcedAt                                        event.name rsvps       day monthYear month year  timeDiff
1 2013-01-29 18:00:00 2012-11-30 11:30:57                                   Intro to Graphs    24   Tuesday   01-2013    01 2013 60.270174
2 2014-06-24 18:30:00 2014-06-18 19:11:19                                   Intro to Graphs    43   Tuesday   06-2014    06 2014  5.971308
3 2014-06-18 18:30:00 2014-06-08 07:03:13                         Neo4j World Cup Hackathon    24 Wednesday   06-2014    06 2014 10.476933
4 2014-05-20 18:30:00 2014-05-14 18:56:06                                   Intro to Graphs    53   Tuesday   05-2014    05 2014  5.981875
5 2014-02-11 18:00:00 2014-02-05 19:11:03                                   Intro to Graphs    35   Tuesday   02-2014    02 2014  5.950660
6 2014-09-04 18:30:00 2014-08-26 06:34:01 Hands On Intro to Cypher - Neo4j's Query Language    20  Thursday   09-2014    09 2014  9.497211
~~~

<p>We want to predict 'rsvps' from the other columns so I started off by creating a linear model which took all the other columns into account:</p>



~~~r

> summary(lm(rsvps ~., data = events))

Call:
lm(formula = rsvps ~ ., data = events)

Residuals:
    Min      1Q  Median      3Q     Max 
-8.2582 -1.1538  0.0000  0.4158 10.5803 

Coefficients: (14 not defined because of singularities)
                                                                    Estimate Std. Error t value Pr(>|t|)   
(Intercept)                                                       -9.365e+03  3.009e+03  -3.113  0.00897 **
eventTime                                                          3.609e-06  2.951e-06   1.223  0.24479   
announcedAt                                                        3.278e-06  2.553e-06   1.284  0.22339   
event.nameGraph Modelling - Do's and Don'ts                        4.884e+01  1.140e+01   4.286  0.00106 **
event.nameHands on build your first Neo4j app for Java developers  3.735e+01  1.048e+01   3.562  0.00391 **
event.nameHands On Intro to Cypher - Neo4j's Query Language        2.560e+01  9.713e+00   2.635  0.02177 * 
event.nameIntro to Graphs                                          2.238e+01  8.726e+00   2.564  0.02480 * 
event.nameIntroduction to Graph Database Modeling                 -1.304e+02  4.835e+01  -2.696  0.01946 * 
event.nameLunch with Neo4j's CEO, Emil Eifrem                      3.920e+01  1.113e+01   3.523  0.00420 **
event.nameNeo4j Clojure Hackathon                                 -3.063e+00  1.195e+01  -0.256  0.80203   
event.nameNeo4j Python Hackathon with py2neo's Nigel Small         2.128e+01  1.070e+01   1.989  0.06998 . 
event.nameNeo4j World Cup Hackathon                                5.004e+00  9.622e+00   0.520  0.61251   
dayTuesday                                                         2.068e+01  5.626e+00   3.676  0.00317 **
dayWednesday                                                       2.300e+01  5.522e+00   4.165  0.00131 **
monthYear01-2014                                                  -2.350e+02  7.377e+01  -3.185  0.00784 **
monthYear02-2013                                                  -2.526e+01  1.376e+01  -1.836  0.09130 . 
monthYear02-2014                                                  -2.325e+02  7.763e+01  -2.995  0.01118 * 
monthYear03-2013                                                  -4.605e+01  1.683e+01  -2.736  0.01805 * 
monthYear03-2014                                                  -2.371e+02  8.324e+01  -2.848  0.01468 * 
monthYear04-2013                                                  -6.570e+01  2.309e+01  -2.845  0.01477 * 
monthYear04-2014                                                  -2.535e+02  8.746e+01  -2.899  0.01336 * 
monthYear05-2013                                                  -8.672e+01  2.845e+01  -3.049  0.01011 * 
monthYear05-2014                                                  -2.802e+02  9.420e+01  -2.975  0.01160 * 
monthYear06-2013                                                  -1.022e+02  3.283e+01  -3.113  0.00897 **
monthYear06-2014                                                  -2.996e+02  1.003e+02  -2.988  0.01132 * 
monthYear07-2014                                                  -3.123e+02  1.054e+02  -2.965  0.01182 * 
monthYear08-2013                                                  -1.326e+02  4.323e+01  -3.067  0.00976 **
monthYear08-2014                                                  -3.060e+02  1.107e+02  -2.763  0.01718 * 
monthYear09-2013                                                          NA         NA      NA       NA   
monthYear09-2014                                                  -3.465e+02  1.164e+02  -2.976  0.01158 * 
monthYear10-2012                                                   2.602e+01  1.959e+01   1.328  0.20886   
monthYear10-2013                                                  -1.728e+02  5.678e+01  -3.044  0.01020 * 
monthYear11-2012                                                   2.717e+01  1.509e+01   1.800  0.09704 . 
month02                                                                   NA         NA      NA       NA   
month03                                                                   NA         NA      NA       NA   
month04                                                                   NA         NA      NA       NA   
month05                                                                   NA         NA      NA       NA   
month06                                                                   NA         NA      NA       NA   
month07                                                                   NA         NA      NA       NA   
month08                                                                   NA         NA      NA       NA   
month09                                                                   NA         NA      NA       NA   
month10                                                                   NA         NA      NA       NA   
month11                                                                   NA         NA      NA       NA   
year2013                                                                  NA         NA      NA       NA   
year2014                                                                  NA         NA      NA       NA   
timeDiff                                                                  NA         NA      NA       NA   
---
Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

Residual standard error: 5.287 on 12 degrees of freedom
Multiple R-squared:  0.9585,	Adjusted R-squared:  0.8512 
F-statistic: 8.934 on 31 and 12 DF,  p-value: 0.0001399
~~~

<p>As I understand it we can look at the R-squared value to understand how much of the variance in the data has been explained by the model - in this case it's 85%. </p>


<p>A lot of the coefficients seem to be based around specific event names which seems a bit too specific to me so I wanted to see what would happen if I derived a feature which indicated whether a session was practical: </p>



~~~r

events$practical = grepl("Hackathon|Hands on|Hands On", events$event.name)
~~~

<p>We can now run the model again with the new column having excluded 'event.name' field:</p>



~~~r

> summary(lm(rsvps ~., data = subset(events, select = -c(event.name))))

Call:
lm(formula = rsvps ~ ., data = subset(events, select = -c(event.name)))

Residuals:
    Min      1Q  Median      3Q     Max 
-18.647  -2.311   0.000   2.908  23.218 

Coefficients: (13 not defined because of singularities)
                   Estimate Std. Error t value Pr(>|t|)  
(Intercept)      -3.980e+03  4.752e+03  -0.838   0.4127  
eventTime         2.907e-06  3.873e-06   0.751   0.4621  
announcedAt       3.336e-08  3.559e-06   0.009   0.9926  
dayTuesday        7.547e+00  6.080e+00   1.241   0.2296  
dayWednesday      2.442e+00  7.046e+00   0.347   0.7327  
monthYear01-2014 -9.562e+01  1.187e+02  -0.806   0.4303  
monthYear02-2013 -4.230e+00  2.289e+01  -0.185   0.8553  
monthYear02-2014 -9.156e+01  1.254e+02  -0.730   0.4742  
monthYear03-2013 -1.633e+01  2.808e+01  -0.582   0.5676  
monthYear03-2014 -8.094e+01  1.329e+02  -0.609   0.5496  
monthYear04-2013 -2.249e+01  3.785e+01  -0.594   0.5595  
monthYear04-2014 -9.230e+01  1.401e+02  -0.659   0.5180  
monthYear05-2013 -3.237e+01  4.654e+01  -0.696   0.4952  
monthYear05-2014 -1.015e+02  1.509e+02  -0.673   0.5092  
monthYear06-2013 -3.947e+01  5.355e+01  -0.737   0.4701  
monthYear06-2014 -1.081e+02  1.604e+02  -0.674   0.5084  
monthYear07-2014 -1.110e+02  1.678e+02  -0.661   0.5163  
monthYear08-2013 -5.144e+01  6.988e+01  -0.736   0.4706  
monthYear08-2014 -1.023e+02  1.784e+02  -0.573   0.5731  
monthYear09-2013 -6.057e+01  7.893e+01  -0.767   0.4523  
monthYear09-2014 -1.260e+02  1.874e+02  -0.672   0.5094  
monthYear10-2012  9.557e+00  2.873e+01   0.333   0.7430  
monthYear10-2013 -6.450e+01  9.169e+01  -0.703   0.4903  
monthYear11-2012  1.689e+01  2.316e+01   0.729   0.4748  
month02                  NA         NA      NA       NA  
month03                  NA         NA      NA       NA  
month04                  NA         NA      NA       NA  
month05                  NA         NA      NA       NA  
month06                  NA         NA      NA       NA  
month07                  NA         NA      NA       NA  
month08                  NA         NA      NA       NA  
month09                  NA         NA      NA       NA  
month10                  NA         NA      NA       NA  
month11                  NA         NA      NA       NA  
year2013                 NA         NA      NA       NA  
year2014                 NA         NA      NA       NA  
timeDiff                 NA         NA      NA       NA  
practicalTRUE    -9.388e+00  5.289e+00  -1.775   0.0919 .
---
Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

Residual standard error: 10.21 on 19 degrees of freedom
Multiple R-squared:  0.7546,	Adjusted R-squared:  0.4446 
F-statistic: 2.434 on 24 and 19 DF,  p-value: 0.02592
~~~

<p>Now we're only accounting for 44% of the variance and none of our coefficients are significant so this wasn't such a good change.</p>


<p>I also noticed that we've got a bit of overlap in the date related features - we've got one column for monthYear and then separate ones for month and year. Let's strip out the combined one:</p>



~~~r

> summary(lm(rsvps ~., data = subset(events, select = -c(event.name, monthYear))))

Call:
lm(formula = rsvps ~ ., data = subset(events, select = -c(event.name, 
    monthYear)))

Residuals:
     Min       1Q   Median       3Q      Max 
-16.5745  -4.0507  -0.1042   3.6586  24.4715 

Coefficients: (1 not defined because of singularities)
                Estimate Std. Error t value Pr(>|t|)  
(Intercept)   -1.573e+03  4.315e+03  -0.364   0.7185  
eventTime      3.320e-06  3.434e-06   0.967   0.3425  
announcedAt   -2.149e-06  2.201e-06  -0.976   0.3379  
dayTuesday     4.713e+00  5.871e+00   0.803   0.4294  
dayWednesday  -2.253e-01  6.685e+00  -0.034   0.9734  
month02        3.164e+00  1.285e+01   0.246   0.8075  
month03        1.127e+01  1.858e+01   0.607   0.5494  
month04        4.148e+00  2.581e+01   0.161   0.8736  
month05        1.979e+00  3.425e+01   0.058   0.9544  
month06       -1.220e-01  4.271e+01  -0.003   0.9977  
month07        1.671e+00  4.955e+01   0.034   0.9734  
month08        8.849e+00  5.940e+01   0.149   0.8827  
month09       -5.496e+00  6.782e+01  -0.081   0.9360  
month10       -5.066e+00  7.893e+01  -0.064   0.9493  
month11        4.255e+00  8.697e+01   0.049   0.9614  
year2013      -1.799e+01  1.032e+02  -0.174   0.8629  
year2014      -3.281e+01  2.045e+02  -0.160   0.8738  
timeDiff              NA         NA      NA       NA  
practicalTRUE -9.816e+00  5.084e+00  -1.931   0.0645 .
---
Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

Residual standard error: 10.19 on 26 degrees of freedom
Multiple R-squared:  0.666,	Adjusted R-squared:  0.4476 
F-statistic: 3.049 on 17 and 26 DF,  p-value: 0.005187
~~~

<p>Again none of the coefficients are statistically significant which is disappointing. I think the main problem may be that I have very few data points (only 42) making it difficult to come up with a general model.</p>


<p>I think my next step is to look for some other features that could impact the number of RSVPs e.g. other events on that day, the weather.</p>


<p>I'm a novice at this but trying to learn more so if you have any ideas of what I should do next please let me know.</p>

