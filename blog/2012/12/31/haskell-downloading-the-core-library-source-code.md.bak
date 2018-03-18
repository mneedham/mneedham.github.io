+++
draft = false
date="2012-12-31 22:39:15"
title="Haskell: Downloading the core library source code"
tag=['haskell']
category=['Haskell']
+++

<p>I've started playing around with Haskell again and since I'm doing so on a new machine I don't have a copy of the language source code.<p>

<p>I wanted to rectify that situation but my Google fu was weak and it took me way too long to figure out how to get it so I thought I'd better document it for future me.</p>


<p>The easiest way is to clone the copy of the GHC repository on github:</p>



~~~text

git clone https://github.com/ghc/ghc.git
~~~

<p>Initially that doesn't have any of the code for the core libraries but running the following command (which takes ages!) sorts it out:</p>



~~~text

cd ghc
./sync-all get
~~~

<p>Noticing that the core libraries weren't there initially I thought I must have done something wrong so I went to the documentation for the function that I wanted to see the source for - <cite><a href="http://hackage.haskell.org/packages/archive/array/0.2.0.0/doc/html/Data-Array-MArray.html#v%3AgetAssocs">getAssocs</a></cite>.</p>


<p>From that page there is <a href="http://hackage.haskell.org/packages/archive/array/0.2.0.0/doc/html/src/Data-Array-Base.html#getAssocs">a link to the source for that function</a> and <a href="http://hackage.haskell.org/packages/archive/array/0.2.0.0/doc/html/">a bit tweaking of the URL</a> lets us know that this function is defined in the <cite>array</cite> package.</p>


<p>Most of the base packages are available from the <a href="http://darcs.haskell.org/packages/">Haskell darcs repository</a> so I ended up cloning the ones I wanted in the time that it took for the <cite>sync-all</cite> script to run.</p>



~~~text

darcs get http://darcs.haskell.org/packages/base/ # gets most of the packages we'd be interested in
darcs get http://darcs.haskell.org/packages/array/ # gets the array package
~~~

<p>Of course I could have just been patient and waited for the script to finish...</p>

