+++
draft = false
date="2013-01-31 23:24:55"
title="Kaggle Digit Recognizer: A feature extraction #fail"
tag=['machine-learning-2', 'kaggle']
category=['Machine Learning']
+++

I've written <a href="http://www.markhneedham.com/blog/tag/kaggle/">a few blog posts</a> about our attempts at the <a href="http://www.kaggle.com/c/digit-recognizer">Kaggle Digit Recogniser</a> problem and one thing we haven't yet tried is feature extraction. 

<p>Feature extraction in this context means that we'd generate some other features to train a classifier with rather than relying on just the pixel values we were provided.</p>


<p>Every week <a href="https://twitter.com/jennifersmithco">Jen</a> would try and persuade me that we should try it out but it wasn't until I was flicking through <a href="http://columbiadatascience.com/2012/10/15/10-important-data-science-ideas/">the notes from the Columbia Data Science class</a> that it struck home:</p>


<blockquote>
5. The Space between the Data Set and the Algorithm 

<strong>Many people go straight from a data set to applying an algorithm</strong>. But there’s a huge space in between of important stuff. It’s easy to run a piece of code that predicts or classifies. That’s not the hard part. The hard part is doing it well.

One needs to conduct exploratory data analysis as I’ve emphasized; and conduct feature selection as Will Cukierski emphasized.
</blockquote>

<p>I've highlighted the part of the post which describes exactly what we've been doing!</p>


<p>There were some <a href="http://www.kaggle.com/c/digit-recognizer/forums/t/2308/feature-extraction-technique">examples of feature extraction</a> on the Kaggle forums so I thought I'd try and create some other features using <a href="http://www.markhneedham.com/blog/category/r/">R</a>.</p>


<p>I created features for the number of non zero pixels, the number of 255 pixels, the average number of pixels and the average of the middle pixels of a number.</p>


<p>The code reads like this:</p>



~~~r

initial <- read.csv("train.csv", header = TRUE)
initial$nonZeros <- apply(initial, 1, function(entries) length(Filter(function (x) x != 0, entries)))
initial$fullHouses <- apply(initial, 1, function(entries) length(Filter(function (x) x == 255, entries)))
initial$meanPixels <- apply(initial, 1, mean)
initial$middlePixels <- apply(initial[,200:500], 1, mean)
~~~

<p>I then wrote those features out into a CSV file like so:</p>



~~~r

newFeatures <- subset(initial, select=c(label, nonZeros, meanPixels, fullHouses, middlePixels))
write.table(file="feature-extraction.txt", newFeatures, row.names=FALSE, sep=",")
~~~

<p>I then created a <a href="http://www.markhneedham.com/blog/2012/12/27/mahout-parallelising-the-creation-of-decisiontrees/">100 tree random forest using Mahout</a> to see whether or not we could get any sort of accuracy using these features.</p>


<p>Unfortunately the accuracy on the cross validation set (10% of the training data) was only 24% which is pretty useless so it's back to the drawing board!</p>


<p>Our next task is to try and work out whether we can derive some features which have a stronger correlation with the label values or combining the new features with the existing pixel values to see if that has any impact.</p>


<p>As you can probably tell I don't really understand how you should go about extracting features so if anybody has ideas or papers/articles I can read to learn more please let me know in the comments!</p>

