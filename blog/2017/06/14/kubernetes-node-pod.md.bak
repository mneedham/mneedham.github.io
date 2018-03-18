+++
draft = false
date="2017-06-14 08:49:06"
title="Kubernetes: Which node is a pod on?"
tag=['kubernetes']
category=['Kubernetes']
+++

<p>
When running Kubernetes on a cloud provider, rather than locally using <a href="https://github.com/kubernetes/minikube">minikube</a>, it's useful to know which node a pod is running on.
</p>


<p>
The normal command to list pods doesn't contain this information:
</p>



~~~bash

$ kubectl get pod
NAME           READY     STATUS    RESTARTS   AGE       
neo4j-core-0   1/1       Running   0          6m        
neo4j-core-1   1/1       Running   0          6m        
neo4j-core-2   1/1       Running   0          2m        
~~~

<p>
I spent a while searching for a command that I could use before I came across <a href="https://tachingchen.com/blog/Kubernetes-Assigning-Pod-to-Nodes/">Ta-Ching Chen's blog post</a> while looking for something else. 
</p>


<p>
Ta-Ching points out that we just need to add the flag <cite>-o wide</cite> to our original command to get the information we require:
</p>




~~~bash

$ kubectl get pod -o wide
NAME           READY     STATUS    RESTARTS   AGE       IP           NODE
neo4j-core-0   1/1       Running   0          6m        10.32.3.6    gke-neo4j-cluster-default-pool-ded394fa-0kpw
neo4j-core-1   1/1       Running   0          6m        10.32.3.7    gke-neo4j-cluster-default-pool-ded394fa-0kpw
neo4j-core-2   1/1       Running   0          2m        10.32.0.10   gke-neo4j-cluster-default-pool-ded394fa-kp68
~~~

<p>
Easy!
</p>

