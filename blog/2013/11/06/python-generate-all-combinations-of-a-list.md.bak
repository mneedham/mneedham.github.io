+++
draft = false
date="2013-11-06 07:25:24"
title="Python: Generate all combinations of a list"
tag=['python']
category=['Python']
+++

<p>Nathan and I have been playing around with different <a href="http://scikit-learn.org/stable/auto_examples/">scikit-learn machine learning classifiers</a> and we wanted to run different combinations of features through each one and work out which gave the best result.</p>


<p>We started with a list of features:</p>



~~~python

all_columns = ["Fare", "Sex", "Pclass", 'Embarked']
~~~

<p><a href="http://docs.python.org/2/library/itertools.html#itertools.combinations">itertools#combinations</a> allows us to create combinations with a length of our choice:</p>



~~~python

>>> import itertools as it
>>> list(it.combinations(all_columns, 3))
[('Fare', 'Sex', 'Pclass'), ('Fare', 'Sex', 'Embarked'), ('Fare', 'Pclass', 'Embarked'), ('Sex', 'Pclass', 'Embarked')]
~~~

<p>We wanted to create combinations of arbitrary length so we wanted to combine a few invocations of that functions like this:</p>



~~~python

>>> list(it.combinations(all_columns, 2)) + list(it.combinations(all_columns, 3))
[('Fare', 'Sex'), ('Fare', 'Pclass'), ('Fare', 'Embarked'), ('Sex', 'Pclass'), ('Sex', 'Embarked'), ('Pclass', 'Embarked'), ('Fare', 'Sex', 'Pclass'), ('Fare', 'Sex', 'Embarked'), ('Fare', 'Pclass', 'Embarked'), ('Sex', 'Pclass', 'Embarked')]
~~~

<p>If we generify that code to remove the repetition we end up with the following:</p>



~~~python

all_the_features = []
for r in range(1, len(all_columns) + 1):
	all_the_features + list(it.combinations(all_columns, r))

>>> all_the_features
[('Fare',), ('Sex',), ('Pclass',), ('Embarked',), ('Fare', 'Sex'), ('Fare', 'Pclass'), ('Fare', 'Embarked'), ('Sex', 'Pclass'), ('Sex', 'Embarked'), ('Pclass', 'Embarked'), ('Fare', 'Sex', 'Pclass'), ('Fare', 'Sex', 'Embarked'), ('Fare', 'Pclass', 'Embarked'), ('Sex', 'Pclass', 'Embarked'), ('Fare', 'Sex', 'Pclass', 'Embarked')]
~~~ 

<p>or if we want to use reduce instead:</p>



~~~python

>>> reduce(lambda acc, x: acc + list(it.combinations(all_columns, x)), range(1, len(all_columns) + 1), [])
[('Fare',), ('Sex',), ('Pclass',), ('Embarked',), ('Fare', 'Sex'), ('Fare', 'Pclass'), ('Fare', 'Embarked'), ('Sex', 'Pclass'), ('Sex', 'Embarked'), ('Pclass', 'Embarked'), ('Fare', 'Sex', 'Pclass'), ('Fare', 'Sex', 'Embarked'), ('Fare', 'Pclass', 'Embarked'), ('Sex', 'Pclass', 'Embarked'), ('Fare', 'Sex', 'Pclass', 'Embarked')]
~~~

<p>I imagine there is probably a simpler way that I don't know about yet…!</p>

