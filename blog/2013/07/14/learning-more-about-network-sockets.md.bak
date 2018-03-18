+++
draft = false
date="2013-07-14 09:52:17"
title="Learning more about network sockets"
tag=['software-development']
category=['Networking']
+++

<p>While reading through some of the <a href="https://github.com/neo4j/neo4j">neo4j code</a> a few weeks ago I realised that I didn't have a very good understanding about the mechanics behind network ports/sockets so I thought I'd try to learn more.</p>


<p>In particular I'd not considered what binding a socket to different network interfaces meant so I decided to setup a few examples using netcat to help me understand better.</p>


<p>To start with let's list the network interfaces that I have on my machine using ifconfig:</p>



~~~bash

$ ifconfig -u
lo0: flags=8049<UP,LOOPBACK,RUNNING,MULTICAST> mtu 16384
	options=3<RXCSUM,TXCSUM>
	inet6 fe80::1%lo0 prefixlen 64 scopeid 0x1 
	inet 127.0.0.1 netmask 0xff000000 
	inet6 ::1 prefixlen 128 
en0: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500
	ether xxxxxxxxxxxx
	inet6 fe80::9afe:94ff:fe4f:ee50%en0 prefixlen 64 scopeid 0x4 
	inet 192.168.1.89 netmask 0xffffff00 broadcast 192.168.1.255
	media: autoselect
	status: active
p2p0: flags=8843<UP,BROADCAST,RUNNING,SIMPLEX,MULTICAST> mtu 2304
	ether xxxxxxxxxxxx
	media: autoselect
	status: inactive
~~~

<p>'p2p0' isn't active so we'll only be able to use the other two to make a socket connection on the machine.</p>


<p>We'll use netcat to setup a server socket on port 4444 listening on the loopback interface:</p>



~~~bash

$ nc -l -k 127.0.0.1 4444
~~~

<p>We can use lsof to see how this has been setup:</p>



~~~bash

$ lsof -Pni :4444
COMMAND   PID         USER   FD   TYPE             DEVICE SIZE/OFF NODE NAME
java    34178 markhneedham   35u  IPv6 0x114b98295506482d      0t0  TCP 127.0.0.1:4444 (LISTEN)
~~~

<p>Let's try and connect to that port using netcat:</p>



~~~bash

$ nc -v 127.0.0.1 4444
Connection to 127.0.0.1 4444 port [tcp/krb524] succeeded!
~~~

<p>That works as we'd expect but if we try to connect using the IP of the 'en0' interface we'll get an error:</p>



~~~bash

$ nc -v 192.168.1.89 4444
nc: connect to 192.168.1.89 port 4444 (tcp) failed: Connection refused
~~~

<p>However, if we setup netcat to listen on the wildcard interface (0.0.0.0) then we would be able to connect to 4444 regardless of the interface:</p>



~~~bash

$ nc -l -k 0.0.0.0 4444
~~~


~~~bash

$ nc -v 192.168.1.89 4444
Connection to 192.168.1.89 4444 port [tcp/krb524] succeeded!
$ nc -v 127.0.0.1 4444
Connection to 127.0.0.1 4444 port [tcp/krb524] succeeded!
~~~

<p>If we check lsof it will confirm that we are listening on 4444 on all interfaces:</p


~~~bash

$ lsof -Pni :4444
COMMAND   PID         USER   FD   TYPE             DEVICE SIZE/OFF NODE NAME
nc      37725 markhneedham    3u  IPv4 0x114b98294ba8dfd5      0t0  TCP *:4444 (LISTEN)
~~~

<p>One thing I hadn't realised is that you can set up two different processes listening on the same port but on different interfaces. e.g.</p>



~~~bash

$ nc -l -k 127.0.0.1 4444
$ nc -l -k 0.0.0.0 4444
~~~

<p>We can see from lsof how this has been setup:</p>



~~~bash

$ lsof -Pni :4444
COMMAND   PID         USER   FD   TYPE             DEVICE SIZE/OFF NODE NAME
nc      38306 markhneedham    3u  IPv4 0x114b98294ba8dfd5      0t0  TCP *:4444 (LISTEN)
nc      38331 markhneedham    3u  IPv4 0x114b98294cc53fd5      0t0  TCP 127.0.0.1:4444 (LISTEN)
~~~

<p>If we make a socket connection to 127.0.0.1 it goes to our first netcat and if we use 192.168.1.89 the second one is used.</p>


<p>Finally, if we try to bind a server socket on an interface that we don't own netcat will fail in a fairly predictable way:</p>



~~~bash

$ nc -l -k 192.168.1.90 4444
nc: Can't assign requested address
~~~
