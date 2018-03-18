+++
draft = false
date="2015-10-27 23:10:47"
title="Spark: MatchError (of class org.apache.spark.sql.catalyst.expressions.GenericRow) spark"
tag=['spark-2']
category=['Spark']
+++

<p>
I've been using <a href="http://spark.apache.org/">Spark</a> again lately to do some pre-processing on the <a href="https://data.gov.uk/dataset/land-registry-monthly-price-paid-data">Land Registry data set</a> and ran into an initially confusing problem when trying to parse the CSV file.
</p>


<p>
I'm using the <a href="https://github.com/databricks/spark-csv">Databricks CSV parsing library</a> and wrote the following script to go over each row, collect up the address components and then derive a 'fullAddress' field.
</p>


<p>
To refresh, this is what the CSV file looks like:
</p>



~~~bash

$ head  -n5 pp-complete.csv
"{0C7ADEF5-878D-4066-B785-0000003ED74A}","163000","2003-02-21 00:00","UB5 4PJ","T","N","F","106","","READING ROAD","NORTHOLT","NORTHOLT","EALING","GREATER LONDON","A"
"{35F67271-ABD4-40DA-AB09-00000085B9D3}","247500","2005-07-15 00:00","TA19 9DD","D","N","F","58","","ADAMS MEADOW","ILMINSTER","ILMINSTER","SOUTH SOMERSET","SOMERSET","A"
"{B20B1C74-E8E1-4137-AB3E-0000011DF342}","320000","2010-09-10 00:00","W4 1DZ","F","N","L","58","","WHELLOCK ROAD","","LONDON","EALING","GREATER LONDON","A"
"{7D6B0915-C56B-4275-AF9B-00000156BCE7}","104000","1997-08-27 00:00","NE61 2BH","D","N","F","17","","WESTGATE","MORPETH","MORPETH","CASTLE MORPETH","NORTHUMBERLAND","A"
"{47B60101-B64C-413D-8F60-000002F1692D}","147995","2003-05-02 00:00","PE33 0RU","D","N","F","4","","MASON GARDENS","WEST WINCH","KING'S LYNN","KING'S LYNN AND WEST NORFOLK","NORFOLK","A"
~~~


~~~scala

import org.apache.spark.sql.{SQLContext, _}
import org.apache.spark.{SparkConf, SparkContext}

case class BlogTransaction(price: Integer, date: String, postCode:String, paon:String, saon:String, street:String, locality:String, city:String, district:String, county:String)

object BlogApp {
  def main(args: Array[String]) {
    val conf = new SparkConf().setAppName("Simple Application")
    val sc = new SparkContext(conf)
    val sqlContext = new SQLContext(sc)
    import sqlContext.implicits._

    sqlContext.read.format("com.databricks.spark.csv").load("/Users/markneedham/projects/land-registry/pp-complete.csv").registerTempTable("transactions")

    val rows = sqlContext.sql("select C1,C2,C3,C7,C8,C9,C10,C11,C12,C13 from transactions where transactions.C3 = 'SW3 4EU'").map(x =>
      Row.fromSeq(x.toSeq ++ Array(Array(x.get(4), x.get(3), x.get(5), x.get(6), x.get(7), x.get(8), x.get(9), x.get(2))
        .map(x => x.toString)
        .filter(x => !x.isEmpty)
        .distinct
        .mkString(" / "))))

    val path: String = "/tmp/tx-" + System.currentTimeMillis() + ".csv"
    rows.map {
      case Row(price: Integer, date: String, postCode:String, paon:String, saon:String, street:String, locality:String, city:String, district:String, county:String) =>
        BlogTransaction(price, date, postCode, paon, saon, street, locality, city, district, county) }
      .toDF()
      .write
      .format("com.databricks.spark.csv")
      .save(path)
  }
}
~~~

<p>Let's execute that job against a local Spark worker:</p>



~~~bash

./spark-1.5.0-bin-hadoop2.6/bin/spark-submit --class BlogApp --master local[8] --packages com.databricks:spark-csv_2.10:1.2.0 target/scala-2.10/simple-project_2.10-1.0.jar

