+++
draft = false
date="2015-07-21 06:11:25"
title="Neo4j 2.2.3: neo4j-import - Encoder StringEncoder[2] returned an illegal encoded value 0"
tag=['neo4j']
category=['neo4j']
+++

<p>
I've been playing around with the Chicago crime data set again while preparing for a Neo4j webinar next week and while running the <a href="http://neo4j.com/docs/stable/import-tool.html">import tool</a> ran into the following exception:
</p>



~~~bash

Importing the contents of these files into tmp/crimes.db:
Nodes:
  /Users/markneedham/projects/neo4j-spark-chicago/tmp/crimes.csv

  /Users/markneedham/projects/neo4j-spark-chicago/tmp/beats.csv

  /Users/markneedham/projects/neo4j-spark-chicago/tmp/primaryTypes.csv

  /Users/markneedham/projects/neo4j-spark-chicago/tmp/locations.csv
Relationships:
  /Users/markneedham/projects/neo4j-spark-chicago/tmp/crimesBeats.csv

  /Users/markneedham/projects/neo4j-spark-chicago/tmp/crimesPrimaryTypes.csv

  /Users/markneedham/projects/neo4j-spark-chicago/tmp/crimesLocationsCleaned.csv

Available memory:
  Free machine memory: 263.17 MB
  Max heap memory : 3.56 GB

Nodes
[*>:17.41 MB/s-------------------------|PROPERTIES(3)=|NODE:3|LABEL SCAN----|v:36.30 MB/s(2)===]  3MImport error: Panic called, so exiting
java.lang.RuntimeException: Panic called, so exiting
	at org.neo4j.unsafe.impl.batchimport.staging.AbstractStep.assertHealthy(AbstractStep.java:200)
	at org.neo4j.unsafe.impl.batchimport.staging.AbstractStep.await(AbstractStep.java:191)
	at org.neo4j.unsafe.impl.batchimport.staging.ProcessorStep.receive(ProcessorStep.java:98)
	at org.neo4j.unsafe.impl.batchimport.staging.ProcessorStep.sendDownstream(ProcessorStep.java:224)
	at org.neo4j.unsafe.impl.batchimport.staging.ProcessorStep.access$400(ProcessorStep.java:42)
	at org.neo4j.unsafe.impl.batchimport.staging.ProcessorStep$Sender.send(ProcessorStep.java:250)
	at org.neo4j.unsafe.impl.batchimport.LabelScanStorePopulationStep.process(LabelScanStorePopulationStep.java:60)
	at org.neo4j.unsafe.impl.batchimport.LabelScanStorePopulationStep.process(LabelScanStorePopulationStep.java:37)
	at org.neo4j.unsafe.impl.batchimport.staging.ProcessorStep$4.run(ProcessorStep.java:120)
	at org.neo4j.unsafe.impl.batchimport.staging.ProcessorStep$4.run(ProcessorStep.java:102)
	at org.neo4j.unsafe.impl.batchimport.executor.DynamicTaskExecutor$Processor.run(DynamicTaskExecutor.java:237)
Caused by: java.lang.IllegalStateException: Encoder StringEncoder[2] returned an illegal encoded value 0
	at org.neo4j.unsafe.impl.batchimport.cache.idmapping.string.EncodingIdMapper.encode(EncodingIdMapper.java:229)
	at org.neo4j.unsafe.impl.batchimport.cache.idmapping.string.EncodingIdMapper.put(EncodingIdMapper.java:208)
	at org.neo4j.unsafe.impl.batchimport.NodeEncoderStep.process(NodeEncoderStep.java:77)
	at org.neo4j.unsafe.impl.batchimport.NodeEncoderStep.process(NodeEncoderStep.java:43)
	... 3 more
~~~

<p>
I narrowed the problem down to a specific file and from tracing the code learned that this exception happens when we've ended up with a node that doesn't have an id.
</p>


<p>
I guessed that this might be due to there being an empty column somewhere in my CSV file so I did a bit of grepping:
</p>



~~~bash

$ grep -rn  "\"\"" tmp/locations.csv
tmp/locations.csv:11:"",Location
~~~

<p>
We can now narrow down the import to just the one line and see if we still get the exception:
</p>



~~~bash

$ cat foo.csv
id:ID(Location),:LABEL
"",Location

$ ./neo4j-community-2.2.3/bin/neo4j-import --into tmp/foo --nodes foo.csv
Importing the contents of these files into tmp/foo:
Nodes:
  /Users/markneedham/projects/neo4j-spark-chicago/foo.csv

Available memory:
  Free machine memory: 2.22 GB
  Max heap memory : 3.56 GB

Nodes
Import error: Encoder StringEncoder[2] returned an illegal encoded value 0
~~~

<p>
Yep, same error. Now we can clean up our CSV file and try again:
</p>



~~~bash

$ grep -v  "\"\"" foo.csv > fooCleaned.csv

# I put in a few real records so we can see them import
$ cat fooCleaned.csv
id:ID(Location),:LABEL
"RAILROAD PROPERTY",Location
"NEWSSTAND",Location
"SCHOOL, PRIVATE, BUILDING",Location

$ ./neo4j-community-2.2.3/bin/neo4j-import --into tmp/foo --nodes fooCleaned.csv
Importing the contents of these files into tmp/foo:
Nodes:
  /Users/markneedham/projects/neo4j-spark-chicago/fooCleaned.csv

Available memory:
  Free machine memory: 1.23 GB
  Max heap memory : 3.56 GB

Nodes
[*>:??-------------------------------------------------|PROPE|NODE:7.63 MB-----------------|LA] 10k
Done in 110ms
Prepare node index
[*DETECT:7.63 MB-------------------------------------------------------------------------------]   0
Done in 60ms
Calculate dense nodes
[*>:??-----------------------------------------------------------------------------------------]   0
Done in 10ms
Relationships
[*>:??-----------------------------------------------------------------------------------------]   0
Done in 11ms
Node --> Relationship
[*v:??-----------------------------------------------------------------------------------------] 10k
Done in 1ms
Relationship --> Relationship
[*>:??-----------------------------------------------------------------------------------------]   0
Done in 11ms
Node counts
[>:|*COUNT:76.29 MB----------------------------------------------------------------------------] 10k
Done in 46ms
Relationship counts
[*>:??-----------------------------------------------------------------------------------------]   0
Done in 12ms

IMPORT DONE in 1s 576ms. Imported:
  3 nodes
  0 relationships
  3 properties
~~~

<P>Sweet! We're back in business.</p>

