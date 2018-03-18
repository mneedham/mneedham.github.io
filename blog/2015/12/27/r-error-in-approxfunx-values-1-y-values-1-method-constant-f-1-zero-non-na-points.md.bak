+++
draft = false
date="2015-12-27 12:24:05"
title="R: Error in approxfun(x.values.1, y.values.1, method = \"constant\", f = 1, :  zero non-NA points"
tag=['r-2']
category=['R']
+++

<p>
I've been following <a href="http://www.r-bloggers.com/how-to-perform-a-logistic-regression-in-r/">Michy Alice's logistic regression tutorial</a> to create an attendance model for London dev meetups and ran into an interesting problem while doing so.
</p>


<p>
Our dataset has a class imbalance i.e. most people RSVP 'no' to events which can lead to misleading accuracy score where predicting 'no' every time would lead to supposed high accuracy.
</p>



~~~r

Source: local data frame [2 x 2]

  attended     n
     (dbl) (int)
1        0  1541
2        1    53
~~~

<p>I sampled the data using <cite>caret</cite>'s <cite><a href="http://www.inside-r.org/packages/cran/caret/docs/upSample">upSample</a></cite> function to avoid this:
</p>



~~~r

attended = as.factor((df %>% dplyr::select(attended))$attended)
upSampledDf = upSample(df %>% dplyr::select(-attended), attended)
upSampledDf$attended = as.numeric(as.character(upSampledDf$Class))
~~~

<p>I then trained a logistic regression model but when I tried to plot the area under the curve I ran into trouble:</p>



~~~r

p <- predict(model, newdata=test, type="response")
pr <- prediction(p, test$attended)
prf <- performance(pr, measure = "tpr", x.measure = "fpr")

Error in approxfun(x.values.1, y.values.1, method = "constant", f = 1,  : 
  zero non-NA points
~~~

<p>
I don't have any NA values in my data frame so this message was a bit confusing to start with. As usual <a href="http://stackoverflow.com/questions/23836955/error-in-approxfunx-values-1-y-values-1-method-constant-f-1-zero-no/33028711#33028711">Stack Overflow came to the rescue</a> with the suggestion that I was probably missing positive/negative values for the independent variable i.e. 'approved'.
</p>


<p>
A quick count on the test data frame using dplyr confirmed my mistake:
</p>



~~~r

> test %>% count(attended)
Source: local data frame [1 x 2]

  attended     n
     (dbl) (int)
1        1   582
~~~

<p>
I'll have to <a href="http://stackoverflow.com/questions/9081498/the-correct-approach-of-randomly-re-ordering-a-matrix-in-r">randomly sort the data frame</a> and then reassign my training and test data frames to work around it.
</p>

