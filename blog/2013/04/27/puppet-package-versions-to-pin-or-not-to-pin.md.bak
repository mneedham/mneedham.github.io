+++
draft = false
date="2013-04-27 13:40:28"
title="Puppet: Package Versions - To pin or not to pin"
tag=['puppet']
category=['DevOps']
+++

<p>Over the last year or so I've spent quite a bit of time working with puppet and one of the things that we had to decide when installing packages was whether or not to specify a particular version.</p>


<p>On the first project I worked on we didn't bother and just let the package manager chose the most recent version.</p>


<p>Therefore if we were installing nginx the puppet code would read like this:</p>



~~~puppet

package { 'nginx':
  ensure  => 'present',
}
~~~

<p>We can see which version that would install by checking the version table for the package:</p>



~~~bash

$ apt-cache policy nginx
nginx:
  Installed: (none)
  Candidate: 1:1.2.6-1~43~precise1
  Version table:
     1:1.2.6-1~43~precise1 0
        500 http://ppa.launchpad.net/brightbox/ruby-ng/ubuntu/ precise/main amd64 Packages
     1.4.0-1~precise 0
        500 http://nginx.org/packages/ubuntu/ precise/nginx amd64 Packages
     1.1.19-1ubuntu0.1 0
        500 http://us.archive.ubuntu.com/ubuntu/ precise-updates/universe amd64 Packages
     1.1.19-1 0
        500 http://us.archive.ubuntu.com/ubuntu/ precise/universe amd64 Packages
~~~

<p>In this case if we don't specify a version the Brightbox '1:1.2.6-1~43~precise1' version will be installed.</p>


<p>Running dpkg with the 'compare-versions' flag shows us that this version is considered higher than the nginx.org one:</p>



~~~bash

$ dpkg --compare-versions '1:1.2.6-1~43~precise1' gt '1.4.0-1~precise' ; echo $?
0
~~~

<p>From what I understand you can <a href="http://wiki.debian.org/AptPreferences">pin versions higher up the list</a> by associating a higher number with them but given that all these versions are set to '500' I'm not sure how it decides on the order!</p>


<p>The problem with not specifying a version is that when a new version becomes available the next time puppet runs it will automatically upgrade the version for us.</p>


<p>Most of the time this isn't a problem but there were a couple of occasions when a version got bumped and something elsewhere stopped working and it took us quite a while to work out what had changed.</p>


<p>The alternative approach is to pin the package installation to a specific version. So if we want the <a href="http://nginx.org/">recent 1.4.0 version</a> installed we'd have the following code:</p>



~~~puppet

package { 'nginx':
  ensure  => '1.4.0-1~precise',
}
~~~

<p>The nice thing about this approach is that we always know which version is going to be installed.</p>


<p>The problem we now introduce is that when an updated version is added to the repository the old one is typically removed which means a puppet run on a new machine will fail because it can't find the version.</p>


<p>After working with puppet for a few months it becomes quite easy to see when this is the reason for the failure but it creates the perception that 'puppet is always failing' for newer people which isn't so good.</p>


<p>I think on balance I prefer to have the versions explicitly defined because I find it easier to work out what's going on that way but I'm sure there's an equally strong argument for just picking the latest version.</p>

