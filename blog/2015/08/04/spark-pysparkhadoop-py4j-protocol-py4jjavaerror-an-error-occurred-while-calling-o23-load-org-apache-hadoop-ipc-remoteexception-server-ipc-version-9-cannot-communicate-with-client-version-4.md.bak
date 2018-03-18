+++
draft = false
date="2015-08-04 06:35:40"
title="Spark: pyspark/Hadoop - py4j.protocol.Py4JJavaError: An error occurred while calling o23.load.: org.apache.hadoop.ipc.RemoteException: Server IPC version 9 cannot communicate with client version 4"
tag=['spark-2']
category=['Spark']
+++

<p>
I've been playing around with <a href="https://spark.apache.org/docs/0.9.0/python-programming-guide.html">pyspark</a> - Spark's Python library - and I wanted to execute the following job which takes a file from my local HDFS and then counts how many times each FBI code appears using <a href="https://spark.apache.org/docs/1.3.0/sql-programming-guide.html">Spark SQL</a>:
</p>



~~~python

from pyspark import SparkContext
from pyspark.sql import SQLContext

sc = SparkContext("local", "Simple App")
sqlContext = SQLContext(sc)

file = "hdfs://localhost:9000/user/markneedham/Crimes_-_2001_to_present.csv"

sqlContext.load(source="com.databricks.spark.csv", header="true", path = file).registerTempTable("crimes")
rows = sqlContext.sql("select `FBI Code` AS fbiCode, COUNT(*) AS times FROM crimes GROUP BY `FBI Code` ORDER BY times DESC").collect()

for row in rows:
    print("{0} -> {1}".format(row.fbiCode, row.times))
~~~

<p>I submitted the job and waited:</p>



~~~bash

$ ./spark-1.3.0-bin-hadoop1/bin/spark-submit --driver-memory 5g --packages com.databricks:spark-csv_2.10:1.1.0 fbi_spark.py
...
Traceback (most recent call last):
  File "/Users/markneedham/projects/neo4j-spark-chicago/fbi_spark.py", line 11, in <module>
    sqlContext.load(source="com.databricks.spark.csv", header="true", path = file).registerTempTable("crimes")
  File "/Users/markneedham/projects/neo4j-spark-chicago/spark-1.3.0-bin-hadoop1/python/pyspark/sql/context.py", line 482, in load
    df = self._ssql_ctx.load(source, joptions)
  File "/Users/markneedham/projects/neo4j-spark-chicago/spark-1.3.0-bin-hadoop1/python/lib/py4j-0.8.2.1-src.zip/py4j/java_gateway.py", line 538, in __call__
  File "/Users/markneedham/projects/neo4j-spark-chicago/spark-1.3.0-bin-hadoop1/python/lib/py4j-0.8.2.1-src.zip/py4j/protocol.py", line 300, in get_return_value
