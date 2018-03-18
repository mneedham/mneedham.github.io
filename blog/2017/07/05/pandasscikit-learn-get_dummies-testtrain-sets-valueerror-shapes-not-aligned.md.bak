+++
draft = false
date="2017-07-05 15:42:08"
title="Pandas/scikit-learn: get_dummies test/train sets - ValueError: shapes not aligned"
tag=['python', 'pandas']
category=['Python']
description="How do I use panda's get_dummies function to generate matching dummy columns across training and test datasets so that scikit-learn models can be trained?"
+++

<p>
I've been using panda's <cite><a href="https://pandas.pydata.org/pandas-docs/stable/generated/pandas.get_dummies.html">get_dummies</a></cite> function to generate dummy columns for categorical variables to use with scikit-learn, but noticed that it sometimes doesn't work as I expect.</p>


<h3>Prerequisites</h3>


~~~python

import pandas as pd
import numpy as np
from sklearn import linear_model
~~~

<p>Let's say we have the following training and test sets:</p>


<h3>Training set</h3>


~~~python

train = pd.DataFrame({"letter":["A", "B", "C", "D"], "value": [1, 2, 3, 4]})
X_train = train.drop(["value"], axis=1)
X_train = pd.get_dummies(X_train)
y_train = train["value"]~~~

<h3>Test set</h3>


~~~python

test = pd.DataFrame({"letter":["D", "D", "B", "E"], "value": [4, 5, 7, 19]})
X_test = test.drop(["value"], axis=1)
X_test = pd.get_dummies(X_test)
y_test = test["value"]
~~~

<p>Now say we want to train a linear model on our training set and then use it to predict the values in our test set:</p>


<h3>Train the model</h3>


~~~python

lr = linear_model.LinearRegression()
model = lr.fit(X_train, y_train)
~~~

<h3>Test the model</h3>


~~~python

model.score(X_test, y_test)
~~~


~~~text

ValueError: shapes (4,3) and (4,) not aligned: 3 (dim 1) != 4 (dim 0)
~~~

<p>
Hmmm that didn't go to plan. If we print <cite>X_train</cite> and <cite>X_test</cite> it might help shed some light:
</p>


<h3>Checking the train/test datasets</h3>


~~~python

print(X_train)
~~~


~~~text

   letter_A  letter_B  letter_C  letter_D
0         1         0         0         0
1         0         1         0         0
2         0         0         1         0
3         0         0         0         1
~~~


~~~python

print(X_test)
~~~


~~~text

   letter_B  letter_D  letter_E
0         0         1         0
1         0         1         0
2         1         0         0
3         0         0         1
~~~

<p>They do indeed have different shapes and some different column names because the test set contained some values that weren't present in the training set.
</p>


<p>
We can fix this by <a href="https://github.com/pandas-dev/pandas/issues/8918#issuecomment-145490689">making the 'letter' field categorical</a> before we run the <cite>get_dummies</cite> method over the dataframe. At the moment the field is of type 'object':
</p>


<h3>Column types</h3>


~~~python

print(train.info)
~~~


~~~text

<class 'pandas.core.frame.DataFrame'>
RangeIndex: 4 entries, 0 to 3
Data columns (total 2 columns):
letter    4 non-null object
value     4 non-null int64
dtypes: int64(1), object(1)
memory usage: 144.0+ bytes
~~~

<p>
We can fix this by converting the 'letter' field to the type 'category' and setting the list of allowed values to be the unique set of values in the train/test sets.
</p>


<h3>
All allowed values
</h3>


~~~python

all_data = pd.concat((train,test))
for column in all_data.select_dtypes(include=[np.object]).columns:
    print(column, all_data[column].unique())
~~~


~~~text

letter ['A' 'B' 'C' 'D' 'E']
~~~

<p>
Now let's update the type of our 'letter' field in the train and test dataframes.
</p>


<h3>Type: 'category'</h3>


~~~python

all_data = pd.concat((train,test))

for column in all_data.select_dtypes(include=[np.object]).columns:
    train[column] = train[column].astype('category', categories = all_data[column].unique())
    test[column] = test[column].astype('category', categories = all_data[column].unique())
~~~

<p>
And now if we call <cite>get_dummies</cite> on either dataframe we'll get the same set of columns:
</p>


<h3>get_dummies: Take 2</h3>


~~~python

X_train = train.drop(["value"], axis=1)
X_train = pd.get_dummies(X_train)
print(X_train)
~~~


~~~text

   letter_A  letter_B  letter_C  letter_D  letter_E
0         1         0         0         0         0
1         0         1         0         0         0
2         0         0         1         0         0
3         0         0         0         1         0
~~~


~~~python

X_test = test.drop(["value"], axis=1)
X_test = pd.get_dummies(X_test)
print(X_train)
~~~


~~~text

   letter_A  letter_B  letter_C  letter_D  letter_E
0         0         0         0         1         0
1         0         0         0         1         0
2         0         1         0         0         0
3         0         0         0         0         1
~~~

<p>Great! Now we should be able to train our model and use it against the test set:
</p>


<h3>Train the model: Take 2</h3>


~~~python

lr = linear_model.LinearRegression()
model = lr.fit(X_train, y_train)
~~~

<h3>Test the model: Take 2</h3>


~~~python

model.score(X_test, y_test)
~~~


~~~text

-1.0604490500863557
~~~

<p>
And we're done!
</p>

