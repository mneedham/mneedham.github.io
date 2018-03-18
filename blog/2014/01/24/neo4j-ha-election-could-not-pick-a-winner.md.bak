+++
draft = false
date="2014-01-24 10:30:41"
title="Neo4j HA: Election could not pick a winner"
tag=['neo4j']
category=['neo4j']
+++

<p>Recently I've been spending a reasonable chunk of my time helping people get up and running with their <a href="http://docs.neo4j.org/chunked/stable/ha-setup-tutorial.html">Neo4j High Availability cluster</a> and there's sometimes confusion around how it should be configured.</p>


<p>A Neo4j cluster typically consists of a master and two slaves and you'd usually have it configured so that any machine can be the master.</p>


<p>However, there is a <a href="http://docs.neo4j.org/chunked/stable/ha-configuration.html">configuration parameter</a> 'ha.slave_only' which can be set to 'true' to ensure that a machine will never be elected as master when an election takes place.</p>


<p>We might configure our machine with that setting if it's acting as a reporting instance but we need to make sure that 2 members don't have that setting otherwise we won't have any failover in the cluster.</p>


<p>For example, if we set two of the machines in the cluster to be slave only and then stop the master we'll see output similar to the following in <cite>data/graph.db/messages.log</cite>:</p>



~~~text

2014-01-23 11:17:24.510+0000 INFO  [o.n.c.p.a.m.MultiPaxosContext$ElectionContextImpl]: Doing elections for role coordinator
2014-01-23 11:17:24.510+0000 DEBUG [o.n.c.p.e.ElectionState$2]: ElectionState: election-[performRoleElections]->election from:cluster://10.239.8.251:5001 conversation-id:3/13#
2014-01-23 11:17:24.513+0000 DEBUG [o.n.c.p.e.ElectionState$2]: ElectionState: election-[vote:coordinator]->election from:cluster://10.151.24.237:5001 conversation-id:3/13#
2014-01-23 11:17:24.515+0000 DEBUG [o.n.c.p.e.ElectionState$2]: ElectionState: election-[voted]->election from:cluster://10.138.29.197:5001 conversation-id:3/13#
2014-01-23 11:17:24.516+0000 DEBUG [o.n.c.p.e.ElectionState$2]: ElectionState: election-[voted]->election from:cluster://10.151.24.237:5001 conversation-id:3/13#
2014-01-23 11:17:24.519+0000 DEBUG [o.n.c.p.a.m.MultiPaxosContext$ElectionContextImpl$2]: Elections ended up with list []
2014-01-23 11:17:24.519+0000 WARN  [o.n.c.p.e.ElectionState]: Election could not pick a winner
~~~

<p>This message initially looks confusing but what it's telling us is that the cluster was unable to elect a new master, in this case because there were no machines that could be elected as master.</p>


<p>So if you see that message in your logs, check your config to make sure that there are actually machines to choose from.</p>

