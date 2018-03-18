+++
draft = false
date="2012-08-10 00:58:46"
title="SSHing onto machines via a jumpbox"
tag=['shell-scripting-2', 'ssh']
category=['Shell Scripting']
+++

We wanted to be able to ssh into some machines which were behind a firewall so we set up a <a href="http://blog.industrialdefender.com/?p=612">jumpbox</a>  which our firewall directed any traffic on port 22 towards.

Initially if we wanted to SSH onto a machine inside the network we'd have to do a two step process:


~~~text

$ ssh jumpbox
# now on the jumpbx
$ ssh internal-network-machine
~~~

That got a bit annoying after a while so <a href="http://www.linkedin.com/in/samsharpe">Sam</a> showed us a neat way of proxying the second ssh command through the first one by making use of <a href="http://netcat.sourceforge.net/">netcat</a>.

We put the following into <cite>~/.ssh/config</cite>:


~~~text

Host jumpbox jumpbox-ip
 Hostname jumpbox-ip
 User     user
 IdentityFile ~/.ssh/id_rsa
 ProxyCommand none

Host internal-network-machine
  Hostname internal-network-machine-ip

Host 10.*
 User     ubuntu
 ProxyCommand ssh jumpbox exec nc -w 9000 %h %p
 UserKnownHostsFile /dev/null
 StrictHostKeyChecking no
~~~

The '-w 9000' flag defines a 2 1/2 hour wait period so that any <a href="http://www.lofar.org/wiki/doku.php?id=public:ssh-usage">orphaned connections will die off</a> within that time. 

%h and %p represent the host and port of the internal machine so in this case %h is 'internal-network-machine-ip' and the port will be 22.

We can then just do the following to ssh into the machine:


~~~text

ssh internal-network-machine
~~~

Which is pretty neat!

This is <a href="http://benno.id.au/blog/2006/06/08/ssh_proxy_command">explained further on benno's blog</a> and on the <a href="http://www.undeadly.org/cgi?action=article&sid=20070925181947">Open BSD journal</a>.
