+++
draft = false
date="2014-11-30 08:21:54"
title="Spark: Write to CSV file with header using saveAsFile"
tag=['spark-2']
category=['Spark']
+++

<p>In my last blog post I showed <a href="http://www.markhneedham.com/blog/2014/11/30/spark-write-to-csv-file/">how to write to a single CSV file using Spark and Hadoop</a> and the next thing I wanted to do was add a header row to the resulting row.</p>


<p>
Hadoop's <cite><a href="https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileUtil.html#copyMerge(org.apache.hadoop.fs.FileSystem, org.apache.hadoop.fs.Path, org.apache.hadoop.fs.FileSystem, org.apache.hadoop.fs.Path, boolean, org.apache.hadoop.conf.Configuration, java.lang.String)">FileUtil#copyMerge</a></cite> function does take a String parameter but it adds this text to the end of each partition file which isn't quite what we want.
</p>


<p>However, if we copy that function into our own FileUtil class we can restructure it to do what we want:</p>



~~~java

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.*;
import org.apache.hadoop.io.IOUtils;
import java.io.IOException;

public class MyFileUtil {
    public static boolean copyMergeWithHeader(FileSystem srcFS, Path srcDir, FileSystem dstFS, Path dstFile, boolean deleteSource, Configuration conf, String header) throws IOException {
        dstFile = checkDest(srcDir.getName(), dstFS, dstFile, false);
        if(!srcFS.getFileStatus(srcDir).isDir()) {
            return false;
        } else {
            FSDataOutputStream out = dstFS.create(dstFile);
            if(header != null) {
                out.write((header + "\n").getBytes("UTF-8"));
            }

            try {
                FileStatus[] contents = srcFS.listStatus(srcDir);

                for(int i = 0; i < contents.length; ++i) {
                    if(!contents[i].isDir()) {
                        FSDataInputStream in = srcFS.open(contents[i].getPath());

                        try {
                            IOUtils.copyBytes(in, out, conf, false);

                        } finally {
                            in.close();
                        }
                    }
                }
            } finally {
                out.close();
            }

            return deleteSource?srcFS.delete(srcDir, true):true;
        }
    }

    private static Path checkDest(String srcName, FileSystem dstFS, Path dst, boolean overwrite) throws IOException {
        if(dstFS.exists(dst)) {
            FileStatus sdst = dstFS.getFileStatus(dst);
            if(sdst.isDir()) {
                if(null == srcName) {
                    throw new IOException("Target " + dst + " is a directory");
                }

                return checkDest((String)null, dstFS, new Path(dst, srcName), overwrite);
            }

            if(!overwrite) {
                throw new IOException("Target " + dst + " already exists");
            }
        }
        return dst;
    }
}
~~~

<p>We can then update our merge function to call this instead:</p>



~~~scala

def merge(srcPath: String, dstPath: String, header:String): Unit =  {
  val hadoopConfig = new Configuration()
  val hdfs = FileSystem.get(hadoopConfig)
  MyFileUtil.copyMergeWithHeader(hdfs, new Path(srcPath), hdfs, new Path(dstPath), false, hadoopConfig, header)
}
~~~

<p>We call merge from our code like this:</p>



~~~scala

merge(file, destinationFile, "type,count")
~~~

<p>
I wasn't sure how to import my Java based class into the Spark shell so I compiled the code into a JAR and submitted it as a job instead:</p>



~~~bash

$ sbt package
[info] Loading global plugins from /Users/markneedham/.sbt/0.13/plugins
[info] Loading project definition from /Users/markneedham/projects/spark-play/playground/project
[info] Set current project to playground (in build file:/Users/markneedham/projects/spark-play/playground/)
[info] Compiling 3 Scala sources to /Users/markneedham/projects/spark-play/playground/target/scala-2.10/classes...
[info] Packaging /Users/markneedham/projects/spark-play/playground/target/scala-2.10/playground_2.10-1.0.jar ...
[info] Done packaging.
[success] Total time: 8 s, completed 30-Nov-2014 08:12:26

$ time ./bin/spark-submit --class "WriteToCsvWithHeader" --master local[4] /path/to/playground/target/scala-2.10/playground_2.10-1.0.jar
Spark assembly has been built with Hive, including Datanucleus jars on classpath
Using Spark's default log4j profile: org/apache/spark/log4j-defaults.propertie
...
14/11/30 08:16:15 INFO TaskSchedulerImpl: Removed TaskSet 2.0, whose tasks have all completed, from pool
14/11/30 08:16:15 INFO SparkContext: Job finished: saveAsTextFile at WriteToCsvWithHeader.scala:49, took 0.589036 s

real	0m13.061s
user	0m38.977s
sys	0m3.393s
~~~

<p>And if we look at our destination file:</p>



~~~bash

$ cat /tmp/singlePrimaryTypes.csv
type,count
THEFT,859197
BATTERY,757530
NARCOTICS,489528
CRIMINAL DAMAGE,488209
BURGLARY,257310
OTHER OFFENSE,253964
ASSAULT,247386
MOTOR VEHICLE THEFT,197404
ROBBERY,157706
DECEPTIVE PRACTICE,137538
CRIMINAL TRESPASS,124974
PROSTITUTION,47245
WEAPONS VIOLATION,40361
PUBLIC PEACE VIOLATION,31585
OFFENSE INVOLVING CHILDREN,26524
CRIM SEXUAL ASSAULT,14788
SEX OFFENSE,14283
GAMBLING,10632
LIQUOR LAW VIOLATION,8847
ARSON,6443
INTERFERE WITH PUBLIC OFFICER,5178
HOMICIDE,4846
KIDNAPPING,3585
INTERFERENCE WITH PUBLIC OFFICER,3147
INTIMIDATION,2471
STALKING,1985
OFFENSES INVOLVING CHILDREN,355
OBSCENITY,219
PUBLIC INDECENCY,86
OTHER NARCOTIC VIOLATION,80
RITUALISM,12
NON-CRIMINAL,12
OTHER OFFENSE ,6
NON - CRIMINAL,2
NON-CRIMINAL (SUBJECT SPECIFIED),2
~~~

<p>Happy days!</p>


<p>The code is available as a <a href="https://gist.github.com/mneedham/881ee5dcb58456855174">gist</a> if you want to see all the details.</p>

