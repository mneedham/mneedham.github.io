+++
draft = false
date="2013-06-19 05:32:50"
title="neo4j: WrappingNeoServerBootstrapper and the case of the /webadmin 404"
tag=['neo4j']
category=['neo4j']
+++

<p>When people first use neo4j they frequently start out by <a href="http://docs.neo4j.org/chunked/stable/tutorials-java-embedded.html">embedding it in a Java application</a> but eventually they want to explore the graph in a more visual way.</p>
 

<p>One simple way to do this is to start neo4j in server mode and use the web console.</p>


<p>Our initial code might read like this:</p>



~~~java

public class GraphMeUp {
    public static void main(String[] args) {
        GraphDatabaseService graphDb = new EmbeddedGraphDatabase("/path/to/data/graph.db");
    }
}
~~~

<p>or:</p>



~~~java

public class GraphMeUp {
    public static void main(String[] args) {
        GraphDatabaseService graphDb = new GraphDatabaseFactory().
          newEmbeddedDatabaseBuilder("/path/to/data/graph.db").
          newGraphDatabase();
    }
}
~~~

<p>And to start our graph up in server mode we can use the <cite><a href="http://components.neo4j.org/neo4j-server/1.9/apidocs/org/neo4j/server/WrappingNeoServerBootstrapper.html">WrappingNeoServerBootstrapper</a></cite> class which is packaged in neo4j-server so we first need to add that dependency:</p>



~~~xml

 <dependency>
    <groupId>org.neo4j.app</groupId>
    <artifactId>neo4j-server</artifactId>
    <version>1.9</version>
</dependency>
~~~


~~~java

public class GraphMeUp {
    public static void main(String[] args) {
        GraphDatabaseService graphDb = new GraphDatabaseFactory().
          newEmbeddedDatabaseBuilder("/path/to/data/graph.db").
          newGraphDatabase();

        new WrappingNeoServerBootstrapper((GraphDatabaseAPI)graphDb).start();
    }
}
~~~

<p>If we then browse to http://localhost:7474/webadmin/ we'll be greeted by a 404 error:</p>



~~~text

HTTP ERROR 404

Problem accessing /webadmin/. Reason:

    Not Found
Powered by Jetty://
~~~

<p>sad panda :(<p>

<p>Until I came across <a href="http://stackoverflow.com/questions/8111959/use-wrappingneoserverbootstrapper-with-spring-data-neo4j">this post on StackOverflow by Michael</a> I didn't realise that there's actually another dependency that we need to include to get the web admin goodness!</p>


<p>To get things worked as we'd expect we need to include the following dependency:</p>



~~~xml

<dependency>
    <groupId>org.neo4j.app</groupId>
    <artifactId>neo4j-server</artifactId>
    <version>1.9</version>
    <type>jar</type>
    <classifier>static-web</classifier>
    <scope>compile</scope>
</dependency>
~~~

<p>I hadn't come across the <cite>classifier</cite> attribute before but what this does is include the following JAR:</p>



~~~bash

$ ls -alh  ~/.m2/repository/org/neo4j/app/neo4j-server/1.9/neo4j-server-1.9-static-web.jar
-rw-r--r--  1 markhneedham  staff   3.5M 17 Jun 11:28 /Users/markhneedham/.m2/repository/org/neo4j/app/neo4j-server/1.9/neo4j-server-1.9-static-web.jar
~~~

<p>If we run our code again we should see the bright and cheery web admin interface and all is good with the world.</p>

