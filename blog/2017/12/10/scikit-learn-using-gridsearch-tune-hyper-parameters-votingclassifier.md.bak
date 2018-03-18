+++
draft = false
date="2017-12-10 07:55:43"
title="scikit-learn: Using GridSearch to tune the hyper-parameters of VotingClassifier"
tag=['python', 'scikit-learn', 'machine-learning', 'sklearn']
category=['Python']
+++

<p>
In my last blog post I showed how to create a multi class classification ensemble using scikit-learn's <cite><a href="http://scikit-learn.org/stable/modules/ensemble.html#voting-classifier">VotingClassifier</a></cite> and finished mentioning that I didn't know which classifiers should be part of the ensemble.
</p>


<p>
We need to get a better score with each of the classifiers in the ensemble otherwise they can be excluded.
</p>


<p>
We have a TF/IDF based classifier as well as well as the classifiers I wrote about in the last post. This is the code describing the classifiers:
</p>



~~~python

import pandas as pd
from sklearn import linear_model
from sklearn.ensemble import VotingClassifier
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

Y_COLUMN = "author"
TEXT_COLUMN = "text"

unigram_log_pipe = Pipeline([
    ('cv', CountVectorizer()),
    ('logreg', linear_model.LogisticRegression())
])

ngram_pipe = Pipeline([
    ('cv', CountVectorizer(ngram_range=(1, 2))),
    ('mnb', MultinomialNB())
])

tfidf_pipe = Pipeline([
    ('tfidf', TfidfVectorizer(min_df=3, max_features=None,
                              strip_accents='unicode', analyzer='word', token_pattern=r'\w{1,}',
                              ngram_range=(1, 3), use_idf=1, smooth_idf=1, sublinear_tf=1,
                              stop_words='english')),
    ('mnb', MultinomialNB())
])

classifiers = [
    ("ngram", ngram_pipe),
    ("unigram", unigram_log_pipe),
    ("tfidf", tfidf_pipe),
]

mixed_pipe = Pipeline([
    ("voting", VotingClassifier(classifiers, voting="soft"))
])
~~~

<p>
Now we're ready to work out which classifiers are needed. We'll use <a href="http://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html">GridSearchCV</a> to do this.
</p>



~~~python

from sklearn.model_selection import GridSearchCV


def combinations_on_off(num_classifiers):
    return [[int(x) for x in list("{0:0b}".format(i).zfill(num_classifiers))]
            for i in range(1, 2 ** num_classifiers)]


param_grid = dict(
    voting__weights=combinations_on_off(len(classifiers))
)

train_df = pd.read_csv("train.csv", usecols=[Y_COLUMN, TEXT_COLUMN])
y = train_df[Y_COLUMN].copy()
X = pd.Series(train_df[TEXT_COLUMN])

grid_search = GridSearchCV(mixed_pipe, param_grid=param_grid, n_jobs=-1, verbose=10, scoring="neg_log_loss")

grid_search.fit(X, y)

cv_results = grid_search.cv_results_

for mean_score, params in zip(cv_results["mean_test_score"], cv_results["params"]):
    print(params, mean_score)

print("Best score: %0.3f" % grid_search.best_score_)
print("Best parameters set:")
best_parameters = grid_search.best_estimator_.get_params()
for param_name in sorted(param_grid.keys()):
    print("\t%s: %r" % (param_name, best_parameters[param_name]))
~~~

<p>
Let's run the grid scan and see what it comes up with:
</p>



~~~text

{'voting__weights': [0, 0, 1]} -0.60533660756
{'voting__weights': [0, 1, 0]} -0.474562462086
{'voting__weights': [0, 1, 1]} -0.508363479586
{'voting__weights': [1, 0, 0]} -0.697231760084
{'voting__weights': [1, 0, 1]} -0.456599644003
{'voting__weights': [1, 1, 0]} -0.409406571361
{'voting__weights': [1, 1, 1]} -0.439084397238

Best score: -0.409
Best parameters set:
	voting__weights: [1, 1, 0]
~~~

<p>
We can see from the output that we've tried every combination of each of the classifiers. The output suggests that we should only include the <cite>ngram_pipe</cite> and <cite>unigram_log_pipe</cite> classifiers. <cite>tfidf_pipe</cite> should not be included - our log loss score is worse when it is added. 
</p>


<p>

</p>


<p>The <a href="https://gist.github.com/mneedham/3936d657b50b7c07cd3fe0c8d8c71496">code is on GitHub</a> if you want to see it all in one place
</p>

