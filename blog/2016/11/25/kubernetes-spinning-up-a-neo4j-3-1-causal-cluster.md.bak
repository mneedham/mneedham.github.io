+++
draft = false
date="2016-11-25 16:55:56"
title="Kubernetes: Spinning up a Neo4j 3.1 Causal Cluster"
tag=['neo4j', 'kubernetes']
category=['neo4j']
+++

<p>
A couple of weeks ago I wrote a blog post explaining how I'd <a href="http://www.markhneedham.com/blog/2016/11/13/neo4j-3-1-beta3-docker-creating-a-causal-cluster/">created a Neo4j causal cluster using docker containers directly</a> and for my next pet project I wanted to use Kubernetes as an orchestration layer so that I could declaratively change the number of servers in my cluster.
</p>


<p>
I'd never used Kubernetes before but I saw a presentation showing how to use it to create an Elastic cluster at the <a href="https://www.meetup.com/gdgcloud/events/233298216/">GDG Cloud meetup a couple of months ago</a>.
</p>


<p>In that presentation I was introduced to the idea of a <a href="http://kubernetes.io/docs/user-guide/petset/">PetSet</a> which is an abstraction exposed by Kubernetes which allows us to manage a set of pods (containers) which have a fixed identity. The documentation explains it better:
</p>


<blockquote>
A PetSet ensures that a specified number of “pets” with unique identities are running at any given time. The identity of a Pet is comprised of:

<ul>
<li>a stable hostname, available in DNS</li>
<li>an ordinal index</li>
<li>stable storage: linked to the ordinal & hostname</li>
</ul>

</blockquote>

<p>In my case I need to have a stable hostname because each member of a Neo4j cluster is given a list of other cluster members with which it can create a new cluster or join an already existing one. This is the first use case described in the documentation:</p>


<blockquote>
PetSet also helps with the 2 most common problems encountered managing such clustered applications:
<ul>
<li>discovery of peers for quorum</li>
<li>startup/teardown ordering</li>
</ul>
</blockquote>

<p>
So the first thing we need to do is create some stable storage for our pods to use. 
</p>


<p>We'll create a cluster of 3 members so we need to create one <a href="http://kubernetes.io/docs/user-guide/persistent-volumes/">PersistentVolume</a> for each of them. The following script does the job:
</p>


<p><cite>volumes.sh</cite></p>



~~~text

for i in $(seq 0 2); do
  cat <<EOF | kubectl create -f -
kind: PersistentVolume
apiVersion: v1
metadata:
  name: pv${i}
  labels:
    type: local
    app: neo4j
spec:
  capacity:
    storage: 1Gi
  accessModes:
    - ReadWriteOnce
  hostPath:
    path: "/tmp/${i}"
EOF

  cat <<EOF | kubectl create -f -
kind: PersistentVolumeClaim
apiVersion: v1
metadata:
  name: datadir-neo4j-${i}
  labels:
    app: neo4j
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 1Gi
EOF
done;
~~~

<p>
If we run this script it'll create 3 volumes which we can see by running the following command:
</p>



~~~bash

$ kubectl get pv
NAME      CAPACITY   ACCESSMODES   STATUS    CLAIM                     REASON    AGE
pv0       1Gi        RWO           Bound     default/datadir-neo4j-0             7s
pv1       1Gi        RWO           Bound     default/datadir-neo4j-1             7s
pv2       1Gi        RWO           Bound     default/datadir-neo4j-2             7s
~~~


~~~bash

$ kubectl get pvc
NAME              STATUS    VOLUME    CAPACITY   ACCESSMODES   AGE
datadir-neo4j-0   Bound     pv0       1Gi        RWO           26s
datadir-neo4j-1   Bound     pv1       1Gi        RWO           26s
datadir-neo4j-2   Bound     pv2       1Gi        RWO           25s
~~~

<p>
Next we need to create a PetSet template. After a lot of iterations I ended up with the following:
</p>



