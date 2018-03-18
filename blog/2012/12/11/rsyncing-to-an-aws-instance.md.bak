+++
draft = false
date="2012-12-11 23:44:05"
title="rsyncing to an AWS instance"
tag=['software-development']
category=['Software Development']
+++

<p>I wanted to try running some of the <a href="http://www.markhneedham.com/blog/category/machine-learning/">machine learning algorithms</a> that <a href="https://twitter.com/jennifersmithco">Jen</a> and I have been playing around with on a beefier machine so I thought spinning up an AWS instance would be the best way to do that.</p>


<p>I built the JAR with the appropriate algorithms on my machine and then wanted to copy it up onto an AWS instance.</p>


<p>I could have used <cite>scp</cite> but I quite like the progress bar that you can get with <cite>rsync</cite> and since the JAR had somehow drifted to a size of 47MB the progress bar was useful.</p>


<p>When I provisioned the machine I created a public/private key pair and I was able to ssh into the machine like this:</p>



~~~text

ssh -l ubuntu -i ~/Downloads/machinenursery.pem ec2-54-242-108-142.compute-1.amazonaws.com
~~~

<p>I needed to tell rsync to use the pen file which I initially tried to do with the following command:</p>



~~~text

rsync --progress 'ssh -i /Users/markhneedham/Downloads/machinenursery.pem' -avz target/ ubuntu@ec2-54-242-108-142.compute-1.amazonaws.com:machinenursery
~~~

<p>It seemed to ignore the pem file and I got a permission denied error when I ran this:</p>



~~~text

Permission denied (publickey).
rsync: connection unexpectedly closed (0 bytes received so far) [sender]
rsync error: unexplained error (code 255) at /SourceCache/rsync/rsync-42/rsync/io.c(452) [sender=2.6.9]
~~~

<p>Eventually <a href="http://alestic.com/2009/04/ubuntu-ec2-sudo-ssh-rsync">came across an article which explained a way around the problem</a> using RSH instead of SSH:</p>



~~~text

rsync --progress --rsh 'ssh -i /Users/markhneedham/Downloads/machinenursery.pem' -avz target/ ubuntu@ec2-54-242-108-142.compute-1.amazonaws.com:machine nursery
~~~

<p>As I understand it RSH isn't secure but all I'm transferring is a JAR file so it didn't seem like too much of an issue.</p>


<p>I'm sure there must be a way to transfer this file using SSH but I've tried all the different flags and I can't figure it out so if you know how to please let me know!.</p>

