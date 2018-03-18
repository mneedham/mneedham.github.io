+++
draft = false
date="2013-11-09 13:58:54"
title="Python: Making scikit-learn and pandas play nice"
tag=['python']
category=['Python']
+++

<p>In the last post I wrote about <a href="http://junctionbox.ca/">Nathan</a> and my <a href="http://www.markhneedham.com/blog/2013/10/30/kaggle-titanic-python-pandas-attempt/">attempts at the <a href="http://www.kaggle.com/c/titanic-gettingStarted">Kaggle Titanic Problem</a> I mentioned that we our next step was to try out <a href="http://scikit-learn.org/stable/tutorial/">scikit-learn</a> so I thought I should summarise where we've got up to.</p>


<p>We needed to write a classification algorithm to work out whether a person onboard the Titanic survived and luckily scikit-learn has <a href="http://scikit-learn.org/stable/supervised_learning.html#supervised-learning">extensive documentation on each of the algorithms</a>.</p>


<p>Unfortunately almost all those examples use <a href="http://www.numpy.org/">numpy</a> data structures and we'd loaded the data using <a href="http://pandas.pydata.org/">pandas</a> and didn't particularly want to switch back!</p>


<p>Luckily it was really easy to get the data into numpy format by calling 'values' on the pandas data structure, something we learnt from <a href="http://stackoverflow.com/questions/17682613/how-to-convert-a-pandas-dataframe-subset-of-columns-and-rows-into-a-numpy-array">a reply on Stack Overflow</a>.</p>


<p>For example if we were to wire up an <a href="http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.ExtraTreesClassifier.html">ExtraTreesClassifier</a> which worked out survival rate based on the 'Fare' and 'Pclass' attributes we could write the following code:</p>



~~~python

import pandas as pd
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.cross_validation import cross_val_score

train_df = pd.read_csv("train.csv")

et = ExtraTreesClassifier(n_estimators=100, max_depth=None, min_samples_split=1, random_state=0)

columns = ["Fare", "Pclass"]

labels = train_df["Survived"].values
features = train_df[list(columns)].values
	
et_score = cross_val_score(et, features, labels, n_jobs=-1).mean()

print("{0} -> ET: {1})".format(columns, et_score))
~~~

<p>To start with with read in the CSV file which looks like this:</p>



~~~bash

$ head -n5 train.csv 
PassengerId,Survived,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked
1,0,3,"Braund, Mr. Owen Harris",male,22,1,0,A/5 21171,7.25,,S
2,1,1,"Cumings, Mrs. John Bradley (Florence Briggs Thayer)",female,38,1,0,PC 17599,71.2833,C85,C
3,1,3,"Heikkinen, Miss. Laina",female,26,0,0,STON/O2. 3101282,7.925,,S
4,1,1,"Futrelle, Mrs. Jacques Heath (Lily May Peel)",female,35,1,0,113803,53.1,C123,S
~~~

</p>
Next we create our classifier which "<em>fits a number of randomized decision trees (a.k.a. extra-trees) on various sub-samples of the dataset and use averaging to improve the predictive accuracy and control over-fitting.</em>". i.e. a better version of a <a href="http://www.markhneedham.com/blog/2012/10/27/kaggle-digit-recognizer-mahout-random-forest-attempt/">random forest</a>.</p>


<p>On the next line we describe the features we want the classifier to use, then we convert the labels and features into numpy format so we can pass the to the classifier.</p>


<p>Finally we call the <cite><a href="http://scikit-learn.org/stable/modules/generated/sklearn.cross_validation.cross_val_score.html">cross_val_score</a></cite> function which splits our training data set into training and test components and trains the classifier against the former and checks its accuracy using the latter.</p>


<p>If we run this code we'll get roughly the following output:</p>



~~~bash

$ python et.py

['Fare', 'Pclass'] -> ET: 0.687991021324)
~~~

<p>This is actually a worse accuracy than we'd get by saying that females survived and males didn't.</p>


<p>We can introduce 'Sex' into the classifier by adding it to the list of columns:</p>



~~~python

columns = ["Fare", "Pclass", "Sex"]
~~~

<p>If we re-run the code we'll get the following error:</p>



~~~bash

$ python et.py

