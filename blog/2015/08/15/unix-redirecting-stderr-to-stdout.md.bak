+++
draft = false
date="2015-08-15 15:55:32"
title="Unix: Redirecting stderr to stdout"
tag=['unix']
category=['Shell Scripting']
+++

<p>
I've been trying to optimise some Neo4j import queries over the last couple of days and as part of the script I've been executed I wanted to redirect the output of a couple of commands into a file to parse afterwards.
</p>


<p>
I started with the following script which doesn't do any explicit redirection of the output:
</p>



~~~bash

#!/bin/sh

./neo4j-community-2.2.3/bin/neo4j start
~~~

<p>Now let's run that script and redirect the output to a file:</p>



~~~bash

$ ./foo.sh > /tmp/output.txt
Unable to find any JVMs matching version "1.7".

$ cat /tmp/output.txt
Starting Neo4j Server...WARNING: not changing user
process [48230]... waiting for server to be ready.... OK.
http://localhost:7474/ is ready.
~~~

<p>
So the line about not finding a matching JVM is being printed to stderr. That's reasonably easy to fix:
</p>



~~~bash

#!/bin/sh

./neo4j-community-2.2.3/bin/neo4j start 2>&1
~~~

<p>
Let's run the script again:
</p>



~~~bash

$ ./foo.sh > /tmp/output.txt

$ cat /tmp/output.txt
Unable to find any JVMs matching version "1.7".
Starting Neo4j Server...WARNING: not changing user
process [47989]... waiting for server to be ready.... OK.
http://localhost:7474/ is ready.
~~~

<p>Great, that worked as expected. Next I extended the script to stop Neo4j, delete all it's data, start it again and execute a cypher script:
</p>



~~~bash

#!/bin/sh

./neo4j-community-2.2.3/bin/neo4j start 2>&1
rm -rf neo4j-community-2.2.3/data/graph.db/
./neo4j-community-2.2.3/bin/neo4j start 2>&1
time ./neo4j-community-2.2.3/bin/neo4j-shell --file foo.cql 2>&1
~~~

<p>Let's run that script and redirect the output:</p>



~~~bash

$ ./foo.sh > /tmp/output.txt
Unable to find any JVMs matching version "1.7".

real	0m0.604s
user	0m0.334s
sys	0m0.054s

$ cat /tmp/output.txt
Unable to find any JVMs matching version "1.7".
Another server-process is running with [50614], cannot start a new one. Exiting.
Unable to find any JVMs matching version "1.7".
Another server-process is running with [50614], cannot start a new one. Exiting.
+---------+
| "hello" |
+---------+
| "hello" |
+---------+
1 row
4 ms
~~~

<p>
It looks like our stderr -> stdout redirection on the last line didn't work. My understanding is that the 'time' command <a href="http://stackoverflow.com/questions/2408981/how-cant-i-redirect-the-output-of-time-command">swallows all the arguments that follow</a> whereas we want the redirection to be run afterwards.
</p>


<p>
We can work our way around this problem by putting the actual command in a code block and redirected the output of that:
</p>



~~~bash

#!/bin/sh

./neo4j-community-2.2.3/bin/neo4j start 2>&1
rm -rf neo4j-community-2.2.3/data/graph.db/
./neo4j-community-2.2.3/bin/neo4j start 2>&1
{ time ./neo4j-community-2.2.3/bin/neo4j-shell --file foo.cql; } 2>&1
~~~



~~~bash

$ ./foo.sh  > /tmp/output.txt

$ cat /tmp/output.txt
Unable to find any JVMs matching version "1.7".
Another server-process is running with [50614], cannot start a new one. Exiting.
Unable to find any JVMs matching version "1.7".
Another server-process is running with [50614], cannot start a new one. Exiting.
Unable to find any JVMs matching version "1.7".
+---------+
| "hello" |
+---------+
| "hello" |
+---------+
1 row
4 ms

real	0m0.615s
user	0m0.316s
sys	0m0.050s
~~~

<p>
Much better!
</p>

