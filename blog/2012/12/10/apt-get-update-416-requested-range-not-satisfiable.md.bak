+++
draft = false
date="2012-12-10 00:39:34"
title="apt-get update: 416 Requested Range Not Satisfiable"
tag=['software-development']
category=['Software Development']
+++

<p>We were trying to run a puppet update on some machines last week and one of the first things it does is run 'apt-get update' which was working on all but one node for which it was returning the following exception:</p>



~~~text

Err http://us-west-1.ec2.archive.ubuntu.com/ubuntu/ i386 Packages
  416 Requested Range Not Satisfiable
Fetched 5,079B in 2s (2,296B/s)
W: Failed to fetch http://us-west-1.ec2.archive.ubuntu.com/ubuntu/dists/maverick-updates/main/binary-i386/Packages.gz 
416 Requested Range Not Satisfiable
~~~

<p>It turns out one way that exception can manifest is if you've got a partial copy of the index files from the repository and in this case the solution was <a href="https://bugs.launchpad.net/ubuntu/+source/apt/+bug/798023">as simple as deleting those and trying again</a>:</p>



~~~text

sudo rm -rf /var/lib/apt/lists/partial/*
~~~

<p>Running 'apt-get update' again after that worked perfectly and the world was a happy place again.</p>

