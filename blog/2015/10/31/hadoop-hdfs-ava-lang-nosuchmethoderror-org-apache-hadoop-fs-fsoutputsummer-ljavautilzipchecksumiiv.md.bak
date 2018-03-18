+++
draft = false
date="2015-10-31 23:58:22"
title="Hadoop: HDFS - ava.lang.NoSuchMethodError: org.apache.hadoop.fs.FSOutputSummer.<init>(Ljava/util/zip/Checksum;II)V"
tag=['hadoop', 'hdfs']
category=['Software Development']
+++

<p>I wanted to write a little program to check that one machine could communicate a HDFS server running on the other and adapted <a href="https://wiki.apache.org/hadoop/HadoopDfsReadWriteExample">some code from the Hadoop wiki</a> as follows:</p>



~~~java

package org.playground;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FSDataInputStream;
import org.apache.hadoop.fs.FSDataOutputStream;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;

import java.io.IOException;

public class HadoopDFSFileReadWrite {

    static void printAndExit(String str) {
        System.err.println( str );
        System.exit(1);
    }

    public static void main (String[] argv) throws IOException {
        Configuration conf = new Configuration();
        conf.addResource(new Path("/Users/markneedham/Downloads/core-site.xml"));

        FileSystem fs = FileSystem.get(conf);

        Path inFile = new Path("hdfs://192.168.0.11/user/markneedham/explore.R");
        Path outFile = new Path("hdfs://192.168.0.11/user/markneedham/output-" + System.currentTimeMillis());

        // Check if input/output are valid
        if (!fs.exists(inFile))
            printAndExit("Input file not found");
        if (!fs.isFile(inFile))
            printAndExit("Input should be a file");
        if (fs.exists(outFile))
            printAndExit("Output already exists");

        // Read from and write to new file
        byte buffer[] = new byte[256];
        try ( FSDataInputStream in = fs.open( inFile ); FSDataOutputStream out = fs.create( outFile ) )
        {
            int bytesRead = 0;
            while ( (bytesRead = in.read( buffer )) > 0 )
            {
                out.write( buffer, 0, bytesRead );
            }
        }
        catch ( IOException e )
        {
            System.out.println( "Error while copying file" );
        }
    }
}
~~~

<p>
I initially thought I only had the following in my POM file:
</p>



~~~xml

<dependency>
    <groupId>org.apache.hadoop</groupId>
    <artifactId>hadoop-common</artifactId>
    <version>2.7.0</version>
</dependency>
~~~

<p>But when I ran the script I got the following exception:</p>



~~~text

Exception in thread "main" java.lang.NoSuchMethodError: org.apache.hadoop.fs.FSOutputSummer.<init>(Ljava/util/zip/Checksum;II)V
	at org.apache.hadoop.hdfs.DFSOutputStream.<init>(DFSOutputStream.java:1553)
	at org.apache.hadoop.hdfs.DFSOutputStream.<init>(DFSOutputStream.java:1582)
	at org.apache.hadoop.hdfs.DFSOutputStream.newStreamForCreate(DFSOutputStream.java:1614)
	at org.apache.hadoop.hdfs.DFSClient.create(DFSClient.java:1465)
	at org.apache.hadoop.hdfs.DFSClient.create(DFSClient.java:1390)
	at org.apache.hadoop.hdfs.DistributedFileSystem$6.doCall(DistributedFileSystem.java:394)
	at org.apache.hadoop.hdfs.DistributedFileSystem$6.doCall(DistributedFileSystem.java:390)
	at org.apache.hadoop.fs.FileSystemLinkResolver.resolve(FileSystemLinkResolver.java:81)
	at org.apache.hadoop.hdfs.DistributedFileSystem.create(DistributedFileSystem.java:390)
	at org.apache.hadoop.hdfs.DistributedFileSystem.create(DistributedFileSystem.java:334)
	at org.apache.hadoop.fs.FileSystem.create(FileSystem.java:909)
	at org.apache.hadoop.fs.FileSystem.create(FileSystem.java:890)
	at org.apache.hadoop.fs.FileSystem.create(FileSystem.java:787)
	at org.apache.hadoop.fs.FileSystem.create(FileSystem.java:776)
	at org.playground.HadoopDFSFileReadWrite.main(HadoopDFSFileReadWrite.java:37)
	at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
	at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)
	at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
	at java.lang.reflect.Method.invoke(Method.java:497)
	at com.intellij.rt.execution.application.AppMain.main(AppMain.java:140)
~~~

<p>From following the stack trace I realised I'd made a mistake and had accidentally pulled in a dependency on hadoop-hdfs 2.4.1. If we don't have the hadoop-hdfs dependency we'd actually see this error instead:</p>



~~~text

Exception in thread "main" java.io.IOException: No FileSystem for scheme: hdfs
	at org.apache.hadoop.fs.FileSystem.getFileSystemClass(FileSystem.java:2644)
	at org.apache.hadoop.fs.FileSystem.createFileSystem(FileSystem.java:2651)
	at org.apache.hadoop.fs.FileSystem.access$200(FileSystem.java:92)
	at org.apache.hadoop.fs.FileSystem$Cache.getInternal(FileSystem.java:2687)
	at org.apache.hadoop.fs.FileSystem$Cache.get(FileSystem.java:2669)
	at org.apache.hadoop.fs.FileSystem.get(FileSystem.java:371)
	at org.apache.hadoop.fs.FileSystem.get(FileSystem.java:170)
	at org.playground.HadoopDFSFileReadWrite.main(HadoopDFSFileReadWrite.java:22)
	at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
	at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)
	at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
	at java.lang.reflect.Method.invoke(Method.java:497)
	at com.intellij.rt.execution.application.AppMain.main(AppMain.java:140)
~~~

<p>Now let's add the correct version of the dependency and make sure it all works as expected:</p>



~~~xml

<dependency>
    <groupId>org.apache.hadoop</groupId>
    <artifactId>hadoop-hdfs</artifactId>
    <version>2.7.0</version>
    <exclusions>
        <exclusion>
            <groupId>ch.qos.logback</groupId>
            <artifactId>logback-classic</artifactId>
        </exclusion>
        <exclusion>
            <groupId>javax.servlet</groupId>
            <artifactId>servlet-api</artifactId>
        </exclusion>
    </exclusions>
</dependency>
~~~

<p>When we run that a new file is created in HDFS on the other machine with the current timestamp:</p>



~~~bash

$ date +%s000
1446336801000

$ hdfs dfs -ls
...
-rw-r--r--   3 markneedham supergroup       9249 2015-11-01 00:13 output-1446337098257
...
~~~
