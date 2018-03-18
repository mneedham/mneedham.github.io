+++
draft = false
date="2015-01-10 08:39:15"
title="Python: gensim - clang: error: unknown argument: '-mno-fused-madd' [-Wunused-command-line-argument-hard-error-in-future]"
tag=['python']
category=['Python']
+++

<p>
While working through <a href="https://www.kaggle.com/c/word2vec-nlp-tutorial/details/part-2-word-vectors">part 2 of Kaggle's bag of words tutorial</a> I needed to install the <a href="https://radimrehurek.com/gensim/">gensim</a> library and initially ran into the following error:
</p>



~~~text

$ pip install gensim

...

cc -fno-strict-aliasing -fno-common -dynamic -arch x86_64 -arch i386 -g -Os -pipe -fno-common -fno-strict-aliasing -fwrapv -mno-fused-madd -DENABLE_DTRACE -DMACOSX -DNDEBUG -Wall -Wstrict-prototypes -Wshorten-64-to-32 -DNDEBUG -g -fwrapv -Os -Wall -Wstrict-prototypes -DENABLE_DTRACE -arch x86_64 -arch i386 -pipe -I/Users/markneedham/projects/neo4j-himym/himym/build/gensim/gensim/models -I/System/Library/Frameworks/Python.framework/Versions/2.7/include/python2.7 -I/Users/markneedham/projects/neo4j-himym/himym/lib/python2.7/site-packages/numpy/core/include -c ./gensim/models/word2vec_inner.c -o build/temp.macosx-10.9-intel-2.7/./gensim/models/word2vec_inner.o

clang: error: unknown argument: '-mno-fused-madd' [-Wunused-command-line-argument-hard-error-in-future]

clang: note: this will be a hard error (cannot be downgraded to a warning) in the future

command 'cc' failed with exit status 1

an integer is required

Traceback (most recent call last):

  File "<string>", line 1, in <module>

  File "/Users/markneedham/projects/neo4j-himym/himym/build/gensim/setup.py", line 166, in <module>

    include_package_data=True,

  File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/distutils/core.py", line 152, in setup

    dist.run_commands()

  File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/distutils/dist.py", line 953, in run_commands

    self.run_command(cmd)

  File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/distutils/dist.py", line 972, in run_command

    cmd_obj.run()

  File "/Users/markneedham/projects/neo4j-himym/himym/lib/python2.7/site-packages/setuptools/command/install.py", line 59, in run

    return orig.install.run(self)

  File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/distutils/command/install.py", line 573, in run

    self.run_command('build')

  File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/distutils/cmd.py", line 326, in run_command

    self.distribution.run_command(command)

  File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/distutils/dist.py", line 972, in run_command

    cmd_obj.run()

  File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/distutils/command/build.py", line 127, in run

    self.run_command(cmd_name)

  File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/distutils/cmd.py", line 326, in run_command

    self.distribution.run_command(command)

  File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/distutils/dist.py", line 972, in run_command

    cmd_obj.run()

  File "/Users/markneedham/projects/neo4j-himym/himym/build/gensim/setup.py", line 71, in run

    "There was an issue with your platform configuration - see above.")

TypeError: an integer is required

----------------------------------------
Cleaning up...
Command /Users/markneedham/projects/neo4j-himym/himym/bin/python -c "import setuptools, tokenize;__file__='/Users/markneedham/projects/neo4j-himym/himym/build/gensim/setup.py';exec(compile(getattr(tokenize, 'open', open)(__file__).read().replace('\r\n', '\n'), __file__, 'exec'))" install --record /var/folders/sb/6zb6j_7n6bz1jhhplc7c41n00000gn/T/pip-i8aeKR-record/install-record.txt --single-version-externally-managed --compile --install-headers /Users/markneedham/projects/neo4j-himym/himym/include/site/python2.7 failed with error code 1 in /Users/markneedham/projects/neo4j-himym/himym/build/gensim
Storing debug log for failure in /Users/markneedham/.pip/pip.log
~~~

<p>The exception didn't make much sense to me but I came across <a href="https://kaspermunck.github.io/2014/03/fixing-clang-error/">a blog post which explained it:</p>
</a>

<blockquote>
The Apple LLVM compiler in Xcode 5.1 treats unrecognized command-line options as errors. This issue has been seen when building both Python native extensions and Ruby Gems, where some invalid compiler options are currently specified.
</blockquote>

<p>
The author suggests this only became a problem with XCode 5.1 so I'm surprised I hadn't come across it sooner since I haven't upgraded XCode in a long time.
</p>


<p>
We can work around the problem by telling the compiler to treat extra command line arguments as a warning rather than an error
</p>



~~~bash

export ARCHFLAGS=-Wno-error=unused-command-line-argument-hard-error-in-future
~~~

<p>
Now it installs with no problems.
</p>

