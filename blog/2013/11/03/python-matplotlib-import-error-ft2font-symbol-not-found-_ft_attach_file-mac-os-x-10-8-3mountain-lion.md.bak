+++
draft = false
date="2013-11-03 11:14:48"
title="Python: matplotlib -  Import error ft2font Symbol not found: _FT_Attach_File (Mac OS X 10.8.3/Mountain Lion)"
tag=['python']
category=['Python']
+++

<p>As I mentioned at the end of <a href="http://www.markhneedham.com/blog/2013/10/30/kaggle-titanic-python-pandas-attempt/">my last post about the Titanic Kaggle problem</a> our next step was to do some proper machine learning&trade; using <a href="http://scikit-learn.org/stable/index.html">scikit-learn</a> so I started by looking at the <a href="http://scikit-learn.org/stable/auto_examples/ensemble/plot_adaboost_regression.html#example-ensemble-plot-adaboost-regression-py">Decision Tree example</a>.</p>


<p>Unfortunately I ended up on the mother of all yak shaving missions while trying to execute the code which draws a chart using <a href="http://matplotlib.org/">matplotlib</a>.</p>


<p>I ran the following line from the tutorial:</p>



~~~python

import pylab as pl
~~~

<p>which lead to this exception:</p>



~~~text

ImportError: dlopen(/Library/Python/2.7/site-packages/matplotlib/ft2font.so, 2): Symbol not found: _FT_Attach_File
~~~

<p>I found <a href="http://stackoverflow.com/questions/7503058/import-error-ft2font-from-matplotlib-python-macosx">this post on Stack Overflow</a> which had a variety of suggestions one of which was to attempt to install matplotlib from a <a href="https://downloads.sourceforge.net/project/matplotlib/matplotlib/matplotlib-1.2.1/matplotlib-1.2.1-py2.7-python.org-macosx10.6.dmg">dmg</a> on <a href="http://matplotlib.org/downloads.html">the website</a>.</p>


<p>I tried that and got this error when trying to do so:</p>



~~~text

matplotlib 1.2.1 can't be installed on this disk. matplotlib requires System Python 2.7 to install.
~~~

<p>I do have Python 2.7 installed so the error surprised me. In any case, I eventually came across <a href="http://the.taoofmac.com/space/blog/2011/07/24/2222">a post on Tao of Mac which explained how to install matplotlib from source</a>:</p>



~~~bash

sudo brew install pkgconfig
cd /tmp
git clone git://github.com/matplotlib/matplotlib.git
cd matplotlib/
python setup.py build
sudo python setup.py install
~~~

<p>That installed successfully so I went back to the example which now failed on an earlier import statement:</p>



~~~python

>>> from sklearn.tree import DecisionTreeRegressor
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
ImportError: No module named sklearn.tree
~~~

<p>I tried to reinstall scikit-learn:</p>



~~~bash

$ sudo easy_install scikit-learn
~~~

<p>That installed successfully so I tried to import the DecisionTreeRegressor again:</p>



~~~python

>>> from sklearn.tree import DecisionTreeRegressor
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Library/Python/2.7/site-packages/scikit_learn-0.14.1-py2.7-macosx-10.8-intel.egg/sklearn/__init__.py", line 32, in <module>
    from .base import clone
  File "/Library/Python/2.7/site-packages/scikit_learn-0.14.1-py2.7-macosx-10.8-intel.egg/sklearn/base.py", line 10, in <module>
    from scipy import sparse
ImportError: No module named scipy
~~~

<p>I tried again and got this error message instead:</p>



~~~python

>>> from sklearn.tree import DecisionTreeRegressor
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Library/Python/2.7/site-packages/scikit_learn-0.14.1-py2.7-macosx-10.8-intel.egg/sklearn/__init__.py", line 31, in <module>
    from . import __check_build
ImportError: cannot import name __check_build
~~~

<p>I tried to reinstall scipy to see if that would help:</p>



~~~bash

$ sudo easy_install scipy
~~~

<p>but that led to the following error:</p>



~~~bash

no previously-included directories found matching 'scipy/special/tests/data/boost'
no previously-included directories found matching 'scipy/special/tests/data/gsl'
no previously-included directories found matching 'doc/build'
no previously-included directories found matching 'doc/source/generated'
no previously-included directories found matching '*/__pycache__'
warning: no previously-included files matching '*~' found anywhere in distribution
warning: no previously-included files matching '*.bak' found anywhere in distribution
warning: no previously-included files matching '*.swp' found anywhere in distribution
warning: no previously-included files matching '*.pyo' found anywhere in distribution
Could not locate executable f95
Could not locate executable f90
Could not locate executable f77
Could not locate executable xlf90
Could not locate executable xlf
Could not locate executable ifort
Could not locate executable ifc
Could not locate executable g77
Could not locate executable gfortran
Could not locate executable g95
Could not locate executable pgf90
Could not locate executable pgf77
don't know how to compile Fortran code on platform 'posix'
error: Setup script exited with error: library dfftpack has Fortran sources but no Fortran compiler found
~~~

<p>I came across <a href="http://stackoverflow.com/questions/11442970/numpy-and-scipy-for-preinstalled-python-2-6-7-on-mac-os-lion">this StackOverflow post which suggested installing the Fortran compiler using brew</a>:</p>



~~~bash

$ brew install gfortran
~~~

<p>but that didn't work too well either:</p>



~~~bash

==> Installing gfortran dependency: isl
==> Downloading http://ftp.de.debian.org/debian/pool/main/i/isl/isl_0.11.2.orig.tar.bz2

curl: (22) The requested URL returned error: 404
Trying a mirror...
==> Downloading ftp://ftp.linux.student.kuleuven.be/pub/people/skimo/isl/isl-0.11.2.tar.bz2

curl: (28) connect() timed out!
Trying a mirror...
==> Downloading http://www.kotnet.org/~skimo/isl/isl-0.11.2.tar.bz2

curl: (22) The requested URL returned error: 404
~~~

<p>Instead I downloaded <a href="http://sourceforge.net/projects/hpc/files/hpc/g95/gfortran-4.9-bin.tar.gz/download?use_mirror=optimate&download=">a tar.gz package</a> from <a href="http://hpc.sourceforge.net/">HPC</a> and installed it manually:</p>



~~~bash

$ gunzip gfortran-4.8-bin.tar.gz 
$ sudo tar -xvf gfortran-4.8-bin.tar -C /
~~~

<p>After that had finished I tried reinstalling scipy using pip this time (based on a suggestion in <a href="http://stackoverflow.com/questions/11442970/numpy-and-scipy-for-preinstalled-python-2-6-7-on-mac-os-lion">this post</a>):</p>



~~~bash

$ sudo pip install scipy
~~~

<p>And now I can successfully run the tutorial!</p>


<p>----------------</p>


<p>At some stage in the process I also upgraded numpy but I'm not sure if that's necessary to get things working. Just in case:</p>



~~~bash

$ sudo pip install numpy --upgrade
</p>