15/10/27 22:56:41 INFO Executor: Executor killed task 7.0 in stage 1.0 (TID 8)
Exception in thread "main" org.apache.spark.SparkException: Job aborted due to stage failure: Task 2 in stage 1.0 failed 1 times, most recent failure: Lost task 2.0 in stage 1.0 (TID 3, localhost): scala.MatchError: [14850000,2013-11-13 00:00,SW3 4EU,9,,ORMONDE GATE,,LONDON,KENSINGTON AND CHELSEA,GREATER LONDON,9 / ORMONDE GATE / LONDON / KENSINGTON AND CHELSEA / GREATER LONDON / SW3 4EU] (of class org.apache.spark.sql.catalyst.expressions.GenericRow)
	at BlogApp$$anonfun$main$1.apply(BlogApp.scala:24)
	at BlogApp$$anonfun$main$1.apply(BlogApp.scala:24)
	at scala.collection.Iterator$$anon$11.next(Iterator.scala:328)
	at scala.collection.Iterator$$anon$11.next(Iterator.scala:328)
	at scala.collection.Iterator$$anon$11.next(Iterator.scala:328)
	at com.databricks.spark.csv.package$CsvSchemaRDD$$anonfun$5$$anon$1.next(package.scala:154)
	at com.databricks.spark.csv.package$CsvSchemaRDD$$anonfun$5$$anon$1.next(package.scala:147)
	at scala.collection.Iterator$$anon$11.next(Iterator.scala:328)
	at org.apache.spark.rdd.PairRDDFunctions$$anonfun$saveAsHadoopDataset$1$$anonfun$13$$anonfun$apply$6.apply$mcV$sp(PairRDDFunctions.scala:1109)
	at org.apache.spark.rdd.PairRDDFunctions$$anonfun$saveAsHadoopDataset$1$$anonfun$13$$anonfun$apply$6.apply(PairRDDFunctions.scala:1108)
	at org.apache.spark.rdd.PairRDDFunctions$$anonfun$saveAsHadoopDataset$1$$anonfun$13$$anonfun$apply$6.apply(PairRDDFunctions.scala:1108)
	at org.apache.spark.util.Utils$.tryWithSafeFinally(Utils.scala:1206)
	at org.apache.spark.rdd.PairRDDFunctions$$anonfun$saveAsHadoopDataset$1$$anonfun$13.apply(PairRDDFunctions.scala:1116)
	at org.apache.spark.rdd.PairRDDFunctions$$anonfun$saveAsHadoopDataset$1$$anonfun$13.apply(PairRDDFunctions.scala:1095)
	at org.apache.spark.scheduler.ResultTask.runTask(ResultTask.scala:66)
	at org.apache.spark.scheduler.Task.run(Task.scala:88)
	at org.apache.spark.executor.Executor$TaskRunner.run(Executor.scala:214)
	at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1142)
	at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:617)
	at java.lang.Thread.run(Thread.java:745)

