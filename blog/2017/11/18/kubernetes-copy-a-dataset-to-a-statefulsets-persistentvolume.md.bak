+++
draft = false
date="2017-11-18 12:44:37"
title="Kubernetes: Copy a dataset to a StatefulSet's PersistentVolume"
tag=['neo4j', 'kubernetes']
category=['neo4j', 'Kubernetes']
description="In this post we'll learn how to copy an existing dataset to the PersistentVolumes used by a Neo4j cluster running on Kubernetes."
+++

<p>
In this post we'll learn how to copy an existing dataset to the <a href="https://kubernetes.io/docs/concepts/storage/persistent-volumes/">PersistentVolumes</a> used by a Neo4j cluster running on <a href="https://kubernetes.io/">Kubernetes</a>.
</p>


<h2>Neo4j Clusters on Kubernetes</h2>

<p>
This posts assumes that we're familiar with deploying Neo4j on Kubernetes. I wrote an article on the Neo4j blog <a href="https://neo4j.com/blog/kubernetes-deploy-neo4j-clusters/">explaining this in more detail</a>.
</p>


<p>
The StatefulSet we create for our core servers require <a href="https://kubernetes.io/docs/concepts/storage/persistent-volumes/">persistent storage</a>, achieved via the PersistentVolumeClaim (PVC) primitive. A Neo4j cluster containing 3 core servers would have the following PVCs:
</p>



~~~bash

$ kubectl get pvc
NAME                            STATUS    VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS   AGE
datadir-neo-helm-neo4j-core-0   Bound     pvc-043efa91-cc54-11e7-bfa5-080027ab9eac   10Gi       RWO            standard       45s
datadir-neo-helm-neo4j-core-1   Bound     pvc-1737755a-cc54-11e7-bfa5-080027ab9eac   10Gi       RWO            standard       13s
datadir-neo-helm-neo4j-core-2   Bound     pvc-18696bfd-cc54-11e7-bfa5-080027ab9eac   10Gi       RWO            standard       11s
~~~

<p>
Each of the PVCs has a corresponding PersistentVolume (PV) that satisifies it:
</p>



~~~bash

$ kubectl get pv
NAME                                       CAPACITY   ACCESS MODES   RECLAIM POLICY   STATUS    CLAIM                                   STORAGECLASS   REASON    AGE
pvc-043efa91-cc54-11e7-bfa5-080027ab9eac   10Gi       RWO            Delete           Bound     default/datadir-neo-helm-neo4j-core-0   standard                 41m
pvc-1737755a-cc54-11e7-bfa5-080027ab9eac   10Gi       RWO            Delete           Bound     default/datadir-neo-helm-neo4j-core-1   standard                 40m
pvc-18696bfd-cc54-11e7-bfa5-080027ab9eac   10Gi       RWO            Delete           Bound     default/datadir-neo-helm-neo4j-core-2   standard                 40m
~~~


<p>
The PVCs and PVs are usually created at the same time that we deploy our StatefulSet. We need to intervene in that lifecycle so that our dataset is already in place before the StatefulSet is deployed.
</p>


<h2>Deploying an existing dataset</h2>

<p>
We can do this by following these steps:
</p>


<ul>

<li>Create PVCs with the above names manually</li>
<li>Attach pods to those PVCs</li>
<li>Copy our dataset onto those pods</li>
<li>Delete the pods</li>
<li>Deploy our Neo4j cluster</li>
</ul>

<p>
We can use the following script to create the PVCs and pods:
</p>


<p>
<cite>pvs.sh</cite>
</p>



~~~shell

#!/usr/bin/env bash

set -exuo pipefail

for i in $(seq 0 2); do
  cat <<EOF | kubectl apply -f -
kind: PersistentVolumeClaim
apiVersion: v1
metadata:
  name: datadir-neo-helm-neo4j-core-${i}
  labels:
    app: neo4j
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 10Gi
EOF

  cat <<EOF | kubectl apply -f -
kind: Pod
apiVersion: v1
metadata:
  name: neo4j-load-data-${i}
  labels:
    app: neo4j-loader
spec:
  volumes:
    - name: datadir-neo4j-core-${i}
      persistentVolumeClaim:
        claimName: datadir-neo-helm-neo4j-core-${i}
  containers:
    - name: neo4j-load-data-${i}
      image: ubuntu
      volumeMounts:
      - name: datadir-neo4j-core-${i}
        mountPath: /data
      command: ["/bin/bash", "-ecx", "while :; do printf '.'; sleep 5 ; done"]
