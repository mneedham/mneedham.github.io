+++
draft = false
date="2015-03-14 02:52:02"
title="Python: Checking any value in a list exists in a line of text"
tag=['python']
category=['Python']
+++

<p>
I've been doing some log file analysis to see what cypher queries were being run on a Neo4j instance and I wanted to narrow down the lines I looked at to only contain ones which had mutating operations i.e. those  containing the words MERGE, DELETE, SET or CREATE
</p>


<p>Here's an example of the text file I was parsing:</p>



~~~bash

$ cat blog.txt
MATCH n RETURN n
MERGE (n:Person {name: "Mark"}) RETURN n
MATCH (n:Person {name: "Mark"}) ON MATCH SET n.counter = 1 RETURN n
~~~

<p>So I only want lines 2 & 3 to be returned as the first one only returns data and doesn't execute any updates on the graph.</p>


<p>
I started off with a very crude way of doing this;
</p>



~~~python

with open("blog.txt", "r") as ins:
    for line in ins:
        if "MERGE" in line or "DELETE" in line or "SET" in line or "CREATE" in line:
           print line.strip()
~~~

<p>
A better way of doing this is to use the <cite><a href="https://docs.python.org/2/library/functions.html#any">any</a></cite> command and make sure at least one of the words exists in the line:
</p>



~~~python

mutating_commands = ["SET", "DELETE", "MERGE", "CREATE"]
with open("blog.txt", "r") as ins:
    for line in ins:
        if any(command in line for command in mutating_commands):
           print line.strip()
~~~

<p>I thought I might be able to simplify the code even further by using <a href="https://docs.python.org/2/library/itertools.html">itertools</a> but my best attempt so far is less legible than the above:</p>



~~~python

import itertools

commands = ["SET", "CREATE", "MERGE", "DELETE"]
with open("blog.txt", "r") as ins:
    for line in ins:
        if len(list(itertools.ifilter(lambda x: x in line, mutating_commands))) > 0:
            print line.strip()
~~~

<p>
I think I'll go with the 2nd approach for now but if I'm doing something wrong with itertools and it's much easier to use than the example I've shown do correct me!
</p>

