+++
draft = false
date="2018-03-07 03:11:12"
title="Neo4j Import: java.lang.IllegalStateException: Mixing specified and unspecified group belongings in a single import isn't supported"
tag=['neo4j', 'neo4j-import', 'bulk-import']
category=['neo4j']
+++

<p>
I've been working with the <a href="https://neo4j.com/docs/operations-manual/current/tools/import/">Neo4j Import Tool</a> recently after a bit of a break and ran into an interesting error message that I initially didn't understand.
</p>


<p>
I had some CSV files containing nodes that I wanted to import into Neo4j. Their contents look like this:
</p>



~~~bash

$ cat people_header.csv 
name:ID(Person)

$ cat people.csv 
"Mark"
"Michael"
"Ryan"
"Will"
"Jennifer"
"Karin"

$ cat companies_header.csv 
name:ID(Company)

$ cat companies.csv 
"Neo4j"
~~~

<p>
I find it easier to use separate header files because I often make typos with my column names and it's easier to update a single line file than to open a multi-million line file and change the first line.
</p>


<p>
I ran the following command to create a new Neo4j database from these files:
</p>



~~~bash

$ ./bin/neo4j-admin import \
	--database=blog.db \
	--mode=csv \
	--nodes:Person people_header.csv,people.csv \
	--nodes:Company companies_heade.csv,companies.csv
~~~

<p>
which resulted in this error message:
</p>



~~~bash

Neo4j version: 3.3.3
Importing the contents of these files into /Users/markneedham/Library/Application Support/Neo4j Desktop/Application/neo4jDatabases/database-b59e33d5-2060-4a5d-bdb8-0b9f6dc919fa/installation-3.3.3/data/databases/blog.db:
Nodes:
  :Person
  /Users/markneedham/Library/Application Support/Neo4j Desktop/Application/neo4jDatabases/database-b59e33d5-2060-4a5d-bdb8-0b9f6dc919fa/installation-3.3.3/people_header.csv
  /Users/markneedham/Library/Application Support/Neo4j Desktop/Application/neo4jDatabases/database-b59e33d5-2060-4a5d-bdb8-0b9f6dc919fa/installation-3.3.3/people.csv

  :Company
  /Users/markneedham/Library/Application Support/Neo4j Desktop/Application/neo4jDatabases/database-b59e33d5-2060-4a5d-bdb8-0b9f6dc919fa/installation-3.3.3/companies.csv

...

Import error: Mixing specified and unspecified group belongings in a single import isn't supported
Caused by:Mixing specified and unspecified group belongings in a single import isn't supported
java.lang.IllegalStateException: Mixing specified and unspecified group belongings in a single import isn't supported
	at org.neo4j.unsafe.impl.batchimport.input.Groups.getOrCreate(Groups.java:52)
	at org.neo4j.unsafe.impl.batchimport.input.csv.InputNodeDeserialization.initialize(InputNodeDeserialization.java:60)
	at org.neo4j.unsafe.impl.batchimport.input.csv.InputEntityDeserializer.initialize(InputEntityDeserializer.java:68)
	at org.neo4j.unsafe.impl.batchimport.input.csv.ParallelInputEntityDeserializer.lambda$new$0(ParallelInputEntityDeserializer.java:104)
	at org.neo4j.unsafe.impl.batchimport.staging.TicketedProcessing.lambda$submit$1(TicketedProcessing.java:103)
	at org.neo4j.unsafe.impl.batchimport.executor.DynamicTaskExecutor$Processor.run(DynamicTaskExecutor.java:237)
~~~

<p>
The output actually helpfully indicates which files it's importing from and we can see under the 'Company' section that the header file is missing.
</p>


<p>As a result of the typo I made when trying to type <cite>companies_header.csv</cite>, the tool now treats the first line of <cite>companies.csv</cite> as the header and since we haven't specified a group (e.g. Company, Person) on that line we receive this error.
</p>


<p>
Let's fix the typo and try again:
</p>



~~~bash

$ ./bin/neo4j-admin import \
	--database=blog.db \
	--mode=csv \
	--nodes:Person people_header.csv,people.csv \
	--nodes:Company companies_header.csv,companies.csv

Neo4j version: 3.3.3
Importing the contents of these files into /Users/markneedham/Library/Application Support/Neo4j Desktop/Application/neo4jDatabases/database-b59e33d5-2060-4a5d-bdb8-0b9f6dc919fa/installation-3.3.3/data/databases/blog.db:
Nodes:
  :Person
  /Users/markneedham/Library/Application Support/Neo4j Desktop/Application/neo4jDatabases/database-b59e33d5-2060-4a5d-bdb8-0b9f6dc919fa/installation-3.3.3/people_header.csv
  /Users/markneedham/Library/Application Support/Neo4j Desktop/Application/neo4jDatabases/database-b59e33d5-2060-4a5d-bdb8-0b9f6dc919fa/installation-3.3.3/people.csv

  :Company
  /Users/markneedham/Library/Application Support/Neo4j Desktop/Application/neo4jDatabases/database-b59e33d5-2060-4a5d-bdb8-0b9f6dc919fa/installation-3.3.3/companies_header.csv
  /Users/markneedham/Library/Application Support/Neo4j Desktop/Application/neo4jDatabases/database-b59e33d5-2060-4a5d-bdb8-0b9f6dc919fa/installation-3.3.3/companies.csv

...

IMPORT DONE in 1s 5ms. 
Imported:
  7 nodes
  0 relationships
  7 properties
Peak memory usage: 480.00 MB
~~~

<p>
Success!
</p>

