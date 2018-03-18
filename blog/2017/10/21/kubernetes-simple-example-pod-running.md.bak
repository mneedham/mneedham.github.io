+++
draft = false
date="2017-10-21 10:06:55"
title="Kubernetes: Simple example of pod running"
tag=['bash', 'kubernetes']
category=['Kubernetes']
+++

<p>
I recently needed to create a Kubernetes pod that would 'just sit there' while I used <cite>kube cp</cite> to copy some files to a persistent volume to which it was bound.
</p>


<p>I started out with this naive pod spec:</p>


<p>
<cite>pod_no_while.yaml</cite>
</p>



~~~yaml

kind: Pod
apiVersion: v1
metadata:
  name: marks-dummy-pod
spec:
  containers:
    - name: marks-dummy-pod
      image: ubuntu
  restartPolicy: Never    

~~~

<p>Let's apply that template:</p>



~~~bash

$ kubectl apply -f pod_no_while.yaml 
pod "marks-dummy-pod" created
~~~

<p>
And let's check if we have any running pods:
</p>



~~~bash

$ kubectl get pods
No resources found, use --show-all to see completed objects.
~~~

<p>
We won't see anything here because unsurprisingly the pod has run to completion as there's nothing to keep it running! We can confirm that by running this command:</p>



~~~bash

$ kubectl get pods --show-all
NAME              READY     STATUS      RESTARTS   AGE
marks-dummy-pod   0/1       Completed   0          1m
~~~

<p>
Now let's create a pod that has an infinite bash while loop:
</p>


<p>
<cite>pod.yaml</cite>
</p>




~~~yaml

kind: Pod
apiVersion: v1
metadata:
  name: marks-dummy-pod
spec:
  containers:
    - name: marks-dummy-pod
      image: ubuntu
      command: ["/bin/bash", "-ec", "while :; do echo '.'; sleep 5 ; done"]
  restartPolicy: Never

~~~

<p>Let's apply that one instead:</p>



~~~bash

$ kubectl apply -f pod.yaml 
The Pod "marks-dummy-pod" is invalid: spec: Forbidden: pod updates may not change fields other than `spec.containers[*].image`, `spec.initContainers[*].image`, `spec.activeDeadlineSeconds` or `spec.tolerations` (only additions to existing tolerations)
~~~

<p>
Oops, we need to delete it first so let's do that:
</p>



~~~bash

$ kubectl delete pod marks-dummy-pod
pod "marks-dummy-pod" deleted
~~~

<p>Attempt #2:</p>



~~~bash

$ kubectl apply -f pod.yaml 
pod "marks-dummy-pod" created
~~~

<p>And let's checkup on our pod:</p>



~~~bash

$ kubectl get pods
NAME              READY     STATUS    RESTARTS   AGE
marks-dummy-pod   1/1       Running   0          14s
~~~

<p>Looks better already. Let's check the logs</p>



~~~bash

$ kubectl logs marks-dummy-pod 
.
.
~~~

<p>
Great! We can now <cite>kubectl cp</cite> to our heart's content and then delete the pod aftewards.
</p>

