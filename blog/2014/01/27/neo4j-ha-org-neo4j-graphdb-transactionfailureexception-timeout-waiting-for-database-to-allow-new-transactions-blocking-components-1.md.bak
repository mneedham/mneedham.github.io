+++
draft = false
date="2014-01-27 09:42:18"
title="Neo4j HA: org.neo4j.graphdb.TransactionFailureException: Timeout waiting for database to allow new transactions. Blocking components (1): []"
tag=['neo4j']
category=['neo4j']
+++

<p>As I <a href="http://www.markhneedham.com/blog/2014/01/24/neo4j-ha-election-could-not-pick-a-winner/">mentioned in my previous post</a>, I've been spending quite a bit of time working with Neo4j HA and recently came across the following exception in <cite>data/graph.db/messages.log</cite>:</p>



~~~text

org.neo4j.graphdb.TransactionFailureException: Timeout waiting for database to allow new transactions. Blocking components (1): []
	at org.neo4j.kernel.ha.HighlyAvailableGraphDatabase.beginTx(HighlyAvailableGraphDatabase.java:199)
	at org.neo4j.kernel.TransactionBuilderImpl.begin(TransactionBuilderImpl.java:43)
	at org.neo4j.kernel.InternalAbstractGraphDatabase.beginTx(InternalAbstractGraphDatabase.java:949)
	at org.neo4j.server.rest.transactional.TransactionalRequestDispatcher.dispatch(TransactionalRequestDispatcher.java:52)
	at com.sun.jersey.server.impl.uri.rules.HttpMethodRule.accept(HttpMethodRule.java:288)
	at com.sun.jersey.server.impl.uri.rules.ResourceClassRule.accept(ResourceClassRule.java:108)
	at com.sun.jersey.server.impl.uri.rules.RightHandPathRule.accept(RightHandPathRule.java:147)
	at com.sun.jersey.server.impl.uri.rules.RootResourceClassesRule.accept(RootResourceClassesRule.java:84)
	at com.sun.jersey.server.impl.application.WebApplicationImpl._handleRequest(WebApplicationImpl.java:1469)
	at com.sun.jersey.server.impl.application.WebApplicationImpl._handleRequest(WebApplicationImpl.java:1400)
	at com.sun.jersey.server.impl.application.WebApplicationImpl.handleRequest(WebApplicationImpl.java:1349)
	at com.sun.jersey.server.impl.application.WebApplicationImpl.handleRequest(WebApplicationImpl.java:1339)
	at com.sun.jersey.spi.container.servlet.WebComponent.service(WebComponent.java:416)
	at com.sun.jersey.spi.container.servlet.ServletContainer.service(ServletContainer.java:537)
	at com.sun.jersey.spi.container.servlet.ServletContainer.service(ServletContainer.java:699)
	at javax.servlet.http.HttpServlet.service(HttpServlet.java:848)
	at org.eclipse.jetty.servlet.ServletHolder.handle(ServletHolder.java:698)
	at org.eclipse.jetty.servlet.ServletHandler$CachedChain.doFilter(ServletHandler.java:1506)
	at org.neo4j.server.rest.security.SecurityFilter.doFilter(SecurityFilter.java:112)
	at org.eclipse.jetty.servlet.ServletHandler$CachedChain.doFilter(ServletHandler.java:1477)
	at org.eclipse.jetty.servlet.ServletHandler.doHandle(ServletHandler.java:503)
	at org.eclipse.jetty.server.session.SessionHandler.doHandle(SessionHandler.java:211)
	at org.eclipse.jetty.server.handler.ContextHandler.doHandle(ContextHandler.java:1096)
	at org.eclipse.jetty.servlet.ServletHandler.doScope(ServletHandler.java:432)
	at org.eclipse.jetty.server.session.SessionHandler.doScope(SessionHandler.java:175)
	at org.eclipse.jetty.server.handler.ContextHandler.doScope(ContextHandler.java:1030)
	at org.eclipse.jetty.server.handler.ScopedHandler.handle(ScopedHandler.java:136)
	at org.eclipse.jetty.server.handler.HandlerList.handle(HandlerList.java:52)
	at org.eclipse.jetty.server.handler.HandlerWrapper.handle(HandlerWrapper.java:97)
	at org.eclipse.jetty.server.Server.handle(Server.java:445)
	at org.eclipse.jetty.server.HttpChannel.handle(HttpChannel.java:268)
	at org.eclipse.jetty.server.HttpConnection.onFillable(HttpConnection.java:229)
	at org.eclipse.jetty.io.AbstractConnection$ReadCallback.run(AbstractConnection.java:358)
	at org.eclipse.jetty.util.thread.QueuedThreadPool.runJob(QueuedThreadPool.java:601)
	at org.eclipse.jetty.util.thread.QueuedThreadPool$3.run(QueuedThreadPool.java:532)
	at java.lang.Thread.run(Thread.java:744)
