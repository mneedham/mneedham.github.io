+++
draft = false
date="2017-11-19 07:16:56"
title="Python 3: TypeError: unsupported format string passed to numpy.ndarray.__format__"
tag=['python', 'python3']
category=['Python']
description="This post explains how to work around a change in how Python string formatting works for numpy arrays between Python 2 and Python 3."
+++

<p>
This post explains how to work around a change in how Python string formatting works for numpy arrays between Python 2 and Python 3.
</p>


<p>
I've been going through <a href="https://twitter.com/justmarkham">Kevin Markham</a>'s scikit-learn Jupyter notebooks and ran into a problem on the <a href="https://github.com/justmarkham/scikit-learn-videos/blob/master/07_cross_validation.ipynb">Cross Validation</a> one, which was throwing this error when attempting to print the KFold example:
</p>



~~~python

Iteration                   Training set observations                   Testing set observations
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-28-007cbab507e3> in <module>()
      6 print('{} {:^61} {}'.format('Iteration', 'Training set observations', 'Testing set observations'))
      7 for iteration, data in enumerate(kf, start=1):
----> 8     print('{0:^9} {1} {2:^25}'.format(iteration, data[0], data[1]))

TypeError: unsupported format string passed to numpy.ndarray.__format__
~~~

<p>
We can reproduce this easily:
</p>



~~~python

>>> import numpy as np
~~~


~~~python

>>> "{:9}".format(np.array([1,2,3]))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported format string passed to numpy.ndarray.__format__
~~~

<p>
What about if we use Python 2?
</p>



~~~python

>>> "{:9}".format(np.array([1,2,3]))
'[1 2 3]  '
~~~

<p>
Hmmm, must be a change between the Python versions.</p>
 

<p>We can work around it by coercing our numpy array to a string:
</p>



~~~python

>>> "{:9}".format(str(np.array([1,2,3])))
'[1 2 3]  '
~~~