Driver stacktrace:
	at org.apache.spark.scheduler.DAGScheduler.org$apache$spark$scheduler$DAGScheduler$$failJobAndIndependentStages(DAGScheduler.scala:1280)
	at org.apache.spark.scheduler.DAGScheduler$$anonfun$abortStage$1.apply(DAGScheduler.scala:1268)
	at org.apache.spark.scheduler.DAGScheduler$$anonfun$abortStage$1.apply(DAGScheduler.scala:1267)
	at scala.collection.mutable.ResizableArray$class.foreach(ResizableArray.scala:59)
	at scala.collection.mutable.ArrayBuffer.foreach(ArrayBuffer.scala:47)
	at org.apache.spark.scheduler.DAGScheduler.abortStage(DAGScheduler.scala:1267)
	at org.apache.spark.scheduler.DAGScheduler$$anonfun$handleTaskSetFailed$1.apply(DAGScheduler.scala:697)
	at org.apache.spark.scheduler.DAGScheduler$$anonfun$handleTaskSetFailed$1.apply(DAGScheduler.scala:697)
	at scala.Option.foreach(Option.scala:236)
	at org.apache.spark.scheduler.DAGScheduler.handleTaskSetFailed(DAGScheduler.scala:697)
	at org.apache.spark.scheduler.DAGSchedulerEventProcessLoop.doOnReceive(DAGScheduler.scala:1493)
	at org.apache.spark.scheduler.DAGSchedulerEventProcessLoop.onReceive(DAGScheduler.scala:1455)
	at org.apache.spark.scheduler.DAGSchedulerEventProcessLoop.onReceive(DAGScheduler.scala:1444)
	at org.apache.spark.util.EventLoop$$anon$1.run(EventLoop.scala:48)
	at org.apache.spark.scheduler.DAGScheduler.runJob(DAGScheduler.scala:567)
	at org.apache.spark.SparkContext.runJob(SparkContext.scala:1813)
	at org.apache.spark.SparkContext.runJob(SparkContext.scala:1826)
	at org.apache.spark.SparkContext.runJob(SparkContext.scala:1903)
	at org.apache.spark.rdd.PairRDDFunctions$$anonfun$saveAsHadoopDataset$1.apply$mcV$sp(PairRDDFunctions.scala:1124)
	at org.apache.spark.rdd.PairRDDFunctions$$anonfun$saveAsHadoopDataset$1.apply(PairRDDFunctions.scala:1065)
	at org.apache.spark.rdd.PairRDDFunctions$$anonfun$saveAsHadoopDataset$1.apply(PairRDDFunctions.scala:1065)
	at org.apache.spark.rdd.RDDOperationScope$.withScope(RDDOperationScope.scala:147)
	at org.apache.spark.rdd.RDDOperationScope$.withScope(RDDOperationScope.scala:108)
	at org.apache.spark.rdd.RDD.withScope(RDD.scala:306)
	at org.apache.spark.rdd.PairRDDFunctions.saveAsHadoopDataset(PairRDDFunctions.scala:1065)
	at org.apache.spark.rdd.PairRDDFunctions$$anonfun$saveAsHadoopFile$4.apply$mcV$sp(PairRDDFunctions.scala:989)
	at org.apache.spark.rdd.PairRDDFunctions$$anonfun$saveAsHadoopFile$4.apply(PairRDDFunctions.scala:965)
	at org.apache.spark.rdd.PairRDDFunctions$$anonfun$saveAsHadoopFile$4.apply(PairRDDFunctions.scala:965)
	at org.apache.spark.rdd.RDDOperationScope$.withScope(RDDOperationScope.scala:147)
	at org.apache.spark.rdd.RDDOperationScope$.withScope(RDDOperationScope.scala:108)
	at org.apache.spark.rdd.RDD.withScope(RDD.scala:306)
	at org.apache.spark.rdd.PairRDDFunctions.saveAsHadoopFile(PairRDDFunctions.scala:965)
	at org.apache.spark.rdd.PairRDDFunctions$$anonfun$saveAsHadoopFile$1.apply$mcV$sp(PairRDDFunctions.scala:897)
	at org.apache.spark.rdd.PairRDDFunctions$$anonfun$saveAsHadoopFile$1.apply(PairRDDFunctions.scala:897)
	at org.apache.spark.rdd.PairRDDFunctions$$anonfun$saveAsHadoopFile$1.apply(PairRDDFunctions.scala:897)
	at org.apache.spark.rdd.RDDOperationScope$.withScope(RDDOperationScope.scala:147)
	at org.apache.spark.rdd.RDDOperationScope$.withScope(RDDOperationScope.scala:108)
	at org.apache.spark.rdd.RDD.withScope(RDD.scala:306)
	at org.apache.spark.rdd.PairRDDFunctions.saveAsHadoopFile(PairRDDFunctions.scala:896)
	at org.apache.spark.rdd.RDD$$anonfun$saveAsTextFile$1.apply$mcV$sp(RDD.scala:1426)
	at org.apache.spark.rdd.RDD$$anonfun$saveAsTextFile$1.apply(RDD.scala:1405)
	at org.apache.spark.rdd.RDD$$anonfun$saveAsTextFile$1.apply(RDD.scala:1405)
	at org.apache.spark.rdd.RDDOperationScope$.withScope(RDDOperationScope.scala:147)
	at org.apache.spark.rdd.RDDOperationScope$.withScope(RDDOperationScope.scala:108)
	at org.apache.spark.rdd.RDD.withScope(RDD.scala:306)
	at org.apache.spark.rdd.RDD.saveAsTextFile(RDD.scala:1405)
	at com.databricks.spark.csv.package$CsvSchemaRDD.saveAsCsvFile(package.scala:169)
	at com.databricks.spark.csv.DefaultSource.createRelation(DefaultSource.scala:165)
	at org.apache.spark.sql.execution.datasources.ResolvedDataSource$.apply(ResolvedDataSource.scala:170)
	at org.apache.spark.sql.DataFrameWriter.save(DataFrameWriter.scala:146)
	at org.apache.spark.sql.DataFrameWriter.save(DataFrameWriter.scala:137)
	at BlogApp$.main(BlogApp.scala:30)
	at BlogApp.main(BlogApp.scala)
	at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
	at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)
	at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
	at java.lang.reflect.Method.invoke(Method.java:497)
	at org.apache.spark.deploy.SparkSubmit$.org$apache$spark$deploy$SparkSubmit$$runMain(SparkSubmit.scala:672)
	at org.apache.spark.deploy.SparkSubmit$.doRunMain$1(SparkSubmit.scala:180)
	at org.apache.spark.deploy.SparkSubmit$.submit(SparkSubmit.scala:205)
	at org.apache.spark.deploy.SparkSubmit$.main(SparkSubmit.scala:120)
	at org.apache.spark.deploy.SparkSubmit.main(SparkSubmit.scala)
