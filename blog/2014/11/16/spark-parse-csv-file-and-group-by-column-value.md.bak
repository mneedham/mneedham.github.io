+++
draft = false
date="2014-11-16 22:53:49"
title="Spark: Parse CSV file and group by column value"
tag=['spark-2']
category=['Spark']
+++

<p>I've found myself working with large CSV files quite frequently and realising that my existing toolset didn't let me explore them quickly I thought I'd spend a bit of time looking at <a href="http://spark.apache.org/">Spark</a> to see if it could help.</p>


<p>I'm working with a <a href="https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-present/ijzp-q8t2">crime data set released by the City of Chicago</a>: it's 1GB in size and contains details of 4 million crimes:</p>



~~~bash

$ ls -alh ~/Downloads/Crimes_-_2001_to_present.csv
-rw-r--r--@ 1 markneedham  staff   1.0G 16 Nov 12:14 /Users/markneedham/Downloads/Crimes_-_2001_to_present.csv

$ wc -l ~/Downloads/Crimes_-_2001_to_present.csv
 4193441 /Users/markneedham/Downloads/Crimes_-_2001_to_present.csv
~~~

<p>We can get a rough idea of the contents of the file by looking at the first row along with the header:</p>



~~~bash

$ head -n 2 ~/Downloads/Crimes_-_2001_to_present.csv
ID,Case Number,Date,Block,IUCR,Primary Type,Description,Location Description,Arrest,Domestic,Beat,District,Ward,Community Area,FBI Code,X Coordinate,Y Coordinate,Year,Updated On,Latitude,Longitude,Location
9464711,HX114160,01/14/2014 05:00:00 AM,028XX E 80TH ST,0560,ASSAULT,SIMPLE,APARTMENT,false,true,0422,004,7,46,08A,1196652,1852516,2014,01/20/2014 12:40:05 AM,41.75017626412204,-87.55494559131228,"(41.75017626412204, -87.55494559131228)"
~~~

<p>I wanted to do a count of the 'Primary Type' column to see how many of each crime we have. Using just Unix command line tools this is how we'd do that:</p>



~~~bash

$ time tail +2 ~/Downloads/Crimes_-_2001_to_present.csv | cut -d, -f6  | sort | uniq -c | sort -rn
859197 THEFT
757530 BATTERY
489528 NARCOTICS
488209 CRIMINAL DAMAGE
257310 BURGLARY
253964 OTHER OFFENSE
247386 ASSAULT
197404 MOTOR VEHICLE THEFT
157706 ROBBERY
137538 DECEPTIVE PRACTICE
124974 CRIMINAL TRESPASS
47245 PROSTITUTION
40361 WEAPONS VIOLATION
31585 PUBLIC PEACE VIOLATION
26524 OFFENSE INVOLVING CHILDREN
14788 CRIM SEXUAL ASSAULT
14283 SEX OFFENSE
10632 GAMBLING
8847 LIQUOR LAW VIOLATION
6443 ARSON
5178 INTERFERE WITH PUBLIC OFFICER
4846 HOMICIDE
3585 KIDNAPPING
3147 INTERFERENCE WITH PUBLIC OFFICER
2471 INTIMIDATION
1985 STALKING
 355 OFFENSES INVOLVING CHILDREN
 219 OBSCENITY
  86 PUBLIC INDECENCY
  80 OTHER NARCOTIC VIOLATION
  12 RITUALISM
  12 NON-CRIMINAL
   6 OTHER OFFENSE
   2 NON-CRIMINAL (SUBJECT SPECIFIED)
   2 NON - CRIMINAL

real	2m37.495s
user	3m0.337s
sys	0m1.471s
~~~

<p>
This isn't too bad but it seems like the type of calculation that Spark is made for so I had a look at how I could go about doing that. To start with I created an SBT project with the following build file:
</p>



~~~sbt

name := "playground"

version := "1.0"

scalaVersion := "2.10.4"

libraryDependencies += "org.apache.spark" %% "spark-core" % "1.1.0"

libraryDependencies += "net.sf.opencsv" % "opencsv" % "2.3"

ideaExcludeFolders += ".idea"

