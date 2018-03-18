+++
draft = false
date="2013-02-10 13:29:32"
title="R: Building up a data frame row by row"
tag=['r-2']
category=['R']
+++

<p><a href="http://twitter.com/jennifersmithco">Jen</a> and I recently started working on the <a href="http://www.kaggle.com/c/titanic-gettingStarted">Kaggle Titanic problem</a> and we thought it'd probably be useful to start with some exploratory data analysis to get a feel for the data set.</p>


<p>For this problem you are given a selection of different features describing the passengers on board the Titanic and you have to predict whether or not they would have survived or died based on those features.</p>


<p>I thought an interesting first thing to look at would be the survival rate for passengers of different socio economic status as you would imagine that people of a higher status were more likely to have survived.</p>


<p>The data looks like this:</p>



~~~r

> head(titanic)
  survived pclass                                                name    sex age sibsp parch           ticket    fare cabin embarked
1        0      3                             Braund, Mr. Owen Harris   male  22     1     0        A/5 21171  7.2500              S
2        1      1 Cumings, Mrs. John Bradley (Florence Briggs Thayer) female  38     1     0         PC 17599 71.2833   C85        C
3        1      3                              Heikkinen, Miss. Laina female  26     0     0 STON/O2. 3101282  7.9250              S
4        1      1        Futrelle, Mrs. Jacques Heath (Lily May Peel) female  35     1     0           113803 53.1000  C123        S
5        0      3                            Allen, Mr. William Henry   male  35     0     0           373450  8.0500              S
6        0      3                                    Moran, Mr. James   male  NA     0     0           330877  8.4583              Q
~~~

<p>I started by writing the following function to work out how many people in a particular class survived:</p>



~~~r

survived <- function(class) {
  peopleInThatClass <- titanic[titanic$pclass == class,]
  survived <- peopleInThatClass[peopleInThatClass$survived == 1,]  
  nrow(survived)
}
~~~

<p>I could then work out how many people in each class survived by using <cite>lapply</cite>:</p>



~~~r

> lapply(c(1,2,3), survived)
[[1]]
[1] 136

[[2]]
[1] 87

[[3]]
[1] 119
~~~

<p>This works but the output isn't very nice to read and I wanted to put that data side by side with other information about eeach class for which I figured I'd need to construct a data frame.</p>


<p>I came across a solution which works quite well about <a href="http://stackoverflow.com/questions/3642535/creating-an-r-dataframe-row-by-row">half way down a StackOverflow question</a> and reworked my code to make use of that:</p>



~~~r

survivalSummary <- function(classes) {
  summary<-NULL
  for(class in classes) {
    numberSurvived <- survived(class)
    summary <- rbind(summary,data.frame(class=class, survived=numberSurvived))
  }
  
  summary[with(summary, order(class)),]  
}
~~~


~~~r

> survivalSummary(c(1,2,3))
  class survived
1     1      136
2     2       87
3     3      119
~~~

<p>We make use of the <cite><a href="http://stat.ethz.ch/R-manual/R-patched/library/base/html/cbind.html">rbind</a></cite> function which creates a new data frame with a row appended. We then have to reassign the new data frame to the <cite>summary</cite> variable.</p>


<p>If we want to add other information about the class onto each row such as the total number of passengers and the survival rate it's very easy:</p>



~~~r

survivalSummary <- function(classes) {
  summary<-NULL
  for(class in classes) {
    numberSurvived <- survived(class)
    total <- passengers(class)
    percentageSurvived <- numberSurvived / total
    summary <- rbind(summary,data.frame(class=class, survived=numberSurvived, total=total, percentSurvived=percentageSurvived))
  }
  
  summary[with(summary, order(class)),]  
}
~~~


~~~r

> survivalSummary(unique(titanic$pclass))
  class survived total percentSurvived
2     1      136   216       0.6296296
3     2       87   184       0.4728261
1     3      119   491       0.2423625
~~~

<p>We're also now using <cite>unique</cite> to get the different classes rather than hard coding them.</p>