Caused by: scala.MatchError: [14850000,2013-11-13 00:00,SW3 4EU,9,,ORMONDE GATE,,LONDON,KENSINGTON AND CHELSEA,GREATER LONDON,9 / ORMONDE GATE / LONDON / KENSINGTON AND CHELSEA / GREATER LONDON / SW3 4EU] (of class org.apache.spark.sql.catalyst.expressions.GenericRow)
	at BlogApp$$anonfun$main$1.apply(BlogApp.scala:24)
	at BlogApp$$anonfun$main$1.apply(BlogApp.scala:24)
	at scala.collection.Iterator$$anon$11.next(Iterator.scala:328)
	at scala.collection.Iterator$$anon$11.next(Iterator.scala:328)
	at scala.collection.Iterator$$anon$11.next(Iterator.scala:328)
	at com.databricks.spark.csv.package$CsvSchemaRDD$$anonfun$5$$anon$1.next(package.scala:154)
	at com.databricks.spark.csv.package$CsvSchemaRDD$$anonfun$5$$anon$1.next(package.scala:147)
	at scala.collection.Iterator$$anon$11.next(Iterator.scala:328)
	at org.apache.spark.rdd.PairRDDFunctions$$anonfun$saveAsHadoopDataset$1$$anonfun$13$$anonfun$apply$6.apply$mcV$sp(PairRDDFunctions.scala:1109)
	at org.apache.spark.rdd.PairRDDFunctions$$anonfun$saveAsHadoopDataset$1$$anonfun$13$$anonfun$apply$6.apply(PairRDDFunctions.scala:1108)
	at org.apache.spark.rdd.PairRDDFunctions$$anonfun$saveAsHadoopDataset$1$$anonfun$13$$anonfun$apply$6.apply(PairRDDFunctions.scala:1108)
	at org.apache.spark.util.Utils$.tryWithSafeFinally(Utils.scala:1206)
	at org.apache.spark.rdd.PairRDDFunctions$$anonfun$saveAsHadoopDataset$1$$anonfun$13.apply(PairRDDFunctions.scala:1116)
	at org.apache.spark.rdd.PairRDDFunctions$$anonfun$saveAsHadoopDataset$1$$anonfun$13.apply(PairRDDFunctions.scala:1095)
	at org.apache.spark.scheduler.ResultTask.runTask(ResultTask.scala:66)
	at org.apache.spark.scheduler.Task.run(Task.scala:88)
	at org.apache.spark.executor.Executor$TaskRunner.run(Executor.scala:214)
	at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1142)
	at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:617)
	at java.lang.Thread.run(Thread.java:745)
~~~

<p>So it looks like we have something wrong with our matching code and the only place we're matching anything is the <cite>Row</cite> case class when we're mapping over <cite>rows</cite>.</p>


