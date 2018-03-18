+++
draft = false
date="2017-11-17 18:10:28"
title="Kubernetes 1.8: Using Cronjobs to take Neo4j backups"
tag=['neo4j', 'kubernetes', 'cronjob', 'backup']
category=['neo4j', 'Kubernetes']
description="Learn how to take backups of Neo4j clusters deployed on Kubernetes using the Cronjob feature released in Kubernetes 1.8."
+++

<p>
With the <a href="http://blog.kubernetes.io/2017/09/kubernetes-18-security-workloads-and.html">release of Kubernetes 1.8</a> Cronjobs have graduated to beta, which means we can now more easily run Neo4j backup jobs against Kubernetes clusters.
</p>


<p>Before we learn how to write a Cronjob let's first create a local Kubernetes cluster and deploy Neo4j.</p>


<h2>Spinup Kubernetes & Helm</h2>


~~~bash

minikube start --memory 8192
helm init && kubectl rollout status -w deployment/tiller-deploy --namespace=kube-system
~~~

<h2>Deploy a Neo4j cluster</h2>


~~~bash

helm repo add incubator https://kubernetes-charts-incubator.storage.googleapis.com/
helm install incubator/neo4j --name neo-helm --wait --set authEnabled=false,core.extraVars.NEO4J_dbms_backup_address=0.0.0.0:6362
~~~

<h2>Populate our cluster with data</h2>

<p>We can run the following command to check our cluster is ready:</p>



~~~bash

kubectl exec neo-helm-neo4j-core-0 \
  -- bin/cypher-shell --format verbose \
  "CALL dbms.cluster.overview() YIELD id, role RETURN id, role"

+-----------------------------------------------------+
| id                                     | role       |
+-----------------------------------------------------+
| "0b3bfe6c-6a68-4af5-9dd2-e96b564df6e5" | "LEADER"   |
| "09e9bee8-bdc5-4e95-926c-16ea8213e6e7" | "FOLLOWER" |
| "859b9b56-9bfc-42ae-90c3-02cedacfe720" | "FOLLOWER" |
+-----------------------------------------------------+
~~~

<p>
Now let's create some data:
</p>



~~~bash

kubectl exec neo-helm-neo4j-core-0 \
  -- bin/cypher-shell --format verbose \
  "UNWIND range(0,1000) AS id CREATE (:Person {id: id})"

0 rows available after 653 ms, consumed after another 0 ms
Added 1001 nodes, Set 1001 properties, Added 1001 labels
~~~

<p>
Now that our Neo4j cluster is running and contains data we want to take regular backups. 
</p>


<h2>Neo4j backups</h2>

<p>
The <a href="https://neo4j.com/docs/operations-manual/current/backup/perform-backup/">Neo4j backup tool</a> supports full and incremental backups.
</p>


<h3>Full backup</h3>

<p>
A full backup streams a copy of the store files to the backup location and any transactions that happened during the backup. Those transactions are then applied to the backed up copy of the database.
</p>


<h3>Incremental backup</h3>

<p>
An incremental backup is triggered if there is already a Neo4j database in the backup location. In this case there will be no copying of store files. Instead the tool will copy any new transactions from Neo4j and apply them to the backup.
</p>


<h3>Backup Cronjob</h3>

<p>
We will use a <a href="https://kubernetes.io/docs/concepts/workloads/controllers/cron-jobs/">Cronjob</a> to execute a backup. In the example below we attach a PersistentVolumeClaim to our Cronjob so that we can see both of the backup scenarios in action.
</p>



~~~yaml

kind: PersistentVolumeClaim
apiVersion: v1
metadata:
  name: backupdir-neo4j
  labels:
    app: neo4j-backup
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 10Gi
---
apiVersion: batch/v1beta1
kind: CronJob
metadata:
  name: neo4j-backup
