+++
draft = false
date="2013-01-08 00:48:07"
title="Kaggle Digit Recognizer: Finding pixels with no variance using R"
tag=['kaggle']
category=['R', 'Machine Learning']
+++

<p>I've <a href="http://www.markhneedham.com/blog/2012/10/27/kaggle-digit-recognizer-k-means-optimisation-attempt/">written</a> <a href="http://www.markhneedham.com/blog/2012/11/29/kaggle-digit-recognizer-weka-adaboost-attempt/">previously</a> <a href="http://www.markhneedham.com/blog/2012/10/23/kaggle-digit-recognizer-a-k-means-attempt/">about</a> <a href="http://www.markhneedham.com/blog/2012/10/27/kaggle-digit-recognizer-mahout-random-forest-attempt/">our</a> <a href="http://www.markhneedham.com/blog/2012/12/27/mahout-parallelising-the-creation-of-decisiontrees/">attempts</a> at the <a href="http://www.kaggle.com/c/digit-recognizer">Kaggle Digit Recogniser</a> problem and our approach so far has been to use the data provided and plug it into different algorithms and see what we end up with.</p>


<p>From <a href="http://www.kaggle.com/c/digit-recognizer/forums/t/2308/feature-extraction-technique?page=2">browsing through the forums</a> we saw others mentioning feature extraction - an approach where we transform the data into another format , the thinking being that we can train a better classifier with better data.</p>


<p>There was quite a nice quote from a post written by Rachel Schutt about the Columbia Data Science course which <a href="http://columbiadatascience.com/2012/10/15/10-important-data-science-ideas/">summed up the mistake we'd made</a>:</p>


<blockquote>
The Space between the Data Set and the Algorithm 

Many people go straight from a data set to applying an algorithm. But there’s a huge space in between of important stuff. It’s easy to run a piece of code that predicts or classifies. That’s not the hard part. The hard part is doing it well.
</blockquote>

<p>One thing we'd noticed while visually scanning the data set was that a lot of the features seemed to consistently have a value of 0. We thought we'd try and find out which pixels those were by finding the features which had zero variance in their values.</p>


<p>I started out by loading a subset of the data set and then taking a sample of that to play around with:</p>



~~~r

initial <- read.csv("train.csv", nrows=10000, header = TRUE)

# take a sample of 1000 rows of the input 
sampleSet <- initial[sample(1:nrow(initial), 1000), ]
~~~

<p>Just for fun I thought it'd be interesting to see how well the labels were distributed in my sample which we can do with the following code:</p>



~~~r

# get all the labels
sampleSet.labels <- as.factor(sampleSet$label)

> table(sampleSet.labels)
sampleSet.labels
  0   1   2   3   4   5   6   7   8   9 
102 116 100  97  95  91  79 122 102  96 
~~~

<p>There are a few more 1's and 7s than the other labels but they're roughly in the same ballpark so it's ok.</p>


<p>I wanted to <a href="http://stackoverflow.com/questions/6286313/remove-an-entire-column-from-a-data-frame-in-r">exclude the 'label' field</a> from the data set because the variance of labels isn't interesting to us on this occasion. We can do that with the following code:</p>



~~~r

# get data set excluding label
excludingLabel <- subset( sampleSet, select = -label)
~~~

<p>To find all the features with no variance we then do this:</p>




~~~r

# show all the features which don't have any variance - all have the same value
variances <- apply(excludingLabel, 2, var)

# get the names of the labels which have no variance
> pointlessFeatures <- names(excludingLabel[variances == 0][1,])

 [1] "pixel0"   "pixel1"   "pixel2"   "pixel3"   "pixel4"   "pixel5"   "pixel6"   "pixel7"  
  [9] "pixel8"   "pixel9"   "pixel10"  "pixel11"  "pixel12"  "pixel13"  "pixel14"  "pixel15" 
 [17] "pixel16"  "pixel17"  "pixel18"  "pixel19"  "pixel20"  "pixel21"  "pixel22"  "pixel23" 
 [25] "pixel24"  "pixel25"  "pixel26"  "pixel27"  "pixel28"  "pixel29"  "pixel30"  "pixel31" 
 [33] "pixel32"  "pixel33"  "pixel51"  "pixel52"  "pixel53"  "pixel54"  "pixel55"  "pixel56" 
 [41] "pixel57"  "pixel58"  "pixel59"  "pixel60"  "pixel82"  "pixel83"  "pixel84"  "pixel85" 
 [49] "pixel86"  "pixel88"  "pixel110" "pixel111" "pixel112" "pixel113" "pixel114" "pixel139"
 [57] "pixel140" "pixel141" "pixel142" "pixel168" "pixel169" "pixel196" "pixel252" "pixel280"
 [65] "pixel308" "pixel335" "pixel336" "pixel364" "pixel365" "pixel392" "pixel393" "pixel420"
 [73] "pixel421" "pixel448" "pixel476" "pixel504" "pixel532" "pixel559" "pixel560" "pixel587"
 [81] "pixel615" "pixel643" "pixel644" "pixel645" "pixel671" "pixel672" "pixel673" "pixel699"
 [89] "pixel700" "pixel701" "pixel727" "pixel728" "pixel729" "pixel730" "pixel731" "pixel752"
 [97] "pixel753" "pixel754" "pixel755" "pixel756" "pixel757" "pixel758" "pixel759" "pixel760"
[105] "pixel779" "pixel780" "pixel781" "pixel782" "pixel783"
~~~

<p>We can count how many labels there are by using the <cite>length</cite> function:</p>



~~~r

# count how many labels have no variance
> length(names(excludingLabel[apply(excludingLabel, 2, var) == 0][1,]))
[1] 109
~~~

<p>I then wrote those out to a file so that we could use them as the input to the code which builds up our classifier.</p>



~~~r

write(file="pointless-features.txt", pointlessFeatures)
~~~

<p>Of course we should run the variance test against the full data set rather than just a sample and on the whole data set there are only 76 features with zero variance:</p>



~~~r

> sampleSet <- read.csv("train.csv", header = TRUE)
> sampleSet.labels <- as.factor(sampleSet$label)
> table(sampleSet.labels)
sampleSet.labels
   0    1    2    3    4    5    6    7    8    9 
4132 4684 4177 4351 4072 3795 4137 4401 4063 4188 
> excludingLabel <- subset( sampleSet, select = -label)
> variances <- apply(excludingLabel, 2, var)
> pointlessFeatures <- names(excludingLabel[variances == 0][1,])
> length(names(excludingLabel[apply(excludingLabel, 2, var) == 0][1,]))
[1] 76
~~~

<p>We've built decision trees using this reduced data set but haven't yet submitted the forest to Kaggle to see if it's any more accurate!</p>


<p>I picked up the little R I know from the <a href="https://class.coursera.org/compdata-002/class/index">Computing for Data Analysis</a> course which started last week and from the book '<a href="http://www.amazon.co.uk/R-in-a-Nutshell-ebook/dp/B009HE12MK/ref=sr_1_1?ie=UTF8&qid=1357606031&sr=8-1">R in a Nutshell</a>' which my colleague <a href="https://twitter.com/quantisan">Paul Lam</a> recommended.</p>

