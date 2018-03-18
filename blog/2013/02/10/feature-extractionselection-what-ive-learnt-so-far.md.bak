+++
draft = false
date="2013-02-10 15:42:07"
title="Feature Extraction/Selection - What I've learnt so far"
tag=['machine-learning-2']
category=['Machine Learning']
+++

<p>A couple of weeks ago I wrote about <a href="http://www.markhneedham.com/blog/2013/01/31/kaggle-digit-recognizer-a-feature-extraction-fail/">some feature extraction work that I'd done</a> on the <a href="http://www.kaggle.com/c/digit-recognizer">Kaggle Digit Recognizer</a> data set and having realised that I had no idea what I was doing I thought I should probably learn a bit more.</p>


<p>I came across Dunja Mladenic's '<a href="http://videolectures.net/slsfs05_mladenic_drfsm">Dimensionality Reduction by Feature Selection in Machine Learning</a>' presentation in which she sweeps across the landscape of feature selection and explains how everything fits together.</p>


<p>The talk starts off by going through some reasons that we'd want to use dimensionality reduce/feature selection:</p>


<ul>
<li>Improve the prediction performance</li>
<li>Improve learning efficiency</li>
<li>Provide faster predictors possibly requesting less information on the original data</li>
<li>Reduce complexity of the learned results, enable better understanding of the underlying process</li>
</ul>

<p>Mladenic suggests that there are a few ways we can go about reducing the dimensionality of data:</p>


<ul>
<li>Selecting a subset of the original features</li>
<li>Constructing features to replace the original features</li>
<li>Using background knowledge to construct new features to be used in addition to the original features</li>
</ul>

<p>The talk focuses on the first of these and a lot of it focuses on how we can go about using feature selection as a pre-processing step on our data sets.</p>


<p>The approach seems to involve either starting with all the features and removing them one at a time and seeing how the outcome is affected or starting with none of the features and adding them one at a time.</p>


<p>However, about half way through the talk Mladenic points out that <strong>some algorithms actually have feature selection built into them</strong> so there's no need to have the pre-processing step.</p>


<p>I think this is the case with <a href="http://en.wikipedia.org/wiki/Random_forest">random forests of decision trees</a> because the decision trees are constructed by taking into account which features give the greatest <a href="http://en.wikipedia.org/wiki/Information_gain_in_decision_trees">information gain</a> so low impact features are less likely to be used.</p>


<p>I previously wrote <a href="http://www.markhneedham.com/blog/2013/01/08/kaggle-digit-recognizer-finding-pixels-with-no-variance-using-r/">a blog post describing how I removed all the features with zero variance</a> from the data set and after submitting a random forest trained on the new data set we saw no change in accuracy which proved the point.</p>


<p>I also came across an interesting paper by Isabelle Guyon & Andre Elisseeff titled '<a href="http://clopinet.com/isabelle/Papers/guyon03a.pdf">An Introduction to Variable and Feature Selection</a>' which has a flow chart-ish set of questions to help you work out where to start.</p>


<p>One of the things I picked up from reading this paper is that if you have domain knowledge then <strong>you might be able to construct a better set of features by making use of this knowledge</strong>.</p>


<p>Another suggestion is to <strong>come up with a variable ranking for each feature</strong> i.e. how much that feature contributes to the outcome/prediction. This is something also suggested in the <a href="https://class.coursera.org/dataanalysis-001/class/index">Coursera Data Analysis course</a> and in R we can use the <cite><a href="http://web.njit.edu/all_topics/Prog_Lang_Docs/html/library/base/html/glm.html">glm</a></cite> function to help work this out.</p>


<p>The authors also point out that we should separate the problem of model selection (i.e. working out which features to use) from the problem of testing our classifier.</p>


<p>To test the classifier we'd most likely keep a test set aside but we shouldn't use this data for testing feature selection, rather we should use the training data. <a href="http://en.wikipedia.org/wiki/Cross-validation_(statistics)">Cross validation</a> probably works best here.</p>


<p>There's obviously more covered in the presentation & paper than what I've covered here but I've found that in general the material I've come across tends to drift towards being quite abstract/theoretical and therefore quite difficult for me to follow.</p>


<p>If anyone has come across any articles/books which explain how to go about feature selection using an example I'd love to read it/them!</p>

