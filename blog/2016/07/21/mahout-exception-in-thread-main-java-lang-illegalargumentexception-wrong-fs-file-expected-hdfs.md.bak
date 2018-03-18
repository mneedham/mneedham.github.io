+++
draft = false
date="2016-07-21 17:57:41"
title="Mahout: Exception in thread \"main\" java.lang.IllegalArgumentException: Wrong FS: file:/... expected: hdfs://"
tag=['machine-learning-2', 'mahout']
category=['Hadoop']
+++

<p>
I've been playing around with Mahout over the last couple of days to see how well it works for content based filtering.</p>
 

<p>I started following <a href="http://stackoverflow.com/questions/22789986/does-mahout-provide-a-way-to-determine-similarity-between-content-for-content-b/22830903#22830903">a mini tutorial from Stack Overflow</a> but ran into trouble on the first step:
</p>



~~~bash

bin/mahout seqdirectory \
--input file:///Users/markneedham/Downloads/apache-mahout-distribution-0.12.2/foo \
--output file:///Users/markneedham/Downloads/apache-mahout-distribution-0.12.2/foo-out \
-c UTF-8 \
-chunk 64 \
-prefix mah
~~~


~~~bash

16/07/21 21:19:20 INFO AbstractJob: Command line arguments: {--charset=[UTF-8], --chunkSize=[64], --endPhase=[2147483647], --fileFilterClass=[org.apache.mahout.text.PrefixAdditionFilter], --input=[file:///Users/markneedham/Downloads/apache-mahout-distribution-0.12.2/foo], --keyPrefix=[mah], --method=[mapreduce], --output=[file:///Users/markneedham/Downloads/apache-mahout-distribution-0.12.2/foo-out], --startPhase=[0], --tempDir=[temp]}
16/07/21 21:19:20 WARN NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
16/07/21 21:19:20 INFO deprecation: mapred.input.dir is deprecated. Instead, use mapreduce.input.fileinputformat.inputdir
16/07/21 21:19:20 INFO deprecation: mapred.compress.map.output is deprecated. Instead, use mapreduce.map.output.compress
16/07/21 21:19:20 INFO deprecation: mapred.output.dir is deprecated. Instead, use mapreduce.output.fileoutputformat.outputdir
Exception in thread "main" java.lang.IllegalArgumentException: Wrong FS: file:/Users/markneedham/Downloads/apache-mahout-distribution-0.12.2/foo, expected: hdfs://localhost:8020
	at org.apache.hadoop.fs.FileSystem.checkPath(FileSystem.java:646)
	at org.apache.hadoop.hdfs.DistributedFileSystem.getPathName(DistributedFileSystem.java:194)
	at org.apache.hadoop.hdfs.DistributedFileSystem.access$000(DistributedFileSystem.java:106)
	at org.apache.hadoop.hdfs.DistributedFileSystem$22.doCall(DistributedFileSystem.java:1305)
	at org.apache.hadoop.hdfs.DistributedFileSystem$22.doCall(DistributedFileSystem.java:1301)
	at org.apache.hadoop.fs.FileSystemLinkResolver.resolve(FileSystemLinkResolver.java:81)
	at org.apache.hadoop.hdfs.DistributedFileSystem.getFileStatus(DistributedFileSystem.java:1301)
	at org.apache.mahout.text.SequenceFilesFromDirectory.runMapReduce(SequenceFilesFromDirectory.java:156)
	at org.apache.mahout.text.SequenceFilesFromDirectory.run(SequenceFilesFromDirectory.java:90)
	at org.apache.hadoop.util.ToolRunner.run(ToolRunner.java:70)
	at org.apache.hadoop.util.ToolRunner.run(ToolRunner.java:84)
	at org.apache.mahout.text.SequenceFilesFromDirectory.main(SequenceFilesFromDirectory.java:64)
	at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
	at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)
	at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
	at java.lang.reflect.Method.invoke(Method.java:498)
	at org.apache.hadoop.util.ProgramDriver$ProgramDescription.invoke(ProgramDriver.java:71)
	at org.apache.hadoop.util.ProgramDriver.run(ProgramDriver.java:144)
	at org.apache.hadoop.util.ProgramDriver.driver(ProgramDriver.java:152)
	at org.apache.mahout.driver.MahoutDriver.main(MahoutDriver.java:195)
	at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
	at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)
	at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
	at java.lang.reflect.Method.invoke(Method.java:498)
	at org.apache.hadoop.util.RunJar.run(RunJar.java:221)
	at org.apache.hadoop.util.RunJar.main(RunJar.java:136)
~~~

<p>
I was trying to run the command against the local file system on my laptop which should have been possible according to the instructions. I couldn't find any flag I could pass any flag that I could pass to Mahout to tell it not to use HDFS but I eventually stumbled on <a href="http://stackoverflow.com/questions/23779976/java-lang-illegalargumentexception-wrong-fs-expected-hdfs-localhost9000">someone else experiencing a similar problem</a>. 
</p>


<p>It turns out the last time I was playing around with Hadoop, in late 2015, I'd actually configured that and had completely forgotten. I needed to comment out the following config:
</p>


<p>

<em>/usr/local/Cellar/hadoop/2.7.1/libexec/etc/hadoop/core-site.xml</em>
</p>



~~~xml

<property>
    <name>fs.default.name</name>
    <value>hdfs://localhost:8020</value>
</property>
~~~

<p>
I commented that property out and all was happy with the (Hadoop) world again.
</p>

