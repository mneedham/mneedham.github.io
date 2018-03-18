+++
draft = false
date="2013-10-20 11:13:54"
title="Neo4j: Accessing JMX beans via HTTP"
tag=['neo4j']
category=['neo4j']
+++

<p>One of the additional features that Neo4j enterprise provides is access to various <a href="http://docs.neo4j.org/chunked/milestone/jmx-remote.html">JMX properties</a> which describe <a href="http://docs.neo4j.org/chunked/stable/jmx-mxbeans.html">various aspects</a> of the database.</p>


<p>These would typically be accessed by using <a href="http://docs.oracle.com/javase/6/docs/technotes/guides/management/jconsole.html">jConsole</a> or similar but some monitoring tools aren't able to use the JMX hook and a HTTP interface would work better.</p>


<p>Luckily Neo4j server does expose the JMX beans and we can get a list of URIs to query by hitting the following URI:</p>



~~~bash

$ curl -H "Content-Type:application/json" http://localhost:7474/db/manage/server/jmx/
{
  "resources" : {
    "kernelquery" : "http://localhost:7474/db/manage/server/jmx/kernelquery",
    "bean" : "http://localhost:7474/db/manage/server/jmx/domain/{domain}/{objectName}",
    "query" : "http://localhost:7474/db/manage/server/jmx/query",
    "domains" : "http://localhost:7474/db/manage/server/jmx/domain",
    "domain" : "http://localhost:7474/db/manage/server/jmx/domain/{domain}"
  }
}
~~~

<p>If we want to get the output for all JMX beans we can hit the following URI:</p>



~~~bash

$ curl -H "Content-Type:application/json" http://localhost:7474/db/manage/server/jmx/domain/*/*
// cut for verbosity
...
{
  "description" : "Estimates of the numbers of different kinds of Neo4j primitives",
  "name" : "org.neo4j:instance=kernel#0,name=Primitive count",
  "attributes" : [ {
    "description" : "An estimation of the number of nodes used in this Neo4j instance",
    "name" : "NumberOfNodeIdsInUse",
    "value" : 24117,
    "isReadable" : "true",
    "type" : "long",
    "isWriteable" : "false ",
    "isIs" : "false "
  }, {
    "description" : "An estimation of the number of relationships used in this Neo4j instance",
    "name" : "NumberOfRelationshipIdsInUse",
    "value" : 1,
    "isReadable" : "true",
    "type" : "long",
    "isWriteable" : "false ",
    "isIs" : "false "
  }, {
    "description" : "An estimation of the number of properties used in this Neo4j instance",
    "name" : "NumberOfPropertyIdsInUse",
    "value" : 19078,
    "isReadable" : "true",
    "type" : "long",
    "isWriteable" : "false ",
    "isIs" : "false "
  }, {
    "description" : "The number of relationship types used in this Neo4j instance",
    "name" : "NumberOfRelationshipTypeIdsInUse",
    "value" : 0,
    "isReadable" : "true",
    "type" : "long",
    "isWriteable" : "false ",
    "isIs" : "false "
  } ],
  "url" : "org.neo4j/instance%3Dkernel%230%2Cname%3DPrimitive+count"
}
...
~~~

<p>If we only wanted to return the the numbers of different kinds of Neo4j primitives we could run the following query which uses the name returned by the previous query:</p>



~~~bash

$ curl -H "Content-Type:application/json" -d '["org.neo4j:name=Primitive count,instance=*"]' http://localhost:7474/db/manage/server/jmx/query
[ {
  "description" : "Estimates of the numbers of different kinds of Neo4j primitives",
  "name" : "org.neo4j:instance=kernel#0,name=Primitive count",
  "attributes" : [ {
    "description" : "An estimation of the number of nodes used in this Neo4j instance",
    "name" : "NumberOfNodeIdsInUse",
    "value" : 24117,
    "isReadable" : "true",
    "type" : "long",
    "isWriteable" : "false ",
    "isIs" : "false "
  }],
...
  "url" : "org.neo4j/instance%3Dkernel%230%2Cname%3DPrimitive+count"
} ]
~~~

<p>We could also use the following URI if we don't want to/can't send a POST body:</p>



~~~bash

$ curl -H "Content-Type:application/json" http://localhost:7474/db/manage/server/jmx/domain/org.neo4j/instance%3Dkernel%230%2Cname%3DPrimitive+count
[ {
  "description" : "Estimates of the numbers of different kinds of Neo4j primitives",
  "name" : "org.neo4j:instance=kernel#0,name=Primitive count",
  "attributes" : [ {
    "description" : "An estimation of the number of nodes used in this Neo4j instance",
    "name" : "NumberOfNodeIdsInUse",
    "value" : 24117,
    "isReadable" : "true",
    "type" : "long",
    "isWriteable" : "false ",
    "isIs" : "false "
  }],
...
  "url" : "org.neo4j/instance%3Dkernel%230%2Cname%3DPrimitive+count"
} ]
~~~
