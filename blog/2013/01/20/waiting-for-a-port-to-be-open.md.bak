+++
draft = false
date="2013-01-20 15:53:02"
title="telnet/netcat: Waiting for a port to be open"
tag=['devops-2']
category=['Software Development', 'DevOps']
+++

<p>On Friday <a href="http://junctionbox.ca/">Nathan</a> and I were setting up a new virtual machine and we needed a firewall rule to be created to allow us to connect to another machine which had some JAR files we wanted to download.</p>


<p>We wanted to know when it had been done by one of our operations team and I initially thought we might be able to do that using telnet:</p>



~~~text

$ telnet 10.0.0.1 8081
Trying 10.0.0.1...
telnet: connect to address 10.0.0.1: Operation timed out
telnet: Unable to connect to remote host
~~~

<p>We wanted to put a <a href="http://en.wikipedia.org/wiki/Watch_(Unix)">watch</a> on the command so that it would be repeated every few seconds and indicate when we'd could connect to the port. However, as as far as I can tell there's no way to reduce the length of the telnet timeout so Nathan suggested using netcat instead.</p>


<p>We ended up with the following command…</p>



~~~text

$ nc -v -w 1 10.0.0.1 8081
nc: connect to 10.0.0.1 port 8081 (tcp) failed: Connection refused
~~~

<p>...which we can then wire up with watch like so:</p>



~~~text

$ watch "nc -v -w 1 10.0.0.1 8081"

Every 2.0s: nc -v -w 1 10.0.0.1 8081                         Sun Jan 20 15:48:05 2013

nc: connect to 10.0.0.1 port 8081 (tcp) timed out: Operation now in progress
~~~

<p>And then when it works:</p>




~~~text

Every 2.0s: nc -v -w 1 10.0.0.1 8081                         Sun Jan 20 15:49:53 2013

Connection to 10.0.0.1 8081 port [tcp] succeeded!
~~~
