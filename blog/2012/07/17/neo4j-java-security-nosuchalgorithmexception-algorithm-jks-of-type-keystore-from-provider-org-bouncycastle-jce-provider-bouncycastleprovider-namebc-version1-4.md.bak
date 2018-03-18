+++
draft = false
date="2012-07-17 00:02:51"
title="neo4j: java.security.NoSuchAlgorithmException: Algorithm [JKS] of type [KeyStore] from provider [org.bouncycastle.jce.provider.BouncyCastleProvider: name=BC version=1.4]"
tag=['neo4j']
category=['neo4j']
+++

I've spent the last couple of hours moving my neo4j graph from my own machine onto a vanilla CentOS VM and initially tried to run neo using a non Sun version of Java which I installed like so:


~~~text

yum install java
~~~

This is the version of Java that was installed:


~~~text

$ java -version
java version "1.5.0"
gij (GNU libgcj) version 4.4.6 20120305 (Red Hat 4.4.6-4)
~~~

When I tried to start neo4j:


~~~text

neo4j/bin/neo4j start
~~~

I ended up with the following exception in the neo4j log @ <cite>neo4j/data/log/neo4j.0.0.log</cite>:


~~~text

Caused by: java.security.NoSuchAlgorithmException: Algorithm [JKS] of type [KeyStore] 
from provider [org.bouncycastle.jce.provider.BouncyCastleProvider: name=BC version=1.4] is not found
~~~

I assumed this algorithm was only being packaged with the Sun JDK (although <a href="http://www.bouncycastle.org/java.html">the website suggests otherwise</a>) so I'd need to replace my version of Java to get it working.

I got the 64 bit '.bin' file from the Oracle download page and then installed it using rpm:


~~~text

rpm -ivh jdk-6u33-linux-x64-rpm.bin 
~~~

I now have this version of Java installed and neo4j is much happier:


~~~text

java -version
java version "1.6.0_33"
Java(TM) SE Runtime Environment (build 1.6.0_33-b04)
Java HotSpot(TM) 64-Bit Server VM (build 20.8-b03, mixed mode)
~~~

After googling around for a bit I'm still not entirely sure why it wasn't able to work with the original version of Java I installed so if anyone could point me in the direction that'd be useful.