py4j.protocol.Py4JJavaError: An error occurred while calling o23.load.
: org.apache.hadoop.ipc.RemoteException: Server IPC version 9 cannot communicate with client version 4
	at org.apache.hadoop.ipc.Client.call(Client.java:1070)
	at org.apache.hadoop.ipc.RPC$Invoker.invoke(RPC.java:225)
	at com.sun.proxy.$Proxy7.getProtocolVersion(Unknown Source)
	at org.apache.hadoop.ipc.RPC.getProxy(RPC.java:396)
	at org.apache.hadoop.ipc.RPC.getProxy(RPC.java:379)
	at org.apache.hadoop.hdfs.DFSClient.createRPCNamenode(DFSClient.java:119)
	at org.apache.hadoop.hdfs.DFSClient.<init>(DFSClient.java:238)
	at org.apache.hadoop.hdfs.DFSClient.<init>(DFSClient.java:203)
	at org.apache.hadoop.hdfs.DistributedFileSystem.initialize(DistributedFileSystem.java:89)
	at org.apache.hadoop.fs.FileSystem.createFileSystem(FileSystem.java:1386)
	at org.apache.hadoop.fs.FileSystem.access$200(FileSystem.java:66)
	at org.apache.hadoop.fs.FileSystem$Cache.get(FileSystem.java:1404)
	at org.apache.hadoop.fs.FileSystem.get(FileSystem.java:254)
	at org.apache.hadoop.fs.Path.getFileSystem(Path.java:187)
	at org.apache.hadoop.mapred.FileInputFormat.listStatus(FileInputFormat.java:176)
	at org.apache.hadoop.mapred.FileInputFormat.getSplits(FileInputFormat.java:208)
	at org.apache.spark.rdd.HadoopRDD.getPartitions(HadoopRDD.scala:203)
	at org.apache.spark.rdd.RDD$$anonfun$partitions$2.apply(RDD.scala:219)
	at org.apache.spark.rdd.RDD$$anonfun$partitions$2.apply(RDD.scala:217)
	at scala.Option.getOrElse(Option.scala:120)
	at org.apache.spark.rdd.RDD.partitions(RDD.scala:217)
	at org.apache.spark.rdd.MapPartitionsRDD.getPartitions(MapPartitionsRDD.scala:32)
	at org.apache.spark.rdd.RDD$$anonfun$partitions$2.apply(RDD.scala:219)
	at org.apache.spark.rdd.RDD$$anonfun$partitions$2.apply(RDD.scala:217)
	at scala.Option.getOrElse(Option.scala:120)
	at org.apache.spark.rdd.RDD.partitions(RDD.scala:217)
	at org.apache.spark.rdd.RDD.take(RDD.scala:1156)
	at org.apache.spark.rdd.RDD.first(RDD.scala:1189)
	at com.databricks.spark.csv.CsvRelation.firstLine$lzycompute(CsvRelation.scala:129)
	at com.databricks.spark.csv.CsvRelation.firstLine(CsvRelation.scala:127)
	at com.databricks.spark.csv.CsvRelation.inferSchema(CsvRelation.scala:109)
	at com.databricks.spark.csv.CsvRelation.<init>(CsvRelation.scala:62)
	at com.databricks.spark.csv.DefaultSource.createRelation(DefaultSource.scala:115)
	at com.databricks.spark.csv.DefaultSource.createRelation(DefaultSource.scala:40)
	at com.databricks.spark.csv.DefaultSource.createRelation(DefaultSource.scala:28)
	at org.apache.spark.sql.sources.ResolvedDataSource$.apply(ddl.scala:290)
	at org.apache.spark.sql.SQLContext.load(SQLContext.scala:679)
	at org.apache.spark.sql.SQLContext.load(SQLContext.scala:667)
	at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
	at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)
	at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
	at java.lang.reflect.Method.invoke(Method.java:497)
	at py4j.reflection.MethodInvoker.invoke(MethodInvoker.java:231)
	at py4j.reflection.ReflectionEngine.invoke(ReflectionEngine.java:379)
	at py4j.Gateway.invoke(Gateway.java:259)
	at py4j.commands.AbstractCommand.invokeMethod(AbstractCommand.java:133)
	at py4j.commands.CallCommand.execute(CallCommand.java:79)
	at py4j.GatewayConnection.run(GatewayConnection.java:207)
	at java.lang.Thread.run(Thread.java:745)
~~~

<p>
It looks like my <a href="http://glennklockwood.blogspot.co.uk/2014/06/spark-on-supercomputers-few-notes.html">Hadoop Client and Server are using different versions</a> which in fact they are! We can see from the name of the spark folder that I'm using Hadoop 1.x there and if we check the local Hadoop version we'll notice it's using the 2.x seris:
</p>



~~~bash

$ hadoop version
Hadoop 2.6.0
~~~

<p>
In this case the easiest fix is use a version of Spark that's compiled against Hadoop 2.6 which as of now means Spark 1.4.1.
</p>


<p>Let's try and run our job again:</p>



~~~bash

$ ./spark-1.4.1-bin-hadoop2.6/bin/spark-submit --driver-memory 5g --packages com.databricks:spark-csv_2.10:1.1.0 fbi_spark.py

06 -> 859197
08B -> 653575
14 -> 488212
18 -> 457782
26 -> 431316
05 -> 257310
07 -> 197404
08A -> 188964
03 -> 157706
11 -> 112675
04B -> 103961
04A -> 60344
16 -> 47279
15 -> 40361
24 -> 31809
10 -> 22467
17 -> 17555
02 -> 17008
20 -> 15190
19 -> 10878
22 -> 8847
09 -> 6358
01A -> 4830
13 -> 1561
12 -> 835
01B -> 16
~~~

<p>And it's working!</p>

