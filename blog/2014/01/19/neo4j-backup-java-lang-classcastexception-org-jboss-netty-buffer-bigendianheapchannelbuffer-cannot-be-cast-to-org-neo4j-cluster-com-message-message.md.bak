+++
draft = false
date="2014-01-19 19:29:16"
title="Neo4j Backup: java.lang.ClassCastException: org.jboss.netty.buffer.BigEndianHeapChannelBuffer cannot be cast to org.neo4j.cluster.com.message.Message"
tag=['neo4j']
category=['neo4j']
+++

<p><em>(as Gabriel points out in the comments the ability to do a 'HA backup' doesn't exist in more recent versions of Neo4j. I'll leave this post here for people still running on older versions who encounter the error.)</em></p>


<p>When using Neo4j's online backup facility there are two ways of triggering it, either by using the '<a href="http://docs.neo4j.org/chunked/milestone/backup-embedded-and-server.html">single://</a>' or '<a href="http://docs.neo4j.org/chunked/milestone/backup-ha.html">ha://</a>' syntax and these behave slightly differently.</p>


<p>If you're using the 'single://' syntax and don't specify a port then it will connect to '6362' by default:</p>



~~~bash

./neo4j-backup -from single://192.168.1.34 -to /mnt/backup/neo4j-backup
~~~

<p>If you've changed the backup port via the 'online_backup_server' property in <cite>conf/neo4j.properties</cite> you'll need to set the port explicitly:</p>



~~~text

online_backup_server=192.168.1.34:6363
~~~


~~~bash

./neo4j-backup -from single://192.168.1.34:6363 -to /mnt/backup/neo4j-backup
~~~

<p>If you're using the 'ha://' syntax then the backup client joins the HA cluster, works out which machine is the master and then creates a backup from that machine.</p>


<p>In order for the backup client to join the cluster it connects to port '5001' by default:</p>



~~~bash

./neo4j-backup -from ha://192.168.1.34 -to /mnt/backup/neo4j-backup
~~~

<p>If you've changed the 'ha.cluster_server' property then you'll need to set the port explicitly:</p>



~~~text

ha.cluster_server=192.168.1.34:5002
~~~


~~~bash

./neo4j-backup -from ha://192.168.1.34:5002 -to /mnt/backup/neo4j-backup
~~~

<p>A mistake that I made when first using this utility was to use the 'ha://' syntax with the backup port. e.g.</p>



~~~bash

./neo4j-backup -from ha://192.168.1.34:6362 -to /mnt/backup/neo4j-backup
~~~

<p>If you do this you'll end up with the following exception:</p>



~~~text

2014-01-19 19:24:30.842+0000 ERROR [o.n.c.c.NetworkSender]: Receive exception:
java.lang.ClassCastException: org.jboss.netty.buffer.BigEndianHeapChannelBuffer cannot be cast to org.neo4j.cluster.com.message.Message
	at org.neo4j.cluster.com.NetworkSender$NetworkMessageSender.messageReceived(NetworkSender.java:409) ~[neo4j-cluster-2.0.0.jar:2.0.0]
	at org.jboss.netty.channel.Channels.fireMessageReceived(Channels.java:268) ~[netty-3.6.3.Final.jar:na]
	at org.jboss.netty.channel.Channels.fireMessageReceived(Channels.java:255) ~[netty-3.6.3.Final.jar:na]
	at org.jboss.netty.channel.socket.nio.NioWorker.read(NioWorker.java:88) ~[netty-3.6.3.Final.jar:na]
	at org.jboss.netty.channel.socket.nio.AbstractNioWorker.process(AbstractNioWorker.java:107) ~[netty-3.6.3.Final.jar:na]
	at org.jboss.netty.channel.socket.nio.AbstractNioSelector.run(AbstractNioSelector.java:312) ~[netty-3.6.3.Final.jar:na]
	at org.jboss.netty.channel.socket.nio.AbstractNioWorker.run(AbstractNioWorker.java:88) ~[netty-3.6.3.Final.jar:na]
	at org.jboss.netty.channel.socket.nio.NioWorker.run(NioWorker.java:178) ~[netty-3.6.3.Final.jar:na]
	at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1145) [na:1.7.0_45]
	at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:615) [na:1.7.0_45]
	at java.lang.Thread.run(Thread.java:744) [na:1.7.0_45]
~~~

<p>Let me know in the comments if any of this doesn't make sense. There are lots of other examples to follow on <a href="http://docs.neo4j.org/chunked/milestone/re04.html">neo4j-backup's man page</a> in the manual as well.</p>

