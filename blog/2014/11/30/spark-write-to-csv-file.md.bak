+++
draft = false
date="2014-11-30 07:40:00"
title="Spark: Write to CSV file"
tag=['spark-2']
category=['Spark']
+++

<p>
A couple of weeks ago I wrote how I'd been <a href="http://www.markhneedham.com/blog/2014/11/16/spark-parse-csv-file-and-group-by-column-value/">using Spark to explore a City of Chicago Crime data set</a> and having worked out how many of each crime had been committed I wanted to write that to a CSV file.
</p>


<p>
Spark provides a <cite>saveAsTextFile</cite> function which allows us to save RDD's so I refactored my code into the following format to allow me to use that:
</p>



~~~scala

import au.com.bytecode.opencsv.CSVParser
import org.apache.spark.rdd.RDD
import org.apache.spark.SparkContext._

def dropHeader(data: RDD[String]): RDD[String] = {
  data.mapPartitionsWithIndex((idx, lines) => {
    if (idx == 0) {
      lines.drop(1)
    }
    lines
  })
}

// https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-present/ijzp-q8t2
val crimeFile = "/Users/markneedham/Downloads/Crimes_-_2001_to_present.csv"

val crimeData = sc.textFile(crimeFile).cache()
val withoutHeader: RDD[String] = dropHeader(crimeData)

val file = "/tmp/primaryTypes.csv"
FileUtil.fullyDelete(new File(file))

val partitions: RDD[(String, Int)] = withoutHeader.mapPartitions(lines => {
  val parser = new CSVParser(',')
  lines.map(line => {
    val columns = parser.parseLine(line)
    (columns(5), 1)
  })
})

val counts = partitions.
  reduceByKey {case (x,y) => x + y}.
  sortBy {case (key, value) => -value}.
  map { case (key, value) => Array(key, value).mkString(",") }

counts.saveAsTextFile(file)
~~~

<p>If we run that code from the Spark shell we end up with a folder called <cite>/tmp/primaryTypes.csv</cite> containing multiple part files:</p>



~~~bash

$ ls -lah /tmp/primaryTypes.csv/
total 496
drwxr-xr-x  66 markneedham  wheel   2.2K 30 Nov 07:17 .
drwxrwxrwt  80 root         wheel   2.7K 30 Nov 07:16 ..
-rw-r--r--   1 markneedham  wheel     8B 30 Nov 07:16 ._SUCCESS.crc
-rw-r--r--   1 markneedham  wheel    12B 30 Nov 07:16 .part-00000.crc
-rw-r--r--   1 markneedham  wheel    12B 30 Nov 07:16 .part-00001.crc
-rw-r--r--   1 markneedham  wheel    12B 30 Nov 07:16 .part-00002.crc
-rw-r--r--   1 markneedham  wheel    12B 30 Nov 07:16 .part-00003.crc
...
-rwxrwxrwx   1 markneedham  wheel     0B 30 Nov 07:16 _SUCCESS
-rwxrwxrwx   1 markneedham  wheel    28B 30 Nov 07:16 part-00000
-rwxrwxrwx   1 markneedham  wheel    17B 30 Nov 07:16 part-00001
-rwxrwxrwx   1 markneedham  wheel    23B 30 Nov 07:16 part-00002
-rwxrwxrwx   1 markneedham  wheel    16B 30 Nov 07:16 part-00003
...
~~~

<p>If we look at some of those part files we can see that it's written the crime types and counts as expected:</p>



~~~bash

$ cat /tmp/primaryTypes.csv/part-00000
THEFT,859197
BATTERY,757530

$ cat /tmp/primaryTypes.csv/part-00003
BURGLARY,257310
~~~

<p>This is fine if we're going to <a href="http://stackoverflow.com/questions/23527941/how-to-write-to-csv-in-spark">pass those CSV files into another Hadoop based job</a> but I actually want a single CSV file so it's not quite what I want.</p>


<p>One way to achieve this is to force everything to be calculated on one partition which will mean we only get one part file generated:</p>



~~~scala

val counts = partitions.repartition(1).
  reduceByKey {case (x,y) => x + y}.
  sortBy {case (key, value) => -value}.
  map { case (key, value) => Array(key, value).mkString(",") }


counts.saveAsTextFile(file)
~~~

<p>part-00000 now looks like this:</p>



~~~bash