<p>
Although I thought price should be an integer I tweaked it to be a string just in case that was the issue:
</p>



~~~scala

case class BlogTransaction(price: Integer, date: String, postCode:String, paon:String, saon:String, street:String, locality:String, city:String, district:String, county:String)
...
case Row(price: Integer, date: String, postCode:String, paon:String, saon:String, street:String, locality:String, city:String, district:String, county:String) =>
~~~

<p>changed to:</p>



~~~scala

case class BlogTransaction(price: String, date: String, postCode:String, paon:String, saon:String, street:String, locality:String, city:String, district:String, county:String)
...
case Row(price: String, date: String, postCode:String, paon:String, saon:String, street:String, locality:String, city:String, district:String, county:String) =>
~~~

<p>
Attempt #2:
</p>



~~~bash

./spark-1.5.0-bin-hadoop2.6/bin/spark-submit --class BlogApp --master local[8] --packages com.databricks:spark-csv_2.10:1.2.0 target/scala-2.10/simple-project_2.10-1.0.jar

15/10/27 23:01:35 WARN TaskSetManager: Lost task 6.0 in stage 1.0 (TID 7, localhost): TaskKilled (killed intentionally)
Exception in thread "main" 15/10/27 23:01:35 WARN TaskSetManager: Lost task 1.0 in stage 1.0 (TID 2, localhost): TaskKilled (killed intentionally)
org.apache.spark.SparkException: Job aborted due to stage failure: Task 2 in stage 1.0 failed 1 times, most recent failure: Lost task 2.0 in stage 1.0 (TID 3, localhost): scala.MatchError: [14850000,2013-11-13 00:00,SW3 4EU,9,,ORMONDE GATE,,LONDON,KENSINGTON AND CHELSEA,GREATER LONDON,9 / ORMONDE GATE / LONDON / KENSINGTON AND CHELSEA / GREATER LONDON / SW3 4EU] (of class org.apache.spark.sql.catalyst.expressions.GenericRow)
	at BlogApp$$anonfun$main$1.apply(BlogApp.scala:24)
	at BlogApp$$anonfun$main$1.apply(BlogApp.scala:24)
	at scala.collection.Iterator$$anon$11.next(Iterator.scala:328)
	at scala.collection.Iterator$$anon$11.next(Iterator.scala:328)
	at scala.collection.Iterator$$anon$11.next(Iterator.scala:328)
	at com.databricks.spark.csv.package$CsvSchemaRDD$$anonfun$5$$anon$1.next(package.scala:154)
	at com.databricks.spark.csv.package$CsvSchemaRDD$$anonfun$5$$anon$1.next(package.scala:147)
	at scala.collection.Iterator$$anon$11.next(Iterator.scala:328)
	at org.apache.spark.rdd.PairRDDFunctions$$anonfun$saveAsHadoopDataset$1$$anonfun$13$$anonfun$apply$6.apply$mcV$sp(PairRDDFunctions.scala:1109)
	at org.apache.spark.rdd.PairRDDFunctions$$anonfun$saveAsHadoopDataset$1$$anonfun$13$$anonfun$apply$6.apply(PairRDDFunctions.scala:1108)
	at org.apache.spark.rdd.PairRDDFunctions$$anonfun$saveAsHadoopDataset$1$$anonfun$13$$anonfun$apply$6.apply(PairRDDFunctions.scala:1108)
	at org.apache.spark.util.Utils$.tryWithSafeFinally(Utils.scala:1206)
	at org.apache.spark.rdd.PairRDDFunctions$$anonfun$saveAsHadoopDataset$1$$anonfun$13.apply(PairRDDFunctions.scala:1116)
	at org.apache.spark.rdd.PairRDDFunctions$$anonfun$saveAsHadoopDataset$1$$anonfun$13.apply(PairRDDFunctions.scala:1095)
	at org.apache.spark.scheduler.ResultTask.runTask(ResultTask.scala:66)
	at org.apache.spark.scheduler.Task.run(Task.scala:88)
	at org.apache.spark.executor.Executor$TaskRunner.run(Executor.scala:214)
	at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1142)
	at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:617)
	at java.lang.Thread.run(Thread.java:745)