spec:
  schedule: "*/1 * * * *"
  jobTemplate:
    spec:
      template:
        spec:
          volumes:
            - name: backupdir-neo4j
              persistentVolumeClaim:
                claimName: backupdir-neo4j
          containers:
            - name: neo4j-backup
              image: neo4j:3.3.0-enterprise
              env:
                - name: NEO4J_ACCEPT_LICENSE_AGREEMENT
                  value: "yes"
              volumeMounts:
              - name: backupdir-neo4j
                mountPath: /tmp
              command: ["bin/neo4j-admin",  "backup", "--backup-dir", "/tmp", "--name", "backup", "--from", "neo-helm-neo4j-core-2.neo-helm-neo4j.default.svc.cluster.local:6362"]
          restartPolicy: OnFailure
~~~

<p>

</p>



~~~bash

$ kubectl apply -f cronjob.yaml 
cronjob "neo4j-backup" created
~~~


~~~bash

kubectl get jobs -w
NAME                      DESIRED   SUCCESSFUL   AGE
neo4j-backup-1510940940   1         1            34s
~~~

<p>
Now let's view the logs from the job:
</p>



~~~bash

kubectl logs $(kubectl get pods -a --selector=job-name=neo4j-backup-1510940940 --output=jsonpath={.items..metadata.name})

Doing full backup...
2017-11-17 17:49:05.920+0000 INFO [o.n.c.s.StoreCopyClient] Copying neostore.nodestore.db.labels
...
2017-11-17 17:49:06.038+0000 INFO [o.n.c.s.StoreCopyClient] Copied neostore.labelscanstore.db 48.00 kB
2017-11-17 17:49:06.038+0000 INFO [o.n.c.s.StoreCopyClient] Done, copied 18 files
2017-11-17 17:49:06.094+0000 INFO [o.n.b.BackupService] Start recovering store
2017-11-17 17:49:07.669+0000 INFO [o.n.b.BackupService] Finish recovering store
Doing consistency check...
2017-11-17 17:49:07.716+0000 INFO [o.n.k.i.s.f.RecordFormatSelector] Selected RecordFormat:StandardV3_2[v0.A.8] record format from store /tmp/backup
2017-11-17 17:49:07.716+0000 INFO [o.n.k.i.s.f.RecordFormatSelector] Format not configured. Selected format from the store: RecordFormat:StandardV3_2[v0.A.8]
2017-11-17 17:49:07.755+0000 INFO [o.n.m.MetricsExtension] Initiating metrics...
....................  10%
...
.................... 100%
Backup complete.
~~~

<p>
All good so far. Now let's create more data:
</p>



~~~bash

kubectl exec neo-helm-neo4j-core-0 \
  -- bin/cypher-shell --format verbose \
  "UNWIND range(0,1000) AS id CREATE (:Person {id: id})"


0 rows available after 114 ms, consumed after another 0 ms
Added 1001 nodes, Set 1001 properties, Added 1001 labels
~~~

<p>
And wait for another backup job to run:
</p>



~~~bash

kubectl get jobs -w
NAME                      DESIRED   SUCCESSFUL   AGE
neo4j-backup-1510941180   1         1            2m
neo4j-backup-1510941240   1         1            1m
neo4j-backup-1510941300   1         1            17s
~~~


~~~bash

kubectl logs $(kubectl get pods -a --selector=job-name=neo4j-backup-1510941300 --output=jsonpath={.items..metadata.name})

Destination is not empty, doing incremental backup...
Doing consistency check...
2017-11-17 17:55:07.958+0000 INFO [o.n.k.i.s.f.RecordFormatSelector] Selected RecordFormat:StandardV3_2[v0.A.8] record format from store /tmp/backup
2017-11-17 17:55:07.959+0000 INFO [o.n.k.i.s.f.RecordFormatSelector] Format not configured. Selected format from the store: RecordFormat:StandardV3_2[v0.A.8]
2017-11-17 17:55:07.995+0000 INFO [o.n.m.MetricsExtension] Initiating metrics...
....................  10%
...
.................... 100%
Backup complete.
~~~

<p>
If we were to extend this job further we could have it copy each backup it takes to an S3 bucket but I'll leave that for another day.
</p>

