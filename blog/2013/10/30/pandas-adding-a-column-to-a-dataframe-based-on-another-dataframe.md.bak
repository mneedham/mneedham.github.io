+++
draft = false
date="2013-10-30 06:12:08"
title="pandas: Adding a column to a DataFrame (based on another DataFrame)"
tag=['python', 'pandas']
category=['Python']
+++

<p><a href="http://junctionbox.ca/">Nathan</a> and I have been working on the <a href="http://www.kaggle.com/c/titanic-gettingStarted">Titanic Kaggle problem</a> using the <a href="http://pandas.pydata.org/">pandas</a> data analysis library and one thing we wanted to do was add a column to a DataFrame indicating if someone survived.</p>


<p>We had the following (simplified) DataFrame containing some information about customers on board the Titanic:</p>



~~~python

def addrow(df, row):
    return df.append(pd.DataFrame(row), ignore_index=True)

customers = pd.DataFrame(columns=['PassengerId','Pclass','Name','Sex','Fare'])
customers = addrow(customers, [dict(PassengerId=892, Pclass=3, Name="Kelly, Mr. James", Sex="male", Fare=7.8292)])
customers = addrow(customers, [dict(PassengerId=893, Pclass=3, Name="Wilkes, Mrs. James (Ellen Needs)", Sex="female", Fare=7)])

>>> customers

     Fare                              Name  PassengerId  Pclass     Sex
0  7.8292                  Kelly, Mr. James          892       3    male
1  7.0000  Wilkes, Mrs. James (Ellen Needs)          893       3  female
~~~

<p>We wanted to add a 'Survived' column to that by doing a lookup in the <cite>survival_table</cite> below to work out the appropriate value:</p>



~~~python

survival_table = pd.DataFrame(columns=['Sex', 'Pclass', 'PriceDist', 'Survived'])

survival_table = addrow(survival_table, [dict(Pclass=1, Sex="female", PriceDist = 0, Survived = 0)])
survival_table = addrow(survival_table, [dict(Pclass=1, Sex="male", PriceDist = 0, Survived = 0)])
survival_table = addrow(survival_table, [dict(Pclass=1, Sex="female", PriceDist = 1, Survived = 0)])
survival_table = addrow(survival_table, [dict(Pclass=1, Sex="male", PriceDist = 1, Survived = 0)])
survival_table = addrow(survival_table, [dict(Pclass=1, Sex="female", PriceDist = 2, Survived = 1)])
survival_table = addrow(survival_table, [dict(Pclass=1, Sex="male", PriceDist = 2, Survived = 0)])
survival_table = addrow(survival_table, [dict(Pclass=1, Sex="female", PriceDist = 3, Survived = 1)])
survival_table = addrow(survival_table, [dict(Pclass=1, Sex="male", PriceDist = 3, Survived = 0)])

survival_table = addrow(survival_table, [dict(Pclass=2, Sex="female", PriceDist = 0, Survived = 0)])
survival_table = addrow(survival_table, [dict(Pclass=2, Sex="male", PriceDist = 0, Survived = 0)])
survival_table = addrow(survival_table, [dict(Pclass=2, Sex="female", PriceDist = 1, Survived = 1)])
survival_table = addrow(survival_table, [dict(Pclass=2, Sex="male", PriceDist = 1, Survived = 0)])
survival_table = addrow(survival_table, [dict(Pclass=2, Sex="female", PriceDist = 2, Survived = 1)])
survival_table = addrow(survival_table, [dict(Pclass=2, Sex="male", PriceDist = 2, Survived = 0)])
survival_table = addrow(survival_table, [dict(Pclass=2, Sex="female", PriceDist = 3, Survived = 1)])
survival_table = addrow(survival_table, [dict(Pclass=2, Sex="male", PriceDist = 3, Survived = 0)])

survival_table = addrow(survival_table, [dict(Pclass=3, Sex="female", PriceDist = 0, Survived = 1)])
survival_table = addrow(survival_table, [dict(Pclass=3, Sex="male", PriceDist = 0, Survived = 0)])
survival_table = addrow(survival_table, [dict(Pclass=3, Sex="female", PriceDist = 1, Survived = 1)])
survival_table = addrow(survival_table, [dict(Pclass=3, Sex="male", PriceDist = 1, Survived = 0)])
survival_table = addrow(survival_table, [dict(Pclass=3, Sex="female", PriceDist = 2, Survived = 0)])
survival_table = addrow(survival_table, [dict(Pclass=3, Sex="male", PriceDist = 2, Survived = 0)])
survival_table = addrow(survival_table, [dict(Pclass=3, Sex="female", PriceDist = 3, Survived = 0)])
survival_table = addrow(survival_table, [dict(Pclass=3, Sex="male", PriceDist = 3, Survived = 0)])

>>> survival_table

    Pclass  PriceDist     Sex  Survived
