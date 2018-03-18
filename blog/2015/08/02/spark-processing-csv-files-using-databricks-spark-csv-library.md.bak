+++
draft = false
date="2015-08-02 18:08:47"
title="Spark: Processing CSV files using Databricks Spark CSV Library"
tag=['spark-2']
category=['Spark']
+++

<p>
Last year I wrote about <a href="http://www.markhneedham.com/blog/2014/11/16/spark-parse-csv-file-and-group-by-column-value/">exploring the Chicago crime data set using Spark and the OpenCSV parser</a> and while this worked well, a few months ago I noticed that there's now a <a href="https://github.com/databricks/spark-csv">spark-csv</a> library which I should probably use instead.
</p>


<p>
I thought it'd be a fun exercise to translate my code to use it.
</p>


<p>
So to recap our goal: we want to count how many times each type of crime has been committed. I have a more up to date version of the crimes file now so the numbers won't be exactly the same.
</p>


<p>First let's launch the spark-shell and register our CSV file as a temporary table so we can query it as if it was a SQL table:</p>



~~~bash

$ ./spark-1.3.0-bin-hadoop1/bin/spark-shell

scala> import org.apache.spark.sql.SQLContext
import org.apache.spark.sql.SQLContext

scala> val crimeFile = "/Users/markneedham/Downloads/Crimes_-_2001_to_present.csv"
crimeFile: String = /Users/markneedham/Downloads/Crimes_-_2001_to_present.csv

scala> val sqlContext = new SQLContext(sc)
sqlContext: org.apache.spark.sql.SQLContext = org.apache.spark.sql.SQLContext@9746157

scala> sqlContext.load("com.databricks.spark.csv", Map("path" -> crimeFile, "header" -> "true")).registerTempTable("crimes")
java.lang.RuntimeException: Failed to load class for data source: com.databricks.spark.csv
	at scala.sys.package$.error(package.scala:27)
	at org.apache.spark.sql.sources.ResolvedDataSource$.lookupDataSource(ddl.scala:268)
	at org.apache.spark.sql.sources.ResolvedDataSource$.apply(ddl.scala:279)
	at org.apache.spark.sql.SQLContext.load(SQLContext.scala:679)
        at java.lang.reflect.Method.invoke(Method.java:497)
	at org.apache.spark.repl.SparkIMain$ReadEvalPrint.call(SparkIMain.scala:1065)
	at org.apache.spark.repl.SparkIMain$Request.loadAndRun(SparkIMain.scala:1338)
	at org.apache.spark.repl.SparkIMain.loadAndRunReq$1(SparkIMain.scala:840)
	at org.apache.spark.repl.SparkIMain.interpret(SparkIMain.scala:871)
	at org.apache.spark.repl.SparkIMain.interpret(SparkIMain.scala:819)
	at org.apache.spark.repl.SparkILoop.reallyInterpret$1(SparkILoop.scala:856)
	at org.apache.spark.repl.SparkILoop.interpretStartingWith(SparkILoop.scala:901)
	at org.apache.spark.repl.SparkILoop.command(SparkILoop.scala:813)
	at org.apache.spark.repl.SparkILoop.processLine$1(SparkILoop.scala:656)
	at org.apache.spark.repl.SparkILoop.innerLoop$1(SparkILoop.scala:664)
	at org.apache.spark.repl.SparkILoop.org$apache$spark$repl$SparkILoop$$loop(SparkILoop.scala:669)
	at org.apache.spark.repl.SparkILoop$$anonfun$org$apache$spark$repl$SparkILoop$$process$1.apply$mcZ$sp(SparkILoop.scala:996)
	at org.apache.spark.repl.SparkILoop$$anonfun$org$apache$spark$repl$SparkILoop$$process$1.apply(SparkILoop.scala:944)
	at org.apache.spark.repl.SparkILoop$$anonfun$org$apache$spark$repl$SparkILoop$$process$1.apply(SparkILoop.scala:944)
	at scala.tools.nsc.util.ScalaClassLoader$.savingContextLoader(ScalaClassLoader.scala:135)
	at org.apache.spark.repl.SparkILoop.org$apache$spark$repl$SparkILoop$$process(SparkILoop.scala:944)
	at org.apache.spark.repl.SparkILoop.process(SparkILoop.scala:1058)
	at org.apache.spark.repl.Main$.main(Main.scala:31)
	at org.apache.spark.repl.Main.main(Main.scala)
	at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
	at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)
	at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
	at java.lang.reflect.Method.invoke(Method.java:497)
	at org.apache.spark.deploy.SparkSubmit$.org$apache$spark$deploy$SparkSubmit$$runMain(SparkSubmit.scala:569)
	at org.apache.spark.deploy.SparkSubmit$.doRunMain$1(SparkSubmit.scala:166)
	at org.apache.spark.deploy.SparkSubmit$.submit(SparkSubmit.scala:189)
	at org.apache.spark.deploy.SparkSubmit$.main(SparkSubmit.scala:110)
	at org.apache.spark.deploy.SparkSubmit.main(SparkSubmit.scala)
