+++
draft = false
date="2017-06-16 05:55:29"
title="scikit-learn: Random forests - Feature Importance"
tag=['kaggle', 'python', 'scikit-learn', 'data-science', 'random-forest']
category=['Data Science', 'Python']
+++

<p>
As I <a href="http://www.markhneedham.com/blog/2017/06/04/kaggle-house-prices-advanced-regression-techniques-trying-fill-missing-values/">mentioned in a blog post a couple of weeks ago</a>, I've been playing around with the <a href="https://www.kaggle.com/c/house-prices-advanced-regression-techniques">Kaggle House Prices competition</a> and the most recent thing I tried was training a random forest regressor. 
</p>


<p>
Unfortunately, although it gave me better results locally it got a worse score on the unseen data, which I figured meant I'd <a href="https://en.wikipedia.org/wiki/Overfitting">overfitted the model</a>.
</p>


<p>
I wasn't really sure how to work out if that theory was true or not, but by chance I was reading Chris Albon's blog and found a post where he explains how to <a href="https://chrisalbon.com/machine-learning/random_forest_classifier_example_scikit.html">inspect the importance of every feature in a random forest</a>. Just what I needed!
</p>


<p>
Stealing from Chris' post I wrote the following code to work out the feature importance for my dataset:
</p>


<h3>Prerequisites</h3>


~~~python

import numpy as np
import pandas as pd

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

# We'll use this library to make the display pretty
from tabulate import tabulate
~~~

<h3>Load Data</h3>


~~~python

train = pd.read_csv('train.csv')

# the model can only handle numeric values so filter out the rest
data = train.select_dtypes(include=[np.number]).interpolate().dropna()
~~~


<h3>Split train/test sets</h3>


~~~python

y = train.SalePrice
X = data.drop(["SalePrice", "Id"], axis=1)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42, test_size=.33)
~~~

<h3>Train model</h3>


~~~python

clf = RandomForestRegressor(n_jobs=2, n_estimators=1000)
model = clf.fit(X_train, y_train)
~~~


<h3>Feature Importance</h3>


~~~python

headers = ["name", "score"]
values = sorted(zip(X_train.columns, model.feature_importances_), key=lambda x: x[1] * -1)
print(tabulate(values, headers, tablefmt="plain"))
~~~


~~~bash

name                 score
OverallQual    0.553829
GrLivArea      0.131
BsmtFinSF1     0.0374779
TotalBsmtSF    0.0372076
1stFlrSF       0.0321814
GarageCars     0.0226189
GarageArea     0.0215719
LotArea        0.0214979
YearBuilt      0.0184556
2ndFlrSF       0.0127248
YearRemodAdd   0.0126581
WoodDeckSF     0.0108077
OpenPorchSF    0.00945239
LotFrontage    0.00873811
TotRmsAbvGrd   0.00803121
GarageYrBlt    0.00760442
BsmtUnfSF      0.00715158
MasVnrArea     0.00680341
ScreenPorch    0.00618797
Fireplaces     0.00521741
OverallCond    0.00487722
MoSold         0.00461165
MSSubClass     0.00458496
BedroomAbvGr   0.00253031
FullBath       0.0024245
YrSold         0.00211638
HalfBath       0.0014954
KitchenAbvGr   0.00140786
BsmtFullBath   0.00137335
BsmtFinSF2     0.00107147
EnclosedPorch  0.000951266
3SsnPorch      0.000501238
PoolArea       0.000261668
LowQualFinSF   0.000241304
BsmtHalfBath   0.000179506
MiscVal        0.000154799
~~~

<p>
So <cite>OverallQual</cite> is quite a good predictor but then there's a steep fall to <cite>GrLivArea</cite> before things really tail off after <cite>WoodDeckSF</cite>.  
</p>


<p>
I think this is telling us that a lot of these features aren't useful at all and can be removed from the model. There are also a bunch of categorical/factor variables that have been stripped out of the model but might be predictive of the house price. 
</p>


<p>
These are the next things I'm going to explore:
</p>


<ul>

<li>
Make the categorical variables numeric (perhaps by using <a href="http://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html">one hot encoding</a> for some of them)
</li>

<li>
Remove the most predictive features and build a model that only uses the other features
</li>

</ul>
