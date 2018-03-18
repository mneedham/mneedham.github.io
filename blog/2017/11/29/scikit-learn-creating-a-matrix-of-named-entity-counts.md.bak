+++
draft = false
date="2017-11-29 23:01:38"
title="scikit-learn: Creating a matrix of named entity counts"
tag=['nlp', 'scikit-learn', 'polyglot', 'ner', 'entity-extraction']
category=['Python']
description="Learn how to create a matrix of named entities using scikit-learn's CountVectorizer and then train a model on it as part of machine learning pipeline."
+++

<p>
I've been trying to improve my score on Kaggle's <a href="https://www.kaggle.com/c/spooky-author-identification">Spooky Author Identification</a> competition, and my latest idea was building a model which used named entities extracted using the <a href="https://github.com/aboSamoor/polyglot">polyglot NLP library</a>.
</p>


<p>
We'll start by learning how to extract entities form a sentence using polyglot which isn't too tricky:
</p>



~~~python

>>> from polyglot.text import Text
>>> doc = "My name is David Beckham. Hello from London, England"
>>> Text(doc, hint_language_code="en").entities
[I-PER(['David', 'Beckham']), I-LOC(['London']), I-LOC(['England'])]
~~~

<p>
This sentence contains three entities. We'd like each entity to be a string rather than an array of values so let's refactor the code to do that:
</p>



~~~python

>>> ["_".join(entity) for entity in Text(doc, hint_language_code="en").entities]
['David_Beckham', 'London', 'England']
~~~

<p>
That's it for the polyglot part of the solution. Now let's work out how to integrate that with scikit-learn.
</p>


<p>
I've been using scikit-learn's <cite><a href="http://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html">Pipeline</a></cite> abstraction for the other models I've created so I'd like to take the same approach here. This is an example of a model that creates a matrix of unigram counts and creates a Naive Bayes model on top of that:
</p>



~~~python

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

nlp_pipeline = Pipeline([
    ('cv', CountVectorizer(),
    ('mnb', MultinomialNB())
])

...
# Train and Test the model
...
~~~

<p>
I was going to write a class similar to <cite><a href="http://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html">CountVectorizer</a></cite> but after reading its code for a couple of hours I realised that I could just pass in a custom analyzer instead. This is what I ended up with:
</p>



~~~python

entities = {}


def analyze(doc):
    if doc not in entities:
        entities[doc] = ["_".join(entity) for entity in Text(doc, hint_language_code="en").entities]
    return entities[doc]

nlp_pipeline = Pipeline([
    ('cv', CountVectorizer(analyzer=lambda doc: analyze(doc))),
    ('mnb', MultinomialNB())
])
~~~

<p>
I'm caching the results in a dictionary because the entity extraction is quite time consuming and there's no point recalculating it each time the function is called.
</p>


<p>
Unfortunately this model didn't help me improve my best score. It scores a log loss of around 0.5, a bit worse than the 0.45 I've achieved using the unigram model :(
</p>