~~~text

# Headless service to provide DNS lookup
apiVersion: v1
kind: Service
metadata:
  labels:
    app: neo4j
  name: neo4j
spec:
  clusterIP: None
  ports:
    - port: 7474
  selector:
    app: neo4j
----
# new API name
apiVersion: "apps/v1alpha1"
kind: PetSet
metadata:
  name: neo4j
spec:
  serviceName: neo4j
  replicas: 3
  template:
    metadata:
      annotations:
        pod.alpha.kubernetes.io/initialized: "true"
        pod.beta.kubernetes.io/init-containers: '[
            {
                "name": "install",
                "image": "gcr.io/google_containers/busybox:1.24",
                "command": ["/bin/sh", "-c", "echo \"
                unsupported.dbms.edition=enterprise\n
                dbms.mode=CORE\n
                dbms.connectors.default_advertised_address=$HOSTNAME.neo4j.default.svc.cluster.local\n
                dbms.connectors.default_listen_address=0.0.0.0\n
                dbms.connector.bolt.type=BOLT\n
                dbms.connector.bolt.enabled=true\n
                dbms.connector.bolt.listen_address=0.0.0.0:7687\n
                dbms.connector.http.type=HTTP\n
                dbms.connector.http.enabled=true\n
                dbms.connector.http.listen_address=0.0.0.0:7474\n
                causal_clustering.raft_messages_log_enable=true\n
                causal_clustering.initial_discovery_members=neo4j-0.neo4j.default.svc.cluster.local:5000,neo4j-1.neo4j.default.svc.cluster.local:5000,neo4j-2.neo4j.default.svc.cluster.local:5000\n
                causal_clustering.leader_election_timeout=2s\n
                  \" > /work-dir/neo4j.conf" ],
                "volumeMounts": [
                    {
                        "name": "confdir",
                        "mountPath": "/work-dir"
                    }
                ]
            }
        ]'
      labels:
        app: neo4j
    spec:
      containers:
      - name: neo4j
        image: "neo4j/neo4j-experimental:3.1.0-M13-beta3-enterprise"
        imagePullPolicy: Always
        ports:
        - containerPort: 5000
          name: discovery
        - containerPort: 6000
          name: tx
        - containerPort: 7000
          name: raft
        - containerPort: 7474
          name: browser
        - containerPort: 7687
          name: bolt
        securityContext:
          privileged: true
        volumeMounts:
        - name: datadir
          mountPath: /data
        - name: confdir
          mountPath: /conf
      volumes:
      - name: confdir
  volumeClaimTemplates:
  - metadata:
      name: datadir
      annotations:
        volume.alpha.kubernetes.io/storage-class: anything
    spec:
      accessModes: [ "ReadWriteOnce" ]
      resources:
        requests:
          storage: 1Gi
~~~

<p>The main thing I had trouble with was getting the members of the cluster to talk to each other. The default docker config uses hostnames but I found that pods were unable to contact each other unless I specified the FQDN in the config file. We can run the following command to create the PetSet:</p>



~~~bash

$ kubectl create -f neo4j.yaml 
service "neo4j" created
petset "neo4j" created
~~~

<p>We can check if the pods are up and running by executing the following command:</p>



~~~bash

$ kubectl get pods
NAME      READY     STATUS    RESTARTS   AGE
neo4j-0   1/1       Running   0          2m
neo4j-1   1/1       Running   0          14s
neo4j-2   1/1       Running   0          10s
~~~

<p>And we can tail neo4j's log files like this:</p>



~~~bash

$ kubectl logs neo4j-0
Starting Neo4j.
2016-11-25 16:39:50.333+0000 INFO  Starting...
2016-11-25 16:39:51.723+0000 INFO  Bolt enabled on 0.0.0.0:7687.
2016-11-25 16:39:51.733+0000 INFO  Initiating metrics...
2016-11-25 16:39:51.911+0000 INFO  Waiting for other members to join cluster before continuing...
2016-11-25 16:40:12.074+0000 INFO  Started.
2016-11-25 16:40:12.428+0000 INFO  Mounted REST API at: /db/manage
2016-11-25 16:40:13.350+0000 INFO  Remote interface available at http://neo4j-0.neo4j.default.svc.cluster.local:7474/
~~~