Driver stacktrace:
	at org.apache.spark.scheduler.DAGScheduler.org$apache$spark$scheduler$DAGScheduler$$failJobAndIndependentStages(DAGScheduler.scala:1280)
	at org.apache.spark.scheduler.DAGScheduler$$anonfun$abortStage$1.apply(DAGScheduler.scala:1268)
	at org.apache.spark.scheduler.DAGScheduler$$anonfun$abortStage$1.apply(DAGScheduler.scala:1267)
	at scala.collection.mutable.ResizableArray$class.foreach(ResizableArray.scala:59)
	at scala.collection.mutable.ArrayBuffer.foreach(ArrayBuffer.scala:47)
	at org.apache.spark.scheduler.DAGScheduler.abortStage(DAGScheduler.scala:1267)
	at org.apache.spark.scheduler.DAGScheduler$$anonfun$handleTaskSetFailed$1.apply(DAGScheduler.scala:697)
	at org.apache.spark.scheduler.DAGScheduler$$anonfun$handleTaskSetFailed$1.apply(DAGScheduler.scala:697)
	at scala.Option.foreach(Option.scala:236)
	at org.apache.spark.scheduler.DAGScheduler.handleTaskSetFailed(DAGScheduler.scala:697)
	at org.apache.spark.scheduler.DAGSchedulerEventProcessLoop.doOnReceive(DAGScheduler.scala:1493)
	at org.apache.spark.scheduler.DAGSchedulerEventProcessLoop.onReceive(DAGScheduler.scala:1455)
	at org.apache.spark.scheduler.DAGSchedulerEventProcessLoop.onReceive(DAGScheduler.scala:1444)
	at org.apache.spark.util.EventLoop$$anon$1.run(EventLoop.scala:48)
	at org.apache.spark.scheduler.DAGScheduler.runJob(DAGScheduler.scala:567)
	at org.apache.spark.SparkContext.runJob(SparkContext.scala:1813)
	at org.apache.spark.SparkContext.runJob(SparkContext.scala:1826)
	at org.apache.spark.SparkContext.runJob(SparkContext.scala:1903)
	at org.apache.spark.rdd.PairRDDFunctions$$anonfun$saveAsHadoopDataset$1.apply$mcV$sp(PairRDDFunctions.scala:1124)
	at org.apache.spark.rdd.PairRDDFunctions$$anonfun$saveAsHadoopDataset$1.apply(PairRDDFunctions.scala:1065)
	at org.apache.spark.rdd.PairRDDFunctions$$anonfun$saveAsHadoopDataset$1.apply(PairRDDFunctions.scala:1065)
	at org.apache.spark.rdd.RDDOperationScope$.withScope(RDDOperationScope.scala:147)
	at org.apache.spark.rdd.RDDOperationScope$.withScope(RDDOperationScope.scala:108)
	at org.apache.spark.rdd.RDD.withScope(RDD.scala:306)
	at org.apache.spark.rdd.PairRDDFunctions.saveAsHadoopDataset(PairRDDFunctions.scala:1065)
	at org.apache.spark.rdd.PairRDDFunctions$$anonfun$saveAsHadoopFile$4.apply$mcV$sp(PairRDDFunctions.scala:989)
	at org.apache.spark.rdd.PairRDDFunctions$$anonfun$saveAsHadoopFile$4.apply(PairRDDFunctions.scala:965)
	at org.apache.spark.rdd.PairRDDFunctions$$anonfun$saveAsHadoopFile$4.apply(PairRDDFunctions.scala:965)
	at org.apache.spark.rdd.RDDOperationScope$.withScope(RDDOperationScope.scala:147)
	at org.apache.spark.rdd.RDDOperationScope$.withScope(RDDOperationScope.scala:108)
	at org.apache.spark.rdd.RDD.withScope(RDD.scala:306)
	at org.apache.spark.rdd.PairRDDFunctions.saveAsHadoopFile(PairRDDFunctions.scala:965)
	at org.apache.spark.rdd.PairRDDFunctions$$anonfun$saveAsHadoopFile$1.apply$mcV$sp(PairRDDFunctions.scala:897)
	at org.apache.spark.rdd.PairRDDFunctions$$anonfun$saveAsHadoopFile$1.apply(PairRDDFunctions.scala:897)
	at org.apache.spark.rdd.PairRDDFunctions$$anonfun$saveAsHadoopFile$1.apply(PairRDDFunctions.scala:897)
	at org.apache.spark.rdd.RDDOperationScope$.withScope(RDDOperationScope.scala:147)
	at org.apache.spark.rdd.RDDOperationScope$.withScope(RDDOperationScope.scala:108)
	at org.apache.spark.rdd.RDD.withScope(RDD.scala:306)
	at org.apache.spark.rdd.PairRDDFunctions.saveAsHadoopFile(PairRDDFunctions.scala:896)
	at org.apache.spark.rdd.RDD$$anonfun$saveAsTextFile$1.apply$mcV$sp(RDD.scala:1426)
	at org.apache.spark.rdd.RDD$$anonfun$saveAsTextFile$1.apply(RDD.scala:1405)
	at org.apache.spark.rdd.RDD$$anonfun$saveAsTextFile$1.apply(RDD.scala:1405)
	at org.apache.spark.rdd.RDDOperationScope$.withScope(RDDOperationScope.scala:147)
	at org.apache.spark.rdd.RDDOperationScope$.withScope(RDDOperationScope.scala:108)
	at org.apache.spark.rdd.RDD.withScope(RDD.scala:306)
	at org.apache.spark.rdd.RDD.saveAsTextFile(RDD.scala:1405)
	at com.databricks.spark.csv.package$CsvSchemaRDD.saveAsCsvFile(package.scala:169)
	at com.databricks.spark.csv.DefaultSource.createRelation(DefaultSource.scala:165)
	at org.apache.spark.sql.execution.datasources.ResolvedDataSource$.apply(ResolvedDataSource.scala:170)
	at org.apache.spark.sql.DataFrameWriter.save(DataFrameWriter.scala:146)
	at org.apache.spark.sql.DataFrameWriter.save(DataFrameWriter.scala:137)
	at BlogApp$.main(BlogApp.scala:30)
	at BlogApp.main(BlogApp.scala)
	at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
	at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)
	at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
	at java.lang.reflect.Method.invoke(Method.java:497)
	at org.apache.spark.deploy.SparkSubmit$.org$apache$spark$deploy$SparkSubmit$$runMain(SparkSubmit.scala:672)
	at org.apache.spark.deploy.SparkSubmit$.doRunMain$1(SparkSubmit.scala:180)
	at org.apache.spark.deploy.SparkSubmit$.submit(SparkSubmit.scala:205)
	at org.apache.spark.deploy.SparkSubmit$.main(SparkSubmit.scala:120)
	at org.apache.spark.deploy.SparkSubmit.main(SparkSubmit.scala)
