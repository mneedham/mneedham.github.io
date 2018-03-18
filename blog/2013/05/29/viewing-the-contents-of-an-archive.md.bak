+++
draft = false
date="2013-05-29 11:22:35"
title="Viewing the contents of an archive"
tag=['software-development']
category=['Software Development']
+++

<p>Everyone now and then I want to check the contents of an archive without unpacking it and I tend to use <cite><a href="http://linux.about.com/od/commands/l/blcmdl1_unzip.htm">unzip</a></cite> to do so:</p>



~~~bash

$ unzip -l batch-import-jar-with-dependencies.jar | tail -n 10 
     1645  02-17-13 01:03   org/neo4j/batchimport/StdOutReport.class
     3089  02-17-13 01:03   org/neo4j/batchimport/structs/NodeStruct.class
     1244  02-17-13 01:03   org/neo4j/batchimport/structs/Property.class
     1732  02-17-13 01:03   org/neo4j/batchimport/structs/PropertyHolder.class
     1635  02-17-13 01:03   org/neo4j/batchimport/structs/Relationship.class
      905  02-17-13 01:03   org/neo4j/batchimport/utils/Chunker.class
     1884  02-17-13 01:03   org/neo4j/batchimport/utils/Params.class
     4445  02-17-13 01:03   org/neo4j/batchimport/Utils.class
 --------                   -------
 49947859                   16447 files
~~~

<p>It does the job although it does print out some information that we're not really interested in so I was intrigued to see that <a href="https://twitter.com/apcj">Alistair</a> used <cite><a href="http://linux.about.com/library/cmd/blcmdl1_zipinfo.htm">zipinfo</a></cite> when he wanted to achieve a similar thing:</p>



~~~bash

$ zipinfo -1 batch-import-jar-with-dependencies.jar | tail -n 10
org/neo4j/batchimport/ParallelImporter.class
org/neo4j/batchimport/Report.class
org/neo4j/batchimport/StdOutReport.class
org/neo4j/batchimport/structs/NodeStruct.class
org/neo4j/batchimport/structs/Property.class
org/neo4j/batchimport/structs/PropertyHolder.class
org/neo4j/batchimport/structs/Relationship.class
org/neo4j/batchimport/utils/Chunker.class
org/neo4j/batchimport/utils/Params.class
org/neo4j/batchimport/Utils.class
~~~

<p>From a bit of man page reading it sounds like zipinfo is unzip, but with different flags that give an output that's a cross between unzip and ls:</p>


<blockquote>
The format is a cross between
       Unix ``ls -l'' and ``unzip -v'' output.  See DETAILED DESCRIPTION below.  Note that zipinfo is the same program as unzip (under Unix, a link to it); on some  systems,
       however, zipinfo support may have been omitted when unzip was compiled.
</blockquote>

<p>As long as I remember I'll be using zipinfo from now on!</p>

