+++
draft = false
date="2013-10-17 06:47:10"
title="neo4j: Setting query timeout"
tag=['neo4j']
category=['neo4j']
+++

<h3>Updated December 2015</h3>

<p>
When I initially wrote this post in 2013 this was an experimental feature that worked using the Neo4j 1.9 series but no longer does in more recent Neo4j versions (2.2, 2.3). The <a href="http://neo4j.com/docs/stable/tutorials-java-embedded-tx-terminate.html">terminating a running transaction</a> page in the docs describes the supported way of terminating queries.
</p>


<p>- - - - - - - - - - -</p>


<p>When I was first learning cypher, neo4j's query language, I frequently wrote queries which traversed the whole graph multiple times and 'hung' for hours as they were evaluated.</p>


<p>At the time I terminated them by restarting the server but I recently learned from an <a href="https://groups.google.com/forum/#!topic/neo4j/5ec8FThLTeo">old post on the mailing list</a> and from my colleague <a href="https://twitter.com/darthvader42">Stefan Armbruster</a> that you can set a query timeout to avoid this problem.</p>


<p>To do this you need to set the following properties:</p>


<p><em>conf/neo4j-server.properties</p>
</em>

~~~text

# timeout in milliseconds
org.neo4j.server.webserver.limit.executiontime=1000
~~~

<p><em>conf/neo4j.properties</p>
</em>

~~~text

execution_guard_enabled=true
~~~

<p>Now if I run a query which takes longer than 1 second to evaluate it will terminate early with the following exception:</p>



~~~bash

$ start n = node(*) return n;
==> GuardTimeoutException: timeout occured (overtime=1718)
~~~

<p>If you want a stricter maximum execution time on a per query basis you can do so by passing the  'max-execution-time' header on the request. e.g.</p>



~~~bash