An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (514, 0))
...
Traceback (most recent call last):
  File "et.py", line 14, in <module>
    et_score = cross_val_score(et, features, labels, n_jobs=-1).mean()
  File "/Library/Python/2.7/site-packages/scikit_learn-0.14.1-py2.7-macosx-10.8-intel.egg/sklearn/cross_validation.py", line 1152, in cross_val_score
    for train, test in cv)
  File "/Library/Python/2.7/site-packages/scikit_learn-0.14.1-py2.7-macosx-10.8-intel.egg/sklearn/externals/joblib/parallel.py", line 519, in __call__
    self.retrieve()
  File "/Library/Python/2.7/site-packages/scikit_learn-0.14.1-py2.7-macosx-10.8-intel.egg/sklearn/externals/joblib/parallel.py", line 450, in retrieve
    raise exception_type(report)
sklearn.externals.joblib.my_exceptions.JoblibValueError/Library/Python/2.7/site-packages/scikit_learn-0.14.1-py2.7-macosx-10.8-intel.egg/sklearn/externals/joblib/my_exceptions.py:26: DeprecationWarning: BaseException.message has been deprecated as of Python 2.6
  self.message,
: JoblibValueError
___________________________________________________________________________
Multiprocessing exception:
...
ValueError: could not convert string to float: male
___________________________________________________________________________
~~~

<p>This is a slightly verbose way of telling us that we can't pass non numeric features to the classifier - in this case 'Sex' has the values 'female' and 'male'. We'll need to write a function to replace those values with numeric equivalents.</p>



~~~python

train_df["Sex"] = train_df["Sex"].apply(lambda sex: 0 if sex == "male" else 1)
~~~

<p>Now if we re-run the classifier we'll get a slightly more accurate prediction:</p>



~~~bash

$ python et.py 
['Fare', 'Pclass', 'Sex'] -> ET: 0.813692480359)
~~~

<p>The next step is use the classifier against the test data set so let's load the data and run the prediction:</p>



~~~python

test_df = pd.read_csv("test.csv")

et.fit(features, labels)
et.predict(test_df[columns].values)
~~~

<p>Now if we run that:</p>



~~~bash

$ python et.py 
['Fare', 'Pclass', 'Sex'] -> ET: 0.813692480359)
Traceback (most recent call last):
  File "et.py", line 22, in <module>
    et.predict(test_df[columns].values)
  File "/Library/Python/2.7/site-packages/scikit_learn-0.14.1-py2.7-macosx-10.8-intel.egg/sklearn/ensemble/forest.py", line 444, in predict
    proba = self.predict_proba(X)
  File "/Library/Python/2.7/site-packages/scikit_learn-0.14.1-py2.7-macosx-10.8-intel.egg/sklearn/ensemble/forest.py", line 479, in predict_proba
    X = array2d(X, dtype=DTYPE)
  File "/Library/Python/2.7/site-packages/scikit_learn-0.14.1-py2.7-macosx-10.8-intel.egg/sklearn/utils/validation.py", line 91, in array2d
    X_2d = np.asarray(np.atleast_2d(X), dtype=dtype, order=order)
  File "/System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python/numpy/core/numeric.py", line 235, in asarray
    return array(a, dtype, copy=False, order=order)
ValueError: could not convert string to float: male
~~~

<p>which is the same problem we had earlier! We need to replace the 'male' and 'female' values in the test set too so we'll pull out a function to do that now.</p>



~~~python

def replace_non_numeric(df):
	df["Sex"] = df["Sex"].apply(lambda sex: 0 if sex == "male" else 1)
	return df
~~~

<p>Now we'll call that function with our training and test data frames:</p>



~~~python

train_df = replace_non_numeric(pd.read_csv("train.csv"))
...
test_df = replace_non_numeric(pd.read_csv("test.csv"))
~~~

<p>If we run the program again:</p>



~~~bash

