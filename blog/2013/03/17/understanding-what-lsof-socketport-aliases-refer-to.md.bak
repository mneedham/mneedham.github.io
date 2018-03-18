+++
draft = false
date="2013-03-17 14:00:35"
title="Understanding what lsof socket/port aliases refer to"
tag=['software-development', 'devops-2']
category=['DevOps']
+++

<p>Earlier in the week we wanted to check which ports were being listened on and by what processes which we can do with the following command on Mac OS X:</p>



~~~text

$ lsof -ni | grep LISTEN
idea       2398 markhneedham   58u  IPv6 0xac8f13f77b903331      0t0  TCP *:49410 (LISTEN)
idea       2398 markhneedham   65u  IPv6 0xac8f13f7799a4af1      0t0  TCP *:58741 (LISTEN)
idea       2398 markhneedham  122u  IPv6 0xac8f13f7799a4711      0t0  TCP 127.0.0.1:6942 (LISTEN)
idea       2398 markhneedham  249u  IPv6 0xac8f13f777586711      0t0  TCP *:63342 (LISTEN)
idea       2398 markhneedham  253u  IPv6 0xac8f13f777586331      0t0  TCP 127.0.0.1:63342 (LISTEN)
java      16973 markhneedham  152u  IPv6 0xac8f13f777586af1      0t0  TCP *:56471 (LISTEN)
java      16973 markhneedham  154u  IPv6 0xac8f13f779e6b711      0t0  TCP *:menandmice-dns (LISTEN)
java      16973 markhneedham  168u  IPv6 0xac8f13f77b902f51      0t0  TCP 127.0.0.1:7474 (LISTEN)
java      16973 markhneedham  171u  IPv6 0xac8f13f77b013711      0t0  TCP 127.0.0.1:7473 (LISTEN)
~~~

<p>One of the interesting things about this output is that for the most part it shows the port number and which IPs it will accept a connection from but sometimes it uses a socket/port alias.</p>


<p>In this case we can see that the 3rd last line refers to 'menandmice-dns' but others could be 'http-alt' or 'mysql'.</p>


<p>We can find out what port those names refer to by looking in <cite>/etc/services</cite>:</p>



~~~text

$ cat /etc/services | grep menandmice-dns
menandmice-dns  1337/udp    # menandmice DNS
menandmice-dns  1337/tcp    # menandmice DNS
~~~


~~~text

$ cat /etc/services | grep http-alt
http-alt	591/udp     # FileMaker, Inc. - HTTP Alternate (see Port 80)
http-alt	591/tcp     # FileMaker, Inc. - HTTP Alternate (see Port 80)
http-alt	8008/udp     # HTTP Alternate
http-alt	8008/tcp     # HTTP Alternate
http-alt	8080/udp     # HTTP Alternate (see port 80)
http-alt	8080/tcp     # HTTP Alternate (see port 80)
~~~

<p>There's a <a href="http://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xml">massive XML document on the IANA website</a> with a full list of the port assignments which is presumably where <cite>/etc/services</cite> is derived from.</p>

