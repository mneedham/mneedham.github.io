+++
draft = false
date="2012-01-07 17:14:41"
title="Learning Android: java.lang.OutOfMemoryError: Java heap space with android-maven-plugin"
tag=['android']
category=['Android']
+++

I've been trying to adapt my Android application to fit into the structure of the <a href="https://github.com/pivotal/RobolectricSample#readme">RobolectricSample</a> so that I can add some tests around my code but I was running into a problem when trying to deploy the application.

To deploy the application you need to run the following command:


~~~text

mvn package android:deploy
~~~

Which was resulting in the following error:


~~~text

[INFO] UNEXPECTED TOP-LEVEL ERROR:
[INFO] java.lang.OutOfMemoryError: Java heap space
[INFO] 	at com.android.dx.rop.code.PlainInsn.withNewRegisters(PlainInsn.java:152)
[INFO] 	at com.android.dx.ssa.NormalSsaInsn.toRopInsn(NormalSsaInsn.java:121)
[INFO] 	at com.android.dx.ssa.back.SsaToRop.convertInsns(SsaToRop.java:342)
[INFO] 	at com.android.dx.ssa.back.SsaToRop.convertBasicBlock(SsaToRop.java:323)
[INFO] 	at com.android.dx.ssa.back.SsaToRop.convertBasicBlocks(SsaToRop.java:260)
[INFO] 	at com.android.dx.ssa.back.SsaToRop.convert(SsaToRop.java:124)
[INFO] 	at com.android.dx.ssa.back.SsaToRop.convertToRopMethod(SsaToRop.java:70)
[INFO] 	at com.android.dx.ssa.Optimizer.optimize(Optimizer.java:102)
[INFO] 	at com.android.dx.ssa.Optimizer.optimize(Optimizer.java:73)
~~~

I'd added a few dependencies to the original pom.xml file so I figured on of those must be causing the problem and eventually narrowed it down to be the twitter4j-core library which I had defined like this in the pom.xml file:


~~~xml

<dependency>
  <groupId>org.twitter4j</groupId>
  <artifactId>twitter4j-core</artifactId>
  <version>[2.2,)</version>
</dependency>
~~~

I found a bug report for the <a href="http://code.google.com/p/maven-android-plugin/issues/detail?id=146">maven-android-plugin</a> which suggested that <a href="http://www.caucho.com/resin-3.0/performance/jvm-tuning.xtp">increasing the heap size</a> might solve the problem.

That section of the pom.xml file ended up looking like this:


~~~xml

<plugin>
  <groupId>com.jayway.maven.plugins.android.generation2</groupId>
  <artifactId>android-maven-plugin</artifactId>
  <version>3.0.0-alpha-13</version>
  <configuration>
    <sdk>
      <platform>10</platform>
      <path>/path/to/android-sdk</path>                
    </sdk>
    <dex>                                
      <jvmArguments>
        <jvmArgument>-Xms256m</jvmArgument>                                        
        <jvmArgument>-Xmx512m</jvmArgument>
      </jvmArguments>                        
    </dex>
    <undeployBeforeDeploy>true</undeployBeforeDeploy>
  </configuration>
  <extensions>true</extensions>
</plugin>
~~~

That seemed to get rid of the problem but I also tried changing the plugin version to the latest one and that seemed to solve the problem as well without the need to add the JVM arguments:


~~~xml

<plugin>
  <groupId>com.jayway.maven.plugins.android.generation2</groupId>
  <artifactId>android-maven-plugin</artifactId>
  <configuration>
    <sdk>
      <platform>10</platform>
      <path>/path/to/android-sdk</path>                
    </sdk>
    <undeployBeforeDeploy>true</undeployBeforeDeploy>
  </configuration>
  <extensions>true</extensions>
</plugin>
~~~

The latest version is 3.0.2 from what I can tell.
