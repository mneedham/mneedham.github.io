+++
draft = false
date="2017-07-05 14:31:04"
title="Pandas: Find rows where column/field is null"
tag=['python', 'pandas', 'data-science']
category=['Python']
description="In this post we look at how to find null values in a Pandas dataframe."
+++

<p>
In my continued playing around with the <a href="https://www.kaggle.com/c/house-prices-advanced-regression-techniques">Kaggle house prices dataset</a> I wanted to find any columns/fields that have null values in. 
</p>


<p>
If we want to get a count of the number of null fields by column we can use the following code, adapted from <a href="https://www.kaggle.io/svf/1188722/9f7f512433ad6a3bff46445a847dfc15/__results__.html#Missing-Value-Imputation">Poonam Ligade's kernel</a>:
</p>


<h3>Prerequisites</h3>


~~~python

import pandas as pd
~~~

<h3>Count the null columns</h3>


~~~python

train = pd.read_csv("train.csv")
null_columns=train.columns[train.isnull().any()]
train[null_columns].isnull().sum()
~~~


~~~text

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
So there are lots of different columns containing null values. What if we want to find the solitary row which has 'Electrical' as null? 
</p>


<h3>Single column is null</h3>


~~~python

print(train[train["Electrical"].isnull()][null_columns])
~~~


~~~text

      LotFrontage Alley MasVnrType  MasVnrArea BsmtQual BsmtCond BsmtExposure  \
1379         73.0   NaN       None         0.0       Gd       TA           No   

     BsmtFinType1 BsmtFinType2 Electrical FireplaceQu GarageType  GarageYrBlt  \
1379          Unf          Unf        NaN         NaN    BuiltIn       2007.0   

     GarageFinish GarageQual GarageCond PoolQC Fence MiscFeature  
1379          Fin         TA         TA    NaN   NaN         NaN  
~~~

<p>
And what if we want to return <a href="https://stackoverflow.com/questions/14247586/python-pandas-how-to-select-rows-with-one-or-more-nulls-from-a-dataframe-without">every row that contains at least one null value</a>? That's not too difficult - it's just a combination of the code in the previous two sections:
</p>


<h3>All null columns</h3>


~~~python

print(train[train.isnull().any(axis=1)][null_columns].head())
~~~


~~~text

   LotFrontage Alley MasVnrType  MasVnrArea BsmtQual BsmtCond BsmtExposure  \
0         65.0   NaN    BrkFace       196.0       Gd       TA           No   
1         80.0   NaN       None         0.0       Gd       TA           Gd   
2         68.0   NaN    BrkFace       162.0       Gd       TA           Mn   
3         60.0   NaN       None         0.0       TA       Gd           No   
4         84.0   NaN    BrkFace       350.0       Gd       TA           Av   

  BsmtFinType1 BsmtFinType2 Electrical FireplaceQu GarageType  GarageYrBlt  \
0          GLQ          Unf      SBrkr         NaN     Attchd       2003.0   
1          ALQ          Unf      SBrkr          TA     Attchd       1976.0   
2          GLQ          Unf      SBrkr          TA     Attchd       2001.0   
3          ALQ          Unf      SBrkr          Gd     Detchd       1998.0   
4          GLQ          Unf      SBrkr          TA     Attchd       2000.0   

  GarageFinish GarageQual GarageCond PoolQC Fence MiscFeature  
0          RFn         TA         TA    NaN   NaN         NaN  
1          RFn         TA         TA    NaN   NaN         NaN  
2          RFn         TA         TA    NaN   NaN         NaN  
3          Unf         TA         TA    NaN   NaN         NaN  
4          RFn         TA         TA    NaN   NaN         NaN  
~~~

<p>
Hope that helps future Mark!
</p>