~~~bash

$ kubectl logs neo4j-1
Starting Neo4j.
2016-11-25 16:39:53.846+0000 INFO  Starting...
2016-11-25 16:39:56.212+0000 INFO  Bolt enabled on 0.0.0.0:7687.
2016-11-25 16:39:56.225+0000 INFO  Initiating metrics...
2016-11-25 16:39:56.341+0000 INFO  Waiting for other members to join cluster before continuing...
2016-11-25 16:40:16.623+0000 INFO  Started.
2016-11-25 16:40:16.951+0000 INFO  Mounted REST API at: /db/manage
2016-11-25 16:40:17.607+0000 INFO  Remote interface available at http://neo4j-1.neo4j.default.svc.cluster.local:7474/
~~~


~~~bash

$ kubectl logs neo4j-2
Starting Neo4j.
2016-11-25 16:39:57.828+0000 INFO  Starting...
2016-11-25 16:39:59.166+0000 INFO  Bolt enabled on 0.0.0.0:7687.
2016-11-25 16:39:59.176+0000 INFO  Initiating metrics...
2016-11-25 16:39:59.329+0000 INFO  Waiting for other members to join cluster before continuing...
2016-11-25 16:40:19.216+0000 INFO  Started.
2016-11-25 16:40:19.675+0000 INFO  Mounted REST API at: /db/manage
2016-11-25 16:40:21.029+0000 INFO  Remote interface available at http://neo4j-2.neo4j.default.svc.cluster.local:7474/
~~~

<p>
I wanted to log into the servers from my host machine's browser so I setup port forwarding for each of the servers:
</p>



~~~bash

$ kubectl port-forward neo4j-0 7474:7474 7687:7687
~~~

<p>
We can then get an overview of the cluster by running the following procedure:
</p>



~~~bash

CALL dbms.cluster.overview()