ideaExcludeFolders += ".idea_modules"
~~~

<p>I <a href="http://spark.apache.org/downloads.html">downloaded Spark</a> and after unpacking it launched the Spark shell:</p>



~~~bash

$ pwd
/Users/markneedham/projects/spark-play/spark-1.1.0/spark-1.1.0-bin-hadoop1

$ ./bin/spark-shell
...
Welcome to
      ____              __
     / __/__  ___ _____/ /__
    _\ \/ _ \/ _ `/ __/  '_/
   /___/ .__/\_,_/_/ /_/\_\   version 1.1.0
      /_/

Using Scala version 2.10.4 (Java HotSpot(TM) 64-Bit Server VM, Java 1.7.0_51)
...
Spark context available as sc.

scala>
~~~

<p>I first import some classes I'm going to need:</p>



~~~scala

scala> import au.com.bytecode.opencsv.CSVParser
import au.com.bytecode.opencsv.CSVParser

scala> import org.apache.spark.rdd.RDD
import org.apache.spark.rdd.RDD
~~~

<p>Now, following the <a href="http://spark.apache.org/docs/latest/quick-start.html">quick start example</a>, we'll create a Resilient Distributed Dataset (RDD) from our Crime CSV file:</p>



~~~scala

scala> val crimeFile = "/Users/markneedham/Downloads/Crimes_-_2001_to_present.csv"
crimeFile: String = /Users/markneedham/Downloads/Crimes_-_2001_to_present.csv

scala> val crimeData = sc.textFile(crimeFile).cache()
14/11/16 22:31:16 INFO MemoryStore: ensureFreeSpace(32768) called with curMem=0, maxMem=278302556
14/11/16 22:31:16 INFO MemoryStore: Block broadcast_0 stored as values in memory (estimated size 32.0 KB, free 265.4 MB)
crimeData: org.apache.spark.rdd.RDD[String] = /Users/markneedham/Downloads/Crimes_-_2001_to_present.csv MappedRDD[1] at textFile at <console>:17
~~~

<p>Our next step is to process each line of the file using our CSV Parser. A simple way to do this would be to <a href="http://bzhangusc.wordpress.com/2014/06/18/csv-parser/">create a new CSVParser for each line</a>:</p>



~~~scala

scala> crimeData.map(line => {
         val parser = new CSVParser(',')
         parser.parseLine(line).mkString(",")
       }).take(5).foreach(println)
14/11/16 22:35:49 INFO SparkContext: Starting job: take at <console>:23
...
4/11/16 22:35:49 INFO SparkContext: Job finished: take at <console>:23, took 0.013904 s
ID,Case Number,Date,Block,IUCR,Primary Type,Description,Location Description,Arrest,Domestic,Beat,District,Ward,Community Area,FBI Code,X Coordinate,Y Coordinate,Year,Updated On,Latitude,Longitude,Location
9464711,HX114160,01/14/2014 05:00:00 AM,028XX E 80TH ST,0560,ASSAULT,SIMPLE,APARTMENT,false,true,0422,004,7,46,08A,1196652,1852516,2014,01/20/2014 12:40:05 AM,41.75017626412204,-87.55494559131228,(41.75017626412204, -87.55494559131228)
9460704,HX113741,01/14/2014 04:55:00 AM,091XX S JEFFERY AVE,031A,ROBBERY,ARMED: HANDGUN,SIDEWALK,false,false,0413,004,8,48,03,1191060,1844959,2014,01/18/2014 12:39:56 AM,41.729576153145636,-87.57568059471686,(41.729576153145636, -87.57568059471686)
9460339,HX113740,01/14/2014 04:44:00 AM,040XX W MAYPOLE AVE,1310,CRIMINAL DAMAGE,TO PROPERTY,RESIDENCE,false,true,1114,011,28,26,14,1149075,1901099,2014,01/16/2014 12:40:00 AM,41.884543798701515,-87.72803579358926,(41.884543798701515, -87.72803579358926)
9461467,HX114463,01/14/2014 04:43:00 AM,059XX S CICERO AVE,0820,THEFT,$500 AND UNDER,PARKING LOT/GARAGE(NON.RESID.),false,false,0813,008,13,64,06,1145661,1865031,2014,01/16/2014 12:40:00 AM,41.785633535413176,-87.74148516669783,(41.785633535413176, -87.74148516669783)
~~~

<p>That works but it's a bit wasteful to create a new CSVParser each time so instead let's just create one for each partition that Spark splits our file up into:</p>



~~~scala

scala> crimeData.mapPartitions(lines => {
         val parser = new CSVParser(',')
         lines.map(line => {
           parser.parseLine(line).mkString(",")
         })
       }).take(5).foreach(println)
14/11/16 22:38:44 INFO SparkContext: Starting job: take at <console>:25
...
14/11/16 22:38:44 INFO SparkContext: Job finished: take at <console>:25, took 0.015216 s
ID,Case Number,Date,Block,IUCR,Primary Type,Description,Location Description,Arrest,Domestic,Beat,District,Ward,Community Area,FBI Code,X Coordinate,Y Coordinate,Year,Updated On,Latitude,Longitude,Location
9464711,HX114160,01/14/2014 05:00:00 AM,028XX E 80TH ST,0560,ASSAULT,SIMPLE,APARTMENT,false,true,0422,004,7,46,08A,1196652,1852516,2014,01/20/2014 12:40:05 AM,41.75017626412204,-87.55494559131228,(41.75017626412204, -87.55494559131228)
9460704,HX113741,01/14/2014 04:55:00 AM,091XX S JEFFERY AVE,031A,ROBBERY,ARMED: HANDGUN,SIDEWALK,false,false,0413,004,8,48,03,1191060,1844959,2014,01/18/2014 12:39:56 AM,41.729576153145636,-87.57568059471686,(41.729576153145636, -87.57568059471686)
9460339,HX113740,01/14/2014 04:44:00 AM,040XX W MAYPOLE AVE,1310,CRIMINAL DAMAGE,TO PROPERTY,RESIDENCE,false,true,1114,011,28,26,14,1149075,1901099,2014,01/16/2014 12:40:00 AM,41.884543798701515,-87.72803579358926,(41.884543798701515, -87.72803579358926)
9461467,HX114463,01/14/2014 04:43:00 AM,059XX S CICERO AVE,0820,THEFT,$500 AND UNDER,PARKING LOT/GARAGE(NON.RESID.),false,false,0813,008,13,64,06,1145661,1865031,2014,01/16/2014 12:40:00 AM,41.785633535413176,-87.74148516669783,(41.785633535413176, -87.74148516669783)
~~~

<p>You'll notice that we've still got the header being printed which isn't ideal - let's get rid of it!</p?

<p>I expected there to be a 'drop' function which would allow me to do that but in fact there isn't. Instead we can <a href="http://mail-archives.apache.org/mod_mbox/spark-user/201404.mbox/%3CCAEYYnxYuEaie518ODdn-fR7VvD39d71=CgB_Dxw_4COVXgmYYQ@mail.gmail.com%3E">make use of our knowledge that the first partition will contain the first line and strip it out</a> that way:</p>



~~~scala

scala> def dropHeader(data: RDD[String]): RDD[String] = {
         data.mapPartitionsWithIndex((idx, lines) => {
           if (idx == 0) {
             lines.drop(1)
           }
           lines
         })
       }
dropHeader: (data: org.apache.spark.rdd.RDD[String])org.apache.spark.rdd.RDD[String]
~~~

<p>Now let's grab the first 5 lines again and print them out:</p>



~~~scala

scala> val withoutHeader: RDD[String] = dropHeader(crimeData)
withoutHeader: org.apache.spark.rdd.RDD[String] = MapPartitionsRDD[7] at mapPartitionsWithIndex at <console>:14

scala> withoutHeader.mapPartitions(lines => {
         val parser = new CSVParser(',')
         lines.map(line => {
           parser.parseLine(line).mkString(",")
         })
       }).take(5).foreach(println)
14/11/16 22:43:27 INFO SparkContext: Starting job: take at <console>:29
...
14/11/16 22:43:27 INFO SparkContext: Job finished: take at <console>:29, took 0.018557 s
9464711,HX114160,01/14/2014 05:00:00 AM,028XX E 80TH ST,0560,ASSAULT,SIMPLE,APARTMENT,false,true,0422,004,7,46,08A,1196652,1852516,2014,01/20/2014 12:40:05 AM,41.75017626412204,-87.55494559131228,(41.75017626412204, -87.55494559131228)
9460704,HX113741,01/14/2014 04:55:00 AM,091XX S JEFFERY AVE,031A,ROBBERY,ARMED: HANDGUN,SIDEWALK,false,false,0413,004,8,48,03,1191060,1844959,2014,01/18/2014 12:39:56 AM,41.729576153145636,-87.57568059471686,(41.729576153145636, -87.57568059471686)
9460339,HX113740,01/14/2014 04:44:00 AM,040XX W MAYPOLE AVE,1310,CRIMINAL DAMAGE,TO PROPERTY,RESIDENCE,false,true,1114,011,28,26,14,1149075,1901099,2014,01/16/2014 12:40:00 AM,41.884543798701515,-87.72803579358926,(41.884543798701515, -87.72803579358926)
9461467,HX114463,01/14/2014 04:43:00 AM,059XX S CICERO AVE,0820,THEFT,$500 AND UNDER,PARKING LOT/GARAGE(NON.RESID.),false,false,0813,008,13,64,06,1145661,1865031,2014,01/16/2014 12:40:00 AM,41.785633535413176,-87.74148516669783,(41.785633535413176, -87.74148516669783)
9460355,HX113738,01/14/2014 04:21:00 AM,070XX S PEORIA ST,0820,THEFT,$500 AND UNDER,STREET,true,false,0733,007,17,68,06,1171480,1858195,2014,01/16/2014 12:40:00 AM,41.766348042591375,-87.64702037047671,(41.766348042591375, -87.64702037047671)
~~~

<p>We're finally in good shape to extract the values from the 'Primary Type' column and count how many times each of those appears in our data set:</p>



~~~scala

scala> withoutHeader.mapPartitions(lines => {
         val parser=new CSVParser(',')
         lines.map(line => {
           val columns = parser.parseLine(line)
           Array(columns(5)).mkString(",")
         })
       }).countByValue().toList.sortBy(-_._2).foreach(println)
14/11/16 22:45:20 INFO SparkContext: Starting job: countByValue at <console>:30
14/11/16 22:45:20 INFO DAGScheduler: Got job 7 (countByValue at <console>:30) with 32 output partitions (allowLocal=false)
...
14/11/16 22:45:30 INFO SparkContext: Job finished: countByValue at <console>:30, took 9.796565 s
(THEFT,859197)
(BATTERY,757530)
(NARCOTICS,489528)
(CRIMINAL DAMAGE,488209)
(BURGLARY,257310)
(OTHER OFFENSE,253964)
(ASSAULT,247386)
(MOTOR VEHICLE THEFT,197404)
(ROBBERY,157706)
(DECEPTIVE PRACTICE,137538)
(CRIMINAL TRESPASS,124974)
(PROSTITUTION,47245)
(WEAPONS VIOLATION,40361)
(PUBLIC PEACE VIOLATION,31585)
(OFFENSE INVOLVING CHILDREN,26524)
(CRIM SEXUAL ASSAULT,14788)
(SEX OFFENSE,14283)
(GAMBLING,10632)
(LIQUOR LAW VIOLATION,8847)
(ARSON,6443)
(INTERFERE WITH PUBLIC OFFICER,5178)
(HOMICIDE,4846)
(KIDNAPPING,3585)
(INTERFERENCE WITH PUBLIC OFFICER,3147)
(INTIMIDATION,2471)
(STALKING,1985)
(OFFENSES INVOLVING CHILDREN,355)
(OBSCENITY,219)
(PUBLIC INDECENCY,86)
(OTHER NARCOTIC VIOLATION,80)
(NON-CRIMINAL,12)
(RITUALISM,12)
(OTHER OFFENSE ,6)
(NON-CRIMINAL (SUBJECT SPECIFIED),2)
(NON - CRIMINAL,2)
~~~

<p>We get the same results as with the Unix commands except it took less than 10 seconds to calculate which is pretty cool!</p>

