+++
draft = false
date="2015-08-21 20:59:37"
title="Neo4j: Summarising neo4j-shell output"
tag=['neo4j']
category=['neo4j']
+++

</p>

I frequently find myself trying to optimise a set of cypher queries and I tend to group them together in a script that I fed to the <a href="http://neo4j.com/docs/stable/shell.html">Neo4j shell</a>.
</p>


<p>
When tweaking the queries it's easy to make a mistake and end up not creating the same data so I decided to write a script which will show me the aggregates of all the commands executed.
</p>


<p>
I want to see the number of constraints created, indexes added, nodes, relationships and properties created. The first 2 don't need to match across the scripts but the latter 3 should be the same.
</p>


<p>I put together the following script:</p>



~~~python

import re
import sys
from tabulate import tabulate

lines = sys.stdin.readlines()

def search(term, line):
    m =  re.match(term + ": (.*)", line)
    return (int(m.group(1)) if m else 0)

nodes_created, relationships_created, constraints_added, indexes_added, labels_added, properties_set = 0, 0, 0, 0, 0, 0
for line in lines:
    nodes_created = nodes_created + search("Nodes created", line)
    relationships_created = relationships_created + search("Relationships created", line)
    constraints_added = constraints_added + search("Constraints added", line)
    indexes_added = indexes_added + search("Indexes added", line)
    labels_added = labels_added + search("Labels added", line)
    properties_set = properties_set + search("Properties set", line)

    time_match = re.match("real.*([0-9]+m[0-9]+\.[0-9]+s)$", line)

    if time_match:
        time = time_match.group(1)

table = [
            ["Constraints added", constraints_added],
            ["Indexes added", indexes_added],
            ["Nodes created", nodes_created],
            ["Relationships created", relationships_created],
            ["Labels added", labels_added],
            ["Properties set", properties_set],
            ["Time", time]
         ]
print tabulate(table)
~~~

<p>
Its input is the piped output of the neo4j-shell command which will contain a description of all the queries it executed. </p>



~~~bash

$ cat import.sh
#!/bin/sh

{ ./neo4j-community-2.2.3/bin/neo4j stop; } 2>&1
rm -rf neo4j-community-2.2.3/data/graph.db/
{ ./neo4j-community-2.2.3/bin/neo4j start; } 2>&1
{ time ./neo4j-community-2.2.3/bin/neo4j-shell --file $1; } 2>&1
~~~

<p>
We can use the script in two ways.
</p>


<p>Either we can pipe the output of our shell straight into it and just get the summary e.g.</p>



~~~bash

$ ./import.sh local.import.optimised.cql | python summarise.py

---------------------  ---------
Constraints added      5
Indexes added          1
Nodes created          13249
Relationships created  32227
Labels added           21715
Properties set         36480
Time                   0m17.595s
---------------------  ---------
~~~

<p>...or we can make use of the 'tee' function in Unix and pipe the output into stdout and into the file and then either tail the file on another window or inspect it afterwards to see the detailed timings. e.g.
</p>



~~~bash

$ ./import.sh local.import.optimised.cql | tee /tmp/output.txt |  python summarise.py

---------------------  ---------
Constraints added      5
Indexes added          1
Nodes created          13249
Relationships created  32227
Labels added           21715
Properties set         36480
Time                   0m11.428s
---------------------  ---------
~~~


~~~bash

$ tail -f /tmp/output.txt
+-------------+
| appearances |
+-------------+
| 3771        |
+-------------+
1 row
Nodes created: 3439
Properties set: 3439
Labels added: 3439
289 ms
+------------------------------------+
| appearances -> player, match, team |
+------------------------------------+
| 3771                               |
+------------------------------------+
1 row
Relationships created: 10317
1006 ms
...
~~~

<p>My only dependency is the tabulate package to get the pretty table:</p>



~~~bash

$ cat requirements.txt

tabulate==0.7.5
~~~

<p>The <a href="https://github.com/mneedham/neo4j-bbc/blob/master/local.import.optimised.cql">cypher script</a> I'm running creates a BBC football graph which is available as a <a href="https://github.com/mneedham/neo4j-bbc">github project</a>. Feel free to grab it and play around - any problems let me know!</p>