╒════════════════════════════════════╤═════════════════════════════════════════════════════╤════════╕
│id                                  │addresses                                            │role    │
╞════════════════════════════════════╪═════════════════════════════════════════════════════╪════════╡
│81d8e5e2-02db-4414-85de-a7025b346e84│[bolt://neo4j-0.neo4j.default.svc.cluster.local:7687,│LEADER  │
│                                    │ http://neo4j-0.neo4j.default.svc.cluster.local:7474]│        │
├────────────────────────────────────┼─────────────────────────────────────────────────────┼────────┤
│347b7517-7ca0-4b92-b9f0-9249d46b2ad3│[bolt://neo4j-1.neo4j.default.svc.cluster.local:7687,│FOLLOWER│
│                                    │ http://neo4j-1.neo4j.default.svc.cluster.local:7474]│        │
├────────────────────────────────────┼─────────────────────────────────────────────────────┼────────┤
│a5ec1335-91ce-4358-910b-8af9086c2969│[bolt://neo4j-2.neo4j.default.svc.cluster.local:7687,│FOLLOWER│
│                                    │ http://neo4j-2.neo4j.default.svc.cluster.local:7474]│        │
└────────────────────────────────────┴─────────────────────────────────────────────────────┴────────┘
~~~

<p>So far so good. What if we want to have 5 servers in the cluster instead of 3? We can run the following command to increase our replica size:</p>



~~~bash

$ kubectl patch petset neo4j -p '{"spec":{"replicas":5}}'
"neo4j" patched
~~~

<p>
Let's run that procedure again:
</p>



~~~bash

CALL dbms.cluster.overview()

╒════════════════════════════════════╤═════════════════════════════════════════════════════╤════════╕
│id                                  │addresses                                            │role    │
╞════════════════════════════════════╪═════════════════════════════════════════════════════╪════════╡
│81d8e5e2-02db-4414-85de-a7025b346e84│[bolt://neo4j-0.neo4j.default.svc.cluster.local:7687,│LEADER  │
│                                    │ http://neo4j-0.neo4j.default.svc.cluster.local:7474]│        │
├────────────────────────────────────┼─────────────────────────────────────────────────────┼────────┤
│347b7517-7ca0-4b92-b9f0-9249d46b2ad3│[bolt://neo4j-1.neo4j.default.svc.cluster.local:7687,│FOLLOWER│
│                                    │ http://neo4j-1.neo4j.default.svc.cluster.local:7474]│        │
├────────────────────────────────────┼─────────────────────────────────────────────────────┼────────┤
│a5ec1335-91ce-4358-910b-8af9086c2969│[bolt://neo4j-2.neo4j.default.svc.cluster.local:7687,│FOLLOWER│
│                                    │ http://neo4j-2.neo4j.default.svc.cluster.local:7474]│        │
├────────────────────────────────────┼─────────────────────────────────────────────────────┼────────┤
│28613d06-d4c5-461c-b277-ddb3f05e5647│[bolt://neo4j-3.neo4j.default.svc.cluster.local:7687,│FOLLOWER│
│                                    │ http://neo4j-3.neo4j.default.svc.cluster.local:7474]│        │
├────────────────────────────────────┼─────────────────────────────────────────────────────┼────────┤
│2eaa0058-a4f3-4f07-9f22-d310562ad1ec│[bolt://neo4j-4.neo4j.default.svc.cluster.local:7687,│FOLLOWER│
│                                    │ http://neo4j-4.neo4j.default.svc.cluster.local:7474]│        │
└────────────────────────────────────┴─────────────────────────────────────────────────────┴────────┘
~~~

<p>Neat! And it's as easy to go back down to 3 again:</p>



~~~bash

$ kubectl patch petset neo4j -p '{"spec":{"replicas":3}}'
"neo4j" patched
~~~


~~~bash

CALL dbms.cluster.overview()

╒════════════════════════════════════╤══════════════════════════════════════════════════════╤════════╕
│id                                  │addresses                                             │role    │
╞════════════════════════════════════╪══════════════════════════════════════════════════════╪════════╡
│81d8e5e2-02db-4414-85de-a7025b346e84│[bolt://neo4j-0.neo4j.default.svc.cluster.local:7687, │LEADER  │
│                                    │http://neo4j-0.neo4j.default.svc.cluster.local:7474]  │        │
├────────────────────────────────────┼──────────────────────────────────────────────────────┼────────┤
│347b7517-7ca0-4b92-b9f0-9249d46b2ad3│[bolt://neo4j-1.neo4j.default.svc.cluster.local:7687, │FOLLOWER│
│                                    │http://neo4j-1.neo4j.default.svc.cluster.local:7474]  │        │
├────────────────────────────────────┼──────────────────────────────────────────────────────┼────────┤
│a5ec1335-91ce-4358-910b-8af9086c2969│[bolt://neo4j-2.neo4j.default.svc.cluster.local:7687, │FOLLOWER│
│                                    │http://neo4j-2.neo4j.default.svc.cluster.local:7474]  │        │
└────────────────────────────────────┴──────────────────────────────────────────────────────┴────────┘
~~~

<p>
Next I need to look at how we can add read replicas into the cluster. These don't take part in the membership/quorum algorithm so I think I'll be able to use the more common ReplicationController/Pod architecture for those. 
</p>


<p>
If you want to play around with this <a href="https://gist.github.com/mneedham/abd2e28e9ce3ce736ccc5895c7cfda6a">the code is available as a gist</a>. I'm using the <a href="https://github.com/kubernetes/minikube">minikube library</a> for all my experiments but I'll hopefully get around to trying this on GCE or AWS soon.
</p>

