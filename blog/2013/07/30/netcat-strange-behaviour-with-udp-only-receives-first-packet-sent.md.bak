+++
draft = false
date="2013-07-30 06:01:47"
title="netcat: Strange behaviour with UDP - only receives first packet sent"
tag=['netcat']
category=['Networking']
+++

<p>I was playing around with <a href="http://nc110.sourceforge.net/">netcat</a> yesterday to create a client and server which would communicate via UDP packets and I rediscovered some "weird" behaviour which I'd previously encountered but not explained.</p>


<p>I started up a netcat server listening for UDP packets on port 9000 of my machine:</p>



~~~bash

$ nc -kluv localhost 9000
~~~

<p>We can check with lsof what running that command has done:</p>



~~~bash

$ lsof -Pni :9000
COMMAND   PID         USER   FD   TYPE             DEVICE SIZE/OFF NODE NAME
nc      63289 markhneedham    5u  IPv6 0xc99222a54b3975b5      0t0  UDP [::1]:9000
~~~

<p>We can see that the netcat process is listening on port 9000 so let's send it a UDP packet, using another netcat process:</p>



~~~bash

$ echo "mark" | nc -vvu localhost 9000 -4
Connection to localhost 9000 port [udp/cslistener] succeeded!
~~~

<p>We can see the sending of the UDP packet was successful and it shows up on the netcat server's terminal as well.</p>



~~~bash

$ nc -kluv localhost 9000
XXXXmark
~~~

<p>If we 'Ctrl-C' the netcat client and run it again we'll notice that it's still able to connect to the port but we don't see the message in the netcat server's terminal:</p>



~~~bash

$ echo "mike" | nc -vvu localhost 9000 -4
Connection to localhost 9000 port [udp/cslistener] succeeded!
~~~


~~~bash

$ nc -kluv localhost 9000
XXXXmark
~~~

<p>I wasn't sure what was going on but eventually came across <a href="http://stackoverflow.com/questions/7696862/strange-behavoiur-of-netcat-with-udp">an explanation by David Schwartz</a>:</p>


<blockquote>
When nc is listening to a UDP socket, it 'locks on' to the source port and source IP of the first packet it receives.

As soon as it received its first datagram (from port 52832), it issued a connect system call 'connecting' it to the 127.0.0.1:52832. For UDP, a connect rejects all packets that don't match the IP and port in the connect.
</blockquote>

<p>If we use lsof again we can see that we have exactly the same problem:</p>



~~~bash

$ lsof -Pni :9000
COMMAND   PID         USER   FD   TYPE             DEVICE SIZE/OFF NODE NAME
nc      63508 markhneedham    5u  IPv6 0xc99222a54b394c5d      0t0  UDP [::1]:9000->[::1]:63732
~~~

<p>In our case the netcat server has created a connection between port 9000 and port 63732 and rejects packets coming in from any other IP/port combination.</p>


<p>I thought 'Ctrl-C' on the netcat client would kill the connection but it doesn't.</p>


<p>At this stage I wasn't sure what to do but <a href="https://twitter.com/natbobc">Nathan</a> pointed out that if I made use of timeouts on the client and server then it would be possible to send multiple UDP packets.</p>


<p>I restarted the netcat server but this time with a 1 second timeout:</p>



~~~bash

$ nc -kluvw 1 localhost 9000
~~~

<p>And then started sending UDP packets from a netcat client also with a 1 second timeout:</p>



~~~bash

$ echo -e "all" | nc -vvuw 1 localhost 9000
Connection to localhost 9000 port [udp/cslistener] succeeded!
$ echo -e "the" | nc -vvuw 1 localhost 9000
Connection to localhost 9000 port [udp/cslistener] succeeded!
$ echo -e "udp" | nc -vvuw 1 localhost 9000
Connection to localhost 9000 port [udp/cslistener] succeeded!
$ echo -e "packets" | nc -vvuw 1 localhost 9000
Connection to localhost 9000 port [udp/cslistener] succeeded!
~~~

<p>And the netcat server now receives all of them:</p>



~~~bash

$ nc -kluvw 1 localhost 9000
XXXXall
XXXXthe
XXXXudp
XXXXpackets
~~~

<p>If we increase the client timeout a bit so that we can run lsof while it's connected we can see that the connection exists for the duration of the timeout:</p>



~~~bash

$ lsof -Pni :9000
COMMAND   PID         USER   FD   TYPE             DEVICE SIZE/OFF NODE NAME
nc      64317 markhneedham    5u  IPv6 0xc99222a54b394c5d      0t0  UDP [::1]:9000
nc      64541 markhneedham    5u  IPv6 0xc99222a54cc0101d      0t0  UDP [::1]:55792->[::1]:9000
~~~

<p>But then once it's finished it goes back to generally listening for UDP packets on that port which is exactly what we want:</p>



~~~bash

$ lsof -Pni :9000
COMMAND   PID         USER   FD   TYPE             DEVICE SIZE/OFF NODE NAME
nc      64317 markhneedham    5u  IPv6 0xc99222a54b394c5d      0t0  UDP [::1]:9000
~~~
