+++
draft = false
date="2017-12-05 22:19:34"
title="scikit-learn: Building a multi class classification ensemble"
tag=['scikit-learn', 'ensemble', 'votingclassifier', 'classification', 'machine-learning']
category=['Python']
+++

<p>
For the Kaggle <a href="https://www.kaggle.com/c/spooky-author-identification">Spooky Author Identification</a> I wanted to combine multiple classifiers together into an ensemble and found the <a href="http://scikit-learn.org/stable/modules/ensemble.html#voting-classifier"><cite>VotingClassifier</cite></a> that does exactly that.
</p>


<p>
We need to predict the probability that a sentence is written by one of three authors so the VotingClassifier needs to make a  'soft' prediction. If we only needed to know the most likely author we could have it make a 'hard' prediction instead.
</p>


<p>
We start with three classifiers which generate different n-gram based features. The code for those is as follows:
</p>




~~~python

from sklearn import linear_model
from sklearn.ensemble import VotingClassifier
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

ngram_pipe = Pipeline([
    ('cv', CountVectorizer(ngram_range=(1, 2))),
    ('mnb', MultinomialNB())
])

unigram_log_pipe = Pipeline([
    ('cv', CountVectorizer()),
    ('logreg', linear_model.LogisticRegression())
])
~~~

<p>We can combine those classifiers together like this:</p>



~~~python

classifiers = [
    ("ngram", ngram_pipe),
    ("unigram", unigram_log_pipe),
]

mixed_pipe = Pipeline([
    ("voting", VotingClassifier(classifiers, voting="soft"))
])
~~~

<p>
Now it's time to test our ensemble. I got the code for the test function from <a href="https://www.kaggle.com/sohier/intermediate-tutorial-python/">Sohier Dane</a>'s tutorial.
</p>



~~~python

import pandas as pd
import numpy as np

from sklearn.model_selection import StratifiedKFold
from sklearn import metrics

Y_COLUMN = "author"
TEXT_COLUMN = "text"


def test_pipeline(df, nlp_pipeline):
    y = df[Y_COLUMN].copy()
    X = pd.Series(df[TEXT_COLUMN])
    rskf = StratifiedKFold(n_splits=5, random_state=1)
    losses = []
    accuracies = []
    for train_index, test_index in rskf.split(X, y):
        X_train, X_test = X[train_index], X[test_index]
        y_train, y_test = y[train_index], y[test_index]
        nlp_pipeline.fit(X_train, y_train)
        losses.append(metrics.log_loss(y_test, nlp_pipeline.predict_proba(X_test)))
        accuracies.append(metrics.accuracy_score(y_test, nlp_pipeline.predict(X_test)))

    print("{kfolds log losses: {0}, mean log loss: {1}, mean accuracy: {2}".format(
        str([str(round(x, 3)) for x in sorted(losses)]),
        round(np.mean(losses), 3),
        round(np.mean(accuracies), 3)
    ))

train_df = pd.read_csv("train.csv", usecols=[Y_COLUMN, TEXT_COLUMN])
test_pipeline(train_df, mixed_pipe)
~~~

<p>
Let's run <a href="https://gist.github.com/mneedham/0f640497ae3c662fc89fda199b5b7833">the script</a>:
</p>



~~~text

kfolds log losses: ['0.388', '0.391', '0.392', '0.397', '0.398'], mean log loss: 0.393 mean accuracy: 0.849
~~~

<p>
Looks good. 
</p>


<p>
I've actually got several other classifiers as well but I'm not sure which ones should be part of the ensemble. In a future post we'll look at how to use <a href="http://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html">GridSearch</a> to work that out.
</p>