~~~

<p>I traced the error message back to <a href="https://github.com/neo4j/neo4j/blob/master/community/kernel/src/main/java/org/neo4j/kernel/AvailabilityGuard.java#L212">AvailabilityGuard#describeWhoIsBlocking</a> and discovered that this error message is thrown when we don't want the cluster to accept transactions.</p>


<p>Usually the blocking component (the thing that's stopping transactions from being accepted) is described but in this case the error message indicates that the cluster hasn't been formed.</p>


<p>I was able to reproduce the error message by trying to commit a transaction from a slave in a cluster which was misconfigured so that the slaves were unable to interact with the master.</p>


<p>To find the root cause for this error message we need to scroll up the log a bit and look for the exception that happened immediately before this one. In this case we see the following:</p>



~~~text

2014-01-24 11:48:53.889+0000 WARN  [o.n.k.h.c.HighAvailabilityModeSwitcher]: Consistency checker failed
org.neo4j.com.ComException: MasterClient20 could not connect to /10.137.62.4:6001
	at org.neo4j.com.Client$1.create(Client.java:141) ~[neo4j-com-2.0.0.jar:2.0.0]
	at org.neo4j.com.Client$1.create(Client.java:123) ~[neo4j-com-2.0.0.jar:2.0.0]
	at org.neo4j.com.ResourcePool.acquire(ResourcePool.java:175) ~[neo4j-com-2.0.0.jar:2.0.0]
	at org.neo4j.com.Client.getChannel(Client.java:336) ~[neo4j-com-2.0.0.jar:2.0.0]
	at org.neo4j.com.Client.sendRequest(Client.java:216) ~[neo4j-com-2.0.0.jar:2.0.0]
	at org.neo4j.kernel.ha.MasterClient20.getMasterIdForCommittedTx(MasterClient20.java:359) ~[neo4j-ha-2.0.0.jar:2.0.0]
	at org.neo4j.kernel.ha.cluster.HighAvailabilityModeSwitcher.checkDataConsistencyWithMaster(HighAvailabilityModeSwitcher.java:679) [neo4j-ha-2.0.0.jar:2.0.0]
	at org.neo4j.kernel.ha.cluster.HighAvailabilityModeSwitcher.checkDataConsistency(HighAvailabilityModeSwitcher.java:498) [neo4j-ha-2.0.0.jar:2.0.0]
	at org.neo4j.kernel.ha.cluster.HighAvailabilityModeSwitcher.access$900(HighAvailabilityModeSwitcher.java:110) [neo4j-ha-2.0.0.jar:2.0.0]
	at org.neo4j.kernel.ha.cluster.HighAvailabilityModeSwitcher$2.run(HighAvailabilityModeSwitcher.java:393) [neo4j-ha-2.0.0.jar:2.0.0]
	at java.util.concurrent.Executors$RunnableAdapter.call(Executors.java:471) [na:1.7.0_51]
	at java.util.concurrent.FutureTask.run(FutureTask.java:262) [na:1.7.0_51]
	at java.util.concurrent.ScheduledThreadPoolExecutor$ScheduledFutureTask.access$201(ScheduledThreadPoolExecutor.java:178) [na:1.7.0_51]
	at java.util.concurrent.ScheduledThreadPoolExecutor$ScheduledFutureTask.run(ScheduledThreadPoolExecutor.java:292) [na:1.7.0_51]
	at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1145) [na:1.7.0_51]
	at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:615) [na:1.7.0_51]
	at java.lang.Thread.run(Thread.java:744) [na:1.7.0_51]
~~~

<p>A quick configuration change was able to get me going again but you could also see this error message if firewall rules were misconfigured so that's something else to look out for.</p>