~~~

<p>
I've actually forgotten to tell spark-shell about the CSV package so let's restart the shell and pass it as an argument:
</p>



~~~bash

$ ./spark-1.3.0-bin-hadoop1/bin/spark-shell --packages com.databricks:spark-csv_2.10:1.1.0

scala> import org.apache.spark.sql.SQLContext
import org.apache.spark.sql.SQLContext

scala> val crimeFile = "/Users/markneedham/Downloads/Crimes_-_2001_to_present.csv"
crimeFile: String = /Users/markneedham/Downloads/Crimes_-_2001_to_present.csv

scala> val sqlContext = new SQLContext(sc)
sqlContext: org.apache.spark.sql.SQLContext = org.apache.spark.sql.SQLContext@44587c44

scala> sqlContext.load("com.databricks.spark.csv", Map("path" -> crimeFile, "header" -> "true")).registerTempTable("crimes")
...
15/08/02 18:57:46 INFO TaskSchedulerImpl: Removed TaskSet 0.0, whose tasks have all completed, from pool
15/08/02 18:57:46 INFO DAGScheduler: Stage 0 (first at CsvRelation.scala:129) finished in 0.207 s
15/08/02 18:57:46 INFO DAGScheduler: Job 0 finished: first at CsvRelation.scala:129, took 0.267327 s
~~~

<p>Now we can write a simple SQL query on our 'crimes' table to find the most popular crime types:</p>



~~~bash

scala>  sqlContext.sql(
        """
        select `Primary Type` as primaryType, COUNT(*) AS times
        from crimes
        group by `Primary Type`
        order by times DESC
        """).save("/tmp/agg.csv", "com.databricks.spark.csv")
~~~

<p>That spits out a load of CSV 'part files' into <cite>/tmp/agg.csv</cite> so let's bring in the merge function that we've used previously to combine these into one CSV file:</p>



~~~scala

scala> import org.apache.hadoop.conf.Configuration
scala> import org.apache.hadoop.fs._

scala> def merge(srcPath: String, dstPath: String): Unit =  {
         val hadoopConfig = new Configuration()
         val hdfs = FileSystem.get(hadoopConfig)
         FileUtil.copyMerge(hdfs, new Path(srcPath), hdfs, new Path(dstPath), false, hadoopConfig, null)
       }

scala> merge("/tmp/agg.csv", "agg.csv")
~~~

<p>And finally let's browse the contents of our new CSV file:</p>



~~~bash

$ cat agg.csv
THEFT,1206745
BATTERY,1066110
CRIMINAL DAMAGE,672782
NARCOTICS,662257
OTHER OFFENSE,360824
ASSAULT,354583
BURGLARY,343443
MOTOR VEHICLE THEFT,278014
ROBBERY,218190
DECEPTIVE PRACTICE,197477
CRIMINAL TRESPASS,171363
PROSTITUTION,65660
WEAPONS VIOLATION,56218
PUBLIC PEACE VIOLATION,42446
OFFENSE INVOLVING CHILDREN,37010
CRIM SEXUAL ASSAULT,21346
SEX OFFENSE,21305
GAMBLING,13704
LIQUOR LAW VIOLATION,13264
INTERFERENCE WITH PUBLIC OFFICER,11366
ARSON,9642
HOMICIDE,7192
KIDNAPPING,6029
INTIMIDATION,3443
STALKING,2760
OBSCENITY,331
PUBLIC INDECENCY,123
OTHER NARCOTIC VIOLATION,106
CONCEALED CARRY LICENSE VIOLATION,34
NON-CRIMINAL,31
NON - CRIMINAL,25
RITUALISM,23
HUMAN TRAFFICKING,9
NON-CRIMINAL (SUBJECT SPECIFIED),3
DOMESTIC VIOLENCE,1
~~~

<p>
Great! We've got the same output with much less code which is always a #win.</p>

