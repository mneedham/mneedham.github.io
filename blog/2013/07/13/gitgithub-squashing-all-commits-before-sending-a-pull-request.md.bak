+++
draft = false
date="2013-07-13 18:47:49"
title="Git/GitHub: Squashing all commits before sending a pull request"
tag=['git']
category=['Version Control']
+++

<p>My colleague <a href="https://twitter.com/mesirii">Michael</a> has been doing some work to make it easier for people to <a href="http://www.neo4j.org/develop/import">import data into neo4j</a> and his latest attempt is <a href="https://github.com/jexp/neo4j-shell-tools">neo4j-shell-tools</a> which adds some additional commands to the <a href="http://docs.neo4j.org/chunked/stable/shell.html">neo4j-shell</a>.</p>


<p>I've spent a bit of time refactoring the <a href="https://github.com/jexp/neo4j-shell-tools/blob/master/readme.md">readme</a> which I'd done on <a href="https://github.com/mneedham/neo4j-shell-tools/commits/readme">a branch of my fork of the repository</a> and consisted of 46 commits, most changing 2 or 3 lines.</p>


<p>I wanted to send Michael a pull request on Github but first I needed to squash all my commits down into a single one.</p>


<p>I initially thought there might be a way that I could do that via Github but I couldn't see how to do that and eventually came across <a href="http://blog.steveklabnik.com/posts/2012-11-08-how-to-squash-commits-in-a-github-pull-request">a post on Steve Klabnik's blog</a> which explained what I needed to do.</p>


<p>This is what my .git/config looked like initially:</p>



~~~bash

[remote "origin"]
	fetch = +refs/heads/*:refs/remotes/origin/*
	url = git@github.com:mneedham/neo4j-shell-tools.git
[branch "master"]
	remote = origin
	merge = refs/heads/master
[remote "base"]
	url = git@github.com:jexp/neo4j-shell-tools.git
	fetch = +refs/heads/*:refs/remotes/base/*
[branch "readme"]
	remote = origin
	merge = refs/heads/readme
~~~

<p>I had all my commits on the 'readme' branch but the easiest approach seemed to be to create another branch on which I could squash all my commit - I called that branch 'readme-pull':</p>



~~~bash

$ git branch readme-pull
$ git checkout readme-pull
Switched to branch 'readme-pull'
~~~

<p>I then synced myself with Michael's repository:</p>



~~~bash

$ git fetch base
remote: Counting objects: 77, done.
remote: Compressing objects: 100% (18/18), done.
remote: Total 43 (delta 15), reused 40 (delta 12)
Unpacking objects: 100% (43/43), done.
From github.com:jexp/neo4j-shell-tools
   e81c431..c4e94f6  master     -> base/master

$ git rebase base/master
First, rewinding head to replay your work on top of it...
~~~

<p>I then had to handle any conflicts when applying my changes on top of Michael's master repository and then I was in a position to squash all my commits!</p>


<p>We can use rebase in interactive mode to do this and I've always done so by counting back how many commits I want to squash, so in this case it was 35:


~~~bash

$ git rebase -i HEAD~35

pick 141d0ae updating readme with link
pick 94f8f93 more updating
pick 03de50b readme updates
pick 4e60332 more updates
pick 3447d50 simplifying
pick d577520 tweaks
pick 2d993d4 more
pick f948582 list of commands
pick 713aae8 updating
~~~

<p>I later realised that I could have just passed in the last commit hash from the master to the rebase command i.e.</p>



~~~bash

commit c4e94f668223d53f6c7364d19aa965d09ea7eb00
Author: Michael Hunger <github@jexp.de>
Date:   Fri Jul 12 10:33:55 2013 +0200

    fixed test
~~~


~~~bash

$ git rebase -i c4e94f668223d53f6c7364d19aa965d09ea7eb00
~~~

<p>I then set all but the first commit to '<a href="http://git-scm.com/book/en/Git-Tools-Rewriting-History#Changing-Multiple-Commit-Messages">squash</a>' and pushed to my repository:</p>



~~~bash

$ git push -u origin readme-pull:readme-pull
~~~

<p>Finally I issued <a href="https://github.com/jexp/neo4j-shell-tools/pull/12">my pull request</a> and Michael merged it in!</p>