Caused by: scala.MatchError: [14850000,2013-11-13 00:00,SW3 4EU,9,,ORMONDE GATE,,LONDON,KENSINGTON AND CHELSEA,GREATER LONDON,9 / ORMONDE GATE / LONDON / KENSINGTON AND CHELSEA / GREATER LONDON / SW3 4EU] (of class org.apache.spark.sql.catalyst.expressions.GenericRow)
	at BlogApp$$anonfun$main$1.apply(BlogApp.scala:24)
	at BlogApp$$anonfun$main$1.apply(BlogApp.scala:24)
	at scala.collection.Iterator$$anon$11.next(Iterator.scala:328)
	at scala.collection.Iterator$$anon$11.next(Iterator.scala:328)
	at scala.collection.Iterator$$anon$11.next(Iterator.scala:328)
	at com.databricks.spark.csv.package$CsvSchemaRDD$$anonfun$5$$anon$1.next(package.scala:154)
	at com.databricks.spark.csv.package$CsvSchemaRDD$$anonfun$5$$anon$1.next(package.scala:147)
	at scala.collection.Iterator$$anon$11.next(Iterator.scala:328)
	at org.apache.spark.rdd.PairRDDFunctions$$anonfun$saveAsHadoopDataset$1$$anonfun$13$$anonfun$apply$6.apply$mcV$sp(PairRDDFunctions.scala:1109)
	at org.apache.spark.rdd.PairRDDFunctions$$anonfun$saveAsHadoopDataset$1$$anonfun$13$$anonfun$apply$6.apply(PairRDDFunctions.scala:1108)
	at org.apache.spark.rdd.PairRDDFunctions$$anonfun$saveAsHadoopDataset$1$$anonfun$13$$anonfun$apply$6.apply(PairRDDFunctions.scala:1108)
	at org.apache.spark.util.Utils$.tryWithSafeFinally(Utils.scala:1206)
	at org.apache.spark.rdd.PairRDDFunctions$$anonfun$saveAsHadoopDataset$1$$anonfun$13.apply(PairRDDFunctions.scala:1116)
	at org.apache.spark.rdd.PairRDDFunctions$$anonfun$saveAsHadoopDataset$1$$anonfun$13.apply(PairRDDFunctions.scala:1095)
	at org.apache.spark.scheduler.ResultTask.runTask(ResultTask.scala:66)
	at org.apache.spark.scheduler.Task.run(Task.scala:88)
	at org.apache.spark.executor.Executor$TaskRunner.run(Executor.scala:214)
	at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1142)
	at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:617)
	at java.lang.Thread.run(Thread.java:745)
