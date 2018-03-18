+++
draft = false
date="2012-07-15 08:14:16"
title="netcat: localhost resolution not working when sending UDP packets"
tag=['networking-2']
category=['Networking']
+++

As part of some work we were doing last week <a href="https://twitter.com/philandstuff">Phil</a> and I needed to send UDP packets to a local port and check that they were being picked up.

We initially tried sending a UDP packet to localhost port 8125 using netcat like so:


~~~text

echo -n "hello" | nc -w 1 -u localhost 8125
~~~

That message wasn't being received by the application listening on the port so Phil decided to try and send the same packet from Ruby which worked fine:


~~~ruby

require 'socket'
udp = UDPSocket.new
udp.send("hello", 0, "localhost", 8125)
~~~

We eventually worked out that 'localhost' wasn't being resolved by netcat which we thought was weird since it is correctly mapped:


~~~text

~$ ping localhost
PING localhost (127.0.0.1) 56(84) bytes of data.
64 bytes from localhost (127.0.0.1): icmp_seq=1 ttl=64 time=0.019 ms
~~~

We dumped the packets sent to port 8125 using tcpdump and noticed that the structure of the packets received when using localhost was massively different than when we used 127.0.0.1 but we couldn't work out what exactly was going wrong.

A better way would actually have been to listen on the port with netcat like so:


~~~text

nc -l -u 8125
~~~

In this case netcat doesn't output anything when we use the netcat command but does with the Ruby one.

I <a href="http://hintsforums.macworld.com/archive/index.php/t-101635.html">came across this post</a> which explains exactly what's going on:

<blockquote>
netcat is well behaved in that it will make the getaddrinfo() system call based on the arguments given to it. 

In the case of giving it the name "localhost", a port number and telling it to use UDP, netcat is not aware of the socket family to use for the getaddrinfo() system, so it will leave at it's default 0. 

getaddrinfo() will return <strong>all possible</strong> results for the query. In this case, where you aren't either specifying an actual IPv4 address (127.0.0.1), getaddrinfo() is <strong>also</strong> returning the IPv6 result, which is showing up first and therefore being used. 
</blockquote>

If we try that out in Ruby we can see what's going on:


~~~ruby

> Socket.getaddrinfo("localhost", 10002, nil, :DGRAM)
=> [["AF_INET6", 10002, "::1", "::1", 10, 2, 17], ["AF_INET", 10002, "127.0.0.1", "127.0.0.1", 2, 2, 17]]
~~~

netcat picks the first result which is "::1" - the IPv6 version of 'localhost' - and sends a UDP packet to that address. 

If we were using TCP then netcat would initially send a packet to that address, realise it had failed and then try the next address which is the IPv4 one. 

However since UDP is connectionless netcat can fire the packet and then forget about it, which is exactly what happens!

We can get around the problem by passing the <cite>-4</cite> flag to netcat which forces it to use IPv4 addresses only.

The 'getaddrinfo' lookup would presumably then look like this:


~~~ruby

Socket.getaddrinfo("localhost", 10002, :INET, :DGRAM)
=> [["AF_INET", 10002, "127.0.0.1", "127.0.0.1", 2, 2, 17], ["AF_INET", 10002, "127.0.0.1", "127.0.0.1", 2, 2, 17]]
~~~

Our final netcat command to send UDP packets therefore looks like this:


~~~text

echo -n "hello" | nc -w 1 -u -4 localhost 8125
~~~