$ cat !$
cat /tmp/primaryTypes.csv/part-00000
THEFT,859197
BATTERY,757530
NARCOTICS,489528
CRIMINAL DAMAGE,488209
BURGLARY,257310
OTHER OFFENSE,253964
ASSAULT,247386
MOTOR VEHICLE THEFT,197404
ROBBERY,157706
DECEPTIVE PRACTICE,137538
CRIMINAL TRESPASS,124974
PROSTITUTION,47245
WEAPONS VIOLATION,40361
PUBLIC PEACE VIOLATION,31585
OFFENSE INVOLVING CHILDREN,26524
CRIM SEXUAL ASSAULT,14788
SEX OFFENSE,14283
GAMBLING,10632
LIQUOR LAW VIOLATION,8847
ARSON,6443
INTERFERE WITH PUBLIC OFFICER,5178
HOMICIDE,4846
KIDNAPPING,3585
INTERFERENCE WITH PUBLIC OFFICER,3147
INTIMIDATION,2471
STALKING,1985
OFFENSES INVOLVING CHILDREN,355
OBSCENITY,219
PUBLIC INDECENCY,86
OTHER NARCOTIC VIOLATION,80
NON-CRIMINAL,12
RITUALISM,12
OTHER OFFENSE ,6
NON - CRIMINAL,2
NON-CRIMINAL (SUBJECT SPECIFIED),2
~~~

<p>This works but it's quite a bit slower than when we were doing the aggregation across partitions so it's not ideal.</p>


<p>Instead, what we can do is make use of one of <a href="http://mail-archives.apache.org/mod_mbox/spark-user/201310.mbox/%3C5271F0B6.7000701@icsi.berkeley.edu%3E">Hadoop's merge functions</a> which squashes part files together into a single file.</p>


<p>First we import Hadoop into our SBT file:</p>



~~~text

libraryDependencies += "org.apache.hadoop" % "hadoop-hdfs" % "2.5.2"
~~~

<p>Now let's bring our merge function into the Spark shell:</p>



~~~scala

import org.apache.hadoop.conf.Configuration
import org.apache.hadoop.fs._

def merge(srcPath: String, dstPath: String): Unit =  {
  val hadoopConfig = new Configuration()
  val hdfs = FileSystem.get(hadoopConfig)
  FileUtil.copyMerge(hdfs, new Path(srcPath), hdfs, new Path(dstPath), false, hadoopConfig, null)
}
~~~

<p>And now let's make use of it:</p>



~~~scala

val file = "/tmp/primaryTypes.csv"
FileUtil.fullyDelete(new File(file))

val destinationFile= "/tmp/singlePrimaryTypes.csv"
FileUtil.fullyDelete(new File(destinationFile))

val counts = partitions.
reduceByKey {case (x,y) => x + y}.
sortBy {case (key, value) => -value}.
map { case (key, value) => Array(key, value).mkString(",") }

counts.saveAsTextFile(file)

merge(file, destinationFile)
~~~

<p>And now we've got the best of both worlds:</p>



~~~bash

$ cat /tmp/singlePrimaryTypes.csv
THEFT,859197
BATTERY,757530
NARCOTICS,489528
CRIMINAL DAMAGE,488209
BURGLARY,257310
OTHER OFFENSE,253964
ASSAULT,247386
MOTOR VEHICLE THEFT,197404
ROBBERY,157706
DECEPTIVE PRACTICE,137538
CRIMINAL TRESPASS,124974
PROSTITUTION,47245
WEAPONS VIOLATION,40361
PUBLIC PEACE VIOLATION,31585
OFFENSE INVOLVING CHILDREN,26524
CRIM SEXUAL ASSAULT,14788
SEX OFFENSE,14283
GAMBLING,10632
LIQUOR LAW VIOLATION,8847
ARSON,6443
INTERFERE WITH PUBLIC OFFICER,5178
HOMICIDE,4846
KIDNAPPING,3585
INTERFERENCE WITH PUBLIC OFFICER,3147
INTIMIDATION,2471
STALKING,1985
OFFENSES INVOLVING CHILDREN,355
OBSCENITY,219
PUBLIC INDECENCY,86
OTHER NARCOTIC VIOLATION,80
RITUALISM,12
NON-CRIMINAL,12
OTHER OFFENSE ,6
NON - CRIMINAL,2
NON-CRIMINAL (SUBJECT SPECIFIED),2
~~~

<p>The full code is available as a <a href="https://gist.github.com/mneedham/2fa4752749c8aba7f6b3">gist</a> if you want to play around with it.</p>

