+++
draft = false
date="2013-04-18 23:36:32"
title="Puppet: Installing Oracle Java - oracle-license-v1-1 license could not be presented"
tag=['devops-2', 'vagrant']
category=['DevOps']
+++

<p>In order to run the neo4j server on my Ubuntu 12.04 Vagrant VM I needed to install the Oracle/Sun JDK which proved to be more difficult than I'd expected.</p>


<p>I initially tried to install it via the <a href="https://github.com/flexiondotorg/oab-java6">OAB-Java</a> script but was running into some dependency problems and eventually came across <a href="http://www.ubuntugeek.com/how-to-install-oracle-java-7-in-ubuntu-12-04.html">a post which specified a PPA</a> that had an installer I could use.</p>


<p>I wrote a little puppet Java module to wrap the commands in:</p>



~~~text

class java($version) {
  package { "python-software-properties": }
  
  exec { "add-apt-repository-oracle":
    command => "/usr/bin/add-apt-repository -y ppa:webupd8team/java",
    notify => Exec["apt_update"]
  }

  package { 'oracle-java7-installer':
    ensure => "${version}",
    require => [Exec['add-apt-repository-oracle']],
  }
}
~~~

<p>I then included this in my default node definition:</p>



~~~text

node default {
  class { 'java': version => '7u21-0~webupd8~0', }
}
~~~

<p>(as Dave Yeung points out in the comments, you may need to tweak the version. Running <cite>aptitude versions oracle-java7-installer</cite> should indicate the latest version.)</p>


<p>Unfortunately when I ran that I ended up with the following error:</p>



~~~text

err: /Stage[main]/Java/Package[oracle-java7-installer]/ensure: change from purged to present failed: Execution of '/usr/bin/apt-get -q -y -o DPkg::Options::=--force-confold install oracle-java7-installer' returned 100: Reading package lists...
Building dependency tree...
Reading state information...
The following extra packages will be installed:
  java-common
Suggested packages:
...
Unpacking oracle-java7-installer (from .../oracle-java7-installer_7u21-0~webupd8~0_all.deb) ...

oracle-license-v1-1 license could not be presented
try 'dpkg-reconfigure debconf' to select a frontend other than noninteractive

dpkg: error processing /var/cache/apt/archives/oracle-java7-installer_7u21-0~webupd8~0_all.deb (--unpack):
 subprocess new pre-installation script returned error exit status 2
Processing triggers for man-db ...
Errors were encountered while processing:
 /var/cache/apt/archives/oracle-java7-installer_7u21-0~webupd8~0_all.deb
E: Sub-process /usr/bin/dpkg returned an error code (1)
~~~

<p>I came across <a href="http://askubuntu.com/questions/190582/installing-java-automatically-with-silent-option">this post on Ask Ubuntu</a> which explained a neat trick for getting around it by making it look like we've agreed to the licence. This is done by passing options to <cite><a href="http://man.he.net/man1/debconf-set-selections">debconf-set-selections</a><cite>.</p>


<p>For a real server I guess you'd want some step where a person accepts the licence but since this is just for my hacking it seems to make sense.</p>


<p>My new Java manifest looks like this:</p>



~~~text

class java($version) {
  package { "python-software-properties": }
  
  exec { "add-apt-repository-oracle":
    command => "/usr/bin/add-apt-repository -y ppa:webupd8team/java",
    notify => Exec["apt_update"]
  }

  exec {
    'set-licence-selected':
      command => '/bin/echo debconf shared/accepted-oracle-license-v1-1 select true | /usr/bin/debconf-set-selections';

    'set-licence-seen':
      command => '/bin/echo debconf shared/accepted-oracle-license-v1-1 seen true | /usr/bin/debconf-set-selections';
  }

  package { 'oracle-java7-installer':
    ensure => "${version}",
    require => [Exec['add-apt-repository-oracle'], Exec['set-licence-selected'], Exec['set-licence-seen']],
  }
}
~~~
