+++
draft = false
date="2012-01-18 00:30:59"
title="Installing Puppet on Oracle Linux"
tag=['software-development']
category=['Software Development']
+++

We've been spending some time trying to setup our developer environment on a Oracle Linux 5.7 build and one of the first steps was to install Puppet as we've already created scripts which automate the installation of most things.

Unfortunately Oracle Linux builds don't come with any yum repos configured so when you run the following command...


~~~text

ls -alh /etc/yum.repos.d/
~~~

...you don't see anything :(

We eventually realised that there are a <a href="http://public-yum.oracle.com/">list of public yum repositories on the Oracle website</a>, of which we needed to download the definition for Oracle Linux 5 like so:


~~~text

cd /etc/yum.repos.d
wget http://public-yum.oracle.com/public-yum-el5.repo
~~~

We then need to edit that file to enable the appropriate repository. In this case we want to enable <cite>ol5_u7_base</cite>:


~~~text

[ol5_u7_base]
name=Oracle Linux $releasever - U7 - $basearch - base
baseurl=http://public-yum.oracle.com/repo/OracleLinux/OL5/7/base/$basearch/
gpgkey=http://public-yum.oracle.com/RPM-GPG-KEY-oracle-el5
gpgcheck=1
enabled=1
~~~

I made the mistake of enabling <cite>ol5_u5_base</cite> which led to us getting some really weird problems whereby yum got confused as to which version of <cite>libselinux</cite> we had installed and was therefore unable to install <cite>libselinux-ruby</cite> as its dependencies weren't being properly satisfied.

Calling 'yum list installed' suggested that we had <cite>libselinux</cite> 1.33.4.5-7 installed but if we ran 'yum install libselinux' then it suggested we already had 1.33.4.5-5 installed. Very confusing!

After trying to uninstall and downgrade <cite>libselinux</cite> and pretty much destroying the installation in the process, another colleague spotted my mistake.

We also found that we had to add the epel repo which gave us access to some other packages that we needed:


~~~text

rpm -Uvh http://download.fedora.redhat.com/pub/epel/5/x86_64/epel-release-5-4.noarch.rpm
~~~

After all that was done we were able to run the command to install puppet:


~~~text

yum install puppet
~~~

That installs puppet 2.6.12 as that's the latest version in that repo. The latest stable version is 2.7.9 but I think we'll need to hook up a puppet specific repo to get that working.
