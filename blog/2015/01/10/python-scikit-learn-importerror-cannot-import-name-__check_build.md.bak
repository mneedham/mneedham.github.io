+++
draft = false
date="2015-01-10 08:48:04"
title="Python: scikit-learn: ImportError: cannot import name __check_build"
tag=['python']
category=['Python']
+++

<p>
In <a href="https://www.kaggle.com/c/word2vec-nlp-tutorial/details/part-3-more-fun-with-word-vectors">part 3 of Kaggle's series on text analytics</a> I needed to install <a href="http://scikit-learn.org/stable/">scikit-learn</a> and having done so ran into the following error when trying to use one of its classes:
</p>



~~~python

>>> from sklearn.feature_extraction.text import CountVectorizer
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/markneedham/projects/neo4j-himym/himym/lib/python2.7/site-packages/sklearn/__init__.py", line 37, in <module>
    from . import __check_build
ImportError: cannot import name __check_build
~~~

<p>This error doesn't reveal very much but I found that when I exited the REPL and tried the same command again I got a different error which was a bit more useful:</p>



~~~python

>>> from sklearn.feature_extraction.text import CountVectorizer
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/markneedham/projects/neo4j-himym/himym/lib/python2.7/site-packages/sklearn/__init__.py", line 38, in <module>
    from .base import clone
  File "/Users/markneedham/projects/neo4j-himym/himym/lib/python2.7/site-packages/sklearn/base.py", line 10, in <module>
    from scipy import sparse
ImportError: No module named scipy
~~~

<p>The fix for this is now obvious:</p>



~~~python

$ pip install scipy
~~~

<p>And I can now load <cite>CountVectorizer</cite> without any problem:</p>



~~~python

$ python
Python 2.7.5 (default, Aug 25 2013, 00:04:04)
[GCC 4.2.1 Compatible Apple LLVM 5.0 (clang-500.0.68)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from sklearn.feature_extraction.text import CountVectorizer
~~~