0        1          0  female         0
1        1          0    male         0
2        1          1  female         0
3        1          1    male         0
4        1          2  female         1
5        1          2    male         0
6        1          3  female         1
7        1          3    male         0
8        2          0  female         0
9        2          0    male         0
10       2          1  female         1
11       2          1    male         0
12       2          2  female         1
13       2          2    male         0
14       2          3  female         1
15       2          3    male         0
16       3          0  female         1
17       3          0    male         0
18       3          1  female         1
19       3          1    male         0
20       3          2  female         0
21       3          2    male         0
22       3          3  female         0
23       3          3    male         0
~~~

<p>To do this we can use the <cite><a href="http://pandas.pydata.org/pandas-docs/dev/generated/pandas.DataFrame.apply.html">DataFrame#apply</a></cite> function which allows us to map over each row.</p>


<p>Our initial attempt read like this:</p>



~~~python

def select_bucket(fare):
    if (fare >= 0 and fare < 10):
        return 0
    elif (fare >= 10 and fare < 20):
        return 1
    elif (fare >= 20 and fare < 30):
        return 2
    else:
        return 3

def calculate_survival(survival_table, customer):
    survival_row = survival_table[(survival_table["Sex"] == customer["Sex"]) & (survival_table["Pclass"] == customer["Pclass"]) & (survival_table["PriceDist"] == select_bucket(customer["Fare"]))]
    return survival_row["Survived"]

>>> customers["Survived"] = customers.apply(lambda customer: calculate_survival(survival_table, customer), axis=1)
~~~

<p>When we ran that we got the following exception:</p>



~~~python

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Library/Python/2.7/site-packages/pandas/core/frame.py", line 2119, in __setitem__
    self._set_item(key, value)
  File "/Library/Python/2.7/site-packages/pandas/core/frame.py", line 2166, in _set_item
    NDFrame._set_item(self, key, value)
  File "/Library/Python/2.7/site-packages/pandas/core/generic.py", line 679, in _set_item
    self._data.set(key, value)
  File "/Library/Python/2.7/site-packages/pandas/core/internals.py", line 1781, in set
    self.insert(len(self.items), item, value)
  File "/Library/Python/2.7/site-packages/pandas/core/internals.py", line 1795, in insert
    self._add_new_block(item, value, loc=loc)
  File "/Library/Python/2.7/site-packages/pandas/core/internals.py", line 1911, in _add_new_block
    self.items, fastpath=True)
  File "/Library/Python/2.7/site-packages/pandas/core/internals.py", line 966, in make_block
    return klass(values, items, ref_items, ndim=values.ndim, fastpath=fastpath, placement=placement)
  File "/Library/Python/2.7/site-packages/pandas/core/internals.py", line 44, in __init__
    % (len(items), len(values)))
ValueError: Wrong number of items passed 1, indices imply 2
~~~

<p>After much googling and confusion as to why we were getting this error I tried printing out the result of calling apply rather than immediately assigning it and realised that the output wasn't what I expected:</p>



~~~python

>>> customers.apply(lambda customer: calculate_survival(survival_table, customer), axis=1)
   16  17
0 NaN   0
1   1 NaN
~~~

<p>I'd expected to get one column showing the survived values but instead we've got a 2x2 DataFrame. Adding some logging to the <cite>calculate_survival</cite> function revealed why:</p>



~~~python

def calculate_survival(survival_table, customer):
    survival_row = survival_table[(survival_table["Sex"] == customer["Sex"]) & (survival_table["Pclass"] == customer["Pclass"]) & (survival_table["PriceDist"] == select_bucket(customer["Fare"]))]
    print(type(survival_row["Survived"]))
    return survival_row["Survived"]

>>> customers.apply(lambda customer: calculate_survival(survival_table, customer), axis=1)
<class 'pandas.core.series.Series'>
<class 'pandas.core.series.Series'>
   16  17
0 NaN   0
1   1 NaN
~~~

<p>Our function is actually returning a Series object rather than a single value 0 or 1 which I found surprising. We can <a href="http://pandas.pydata.org/pandas-docs/stable/indexing.html#fast-scalar-value-getting-and-setting">use the <cite>iat</cite> function</a> to retrieve a scalar value from a Series:</p>



~~~python

def calculate_survival(survival_table, customer):
    survival_row = survival_table[(survival_table["Sex"] == customer["Sex"]) & (survival_table["Pclass"] == customer["Pclass"]) & (survival_table["PriceDist"] == select_bucket(customer["Fare"]))]
    return int(survival_row["Survived"].iat[0])

>>> customers.apply(lambda customer: calculate_survival(survival_table, customer), axis=1)
0    0
1    1
dtype: int64
~~~

<p>Now if we assign the output of that function like before it works as expected:</p>



~~~python

>>> customers["Survived"] = customers.apply(lambda customer: calculate_survival(survival_table, customer), axis=1)
>>> customers
     Fare                              Name  PassengerId  Pclass     Sex  Survived
0  7.8292                  Kelly, Mr. James          892       3    male         0
1  7.0000  Wilkes, Mrs. James (Ellen Needs)          893       3  female         1
~~~
