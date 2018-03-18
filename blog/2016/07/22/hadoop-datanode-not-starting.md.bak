+++
draft = false
date="2016-07-22 13:31:15"
title="Hadoop: DataNode not starting"
tag=['hadoop']
category=['Hadoop']
+++

<p>In my <a href="http://www.markhneedham.com/blog/2016/07/21/mahout-exception-in-thread-main-java-lang-illegalargumentexception-wrong-fs-file-expected-hdfs/">continued playing with Mahout</a> I eventually decided to give up using my local file system and use a local Hadoop instead since that seems to have much less friction when following any examples.</p>


<p>
Unfortunately all my attempts to upload any files from my local file system to HDFS were being met with the following exception:
</p>



~~~text

java.io.IOException: File /user/markneedham/book2.txt could only be replicated to 0 nodes, instead of 1
at org.apache.hadoop.hdfs.server.namenode.FSNamesystem.getAdditionalBlock(FSNamesystem.java:1448)
at org.apache.hadoop.hdfs.server.namenode.NameNode.addBlock(NameNode.java:690)
at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:39)
at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:25)
at java.lang.reflect.Method.invoke(Method.java:597)
at org.apache.hadoop.ipc.WritableRpcEngine$Server.call(WritableRpcEngine.java:342)
at org.apache.hadoop.ipc.Server$Handler$1.run(Server.java:1350)
at org.apache.hadoop.ipc.Server$Handler$1.run(Server.java:1346)
at java.security.AccessController.doPrivileged(Native Method)
at javax.security.auth.Subject.doAs(Subject.java:396)
at org.apache.hadoop.security.UserGroupInformation.doAs(UserGroupInformation.java:742)
at org.apache.hadoop.ipc.Server$Handler.run(Server.java:1344)

at org.apache.hadoop.ipc.Client.call(Client.java:905)
at org.apache.hadoop.ipc.WritableRpcEngine$Invoker.invoke(WritableRpcEngine.java:198)
at $Proxy0.addBlock(Unknown Source)
at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:39)
at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:25)
at java.lang.reflect.Method.invoke(Method.java:597)
at org.apache.hadoop.io.retry.RetryInvocationHandler.invokeMethod(RetryInvocationHandler.java:82)
at org.apache.hadoop.io.retry.RetryInvocationHandler.invoke(RetryInvocationHandler.java:59)
at $Proxy0.addBlock(Unknown Source)
at org.apache.hadoop.hdfs.DFSOutputStream$DataStreamer.locateFollowingBlock(DFSOutputStream.java:928)
at org.apache.hadoop.hdfs.DFSOutputStream$DataStreamer.nextBlockOutputStream(DFSOutputStream.java:811)
at org.apache.hadoop.hdfs.DFSOutputStream$DataStreamer.run(DFSOutputStream.java:427)
~~~

<p>
I eventually realised, from looking at the output of <cite>jps</cite>, that the DataNode wasn't actually starting up which explains the error message I was seeing. 
</p>


<p>A quick look at the log files showed what was going wrong:</p>


<p>
<cite>
/usr/local/Cellar/hadoop/2.7.1/libexec/logs/hadoop-markneedham-datanode-marks-mbp-4.zte.com.cn.log
</cite>
</p>



~~~text

2016-07-21 18:58:00,496 WARN org.apache.hadoop.hdfs.server.common.Storage: java.io.IOException: Incompatible clusterIDs in /usr/local/Cellar/hadoop/hdfs/tmp/dfs/data: namenode clusterID = CID-c2e0b896-34a6-4dde-b6cd-99f36d613e6a; datanode clusterID = CID-403dde8b-bdc8-41d9-8a30-fe2dc951575c
2016-07-21 18:58:00,496 FATAL org.apache.hadoop.hdfs.server.datanode.DataNode: Initialization failed for Block pool <registering> (Datanode Uuid unassigned) service to /0.0.0.0:8020. Exiting.
java.io.IOException: All specified directories are failed to load.
        at org.apache.hadoop.hdfs.server.datanode.DataStorage.recoverTransitionRead(DataStorage.java:477)
        at org.apache.hadoop.hdfs.server.datanode.DataNode.initStorage(DataNode.java:1361)
        at org.apache.hadoop.hdfs.server.datanode.DataNode.initBlockPool(DataNode.java:1326)
        at org.apache.hadoop.hdfs.server.datanode.BPOfferService.verifyAndSetNamespaceInfo(BPOfferService.java:316)
        at org.apache.hadoop.hdfs.server.datanode.BPServiceActor.connectToNNAndHandshake(BPServiceActor.java:223)
        at org.apache.hadoop.hdfs.server.datanode.BPServiceActor.run(BPServiceActor.java:801)
        at java.lang.Thread.run(Thread.java:745)
2016-07-21 18:58:00,497 WARN org.apache.hadoop.hdfs.server.datanode.DataNode: Ending block pool service for: Block pool <registering> (Datanode Uuid unassigned) service to /0.0.0.0:8020
2016-07-21 18:58:00,602 INFO org.apache.hadoop.hdfs.server.datanode.DataNode: Removed Block pool <registering> (Datanode Uuid unassigned)
2016-07-21 18:58:02,607 WARN org.apache.hadoop.hdfs.server.datanode.DataNode: Exiting Datanode
2016-07-21 18:58:02,608 INFO org.apache.hadoop.util.ExitUtil: Exiting with status 0
2016-07-21 18:58:02,610 INFO org.apache.hadoop.hdfs.server.datanode.DataNode: SHUTDOWN_MSG:
~~~

<p>I'm not sure how my clusterIDs got out of sync, although I expect it's because I reformatted HDFS without realising at some stage. There are <a href="http://stackoverflow.com/questions/29166837/datanode-is-not-starting-in-singlenode-hadoop-2-6-0">other</a> <a href="http://stackoverflow.com/questions/22316187/datanode-not-starts-correctly">ways</a> of solving this problem but the quickest for me was to just nuke the DataNode's data directory which the log file told me sits here:</p>



~~~bash

sudo rm -r /usr/local/Cellar/hadoop/hdfs/tmp/dfs/data/current
~~~

<p>
I then re-ran the <cite>hstart</cite> script that I stole from <a href="https://getblueshift.com/setting-up-hadoop-2-4-and-pig-0-12-on-osx-locally/">this tutorial</a> and everything, including the DataNode this time, started up correctly:
</p>



~~~bash

$ jps
26736 NodeManager
26392 DataNode
26297 NameNode
26635 ResourceManager
26510 SecondaryNameNode
~~~

<p>
And now I can upload local files to HDFS again. #win!
</p>

