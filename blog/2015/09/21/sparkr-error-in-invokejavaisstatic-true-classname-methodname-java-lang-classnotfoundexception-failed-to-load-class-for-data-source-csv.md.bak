+++
draft = false
date="2015-09-21 22:06:44"
title="SparkR: Error in invokeJava(isStatic = TRUE, className, methodName, ...) :  java.lang.ClassNotFoundException: Failed to load class for data source: csv."
tag=['spark-2']
category=['Spark']
+++

<p>
I've been wanting to play around with <a href="https://spark.apache.org/docs/latest/sparkr.html">SparkR</a> for a while and over the weekend deciding to explore a large <a href="">Land Registry CSV file</a> containing all the sales of properties in the UK over the last 20 years.

<p>First I started up the SparkR shell with the CSV package loaded in:</p>



~~~bash

./spark-1.5.0-bin-hadoop2.6/bin/sparkR --packages com.databricks:spark-csv_2.11:1.2.0
~~~

<p>
Next I tried to read the CSV file into a Spark data frame by modifying one of the examples from the tutorial:
</p>



~~~bash

> sales <- read.df(sqlContext, "pp-complete.csv", "csv")
15/09/20 19:13:02 ERROR RBackendHandler: loadDF on org.apache.spark.sql.api.r.SQLUtils failed
Error in invokeJava(isStatic = TRUE, className, methodName, ...) :
  java.lang.ClassNotFoundException: Failed to load class for data source: csv.
	at org.apache.spark.sql.execution.datasources.ResolvedDataSource$.lookupDataSource(ResolvedDataSource.scala:67)
	at org.apache.spark.sql.execution.datasources.ResolvedDataSource$.apply(ResolvedDataSource.scala:87)
	at org.apache.spark.sql.DataFrameReader.load(DataFrameReader.scala:114)
	at org.apache.spark.sql.api.r.SQLUtils$.loadDF(SQLUtils.scala:156)
	at org.apache.spark.sql.api.r.SQLUtils.loadDF(SQLUtils.scala)
	at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
	at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)
	at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
	at java.lang.reflect.Method.invoke(Method.java:497)
	at org.apache.spark.api.r.RBackendHandler.handleMethodCall(RBackendHandler.scala:132)
	at org.apache.spark.api.r.RBackendHandler.channelRead0(RBackendHandler.scala:79)
	at org.apache.spark.api.r.RBackendH
~~~

<p>
As far as I can tell I have loaded in the CSV data source so I'm not sure why that doesn't work.</p>
 

<p>However, I came across this <a href="https://github.com/databricks/spark-csv/issues/79">github issue</a> which suggested passing in the full package name as the 3rd argument of 'read.df' rather than just 'csv':
</p>



~~~bash

> sales <- read.df(sqlContext, "pp-complete.csv", "com.databricks.spark.csv", header="false")
> sales
DataFrame[C0:string, C1:string, C2:string, C3:string, C4:string, C5:string, C6:string, C7:string, C8:string, C9:string, C10:string, C11:string, C12:string, C13:string, C14:string]
~~~

<p>And that worked much better! We can now carry on and do some slicing and dicing of the data to see if there are any interesting insights.</p>

