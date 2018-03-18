+++
draft = false
date="2017-12-03 17:23:14"
title="Python: Combinations of values on and off"
tag=['python', 'python3']
category=['Python']
+++

<p>
In my continued exploration of Kaggle's <a href="https://www.kaggle.com/c/spooky-author-identification/leaderboard">Spooky Authors competition</a>, I wanted to run a <a href="http://scikit-learn.org/stable/modules/ensemble.html#using-the-votingclassifier-with-gridsearch">GridSearch</a> turning on and off different classifiers to work out the best combination.
</p>


<p>I therefore needed to generate combinations of 1s and 0s enabling different classifiers.
</p>


<p>e.g. if we had 3 classifiers we'd generate these combinations</p>



~~~text

0 0 1
0 1 0
1 0 0
1 1 0
1 0 1
0 1 1
1 1 1
~~~

<p>
where...</p>


<ul>

<li>'0 0 1' means: classifier1 is disabled, classifier3 is disabled,  classifier3 is enabled</li>
<li>'0 1 0' means: classifier1 is disabled, classifier3 is enabled, classifier3 is disabled</li>
<li>'1 1 0' means: classifier1 is enabled, classifier3 is enabled, classifier3 is disabled</li>
<li>'1 1 1' means: classifier1 is enabled, classifier3 is enabled, classifier3 is enabled</li>
</ul>

<p>
...and so on. In other words, we need to generate the binary representation for all the values from 1 to 2<sup>number of classifiers</sup>-1. 
</p>


<p>We can write the following code fragments to calculate a 3 bit representation of different numbers:</p>



~~~python

>>> "{0:0b}".format(1).zfill(3)
'001'
>>> "{0:0b}".format(5).zfill(3)
'101'
>>> "{0:0b}".format(6).zfill(3)
'110'
~~~

<p>
We need an array of 0s and 1s rather than a string, so let's use the <cite>list</cite> function to create our array and then cast each value to an integer:
</p>



~~~python

>>> [int(x) for x in list("{0:0b}".format(1).zfill(3))]
[0, 0, 1]
~~~

<p>
Finally we can wrap that code inside a list comprehension:
</p>



~~~python

def combinations_on_off(num_classifiers):
    return [[int(x) for x in list("{0:0b}".format(i).zfill(num_classifiers))]
            for i in range(1, 2 ** num_classifiers)]
~~~

<p>
And let's check it works:
</p>



~~~python

>>> for combination in combinations_on_off(3):
       print(combination)
 
[0, 0, 1]
[0, 1, 0]
[0, 1, 1]
[1, 0, 0]
[1, 0, 1]
[1, 1, 0]
[1, 1, 1]
~~~

<p>what about if we have 4 classifiers?</p>



~~~python

>>> for combination in combinations_on_off(4):
       print(combination)

[0, 0, 0, 1]
[0, 0, 1, 0]
[0, 0, 1, 1]
[0, 1, 0, 0]
[0, 1, 0, 1]
[0, 1, 1, 0]
[0, 1, 1, 1]
[1, 0, 0, 0]
[1, 0, 0, 1]
[1, 0, 1, 0]
[1, 0, 1, 1]
[1, 1, 0, 0]
[1, 1, 0, 1]
[1, 1, 1, 0]
[1, 1, 1, 1]
~~~

<p>
Perfect! We can now use this function to help work out which combinations of classifiers are needed.
</p>

