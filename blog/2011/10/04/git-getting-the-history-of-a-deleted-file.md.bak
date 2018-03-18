+++
draft = false
date="2011-10-04 22:33:09"
title="Git: Getting the history of a deleted file"
tag=['git']
category=['Version Control']
+++

We recently wanted to get the Git history of a file which we knew existed but had now been deleted so we could find out what had happened to it.

Using a simple <cite>git log</cite> didn't work:


~~~text

git log deletedFile.txt
fatal: ambiguous argument 'deletedFile.txt': unknown revision or path not in the working tree.
~~~	

We eventually came across <a href="http://feeding.cloud.geek.nz/2010/07/querying-deleted-content-in-git.html">Francois Marier's blog post</a> which points out that you need to use the following command instead:


~~~text

git log -- deletedFile.txt
~~~

I've tried reading through the man page but I'm still not entirely sure what the distinction between using <cite>--</cite> and not using it is supposed to be. 

If someone could explain it that'd be cool...
