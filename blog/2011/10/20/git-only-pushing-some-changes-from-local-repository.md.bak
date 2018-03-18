+++
draft = false
date="2011-10-20 06:50:01"
title="git: Only pushing some changes from local repository"
tag=['git']
category=['Version Control']
+++

Something that we want to do reasonable frequently on my current project is to push some changes which have been committed to our local repository to master but not all of them. 

For example we might end up with 3 changes we haven't pushed:


~~~text

>> ~/github/local$ git status
# On branch master
# Your branch is ahead of 'origin/master' by 3 commits.
#
nothing to commit (working directory clean)
~~~


~~~text

>> ~/github/local$ git hist
* bb7b139 Thu, 20 Oct 2011 07:37:11 +0100 | mark: one last time (HEAD, master) [Mark Needham]
* 1cef99a Thu, 20 Oct 2011 07:36:35 +0100 | mark:another new line [Mark Needham]
* 850e105 Thu, 20 Oct 2011 07:36:01 +0100 | mark: new line [Mark Needham]
* 2b25622 Thu, 20 Oct 2011 07:32:43 +0100 | mark: adding file for first time (origin/master) [Mark Needham]
~~~

And we only want to push the commit with hash <cite>850e105</cite> for example.

The approach which my colleague <a href="https://github.com/uday-rayala">Uday</a> showed us is to first take a temporary branch of the current state.


~~~text

>> ~/github/local$ git checkout -b temp-branch
Switched to a new branch 'temp-branch'
~~~

Then immediately switch back to <cite>master</cite> and 'get rid' of the last two changes from there:


~~~text

>> ~/github/local$ git checkout master
Switched to branch 'master'
Your branch is ahead of 'origin/master' by 3 commits.
~~~ 


~~~text

>> ~/github/local$ git reset HEAD~2 --hard
HEAD is now at 850e105 mark: new line
~~~

We can then push just that change:


~~~text

>> ~/github/local$ git push
Counting objects: 5, done.
Writing objects: 100% (3/3), 257 bytes, done.
Total 3 (delta 0), reused 0 (delta 0)
Unpacking objects: 100% (3/3), done.
To /Users/mneedham/github/remote
   2b25622..850e105  master -> master
~~~

And merge the temporary branch back in again so we're back where we were before:


~~~text

>> ~/github/local$ git merge temp-branch
Updating 850e105..bb7b139
Fast-forward
 foo.txt |    2 ++
 1 files changed, 2 insertions(+), 0 deletions(-)
~~~


~~~text

>> ~/github/local$ git hist
* bb7b139 Thu, 20 Oct 2011 07:37:11 +0100 | mark: one last time (HEAD, temp-branch, master) [Mark Needham]
* 1cef99a Thu, 20 Oct 2011 07:36:35 +0100 | mark:another new line [Mark Needham]
* 850e105 Thu, 20 Oct 2011 07:36:01 +0100 | mark: new line (origin/master) [Mark Needham]
* 2b25622 Thu, 20 Oct 2011 07:32:43 +0100 | mark: adding file for first time [Mark Needham]
~~~


~~~text

>> ~/github/local$ git status
# On branch master
# Your branch is ahead of 'origin/master' by 2 commits.
#
nothing to commit (working directory clean)
~~~

And finally we delete the temporary branch:


~~~text

>> ~/github/local$ git branch -d temp-branch
Deleted branch temp-branch (was bb7b139).
~~~

We can achieve the same thing without creating the branch and just cherry picking the commits back again after we've pushed our changes but this seems approach seems quicker.