$ curl -H "Content-Type:application/json" -H "max-execution-time: 500" -X POST -d '{"query" : "start n = node(*) return n"}' http://localhost:7474/db/data/cypher
{
  "message" : "timeout occured (overtime=1)",
  "exception" : "BadInputException",
  "fullname" : "org.neo4j.server.rest.repr.BadInputException",
  "stacktrace" : [ "org.neo4j.server.rest.repr.RepresentationExceptionHandlingIterable.exceptionOnNext(RepresentationExceptionHandlingIterable.java:39)", "org.neo4j.helpers.collection.ExceptionHandlingIterable$1.next(ExceptionHandlingIterable.java:55)", "org.neo4j.helpers.collection.IteratorWrapper.next(IteratorWrapper.java:47)", "org.neo4j.server.rest.repr.ListRepresentation.serialize(ListRepresentation.java:58)", "org.neo4j.server.rest.repr.Serializer.serialize(Serializer.java:75)", "org.neo4j.server.rest.repr.MappingSerializer.putList(MappingSerializer.java:61)", "org.neo4j.server.rest.repr.CypherResultRepresentation.serialize(CypherResultRepresentation.java:83)", "org.neo4j.server.rest.repr.MappingRepresentation.serialize(MappingRepresentation.java:41)", "org.neo4j.server.rest.repr.OutputFormat.assemble(OutputFormat.java:215)", "org.neo4j.server.rest.repr.OutputFormat.formatRepresentation(OutputFormat.java:147)", "org.neo4j.server.rest.repr.OutputFormat.response(OutputFormat.java:130)", "org.neo4j.server.rest.repr.OutputFormat.ok(OutputFormat.java:67)", "org.neo4j.server.rest.web.CypherService.cypher(CypherService.java:101)", "java.lang.reflect.Method.invoke(Method.java:601)", "org.neo4j.server.rest.transactional.TransactionalRequestDispatcher.dispatch(TransactionalRequestDispatcher.java:132)", "org.neo4j.server.rest.security.SecurityFilter.doFilter(SecurityFilter.java:112)", "org.neo4j.server.guard.GuardingRequestFilter.doFilter(GuardingRequestFilter.java:68)", "java.lang.Thread.run(Thread.java:722)" ],
  "cause" : {
    "message" : "timeout occured (overtime=1)",
    "exception" : "GuardTimeoutException",
    "stacktrace" : [ "org.neo4j.kernel.guard.Guard$Timeout.check(Guard.java:132)", "org.neo4j.kernel.guard.Guard.check(Guard.java:43)", "org.neo4j.kernel.InternalAbstractGraphDatabase$4.getNodeByIdOrNull(InternalAbstractGraphDatabase.java:692)", "org.neo4j.kernel.impl.core.NodeManager$3.fetchNextOrNull(NodeManager.java:339)", "org.neo4j.kernel.impl.core.NodeManager$3.fetchNextOrNull(NodeManager.java:326)", "org.neo4j.helpers.collection.PrefetchingIterator.hasNext(PrefetchingIterator.java:55)", "scala.collection.convert.Wrappers$JIteratorWrapper.hasNext(Wrappers.scala:41)", "scala.collection.Iterator$$anon$11.hasNext(Iterator.scala:327)", "scala.collection.Iterator$$anon$13.hasNext(Iterator.scala:371)", "org.neo4j.cypher.internal.ClosingIterator$$anonfun$next$1.apply(ClosingIterator.scala:48)", "org.neo4j.cypher.internal.ClosingIterator$$anonfun$next$1.apply(ClosingIterator.scala:45)", "org.neo4j.cypher.internal.ClosingIterator.failIfThrows(ClosingIterator.scala:91)", "org.neo4j.cypher.internal.ClosingIterator.next(ClosingIterator.scala:45)", "org.neo4j.cypher.PipeExecutionResult.next(PipeExecutionResult.scala:168)", "org.neo4j.cypher.PipeExecutionResult.next(PipeExecutionResult.scala:34)", "scala.collection.Iterator$$anon$11.next(Iterator.scala:328)", "scala.collection.convert.Wrappers$IteratorWrapper.next(Wrappers.scala:30)", "org.neo4j.cypher.PipeExecutionResult$$anon$1.next(PipeExecutionResult.scala:76)", "org.neo4j.helpers.collection.ExceptionHandlingIterable$1.next(ExceptionHandlingIterable.java:53)", "org.neo4j.helpers.collection.IteratorWrapper.next(IteratorWrapper.java:47)", "org.neo4j.server.rest.repr.ListRepresentation.serialize(ListRepresentation.java:58)", "org.neo4j.server.rest.repr.Serializer.serialize(Serializer.java:75)", "org.neo4j.server.rest.repr.MappingSerializer.putList(MappingSerializer.java:61)", "org.neo4j.server.rest.repr.CypherResultRepresentation.serialize(CypherResultRepresentation.java:83)", "org.neo4j.server.rest.repr.MappingRepresentation.serialize(MappingRepresentation.java:41)", "org.neo4j.server.rest.repr.OutputFormat.assemble(OutputFormat.java:215)", "org.neo4j.server.rest.repr.OutputFormat.formatRepresentation(OutputFormat.java:147)", "org.neo4j.server.rest.repr.OutputFormat.response(OutputFormat.java:130)", "org.neo4j.server.rest.repr.OutputFormat.ok(OutputFormat.java:67)", "org.neo4j.server.rest.web.CypherService.cypher(CypherService.java:101)", "java.lang.reflect.Method.invoke(Method.java:601)", "org.neo4j.server.rest.transactional.TransactionalRequestDispatcher.dispatch(TransactionalRequestDispatcher.java:132)", "org.neo4j.server.rest.security.SecurityFilter.doFilter(SecurityFilter.java:112)", "org.neo4j.server.guard.GuardingRequestFilter.doFilter(GuardingRequestFilter.java:68)", "java.lang.Thread.run(Thread.java:722)" ],
    "fullname" : "org.neo4j.kernel.guard.GuardTimeoutException"
  }
}
~~~

<p>At some stage hopefully we'll have the ability to terminate individual queries from the server but for now this is a decent workaround.</p>

