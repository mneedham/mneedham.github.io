+++
draft = false
date="2010-04-10 11:43:23"
title="Mercurial: Early thoughts"
tag=['mercurial']
category=['Version Control']
+++

We're using <a href="http://mercurial.selenic.com/">Mercurial</a> as our source control system on the project I'm working on at the moment and since I've not yet used a distributed source control system on a team I thought it'd be interesting to note some of my initial thoughts.

One of the neat things about having a local repository and a central one is that you can check in lots of times locally and then push those changes to the central repository when you want everyone else to get the changes that you've made.

So far we've been pushing much more frequently than would usually be the case using something like <a href="http://subversion.tigris.org/">Subversion</a>. For example I checked in after doing some tidy up on unused references whereas with Subversion I'd probably have included that as part of another checkin. 

It actually makes development more fun and reminds me of <a href="http://www.markhneedham.com/blog/2009/08/24/rock-scissors-paper-tdd-as-if-you-meant-it/">a kata I did while checking in almost every minute last year</a>.

We're all still very much learning Mercurial but these are some of the commands that we've found ourselves using a lot so far:

<ul>
<li>
To check if there are any changes to pull from the central repository:

~~~text

hg incoming
hg in
~~~
</li>
<li>
To check if we have any changes that we haven't pushed to the central repository:

~~~text

hg outgoing
hg out
~~~
</li>
<li>
To add any unversioned files and remove any missing files:

~~~text

hg addremove
~~~
</li>
<li>
To remove a file from the repository and from the file system:


~~~text

hg remove /file/name
~~~
</li>
<li>
To remove a file from the repository on the next commit but not remove it from the file system:


~~~text

hg forget /file/name
~~~
</li>
<li>
To pull any changes from the remote repository and update your repository with them:

~~~text

hg pull -u
~~~

This one only completely works if you don't have any changes locally on the files you're pulling in. Otherwise you'll need to do a 'hg merge' afterwards.

It seems like there's a lot more merging to do when using Mercurial than with Subversion which we're still getting used to but seems to be more natural as we use Mercurial more.
</li>
<li>
To undo committing a file locally:


~~~text

hg rollback
hg ci -X /file/to/not/commit -m"message and so on"
~~~
</li>
</ul>

I've found <a href="http://hgbook.red-bean.com/read/">Mercurial: The Definitive Guide</a> by Bryan Sullivan and Joel's <a href="http://hginit.com/">hginit</a> to be useful resources for learning more about this tool.
