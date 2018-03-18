+++
draft = false
date="2015-08-13 19:30:51"
title="Sed: Using environment variables"
tag=['sed']
category=['Shell Scripting']
+++

<p>
I've been playing around with the <a href="http://www.markhneedham.com/blog/2015/05/16/neo4j-bbc-football-live-text-fouls-graph/">BBC football data set</a> that I wrote about a couple of months ago and I wanted to write some code that would take the import script and replace all instances of remote URIs with a file system path.
</p>



<p>
For example the import file contains several lines similar to this:
</p>



~~~text

LOAD CSV WITH HEADERS 
FROM "https://raw.githubusercontent.com/mneedham/neo4j-bbc/master/data/matches.csv" 
AS row
~~~

<p>And I want that to read:</p>




~~~text

LOAD CSV WITH HEADERS 
FROM "file:///Users/markneedham/repos/neo4j-bbc/data/matches.csv" 
AS row
~~~

<p>The start of that path also happens to be my working directory:</p>



~~~bash

$ echo $PWD
/Users/markneedham/repos/neo4j-bbc
~~~

<p>So I wanted to write a script that would look for occurrences of 'https://raw.githubusercontent.com/mneedham/neo4j-bbc/master' and replace it with $PWD. I'm a fan of Sed so I thought I'd try and use it to solve my problem.
</p>


<p>
The first thing we can do to make life easy is to change the default delimiter. Sed usually uses '/' to separate parts of the command but since we're using URIs that's going to be horrible so we'll use an underscore instead.
</p>


<p>
For a first cut I tried just removing that first part of the URI but not replacing it with anything in particular:
</p>



~~~bash

$ sed 's_https://raw.githubusercontent.com/mneedham/neo4j-bbc/master__' import.cql

$ sed 's_https://raw.githubusercontent.com/mneedham/neo4j-bbc/master__' import.cql | grep LOAD
LOAD CSV WITH HEADERS FROM "/data/matches.csv" AS row
LOAD CSV WITH HEADERS FROM "/data/players.csv" AS row
LOAD CSV WITH HEADERS FROM "/data/players.csv" AS row
LOAD CSV WITH HEADERS FROM "/data/fouls.csv" AS row
LOAD CSV WITH HEADERS FROM "/data/attempts.csv" AS row
LOAD CSV WITH HEADERS FROM "/data/attempts.csv" AS row
LOAD CSV WITH HEADERS FROM "/data/corners.csv" AS row
LOAD CSV WITH HEADERS FROM "/data/corners.csv" AS row
LOAD CSV WITH HEADERS FROM "/data/cards.csv" AS row
LOAD CSV WITH HEADERS FROM "/data/cards.csv" AS row
LOAD CSV WITH HEADERS FROM "/data/subs.csv" AS row
~~~

<p>Cool! That worked as expected. Now let's try and replace it with $PWD:</p>



~~~bash

$ sed 's_https://raw.githubusercontent.com/mneedham/neo4j-bbc/master_file://$PWD_' import.cql | grep LOAD
LOAD CSV WITH HEADERS FROM "file://$PWD/data/matches.csv" AS row
LOAD CSV WITH HEADERS FROM "file://$PWD/data/players.csv" AS row
LOAD CSV WITH HEADERS FROM "file://$PWD/data/players.csv" AS row
LOAD CSV WITH HEADERS FROM "file://$PWD/data/fouls.csv" AS row
LOAD CSV WITH HEADERS FROM "file://$PWD/data/attempts.csv" AS row
LOAD CSV WITH HEADERS FROM "file://$PWD/data/attempts.csv" AS row
LOAD CSV WITH HEADERS FROM "file://$PWD/data/corners.csv" AS row
LOAD CSV WITH HEADERS FROM "file://$PWD/data/corners.csv" AS row
LOAD CSV WITH HEADERS FROM "file://$PWD/data/cards.csv" AS row
LOAD CSV WITH HEADERS FROM "file://$PWD/data/cards.csv" AS row
LOAD CSV WITH HEADERS FROM "file://$PWD/data/subs.csv" AS row
~~~

