+++
draft = false
date="2012-02-11 10:02:09"
title="Downloading the JDK 6 source code"
tag=['software-development']
category=['Software Development']
+++

Every now and then I want to get the JDK source code onto a new machine and it always seems to take me longer than I expect it to so this post is an attempt to help future me!

Googling for this takes me to <a href="http://download.java.net/jdk6/6u23/promoted/latest/">this page</a> and I always think I'll just checkout the <a href="http://java.net/projects/jdk-jrl-sources/">SVN repository</a> and hook that up but it doesn't seem to be available.


~~~text

$ wget -S http://java.net/projects/jdk-jrl-sources/
--2012-02-11 09:51:34--  http://java.net/projects/jdk-jrl-sources/
Resolving java.net (java.net)... 192.9.164.103
Connecting to java.net (java.net)|192.9.164.103|:80... connected.
HTTP request sent, awaiting response... 
  HTTP/1.1 404 Not Found
  Date: Sat, 11 Feb 2012 09:51:34 GMT
~~~

The alternative is therefore to download the jar provided which we can do like this:


~~~text

wget http://www.java.net/download/jdk6/6u23/promoted/b05/jdk-6u23-fcs-src-b05-jrl-12_nov_2010.jar
~~~

The next step is then to execute the jar which I somehow didn't realise until I unpacked it and had a look at the README:


~~~text

java -jar jdk-6u23-fcs-src-b05-jrl-12_nov_2010.jar
~~~

You get asked to choose a folder location for the sources and then the code is under 'src/share/classes'. So for me I need to give IntelliJ a source path of :


~~~text

/Users/mneedham/github/j2se/src/share/classes
~~~

You can browse the different versions of the source code by changing the version number at the end of URLs like <a href="http://download.java.net/jdk6/6u23/">this one</a>. At the moment version 23 is the latest one available.
