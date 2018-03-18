+++
draft = false
date="2016-07-22 13:55:14"
title="Mahout/Hadoop: org.apache.hadoop.ipc.RemoteException: Server IPC version 9 cannot communicate with client version 4"
tag=['mahout', 'hadoop']
category=['Hadoop']
+++

<p>
I've been working my way through <a href="http://stackoverflow.com/a/22830903/1093511">Dragan Milcevski's mini tutorial</a> on using Mahout to do content based filtering on documents and reached the final step where I needed to read in the generated item-similarity files.
</p>


<p>
I got the example compiling by using the following Maven dependency:
</p>



~~~xml

<dependency>
      <groupId>org.apache.mahout</groupId>
      <artifactId>mahout-core</artifactId>
      <version>0.9</version>
</dependency>
~~~

<p>Unfortunately when I ran the code I ran into a version incompatibility problem:</p>



~~~text

Exception in thread "main" org.apache.hadoop.ipc.RemoteException: Server IPC version 9 cannot communicate with client version 4
	at org.apache.hadoop.ipc.Client.call(Client.java:1113)
	at org.apache.hadoop.ipc.RPC$Invoker.invoke(RPC.java:229)
	at com.sun.proxy.$Proxy1.getProtocolVersion(Unknown Source)
	at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
	at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)
	at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
	at java.lang.reflect.Method.invoke(Method.java:497)
	at org.apache.hadoop.io.retry.RetryInvocationHandler.invokeMethod(RetryInvocationHandler.java:85)
	at org.apache.hadoop.io.retry.RetryInvocationHandler.invoke(RetryInvocationHandler.java:62)
	at com.sun.proxy.$Proxy1.getProtocolVersion(Unknown Source)
	at org.apache.hadoop.ipc.RPC.checkVersion(RPC.java:422)
	at org.apache.hadoop.hdfs.DFSClient.createNamenode(DFSClient.java:183)
	at org.apache.hadoop.hdfs.DFSClient.<init>(DFSClient.java:281)
	at org.apache.hadoop.hdfs.DFSClient.<init>(DFSClient.java:245)
	at org.apache.hadoop.hdfs.DistributedFileSystem.initialize(DistributedFileSystem.java:100)
	at org.apache.hadoop.fs.FileSystem.createFileSystem(FileSystem.java:1446)
	at org.apache.hadoop.fs.FileSystem.access$200(FileSystem.java:67)
	at org.apache.hadoop.fs.FileSystem$Cache.get(FileSystem.java:1464)
	at org.apache.hadoop.fs.FileSystem.get(FileSystem.java:263)
	at org.apache.hadoop.fs.FileSystem.get(FileSystem.java:124)
	at com.markhneedham.mahout.Similarity.getDocIndex(Similarity.java:86)
	at com.markhneedham.mahout.Similarity.main(Similarity.java:25)
	at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
	at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)
	at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
	at java.lang.reflect.Method.invoke(Method.java:497)
	at com.intellij.rt.execution.application.AppMain.main(AppMain.java:144)
~~~

<p>
Version 0.9.0 of mahout-core was published in early 2014 so I expect it was built against an earlier version of Hadoop than I'm using (2.7.2).
</p>


<p>I tried updating the Hadoop dependencies that were being called in the stack trace to no avail.</p>



~~~xml

<dependency>
    <groupId>org.apache.hadoop</groupId>
    <artifactId>hadoop-client</artifactId>
    <version>2.7.2</version>
</dependency>

<dependency>
    <groupId>org.apache.hadoop</groupId>
    <artifactId>hadoop-hdfs</artifactId>
    <version>2.7.2</version>
</dependency>
~~~

<p>
When stepping through the stack trace I noticed that my program was still using an old version of hadoop-core, so with one last throw of the dice I decided to try explicitly excluding that:
</p>



~~~xml

<dependency>
    <groupId>org.apache.mahout</groupId>
    <artifactId>mahout-core</artifactId>
    <version>0.9</version>

    <exclusions>
        <exclusion>
            <groupId>org.apache.hadoop</groupId>
            <artifactId>hadoop-core</artifactId>
        </exclusion>
    </exclusions>
</dependency>
~~~

<p>And amazingly it worked. Now, finally, I can see how similar my documents are!</p>

