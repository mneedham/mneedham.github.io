+++
draft = false
date="2014-01-22 17:36:53"
title="Neo4j Backup: Store copy and consistency check"
tag=['neo4j']
category=['neo4j']
+++

<p>One of the lesser known things about the <a href="http://docs.neo4j.org/chunked/milestone/backup-embedded-and-server.html">Neo4j online backup tool</a>, which I <a href="http://www.markhneedham.com/blog/2014/01/19/neo4j-backup-java-lang-classcastexception-org-jboss-netty-buffer-bigendianheapchannelbuffer-cannot-be-cast-to-org-neo4j-cluster-com-message-message/">wrote about last week</a>, is that conceptually there are two parts to it:</p>


<ol>
<li>Copying the store files to a location of your choice</li>
<li>Verifying that those store files are consistent.</li>
</ol>

<p>By default both of these run when you run the 'neo4j-backup' script but sometimes it's useful to be able to run them separately.</p>


<p>If we want to just run the copying the store files part of the process we can tell the backup tool to skip the consistency check by using the '<a href="https://github.com/neo4j/neo4j/blob/2.0-maint/enterprise/backup/src/main/java/org/neo4j/backup/BackupTool.java#L97">verify</a>' flag:</p>



~~~bash

$ pwd
/Users/markneedham/Downloads/neo4j-enterprise-2.0.0
~~~


~~~bash

$ ./bin/neo4j-backup -from single://127.0.0.1 -to /tmp/foo -verify false
Performing full backup from 'single://127.0.0.1'
Files copied
................        done
Done
~~~

<p>If we ran that without the 'verify' flag we'd see the output of the consistency checker as well:</p>



~~~bash

$ ./bin/neo4j-backup -from single://127.0.0.1 -to /tmp/foo
Performing full backup from 'single://127.0.0.1'
Files copied
................        done
Full consistency check
....................  10%
....................  20%
....................  30%
....................  40%
....................  50%
....................  60%
....................  70%
....................  80%
....................  90%
.................... 100%
Done
~~~

<p>If we already have a backup and only want to run the consistency checker we can run the following command:</p>



~~~bash

$ java -cp 'lib/*:system/lib/*' org.neo4j.consistency.ConsistencyCheckTool /tmp/foo
Full consistency check
....................  10%
....................  20%
....................  30%
....................  40%
....................  50%
....................  60%
....................  70%
....................  80%
....................  90%
.................... 100%
~~~

<p>The consistency tool itself takes a '<a href="https://github.com/neo4j/neo4j/blob/2.0-maint/enterprise/consistency-check/src/main/java/org/neo4j/consistency/ConsistencyCheckTool.java#L149">config</a>' flag which gives you some control over what things you want to consistency check.</p>


<p>The various options are defined in <cite><a href="https://github.com/neo4j/neo4j/blob/2.0-maint/enterprise/consistency-check/src/main/java/org/neo4j/consistency/ConsistencyCheckSettings.java#L52">org.neo4j.consistency.ConsistencyCheckSettings</a></cite>.</p>
 

<p>For example, if we want to change the file that the consistency check report is written to we could add the following property to our config file:</p>



~~~text

$ tail -n 1 conf/neo4j.properties
consistency_check_report_file=/tmp/foo.txt
~~~

<p>And then run the consistency tool like so:</p>



~~~bash

$ java -cp 'lib/*:system/lib/*' org.neo4j.consistency.ConsistencyCheckTool -config conf/neo4j.properties /tmp/foo
~~~

<p>If there are any inconsistencies they'll now be written to that file rather than to a file in the store directory.</p>


<p>You can also pass that 'config' flag to the backup tool and it will make use of it when it runs the consistency check. e.g.</p>



~~~bash

$ ./bin/neo4j-backup -from single://127.0.0.1 -to /tmp/foo -config conf/neo4j.properties
~~~

<p>Most of the time you don't need to worry too much about either of these commands but I always forget what the various options are so I thought I'd better write it up while it's fresh in my mind.</p>

