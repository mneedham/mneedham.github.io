+++
draft = false
date="2009-08-06 18:58:00"
title="Bear Shaving"
tag=['software-development', 'bear-shaving']
category=['Software Development']
+++

I recently came across a <a href="http://sethgodin.typepad.com/seths_blog/2009/08/bear-shaving.html">blog post by Seth Godin where he coins the term 'bear shaving'</a> which is where we address the symptoms of a problem instead of addressing the problem.

The main example he gives is the idea of <a href="http://www.youtube.com/watch?v=ryUcq1ztQN8">shaving a bear</a> so that it can deal with the increased temperature caused by global warming instead of addressing the underlying problem which has led to this happening in the first place. 

As with <a href="http://www.markhneedham.com/blog/2008/10/25/dont-shave-the-yak-ask-why-are-we-doing-this/">yak shaving</a> which is certainly rife in software development projects, I think we are guilty of bear shaving as well.

Although similar to yak shaving, bear shaving seems to be much more intentional - noone ever means to end up shaving a yak but they sometimes do whereas we might deliberately choose to shave a bear because of one of the following reasons from what I've noticed:

<ul>
<li>We don't want to work out what the root cause of our problem is, perhaps because we don't have the time to do so or it's just easier to find a work around.</li>
<li>We know what the root cause of the problem is but it's too difficult to do anything about it.</li>
<li>We know what the root cause of the problem is but we can't do much about it because it's out of our control (perhaps a bottle neck in another team for example)</li>
</ul>

An example of this that we have been juggling on our project is working out the best thing to do when the continuous integration build is red due to a failure related to an integration end point that is known to be flaky. 

We've massively reduced the impact that this has on the early part of our build pipeline by introducing a <a href="http://martinfowler.com/bliki/SelfInitializingFake.html">self initialising fake</a> but there are still some calls through to the service layer since we aren't storing the result of every single call.

When those service calls that do go through each time are having problems we can often end up with several hours where we can't checkin.

Even when this flakiness goes away we haven't quite managed to reduce the <a href="http://www.markhneedham.com/blog/2009/07/25/cruise-agents-reducing-random-build-failures/">random build failures</a> down to zero which means that the feedback loop is not as quick as it could be.

As a result of this we have come up with two different ways of allowing people to continue working locally without needing to check into the main repository:

<ol>
<li>Using <a href="http://git-scm.com/">Git</a> as a local patch management tool and keeping different changes on different branches. </li>
<li>Making multiple copies of the Subversion repository locally with different changes on different copies</li></ol>

The problem with both of these solutions is that people now have versions of the code sitting on their machines which the rest of the team hasn't yet been able to integrate with.

We are having more individual productivity to a degree but we are also creating more <a href="http://www.learnleanblog.com/2008/01/lean-manufacturing-inventory-and-work.html">work in progress</a> which the rest of the team will later need to integrate against.

We haven't only spent time coming up with bear shaving solutions though.

One of the problems we had was that often when a new version of services was pushed into the integration environment that was the first time that we actually integrated against it. We now spend some time integrating against services in a pre-integration environment which has helped reduce the number of surprises that we get later on.

Another potential solution to part of the problem would be to make use of a distributed source control system such as Git or <a href="http://mercurial.selenic.com/wiki/">Mercurial</a> as the main repository that everyone uses and then push every change into our Subversion repository.

We've tried some of the Git to Subversion and <a href="http://bitbucket.org/durin42/hgsubversion/wiki/Home">Mercurial</a> <a href="http://pypi.python.org/pypi/hgsvn">to Subversion</a> bridges available at the moment and none of them have quite worked for us so we haven't been able to pursue this option. 

Given that we often have constraints that we have to work under perhaps it would therefore seem inevitable that <strong>there will be some amount of bear shaving on any project</strong>?
