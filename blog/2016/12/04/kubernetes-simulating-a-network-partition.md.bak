+++
draft = false
date="2016-12-04 12:37:49"
title="Kubernetes: Simulating a network partition"
tag=['neo4j', 'kubernetes']
category=['neo4j', 'Kubernetes']
+++

<p>A couple of weeks ago I wrote <a href="http://www.markhneedham.com/blog/2016/11/25/kubernetes-spinning-up-a-neo4j-3-1-causal-cluster/">a post explaining how to create a Neo4j causal cluster using Kubernetes</a> and ... the I wanted to work out how to simulate a network partition which would put the leader on the minority side and force an election.
</p>


<p>
We've done this on our internal tooling on AWS using the <cite><a href="https://en.wikipedia.org/wiki/Iptables">iptables</a></cite> command but unfortunately that isn't available in my container, which only has the utilities provided by <a href="https://busybox.net/about.html">BusyBox</a>.
</p>


<p>Luckily one of these is <cite>route</cite> command which will allow us to achieve the same thing.</p>


<p>
To recap, I have 3 Neo4j pods up and running:
</p>



~~~bash

$ kubectl get pods
NAME      READY     STATUS    RESTARTS   AGE
neo4j-0   1/1       Running   0          6h
neo4j-1   1/1       Running   0          6h
neo4j-2   1/1       Running   0          6h
~~~

<p>And we can check that the <cite>route</cite> command is available:</p>



~~~bash

$ kubectl exec neo4j-0 -- ls -alh /sbin/route 
lrwxrwxrwx    1 root     root          12 Oct 18 18:58 /sbin/route -> /bin/busybox
~~~

<p>Let's have a look what role each server is currently playing:</p>



~~~bash

$ kubectl exec neo4j-0 -- bin/cypher-shell "CALL dbms.cluster.role()"
role
"FOLLOWER"

Bye!
~~~


~~~bash

$ kubectl exec neo4j-1 -- bin/cypher-shell "CALL dbms.cluster.role()"
role
"FOLLOWER"

Bye!
~~~


~~~bash

$ kubectl exec neo4j-2 -- bin/cypher-shell "CALL dbms.cluster.role()"
role
"LEADER"

Bye!
~~~


<p>
Slight aside: I'm able to call <cite>cypher-shell</cite> without a user and password because I've disable authorisation by putting the following in <cite>conf/neo4j.conf</cite>:
</p>



~~~text

dbms.connector.bolt.enabled=true
~~~

<p>
Back to the network partitioning...we need to partition away <cite>neo4j-2</cite> from the other two servers which we can do by running the following commands:
</p>



~~~bash

$ kubectl exec neo4j-2 -- route add -host neo4j-0.neo4j.default.svc.cluster.local reject && \
  kubectl exec neo4j-2 -- route add -host neo4j-1.neo4j.default.svc.cluster.local reject && \
  kubectl exec neo4j-0 -- route add -host neo4j-2.neo4j.default.svc.cluster.local reject && \
  kubectl exec neo4j-1 -- route add -host neo4j-2.neo4j.default.svc.cluster.local reject
~~~

<p>If we look at the logs of neo4j-2 we can see that it's stepped down after being disconnected from the other two servers:
</p>



~~~text

$ kubectl exec neo4j-2 -- cat logs/debug.log
...
2016-12-04 11:30:10.186+0000 INFO  [o.n.c.c.c.RaftMachine] Moving to FOLLOWER state after not receiving heartbeat responses in this election timeout period. Heartbeats received: []
...
~~~

<p>
Who's taken over as leader?
</p>



~~~bash

$ kubectl exec neo4j-0 -- bin/cypher-shell "CALL dbms.cluster.role()"
role
"LEADER"

Bye!
~~~


~~~bash

$ kubectl exec neo4j-1 -- bin/cypher-shell "CALL dbms.cluster.role()"
role
"FOLLOWER"

Bye!
~~~


~~~bash

$ kubectl exec neo4j-2 -- bin/cypher-shell "CALL dbms.cluster.role()"
role
"FOLLOWER"