EOF

done;
~~~

<p>
Let's run that script to create our PVCs and pods:
</p>



~~~bash

$ ./pvs.sh 
++ seq 0 2
+ for i in $(seq 0 2)
+ cat
+ kubectl apply -f -
persistentvolumeclaim "datadir-neo-helm-neo4j-core-0" configured
+ cat
+ kubectl apply -f -
pod "neo4j-load-data-0" configured
+ for i in $(seq 0 2)
+ cat
+ kubectl apply -f -
persistentvolumeclaim "datadir-neo-helm-neo4j-core-1" configured
+ cat
+ kubectl apply -f -
pod "neo4j-load-data-1" configured
+ for i in $(seq 0 2)
+ cat
+ kubectl apply -f -
persistentvolumeclaim "datadir-neo-helm-neo4j-core-2" configured
+ cat
+ kubectl apply -f -
pod "neo4j-load-data-2" configured
~~~

<p>
Now we can copy our database onto the pods:
</p>



~~~bash

for i in $(seq 0 2); do
  kubectl cp graph.db.tar.gz neo4j-load-data-${i}:/data/
  kubectl exec neo4j-load-data-${i} -- bash -c "mkdir -p /data/databases && tar -xf  /data/graph.db.tar.gz -C /data/databases"
done
~~~

<p><cite>graph.db.tar.gz</cite> contains a backup from a local database I created:</p>
 


~~~bash

$ tar -tvf graph.db.tar.gz 

drwxr-xr-x  0 markneedham staff       0 24 Jul 15:23 graph.db/
drwxr-xr-x  0 markneedham staff       0 24 Jul 15:23 graph.db/certificates/
drwxr-xr-x  0 markneedham staff       0 17 Feb  2017 graph.db/index/
drwxr-xr-x  0 markneedham staff       0 24 Jul 15:22 graph.db/logs/
-rw-r--r--  0 markneedham staff    8192 24 Jul 15:23 graph.db/neostore
-rw-r--r--  0 markneedham staff     896 24 Jul 15:23 graph.db/neostore.counts.db.a
-rw-r--r--  0 markneedham staff    1344 24 Jul 15:23 graph.db/neostore.counts.db.b
-rw-r--r--  0 markneedham staff       9 24 Jul 15:23 graph.db/neostore.id
-rw-r--r--  0 markneedham staff   65536 24 Jul 15:23 graph.db/neostore.labelscanstore.db
...
-rw-------  0 markneedham staff     1700 24 Jul 15:23 graph.db/certificates/neo4j.key
~~~

<p>
We'll run the following command to check the databases are in place:
</p>



~~~bash

$ kubectl exec neo4j-load-data-0 -- ls -lh /data/databases/
total 4.0K
drwxr-xr-x 6 501 staff 4.0K Jul 24 14:23 graph.db

$ kubectl exec neo4j-load-data-1 -- ls -lh /data/databases/
total 4.0K
drwxr-xr-x 6 501 staff 4.0K Jul 24 14:23 graph.db

$ kubectl exec neo4j-load-data-2 -- ls -lh /data/databases/
total 4.0K
drwxr-xr-x 6 501 staff 4.0K Jul 24 14:23 graph.db
~~~

<p>
All good so far. The pods have done their job so we'll tear those down:</p>



~~~bash

$ kubectl delete pods -l app=neo4j-loader
pod "neo4j-load-data-0" deleted
pod "neo4j-load-data-1" deleted
pod "neo4j-load-data-2" deleted
~~~

<p>
We're now ready to deploy our Neo4j cluster.
</p>



~~~bash

helm install incubator/neo4j --name neo-helm --wait --set authEnabled=false
~~~

<p>
Finally we'll run a Cypher query to check that the Neo4j servers used the database that we uploaded:
</p>



~~~bash

$ kubectl exec neo-helm-neo4j-core-0 -- bin/cypher-shell "match (n) return count(*)"
count(*)
32314

$ kubectl exec neo-helm-neo4j-core-1 -- bin/cypher-shell "match (n) return count(*)"
count(*)
32314

$ kubectl exec neo-helm-neo4j-core-2 -- bin/cypher-shell "match (n) return count(*)"
count(*)
32314
~~~

<p>
Success!</p>


<p>We could achieve similar results by using an <a href="https://kubernetes.io/docs/concepts/workloads/pods/init-containers/">init container</a> but I haven't had a chance to try out that approach yet. If you give it a try let me know in the comments and I'll add it to the post. 
</p>

