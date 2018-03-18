+++
draft = false
date="2013-06-09 23:10:34"
title="Unix: find, xargs, zipinfo and the 'caution: filename not matched:' error"
tag=['unix']
category=['Shell Scripting']
+++

<p>As I mentioned <a href="http://www.markhneedham.com/blog/2013/06/09/neo4j-rb-ha-nameerror-cannot-load-java-class-org-neo4j-graphdb-factory-highlyavailablegraphdatabasefactory/">in my previous post</a> last week I needed to scan all the jar files included with the neo4j-enterprise gem and I started out by finding out where it's located on my machine:</p>



~~~bash

$ bundle show neo4j-enterprise
/Users/markhneedham/.rbenv/versions/jruby-1.7.1/lib/ruby/gems/shared/gems/neo4j-enterprise-1.8.2-java
~~~

<p>I then thought I could get a list of all the jar files using <cite><a href="http://unixhelp.ed.ac.uk/CGI/man-cgi?find">find</a></cite> and pipe it into <cite><a href="http://linux.about.com/library/cmd/blcmdl1_zipinfo.htm">zipinfo</a></cite> via <a href="http://linux.die.net/man/1/xargs">xargs</a> to get all the file names and then search for <cite>HighlyAvailableGraphDatabaseFactory</cite>:</p>


<p>Unfortunately when I tried that it didn't quite work:</p>



~~~bash

$ cd /Users/markhneedham/.rbenv/versions/jruby-1.7.1/lib/ruby/gems/shared/gems/neo4j-enterprise-1.8.2-java/lib/neo4j-enterprise/jars/
$ find . -iname "*.jar" | xargs zipinfo
caution: filename not matched:  ./lib/neo4j-enterprise/jars/logback-classic-0.9.30.jar
caution: filename not matched:  ./lib/neo4j-enterprise/jars/logback-core-0.9.30.jar
caution: filename not matched:  ./lib/neo4j-enterprise/jars/neo4j-backup-1.8.2.jar
caution: filename not matched:  ./lib/neo4j-enterprise/jars/neo4j-com-1.8.2.jar
caution: filename not matched:  ./lib/neo4j-enterprise/jars/neo4j-consistency-check-1.8.2.jar
caution: filename not matched:  ./lib/neo4j-enterprise/jars/neo4j-ha-1.8.2.jar
caution: filename not matched:  ./lib/neo4j-enterprise/jars/neo4j-udc-1.8.2.jar
caution: filename not matched:  ./lib/neo4j-enterprise/jars/org.apache.servicemix.bundles.netty-3.2.5.Final_1.jar
caution: filename not matched:  ./lib/neo4j-enterprise/jars/server-api-1.8.2.jar
caution: filename not matched:  ./lib/neo4j-enterprise/jars/slf4j-api-1.6.2.jar
caution: filename not matched:  ./lib/neo4j-enterprise/jars/zookeeper-3.3.2.jar
~~~

<p>I switched 'zipinfo' to 'echo' to see what was going on which resulted in the following output:</p>



~~~bash

$ find . -iname "*.jar" | xargs echo
./log4j-1.2.16.jar ./logback-classic-0.9.30.jar ./logback-core-0.9.30.jar ./neo4j-backup-1.8.2.jar ./neo4j-com-1.8.2.jar ./neo4j-consistency-check-1.8.2.jar ./neo4j-ha-1.8.2.jar ./neo4j-udc-1.8.2.jar ./org.apache.servicemix.bundles.netty-3.2.5.Final_1.jar ./server-api-1.8.2.jar ./slf4j-api-1.6.2.jar ./zookeeper-3.3.2.jar
~~~

<p>As I understand it, xargs expects arguments to be separated by a space and I thought it would apply the command to each argument individually but it seemed to be including the space as part of the file name.</p>


<p>I've previously used the '-n' flag to <cite>xargs</cite> to explicitly tell it to call the corresponding command with one argument at a time and that seemed to do the trick:</p>



~~~bash

$ find . -iname "*.jar" | xargs -n1 zipinfo
Archive:  ./log4j-1.2.16.jar   481535 bytes   346 files
-rw----     2.0 fat     3186 bX defN 30-Mar-10 23:25 META-INF/MANIFEST.MF
-rw----     2.0 fat        0 bl defN 30-Mar-10 23:25 META-INF/
-rw----     2.0 fat    11366 bl defN 30-Mar-10 23:14 META-INF/LICENSE
-rw----     2.0 fat      160 bl defN 30-Mar-10 23:14 META-INF/NOTICE
-rw----     2.0 fat        0 bl defN 30-Mar-10 23:25 META-INF/maven/
-rw----     2.0 fat        0 bl defN 30-Mar-10 23:25 META-INF/maven/log4j/
...
~~~

<p>Of course to solve this particular we don't actually need to use <cite>find</cite> and <cite>xargs</cite> since we can just call <cite>zipinfo</cite> <a href="http://rubenerd.com/caution-filename-not-matched-unzip-error/">with the wildcard match</a>:</p>



~~~bash

$ zipinfo \*.jar
Archive:  log4j-1.2.16.jar   481535 bytes   346 files
-rw----     2.0 fat     3186 bX defN 30-Mar-10 23:25 META-INF/MANIFEST.MF
-rw----     2.0 fat        0 bl defN 30-Mar-10 23:25 META-INF/
-rw----     2.0 fat    11366 bl defN 30-Mar-10 23:14 META-INF/LICENSE
-rw----     2.0 fat      160 bl defN 30-Mar-10 23:14 META-INF/NOTICE
-rw----     2.0 fat        0 bl defN 30-Mar-10 23:25 META-INF/maven/
-rw----     2.0 fat        0 bl defN 30-Mar-10 23:25 META-INF/maven/log4j/
-rw----    
...
~~~

<p>I'm curious why <cite>xargs</cite> didn't work as I expected it to though - have I just misremembered its default behaviour or is something weird going on?</p>