Bye!
~~~

<p>Looks like neo4j-0! Let's put some data into the database:</p>
 


~~~bash

$ kubectl exec neo4j-0 -- bin/cypher-shell "CREATE (:Person {name: 'Mark'})"
Added 1 nodes, Set 1 properties, Added 1 labels

Bye!
~~~

<p>Let's check if that node made it to the other two servers. We'd expect it to be on neo4j-1 but not on neo4j-2:</p>



~~~bash

$ kubectl exec neo4j-1 -- bin/cypher-shell "MATCH (p:Person) RETURN p"
p
(:Person {name: "Mark"})

Bye!
~~~


~~~bash

$ kubectl exec neo4j-2 -- bin/cypher-shell "MATCH (p:Person) RETURN p"


Bye!
~~~

<p>On neo4j-2 we'll repeatedly see these types of entries in the log as its election timeout triggers but fails to get any responses to the vote requests it sends out:</p>




~~~text

$ kubectl exec neo4j-2 -- cat logs/debug.log
...
2016-12-04 11:32:56.735+0000 INFO  [o.n.c.c.c.RaftMachine] Election timeout triggered
2016-12-04 11:32:56.736+0000 INFO  [o.n.c.c.c.RaftMachine] Election started with vote request: Vote.Request from MemberId{ca9b954c} {term=11521, candidate=MemberId{ca9b954c}, lastAppended=68, lastLogTerm=11467} and members: [MemberId{484178c4}, MemberId{0acdb8dd}, MemberId{ca9b954c}]
...
~~~

<p>We can see those vote requests by looking at the <cite>raft-messages.log</cite> which can be enabled by setting the following property in <cite>conf/neo4j.conf</cite>:</p>



~~~text

causal_clustering.raft_messages_log_enable=true
~~~


~~~text

$ kubectl exec neo4j-2 -- cat logs/raft-messages.log
...
11:33:42.101 -->MemberId{484178c4}: Request: Vote.Request from MemberId{ca9b954c} {term=11537, candidate=MemberId{ca9b954c}, lastAppended=68, lastLogTerm=11467}
11:33:42.102 -->MemberId{0acdb8dd}: Request: Vote.Request from MemberId{ca9b954c} {term=11537, candidate=MemberId{ca9b954c}, lastAppended=68, lastLogTerm=11467}

11:33:45.432 -->MemberId{484178c4}: Request: Vote.Request from MemberId{ca9b954c} {term=11538, candidate=MemberId{ca9b954c}, lastAppended=68, lastLogTerm=11467}
11:33:45.433 -->MemberId{0acdb8dd}: Request: Vote.Request from MemberId{ca9b954c} {term=11538, candidate=MemberId{ca9b954c}, lastAppended=68, lastLogTerm=11467}

11:33:48.362 -->MemberId{484178c4}: Request: Vote.Request from MemberId{ca9b954c} {term=11539, candidate=MemberId{ca9b954c}, lastAppended=68, lastLogTerm=11467}
11:33:48.362 -->MemberId{0acdb8dd}: Request: Vote.Request from MemberId{ca9b954c} {term=11539, candidate=MemberId{ca9b954c}, lastAppended=68, lastLogTerm=11467}
...
~~~

<p>
To 'heal' the network partition we just need to delete all the commands we ran earlier:
</p>



~~~bash

$ kubectl exec neo4j-2 -- route delete neo4j-0.neo4j.default.svc.cluster.local reject && \
  kubectl exec neo4j-2 -- route delete neo4j-1.neo4j.default.svc.cluster.local reject && \
  kubectl exec neo4j-0 -- route delete neo4j-2.neo4j.default.svc.cluster.local reject && \
  kubectl exec neo4j-1 -- route delete neo4j-2.neo4j.default.svc.cluster.local reject
~~~

<p>Now let's check that neo4j-2 now has the node that we created earlier:</p>



~~~bash

$ kubectl exec neo4j-2 -- bin/cypher-shell "MATCH (p:Person) RETURN p"
p
(:Person {name: "Mark"})

Bye!
~~~

<p>That's all for now!</p>

