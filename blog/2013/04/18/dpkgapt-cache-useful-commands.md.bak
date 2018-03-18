+++
draft = false
date="2013-04-18 21:54:10"
title="dpkg/apt-cache: Useful commands"
tag=['devops-2', 'dpkg', 'apt']
category=['DevOps']
+++

<p>As I've mentioned in a couple of previous posts I've been playing around with creating a Vagrant VM that I can use for my neo4j hacking which has involved a lot of messing around with installing apt packages.</p>


<p>There are loads of different ways of working out what's going on when packages aren't installing as you'd expect so I thought it'd be good to document the ones I've been using so I can find them more easily next time.</p>


<h4>Finding reverse dependencies</h4>

<p>A couple of times I found myself wondering how a certain package had ended up on the VM because I hadn't specified that it should be installed so I wanted to know who had!</p>


<p>I wanted to find out the reverse dependency for the package. e.g. to find out who depended on make which we can find out with the following command:</p>



~~~text

$ apt-cache rdepends make
make
Reverse Depends:
...
  build-essential
  make:i386
  libc6-dev:i386
  open-vm-dkms
  mythbuntu-desktop
  broadcom-sta-source
...
~~~

<p>The nice thing about 'rdepends' is that it will tell us reverse dependencies even for a package that we haven't installed. This was helpful here as I had forgotten to install 'build-essential' and this made it obvious.</p>


<h4>Finding which version of a package is installed</h4>

<p>I added one of the Brightbox repositories to get a more recent Ruby version and noticed that something weird was going on with the version of 'nginx-common' that puppet was trying to install.</p>


<p>It seemed like one one my dependencies was trying to pull in the 'latest' version of 'nginx-common' which I'd expected to be '1.1.19-1ubuntu0.1'.</p>


<p>By passing the 'policy' flag to apt-cache I was able to see that there was a recent version available via Brightbox:</p>



~~~text

$ apt-cache policy nginx-common
nginx-common:
  Installed: 1.1.19-1ubuntu0.1
  Candidate: 1:1.2.6-1~43~precise1
  Version table:
     1:1.2.6-1~43~precise1 0
        500 http://ppa.launchpad.net/brightbox/ruby-ng/ubuntu/ precise/main amd64 Packages
 *** 1.1.19-1ubuntu0.1 0
        500 http://us.archive.ubuntu.com/ubuntu/ precise-updates/universe amd64 Packages
        100 /var/lib/dpkg/status
     1.1.19-1 0
        500 http://us.archive.ubuntu.com/ubuntu/ precise/universe amd64 Packages
~~~

<h4>Finding which versions of a package are available</h4>

<p>Another flag that we can pass to apt-cache is 'madison' which shows us the available versions for a package but doesn't indicate which version is installed:</p>



~~~text

$ apt-cache madison nginx-common
nginx-common | 1:1.2.6-1~43~precise1 | http://ppa.launchpad.net/brightbox/ruby-ng/ubuntu/ precise/main amd64 Packages
nginx-common | 1.1.19-1ubuntu0.1 | http://us.archive.ubuntu.com/ubuntu/ precise-updates/universe amd64 Packages
nginx-common |   1.1.19-1 | http://us.archive.ubuntu.com/ubuntu/ precise/universe amd64 Packages
     nginx |   1.1.19-1 | http://us.archive.ubuntu.com/ubuntu/ precise/universe Sources
     nginx | 1.1.19-1ubuntu0.1 | http://us.archive.ubuntu.com/ubuntu/ precise-updates/universe Sources
     nginx | 1:1.2.6-1~43~precise1 | http://ppa.launchpad.net/brightbox/ruby-ng/ubuntu/ precise/main Sources
~~~

<h4>Finding which package a file belongs to</h4>

<p>At some stage I wanted to check which exact package was installing nginx which I was able to do with the following command:</p>



~~~text

$ dpkg -S `which nginx`
nginx-extras: /usr/sbin/nginx
~~~

<p>I had installed 'nginx-common' which I learn depends on 'nginx-extras' by using our 'rdepends' command:</p>



~~~text

$ apt-cache rdepends nginx-extras
nginx-extras
Reverse Depends:
  nginx-naxsi:i386
...
  nginx-common
~~~

<h4>Finding the dependencies of a package</h4>

<p>I wanted to check the dependencies of the 'ruby1.9.1' package to see whether or not I needed to explicitly install 'libruby1.9.1' or if that would be taken care of.</p>


<p>Passing the '-s' flag to dpkg let me check this:</p>



~~~text

$ dpkg -s ruby1.9.1
Package: ruby1.9.1
Status: install ok installed
Architecture: amd64
Version: 1:1.9.3.327-1bbox2~precise1
Replaces: irb1.9.1, rdoc1.9.1, rubygems1.9.1
Provides: irb1.9.1, rdoc1.9.1, ruby-interpreter, rubygems1.9.1
Depends: libruby1.9.1 (= 1:1.9.3.327-1bbox2~precise1), libc6 (>= 2.2.5)
Suggests: ruby1.9.1-examples, ri1.9.1, graphviz, ruby1.9.1-dev, ruby-switch
Conflicts: irb1.9.1 (<< 1.9.1.378-2~), rdoc1.9.1 (<< 1.9.1.378-2~), ri (<= 4.5), ri1.9.1 (<< 1.9.2.180-3~), ruby (<= 4.5), rubygems1.9.1
...
~~~

<p>These are the ones that I've found useful so far. I'd love to here other people's favourites though as I'm undoubtably missing some.</p>

