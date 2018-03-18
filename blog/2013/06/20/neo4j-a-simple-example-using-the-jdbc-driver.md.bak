+++
draft = false
date="2013-06-20 07:21:46"
title="neo4j: A simple example using the JDBC driver"
tag=['neo4j', 'cypher']
category=['neo4j']
+++

<p><a href="https://twitter.com/mesirii">Michael</a> recently pointed me to the <a href="https://github.com/rickardoberg/neo4j-jdbc">neo4j JDBC driver</a> which he and <a href="https://twitter.com/rickardoberg">Rickard</a> have written so I thought I'd try and port <a href="http://www.markhneedham.com/blog/2013/06/20/neo4jcypher-create-with-optional-properties/">the code from my previous post</a> to use that instead of the console.</p>


<p>To start with I added the following dependencies to my POM file:</p>



~~~xml

    <dependencies>
    ...
        <dependency>
            <groupId>org.neo4j</groupId>
            <artifactId>neo4j-jdbc</artifactId>
            <version>1.9</version>
        </dependency>
    </dependencies>

    <repositories>
        <repository>
            <id>neo4j-maven</id>
            <name>neo4j maven</name>
            <url>http://m2.neo4j.org</url>
        </repository>
    </repositories>
~~~

<p>I then tried to create a connection to a local neo4j server instance that I had running on port 7474:</p>



~~~java

Neo4jConnection connect = new Driver().
  connect("jdbc:neo4j://localhost:7474", new Properties());
~~~

<p>which leads to the following exception:</p>



~~~text

Exception in thread "main" java.lang.NoClassDefFoundError: org/neo4j/cypherdsl/grammar/Execute
	at org.neo4j.jdbc.Driver.<init>(Driver.java:52)
	at org.neo4j.jdbc.Driver.<clinit>(Driver.java:43)
	at com.centrica.bigquery.JDBCTest.main(JDBCTest.java:17)
	at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
	at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:57)
	at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
	at java.lang.reflect.Method.invoke(Method.java:601)
	at com.intellij.rt.execution.application.AppMain.main(AppMain.java:120)
Caused by: java.lang.ClassNotFoundException: org.neo4j.cypherdsl.grammar.Execute
	at java.net.URLClassLoader$1.run(URLClassLoader.java:366)
	at java.net.URLClassLoader$1.run(URLClassLoader.java:355)
	at java.security.AccessController.doPrivileged(Native Method)
	at java.net.URLClassLoader.findClass(URLClassLoader.java:354)
	at java.lang.ClassLoader.loadClass(ClassLoader.java:423)
	at sun.misc.Launcher$AppClassLoader.loadClass(Launcher.java:308)
	at java.lang.ClassLoader.loadClass(ClassLoader.java:356)
	... 8 more
~~~

<p>It turns out we also need to add the following dependency:</p>



~~~xml

        <dependency>
            <groupId>org.neo4j</groupId>
            <artifactId>neo4j-cypher-dsl</artifactId>
            <version>1.9</version>
        </dependency>
~~~

<p>We can now run the following code to create some people and then query for one of them:</p>



~~~java

Neo4jConnection connect = new Driver().
  connect("jdbc:neo4j://localhost:7474", new Properties());

List<String> dataLoad = new ArrayList<String>();
dataLoad.add("CREATE (person1 { personId: 1, started: 1361708546 })");
dataLoad.add("CREATE (person2 { personId: 2, started: 1361708546, left: 1371708646 })");
dataLoad.add("CREATE (company { companyId: 1 })");

connect.createStatement().executeQuery(StringUtils.join(dataLoad, "\n"));

ResultSet resultSet = connect.createStatement().
  executeQuery("START person1 = node:node_auto_index('personId:1') RETURN person1");

if(resultSet.next()) {
    Map<String, Object> e = (Map<String, Object>) resultSet.getObject("person1");
    System.out.println("personId: " + e.get("personId") + ", started: " + e.get("started"));
}
~~~

<p>which gives the following output:</p>



~~~text

Connecting to URL http://localhost:7474
Starting the Apache HTTP client
Executing query: START person1 = node:node_auto_index('personId:1') RETURN person1
 with params{}
Starting the Apache HTTP client
personId: 1, started: 1361708546
~~~

<p>I haven't done much more with it but JDBC seems like quite a neat integration point because so many other understand that API.</p>

