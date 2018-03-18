+++
draft = false
date="2014-11-27 12:28:14"
title="Docker/Neo4j: Port forwarding on Mac OS X not working"
tag=['docker']
category=['Software Development']
+++

<p>Prompted by <a href="http://ognjenbubalo.blogspot.co.uk/2014/11/creating-graph-of-software-technologies.html">Ognjen Bubalo's excellent blog post</a> I thought it was about time I tried running Neo4j on a docker container on my Mac Book Pro to make it easier to play around with different data sets.</p>
 

<p>I got the container up and running by following Ognien's instructions and had the following ports forwarded to my host machine:</p>



~~~bash

$ docker ps
CONTAINER ID        IMAGE                 COMMAND                CREATED             STATUS              PORTS                                              NAMES
c62f8601e557        tpires/neo4j:latest   "/bin/bash -c /launc   About an hour ago   Up About an hour    0.0.0.0:49153->1337/tcp, 0.0.0.0:49154->7474/tcp   neo4j
~~~

<p>This should allow me to access Neo4j on port 49154 but when I tried to access that host:port pair I got a connection refused message:</p>



~~~bash

$ curl -v http://localhost:49154
* Adding handle: conn: 0x7ff369803a00
* Adding handle: send: 0
* Adding handle: recv: 0
* Curl_addHandleToPipeline: length: 1
* - Conn 0 (0x7ff369803a00) send_pipe: 1, recv_pipe: 0
* About to connect() to localhost port 49154 (#0)
*   Trying ::1...
*   Trying 127.0.0.1...
*   Trying fe80::1...
* Failed connect to localhost:49154; Connection refused
* Closing connection 0
curl: (7) Failed connect to localhost:49154; Connection refused
~~~

<p>My first thought was the maybe Neo4j hadn't started up correctly inside the container so I checked the logs:</p>



~~~bash

$ docker logs --tail=10 c62f8601e557
10:59:12.994 [main] INFO  o.e.j.server.handler.ContextHandler - Started o.e.j.w.WebAppContext@2edfbe28{/webadmin,jar:file:/usr/share/neo4j/system/lib/neo4j-server-2.1.5-static-web.jar!/webadmin-html,AVAILABLE}
10:59:13.449 [main] INFO  o.e.j.server.handler.ContextHandler - Started o.e.j.s.ServletContextHandler@192efb4e{/db/manage,null,AVAILABLE}
10:59:13.699 [main] INFO  o.e.j.server.handler.ContextHandler - Started o.e.j.s.ServletContextHandler@7e94c035{/db/data,null,AVAILABLE}
10:59:13.714 [main] INFO  o.e.j.w.StandardDescriptorProcessor - NO JSP Support for /browser, did not find org.apache.jasper.servlet.JspServlet
10:59:13.715 [main] INFO  o.e.j.server.handler.ContextHandler - Started o.e.j.w.WebAppContext@3e84ae71{/browser,jar:file:/usr/share/neo4j/system/lib/neo4j-browser-2.1.5.jar!/browser,AVAILABLE}
10:59:13.807 [main] INFO  o.e.j.server.handler.ContextHandler - Started o.e.j.s.ServletContextHandler@4b6690b1{/,null,AVAILABLE}
10:59:13.819 [main] INFO  o.e.jetty.server.ServerConnector - Started ServerConnector@495350f0{HTTP/1.1}{c62f8601e557:7474}
10:59:13.900 [main] INFO  o.e.jetty.server.ServerConnector - Started ServerConnector@23ad0c5a{SSL-HTTP/1.1}{c62f8601e557:7473}
2014-11-27 10:59:13.901+0000 INFO  [API] Server started on: http://c62f8601e557:7474/
2014-11-27 10:59:13.902+0000 INFO  [API] Remote interface ready and available at [http://c62f8601e557:7474/]
~~~

<p>Nope! It's up and running perfectly fine which suggested the problemw was with port forwarding.</p>


<p>I eventually found my way to Chris Jones' '<a href="http://viget.com/extend/how-to-use-docker-on-os-x-the-missing-guide">How to use Docker on OS X: The Missing Guide</a>' which explained the problem:</p>


<blockquote>
The Problem: Docker forwards ports from the container to the host, which is boot2docker, not OS X.

The Solution: Use the VM’s IP address.
</blockquote>

<p>So to access Neo4j on my machine I need to use the VM's IP address rather than localhost. We can get the VM's IP address like so:</p>



~~~bash

$ boot2docker ip

The VM's Host only interface IP address is: 192.168.59.103
~~~

<p>Let's strip out that surrounding text though:</p>



~~~bash

$ boot2docker ip 2> /dev/null
192.168.59.103
~~~

<p>Now if we cURL using that IP instead:</p>



~~~bash

$ curl -v http://192.168.59.103:49154
* About to connect() to 192.168.59.103 port 49154 (#0)
*   Trying 192.168.59.103...
* Adding handle: conn: 0x7fd794003a00
* Adding handle: send: 0
* Adding handle: recv: 0
* Curl_addHandleToPipeline: length: 1
* - Conn 0 (0x7fd794003a00) send_pipe: 1, recv_pipe: 0
* Connected to 192.168.59.103 (192.168.59.103) port 49154 (#0)
> GET / HTTP/1.1
> User-Agent: curl/7.30.0
> Host: 192.168.59.103:49154
> Accept: */*
>
< HTTP/1.1 200 OK
< Content-Type: application/json; charset=UTF-8
< Access-Control-Allow-Origin: *
< Content-Length: 112
* Server Jetty(9.0.5.v20130815) is not blacklisted
< Server: Jetty(9.0.5.v20130815)
<
{
  "management" : "http://192.168.59.103:49154/db/manage/",
  "data" : "http://192.168.59.103:49154/db/data/"
* Connection #0 to host 192.168.59.103 left intact
~~~

<p>Happy days!</p>


<p>Chris has solutions to lots of other common problems people come across when using Docker with Mac OS X so it's worth <a href="http://viget.com/extend/how-to-use-docker-on-os-x-the-missing-guide">having a flick through his post</a>.</p>