~~~

<p>
Hmmm....no improvement. At this point I realised I'd accidentally missed off the <cite>fullAddress</cite> argument from the case statement so I added that in:
</p>



~~~scala

case class BlogTransaction(price: String, date: String, postCode:String, paon:String, saon:String, street:String, locality:String, city:String, district:String, county:String)
...
case Row(price: String, date: String, postCode:String, paon:String, saon:String, street:String, locality:String, city:String, district:String, county:String) =>
~~~

<p>changed to:</p>



~~~scala

case class BlogTransaction(price: String, date: String, postCode:String, paon:String, saon:String, street:String, locality:String, city:String, district:String, county:String, fullAddress:String)
...
case Row(price: String, date: String, postCode:String, paon:String, saon:String, street:String, locality:String, city:String, district:String, county:String, fullAddress:String) =>
~~~

<p>Attempt #3:</p>



~~~bash

./spark-1.5.0-bin-hadoop2.6/bin/spark-submit --class BlogApp --master local[8] --packages com.databricks:spark-csv_2.10:1.2.0 target/scala-2.10/simple-project_2.10-1.0.jar
...
15/10/27 23:06:03 INFO DAGScheduler: Job 1 finished: saveAsTextFile at package.scala:169, took 39.665661 s
~~~

<p>Hoorah, it took a bit of guess work but finally it's finally working!</p>


<p>For completeness, here's the final version of the Spark job:</p>



~~~scala

import org.apache.spark.sql.{SQLContext, _}
import org.apache.spark.{SparkConf, SparkContext}

case class BlogTransaction(price: Integer, date: String, postCode:String, paon:String, saon:String, street:String, locality:String, city:String, district:String, county:String, fullAddress:String)

object BlogApp {
  def main(args: Array[String]) {
    val conf = new SparkConf().setAppName("Simple Application")

    val sc = new SparkContext(conf)
    val sqlContext = new SQLContext(sc)
    import sqlContext.implicits._

    sqlContext.read.format("com.databricks.spark.csv").load("/Users/markneedham/projects/land-registry/pp-complete.csv").registerTempTable("transactions")

    val rows = sqlContext.sql("select C1,C2,C3,C7,C8,C9,C10,C11,C12,C13 from transactions where transactions.C3 = 'SW3 4EU'").map(x =>
      Row.fromSeq(x.toSeq ++ Array(Array(x.get(4), x.get(3), x.get(5), x.get(6), x.get(7), x.get(8), x.get(9), x.get(2))
        .map(x => x.toString)
        .filter(x => !x.isEmpty)
        .distinct
        .mkString(" / "))))

    val path: String = "/tmp/tx-" + System.currentTimeMillis() + ".csv"
    rows.map {
      case Row(price: Integer, date: String, postCode:String, paon:String, saon:String, street:String, locality:String, city:String, district:String, county:String, fullAddress:String) =>
        BlogTransaction(price, date, postCode, paon, saon, street, locality, city, district, county, fullAddress) }
      .toDF()
      .write
      .format("com.databricks.spark.csv")
      .save(path)
  }
}
~~~