$ python et.py 
['Fare', 'Pclass', 'Sex'] -> ET: 0.813692480359)
Traceback (most recent call last):
  File "et.py", line 26, in <module>
    et.predict(test_df[columns].values)
  File "/Library/Python/2.7/site-packages/scikit_learn-0.14.1-py2.7-macosx-10.8-intel.egg/sklearn/ensemble/forest.py", line 444, in predict
    proba = self.predict_proba(X)
  File "/Library/Python/2.7/site-packages/scikit_learn-0.14.1-py2.7-macosx-10.8-intel.egg/sklearn/ensemble/forest.py", line 479, in predict_proba
    X = array2d(X, dtype=DTYPE)
  File "/Library/Python/2.7/site-packages/scikit_learn-0.14.1-py2.7-macosx-10.8-intel.egg/sklearn/utils/validation.py", line 93, in array2d
    _assert_all_finite(X_2d)
  File "/Library/Python/2.7/site-packages/scikit_learn-0.14.1-py2.7-macosx-10.8-intel.egg/sklearn/utils/validation.py", line 27, in _assert_all_finite
    raise ValueError("Array contains NaN or infinity.")
ValueError: Array contains NaN or infinity.
~~~

<p>There are missing values in the test set so we'll replace those with average values from our training set using an <a href="http://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.Imputer.html">Imputer</a>:</p>



~~~python

from sklearn.preprocessing import Imputer

imp = Imputer(missing_values='NaN', strategy='mean', axis=0)
imp.fit(features)

test_df = replace_non_numeric(pd.read_csv("test.csv"))

et.fit(features, labels)
print et.predict(imp.transform(test_df[columns].values))
~~~

<p>If we run that it completes successfully:</p>



~~~python

$ python et.py 
['Fare', 'Pclass', 'Sex'] -> ET: 0.813692480359)
[0 1 0 0 1 0 0 1 1 0 0 0 1 0 1 1 0 0 1 1 0 0 1 0 1 0 1 0 1 0 0 0 1 0 1 0 0
 0 0 1 0 0 0 1 1 0 0 0 1 1 0 0 1 1 0 0 0 0 0 1 0 0 0 1 0 1 1 0 0 1 1 0 1 0
 1 0 0 1 0 1 1 0 0 0 0 0 1 0 1 0 1 0 1 0 0 0 1 0 0 0 1 0 0 0 0 0 0 0 0 0 0
 1 1 1 1 0 0 1 1 1 1 0 1 0 0 1 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
 0 0 1 0 0 1 0 0 1 0 0 1 1 1 1 0 0 1 0 0 1 0 0 0 0 0 0 1 1 1 1 1 0 0 1 0 1
 0 1 0 0 0 0 0 0 0 0 0 1 0 0 0 1 0 0 1 0 0 1 0 1 0 0 0 0 1 0 0 1 0 1 0 1 0
 1 0 1 0 0 1 0 0 0 1 0 0 0 0 1 0 1 1 1 1 1 0 0 0 1 0 1 0 1 0 0 0 0 0 0 0 1
 0 0 0 1 1 0 0 0 0 0 0 1 0 1 1 0 1 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 1 0 0
 1 0 0 0 0 0 0 0 1 1 1 0 1 0 0 0 0 1 1 1 1 0 0 0 0 0 0 0 1 0 1 0 0 0 1 0 0
 1 0 0 0 0 0 0 0 0 0 1 0 1 0 1 0 1 1 0 0 0 1 0 1 0 0 1 0 1 1 0 1 0 0 0 1 1
 0 1 0 0 1 1 0 0 0 0 0 0 0 1 0 1 0 0 0 0 1 1 0 0 0 1 0 1 0 0 1 0 1 0 0 1 0
 0 1 1 1 1 0 0 1 0 0 0]
~~~

<p>The final step is to add these values to our test data frame and then write that to a file so we can submit it to Kaggle.</p>


<p>The type of those values is 'numpy.ndarray' which we can convert to a pandas Series quite easily:</p>



~~~python

predictions = et.predict(imp.transform(test_df[columns].values))
test_df["Survived"] = pd.Series(predictions)
~~~

<p>We can then write the 'PassengerId' and 'Survived' columns to a file:</p>



~~~python

test_df.to_csv("foo.csv", cols=['PassengerId', 'Survived'], index=False)
~~~

<p>Then output file looks like this:</p>



~~~bash

$ head -n5 foo.csv 
PassengerId,Survived
892,0
893,1
894,0
~~~

<p>The <a href="https://github.com/mneedham/kaggle-titanic/blob/master/et.py">code we've written is on github</a> in case it's useful to anyone.</p>

