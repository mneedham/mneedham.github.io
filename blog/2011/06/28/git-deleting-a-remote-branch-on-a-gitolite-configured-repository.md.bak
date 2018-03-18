+++
draft = false
date="2011-06-28 22:09:18"
title="Git: Deleting a remote branch on a gitolite configured repository"
tag=['git']
category=['Version Control']
+++

We've had an <a href="https://github.com/harrah/xsbt">xsbt</a> branch on our <a href="https://github.com/sitaramc/gitolite">gitolite</a> powered repository for the last couple of weeks while we worked out how to move our build from sbt 0.7 to sbt 0.10 but having finally done that we needed to delete it.

I originally tried running the following command from one of our developer workstations:


~~~text

git push origin :xsbt
~~~

But ended up with the following error:

<blockquote>
remote: error: denying ref deletion for regs/head/xsbt

! [remote rejected] xsbt (deletion prohibited)
</blockquote>

A bit of googling led me to <a href="http://stackoverflow.com/questions/5723511/how-do-i-remove-a-remote-branch-when-i-get-an-error">this stackoverflow thread</a> which suggested that you needed to be an administrator in order to delete a remote branch.

Once we've done that we can run the following command on each machine to delete the remote tracking reference to the repository:


~~~text

git branch -d -r origin/xsbt
~~~