<p>Hmmm that didn't work as expected. The $PWD is being treated as a literal instead of being evaluated like we want it to be.</p>


<p>
It turns out this is <a href="http://askubuntu.com/questions/76808/how-to-use-variables-in-sed-command">a popular question on Stack Overflow</a> and there are lots of suggestions - I tried a few of them and found that single quotes did the trick:
</p>



~~~bash

$ sed 's_https://raw.githubusercontent.com/mneedham/neo4j-bbc/master_file://'$PWD'_' import.cql | grep LOAD
LOAD CSV WITH HEADERS FROM "file:///Users/markneedham/repos/neo4j-bbc/data/matches.csv" AS row
LOAD CSV WITH HEADERS FROM "file:///Users/markneedham/repos/neo4j-bbc/data/players.csv" AS row
LOAD CSV WITH HEADERS FROM "file:///Users/markneedham/repos/neo4j-bbc/data/players.csv" AS row
LOAD CSV WITH HEADERS FROM "file:///Users/markneedham/repos/neo4j-bbc/data/fouls.csv" AS row
LOAD CSV WITH HEADERS FROM "file:///Users/markneedham/repos/neo4j-bbc/data/attempts.csv" AS row
LOAD CSV WITH HEADERS FROM "file:///Users/markneedham/repos/neo4j-bbc/data/attempts.csv" AS row
LOAD CSV WITH HEADERS FROM "file:///Users/markneedham/repos/neo4j-bbc/data/corners.csv" AS row
LOAD CSV WITH HEADERS FROM "file:///Users/markneedham/repos/neo4j-bbc/data/corners.csv" AS row
LOAD CSV WITH HEADERS FROM "file:///Users/markneedham/repos/neo4j-bbc/data/cards.csv" AS row
LOAD CSV WITH HEADERS FROM "file:///Users/markneedham/repos/neo4j-bbc/data/cards.csv" AS row
LOAD CSV WITH HEADERS FROM "file:///Users/markneedham/repos/neo4j-bbc/data/subs.csv" AS row
~~~

<p>
We could also use double quotes everywhere if we prefer:
</p>



~~~bash

$ sed "s_https://raw.githubusercontent.com/mneedham/neo4j-bbc/master_file://"$PWD"_" import.cql | grep LOAD
LOAD CSV WITH HEADERS FROM "file:///Users/markneedham/repos/neo4j-bbc/data/matches.csv" AS row
LOAD CSV WITH HEADERS FROM "file:///Users/markneedham/repos/neo4j-bbc/data/players.csv" AS row
LOAD CSV WITH HEADERS FROM "file:///Users/markneedham/repos/neo4j-bbc/data/players.csv" AS row
LOAD CSV WITH HEADERS FROM "file:///Users/markneedham/repos/neo4j-bbc/data/fouls.csv" AS row
LOAD CSV WITH HEADERS FROM "file:///Users/markneedham/repos/neo4j-bbc/data/attempts.csv" AS row
LOAD CSV WITH HEADERS FROM "file:///Users/markneedham/repos/neo4j-bbc/data/attempts.csv" AS row
LOAD CSV WITH HEADERS FROM "file:///Users/markneedham/repos/neo4j-bbc/data/corners.csv" AS row
LOAD CSV WITH HEADERS FROM "file:///Users/markneedham/repos/neo4j-bbc/data/corners.csv" AS row
LOAD CSV WITH HEADERS FROM "file:///Users/markneedham/repos/neo4j-bbc/data/cards.csv" AS row
LOAD CSV WITH HEADERS FROM "file:///Users/markneedham/repos/neo4j-bbc/data/cards.csv" AS row
LOAD CSV WITH HEADERS FROM "file:///Users/markneedham/repos/neo4j-bbc/data/subs.csv" AS row
~~~
