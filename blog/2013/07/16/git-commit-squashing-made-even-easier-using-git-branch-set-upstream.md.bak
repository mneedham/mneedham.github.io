+++
draft = false
date="2013-07-16 08:13:02"
title="Git: Commit squashing made even easier using 'git branch --set-upstream'"
tag=['git']
category=['Version Control']
+++

<p>A few days ago I wrote a blog post describing how I wanted to <a href="http://www.markhneedham.com/blog/2013/07/13/gitgithub-squashing-all-commits-before-sending-a-pull-request/">squash a series of commits into one bigger one</a> before making a pull request and in the comments Rob Hunter showed me an even easier way to do so.</p>


<p>To recap, by the end of the post I had the following git config:</p>



~~~bash

$ cat .git/config
[remote "origin"]
	fetch = +refs/heads/*:refs/remotes/origin/*
	url = git@github.com:mneedham/neo4j-shell-tools.git
[branch "master"]
	remote = origin
	merge = refs/heads/master
[remote "base"]
	url = git@github.com:jexp/neo4j-shell-tools.git
	fetch = +refs/heads/*:refs/remotes/base/*
[branch "readme-pull"]
	remote = origin
	merge = refs/heads/readme-pull
[branch "readme"]
	remote = origin
	merge = refs/heads/readme
~~~

<p>I was working against the remote 'origin' but the actual home of this repository is 'base'.</p>


<p>I'd created a load of commits on 'origin/readme' and had then squashed them all into one commit on 'origin/readme-pull' by using the following command:</p>



~~~bash

$ git rebase -i c4e94f668223d53f6c7364d19aa965d09ea7eb00
~~~

<p>where 'c4e94f668223d53f6c7364d19aa965d09ea7eb00' is the hash of the last commit that was made in 'base/master'.</p>


<p>Rob suggested that I should try using <a href="http://stackoverflow.com/questions/520650/how-do-you-make-an-existing-git-branch-track-a-remote-branch">upstream tracking</a> to simplify this even further. When we use upstream tracking we create a link between a local and remote repository which in this case is useful for working out where our commits start from.</p>
 

<p>I thought I'd try it out on another branch. We want to set the new branch to track 'base/master' since that's the one we eventually want to have our commit applied against.</p>


<p>We'll start from the 'readme' branch which has the list of commits that we want to squash</p>



~~~bash

$ git branch
  master
* readme
  readme-pull
~~~

<p>Now let's create a new branch and then track it against 'base/master':</p>



~~~bash

$ git checkout -b readme-pull-new
Switched to a new branch 'readme-pull-new'
$ git branch --set-upstream readme-pull-new base/master
Branch readme-pull-new set up to track remote branch master from base.
~~~

<p>Squashing all our commits is now as simple as running the following command:</p>



~~~bash

$ git rebase -i
~~~

<p>And then choosing 'squash' against all commits except for the first one which can stay as 'pick'. We then need to edit the commit message into shape which mostly involves deleting the commit messages from the commits we've squashed in this instance.</p>


<p>Thanks to Rob for the tip!</p>

