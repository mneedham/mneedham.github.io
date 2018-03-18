+++
draft = false
date="2013-09-14 00:06:37"
title="jackson-core-asl - java.lang.AbstractMethodError: org.codehaus.jackson.JsonNode.getValueAsText()Ljava/lang/String;"
tag=['software-development', 'java']
category=['Java']
+++

<p><a href="https://twitter.com/iansrobinson">Ian</a> and I were doing a bit of work on an internal application which processes JSON messages and interacts with AWS and we started seeing the following exception after doing an upgrade of <cite><a href="http://mvnrepository.com/artifact/org.codehaus.jackson/jackson-mapper-asl">jackson-mapper-asl</a></cite> from 1.8.9 to 1.9.13:</p>



~~~text

2013-09-13 11:01:50 +0000: Exception while handling {MessageId: 7e695fb3-549a-4b
40-b1cf-9dbc5e97a8df, ... }
java.lang.AbstractMethodError: org.codehaus.jackson.JsonNode.getValueAsText()Lja
va/lang/String;                                                                 
...                                                                
        at com.amazonaws.services.sqs.AmazonSQSAsyncClient$20.call(AmazonSQSAsyn
cClient.java:1200)                                                              
        at com.amazonaws.services.sqs.AmazonSQSAsyncClient$20.call(AmazonSQSAsyn
cClient.java:1191)                                                              
        at java.util.concurrent.FutureTask$Sync.innerRun(FutureTask.java:334)   
        at java.util.concurrent.FutureTask.run(FutureTask.java:166)             
        at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.
java:1145)                                                                      
        at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor
.java:615)                                                                      
        at java.lang.Thread.run(Thread.java:724) 
~~~

<p>I'd not seen this exception before but we figured that it was probably happening because we had <a href="http://stackoverflow.com/questions/14954738/runtime-exception-with-jersey-java-lang-abstractmethoderror">conflicting versions of some Jackson related JAR on the class path</a>.</p>


<p>We could see in the external libraries section of IntelliJ that we had both the 1.8.9 and 1.9.13 versions of jackson-mapper-asl but we weren't sure which dependency was pulling in the earlier version.</p>


<p><a href="https://twitter.com/apcj">Alistair</a> pointed out quite a neat command you can pass to Maven which shows transitive dependencies so we gave that a try:</p>



~~~bash

$ mvn dependency:tree
...
[INFO] --- maven-dependency-plugin:2.1:tree (default-cli) @ load-generator ---
[INFO] +- com.amazonaws:aws-java-sdk:jar:1.5.6:compile
[INFO] |  +- commons-logging:commons-logging:jar:1.1.1:compile
[INFO] |  +- org.apache.httpcomponents:httpclient:jar:4.2.2:compile (version managed from 4.2)
[INFO] |  +- commons-codec:commons-codec:jar:1.6:compile
[INFO] |  \- org.codehaus.jackson:jackson-core-asl:jar:1.8.9:compile
...
[INFO] +- org.codehaus.jackson:jackson-mapper-asl:jar:1.9.13:compile
[INFO] |   \- org.codehaus.jackson:jackson-core-asl:jar:1.9.13:compile
...
~~~

<p>As you can see, we have two different versions of the <cite>json-core-asl</cite> JAR and the earlier version was being pulled in by the <cite>aws-java-sdk</cite>. We <a href="http://maven.40175.n5.nabble.com/Force-higher-version-dependency-td90566.html">excluded its transitive dependency</a> by changing our pom file to read like this:


~~~xml

    <dependency>
      <groupId>com.amazonaws</groupId>
      <artifactId>aws-java-sdk</artifactId>
      <version>1.5.6</version>

      <exclusions>
        <exclusion>
          <groupId>org.codehaus.jackson</groupId>
          <artifactId>jackson-core-asl</artifactId>
        </exclusion>
      </exclusions>
    </dependency>
~~~

<p>After that everything worked swimmingly.</p>

