+++
draft = false
date="2013-08-22 22:56:23"
title="Unix: tar - Extracting, creating and viewing archives"
tag=['unix', 'tar']
category=['Shell Scripting']
+++

<p>I've been playing around with the Unix <a href="http://www.computerhope.com/unix/utar.htm">tar</a> command a bit this week and realised that I'd memorised some of the flag combinations but didn't actually know what each of them meant.</p>


<p>For example, one of the most common things that I want to do is extract a gripped neo4j archive:</p>



~~~bash

$ wget http://dist.neo4j.org/neo4j-community-1.9.2-unix.tar.gz
$ tar -xvf neo4j-community-1.9.2-unix.tar.gz
~~~

<p>where:</p>


<ul>
<li>-x means extract</li>
<li>-v means produce verbose output i.e. print out the names of all the files as you unpack it</li>
<li>-f means unpack the file which follows this flag i.e. neo4j-community-1.9.2-unix.tar.gz in this example</li>
</ul>

<p>I didn't realise that by default tar runs against standard input so we could actually achieve the above in one go with the following combination:</li>


~~~bash

$ wget http://dist.neo4j.org/neo4j-community-1.9.2-unix.tar.gz -o - | tar -xv
~~~

<p>The other thing I wanted to do was create a gripped archive from the contents of a folder, something which I do much less frequently and am therefore  much more rusty at! The following does the trick:</p>



~~~bash

$ tar -cvzpf neo4j-football.tar.gz neo4j-football/
$ ls -alh neo4j-football.tar.gz 
-rw-r--r--  1 markhneedham  staff   526M 22 Aug 23:38 neo4j-football.tar.gz
~~~

<p>where:</p>


<ul>
<li>-c means create a new archive</li>
<li>-z means gzip that archive</li>
<li>-p means preserve file permissions</li>
</ul>

<p>Sometimes we'll want to exclude some things from our archive which is where the '--exclude' flag comes in handy.</p>


<p>For example I want to exclude the data, git and neo4j folders which sit inside 'neo4j-football' which I can do with the following:</p>



~~~bash

$ tar --exclude "data*" --exclude "neo4j-community*" --exclude ".git" -cvzpf neo4j-football.tar.gz neo4j-football/
$ ls -alh neo4j-football.tar.gz 
-rw-r--r--  1 markhneedham  staff   138M 22 Aug 23:36 neo4j-football.tar.gz
~~~

<p>If we want to quickly check that our file has been created correctly we can run the following:</p>



~~~bash

$ tar -tvf neo4j-football.tar.gz
~~~

<p>where:</p>


<ul>
<li>-t means list the contents of the archive to standard out</li>
</ul>

<p>And that pretty much covers my main use cases for the moment!</p>

