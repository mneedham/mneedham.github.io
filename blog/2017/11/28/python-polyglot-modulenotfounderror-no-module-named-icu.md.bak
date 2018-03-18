+++
draft = false
date="2017-11-28 19:52:13"
title="Python: polyglot - ModuleNotFoundError: No module named 'icu'"
tag=['nlp', 'python', 'polyglot']
category=['Python']
description="Learn how to get around the ModuleNotFoundError: No module named ‘icu’ error when installing Python's polyglot NLP library"
+++

<p>
I wanted to use the <a href="https://github.com/aboSamoor/polyglot">polyglot</a> NLP library that my colleague Will Lyon mentioned in <a href="http://www.lyonwj.com/2017/11/15/entity-extraction-russian-troll-tweets-neo4j/">his analysis of Russian Twitter Trolls</a> but had installation problems which I thought I'd share in case anyone else experiences the same issues.
</p>


<p>
I started by trying to install <cite>polyglot</cite>:
</p>




~~~bash

$ pip install polyglot

ImportError: No module named 'icu'
~~~


<p>
Hmmm I'm not sure what <cite>icu</cite> is but luckily there's a <a href="https://github.com/aboSamoor/polyglot/issues/10">GitHub issue covering this problem</a>. That led me to <a href="https://tobywf.com/2017/05/installing-pyicu-on-macos/">Toby Fleming's blog post</a> that suggests the following steps:
</p>



~~~bash

brew install icu4c
export ICU_VERSION=58
export PYICU_INCLUDES=/usr/local/Cellar/icu4c/58.2/include
export PYICU_LFLAGS=-L/usr/local/Cellar/icu4c/58.2/lib
pip install pyicu
~~~

<p>I already had <cite>icu4c</cite> installed so I just had to make sure that I had the same version of that library as Toby did. I ran the following command to check that:
</p>



~~~bash

$ ls -lh /usr/local/Cellar/icu4c/
total 0
drwxr-xr-x  12 markneedham  admin   408B 28 Nov 06:12 58.2
~~~

<p>
That still wasn't enough though! I had to install these two libraries as well:
</p>



~~~bash

pip install pycld2
pip install morfessor
~~~

<p>
I was then able to install polyglot, but had to then run the following commands to download the files needed for entity extraction:
</p>



~~~bash

polyglot download embeddings2.de
polyglot download ner2.de
polyglot download embeddings2.en
polyglot download ner2.en
~~~
