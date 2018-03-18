+++
draft = false
date="2017-06-04 09:22:47"
title="Kaggle: House Prices: Advanced Regression Techniques - Trying to fill in missing values"
tag=['kaggle', 'python']
category=['Data Science', 'Python']
+++

<p>
I've been playing around with the data in Kaggle's <a href="https://www.kaggle.com/c/house-prices-advanced-regression-techniques">House Prices: Advanced Regression Techniques</a> and while replicating <a href="https://www.kaggle.com/poonaml/house-prices-data-exploration-and-visualisation">Poonam Ligade's exploratory analysis</a> I wanted to see if I could create a model to fill in some of the missing values.
</p>


<p>
Poonam wrote the following code to identify which columns in the dataset had the most missing values:
</p>



~~~python

import pandas as pd
train = pd.read_csv('train.csv')
null_columns=train.columns[train.isnull().any()]

>>> print(train[null_columns].isnull().sum())
LotFrontage      259
Alley           1369
MasVnrType         8
MasVnrArea         8
BsmtQual          37
BsmtCond          37
BsmtExposure      38
BsmtFinType1      37
BsmtFinType2      38
Electrical         1
FireplaceQu      690
GarageType        81
GarageYrBlt       81
GarageFinish      81
GarageQual        81
GarageCond        81
PoolQC          1453
Fence           1179
MiscFeature     1406
dtype: int64
~~~

<p>
The one that I'm most interested in is <cite>LotFrontage</cite>, which describes 'Linear feet of street connected to property'. There are a few other columns related to lots so I thought I might be able to use them to fill in the missing <cite>LotFrontage</cite> values.
</p>


<p>
We can write the following code to find a selection of the rows missing a <cite>LotFrontage</cite> value:
</p>



~~~python

cols = [col for col in train.columns if col.startswith("Lot")]
missing_frontage = train[cols][train["LotFrontage"].isnull()]

>>> print(missing_frontage.head())
    LotFrontage  LotArea LotShape LotConfig
7           NaN    10382      IR1    Corner
12          NaN    12968      IR2    Inside
14          NaN    10920      IR1    Corner
16          NaN    11241      IR1   CulDSac
24          NaN     8246      IR1    Inside
~~~

<p>
I want to use <a href="http://scikit-learn.org/">scikit-learn</a>'s <a href="http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html">linear regression model</a> which only works with numeric values so we need to convert our categorical variables into numeric equivalents. We can use pandas <a href="https://pandas.pydata.org/pandas-docs/stable/generated/pandas.get_dummies.html">get_dummies</a> function for this.
</p>


<p>
Let's try it out on the <cite>LotShape</cite> column:
</p>



~~~python

sub_train = train[train.LotFrontage.notnull()]
dummies = pd.get_dummies(sub_train[cols].LotShape)

>>> print(dummies.head())
   IR1  IR2  IR3  Reg
0    0    0    0    1
1    0    0    0    1
2    1    0    0    0
3    1    0    0    0
4    1    0    0    0
~~~

<p>
Cool, that looks good. We can do the same with <cite>LotConfig</cite> and then we need to add these new columns onto the original DataFrame. We can use pandas <a href="https://pandas.pydata.org/pandas-docs/stable/generated/pandas.concat.html">concat</a> function to do this.
</p>



~~~python

import numpy as np

data = pd.concat([
        sub_train[cols],
        pd.get_dummies(sub_train[cols].LotShape),
        pd.get_dummies(sub_train[cols].LotConfig)
    ], axis=1).select_dtypes(include=[np.number])

>>> print(data.head())
   LotFrontage  LotArea  IR1  IR2  IR3  Reg  Corner  CulDSac  FR2  FR3  Inside
0         65.0     8450    0    0    0    1       0        0    0    0       1
1         80.0     9600    0    0    0    1       0        0    1    0       0
2         68.0    11250    1    0    0    0       0        0    0    0       1
3         60.0     9550    1    0    0    0       1        0    0    0       0
4         84.0    14260    1    0    0    0       0        0    1    0       0
~~~

<p>
We can now split <cite>data</cite> into train and test sets and create a model.
</p>



~~~python

from sklearn import linear_model
from sklearn.model_selection import train_test_split

X = data.drop(["LotFrontage"], axis=1)
y = data.LotFrontage

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42, test_size=.33)

lr = linear_model.LinearRegression()

model = lr.fit(X_train, y_train)
~~~

<p>
Now it's time to give it a try on the test set:
</p>



~~~python

>>> print("R^2 is: \n", model.score(X_test, y_test))
R^2 is: 
 -0.84137438493
~~~

<p>
Hmm that didn't work too well - an R^2 score of less than 0 suggests that we'd be better off just predicting the average <cite>LotFrontage</cite> regardless of any of the other features. We can confirm that with the following code:
</p>



~~~python

from sklearn.metrics import r2_score

>>> print(r2_score(y_test, np.repeat(y_test.mean(), len(y_test))))
0.0
~~~

<p>
whereas if we had all of the values correct we'd get a score of 1: 
</p>



~~~python

>>> print(r2_score(y_test, y_test))
1.0
~~~

<p>
In summary, not a very successful experiment. Poonam derives a value for <cite>LotFrontage</cite> based on the square root of <cite>LotArea</cite> so perhaps that's the best we can do here.
</p>

