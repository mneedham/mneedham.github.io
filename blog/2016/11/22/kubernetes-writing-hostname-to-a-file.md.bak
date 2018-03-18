+++
draft = false
date="2016-11-22 19:56:31"
title="Kubernetes: Writing hostname to a file"
tag=['kubernetes']
category=['Software Development']
+++

<p>
Over the weekend I spent a bit of time playing around with Kubernetes and to get the hang of the technology I set myself the task of writing the hostname of the machine to a file.
</p>


<p>
I'm using the excellent <a href="https://github.com/kubernetes/minikube">minikube</a> tool to create a local Kubernetes cluster for my experiments so the first step is to spin that up:</p>



~~~bash

$ minikube start
Starting local Kubernetes cluster...
Kubectl is now configured to use the cluster.
~~~

<p>
The first thing I needed to work out how to get the hostname. I figured there was probably an environment variable that I could access. We can call the <cite>env</cite> command to see a list of all the environment variables in a container so I created a pod template that would show me that information:
</p>



<p>
<cite>hostname_super_simple.yaml</cite>
</p>



~~~text

apiVersion: v1
kind: Pod
metadata:
  name: mark-super-simple-test-pod
spec:
  containers:
    - name: test-container
      image: gcr.io/google_containers/busybox:1.24
      command: [ "/bin/sh", "-c", "env" ]      
  dnsPolicy: Default
  restartPolicy: Never
~~~

<p>
I then created a pod from that template and checked the logs of that pod:
</p>



~~~bash

$ kubectl create -f hostname_super_simple.yaml 
pod "mark-super-simple-test-pod" created
~~~


~~~bash

$ kubectl logs  mark-super-simple-test-pod
KUBERNETES_SERVICE_PORT=443
KUBERNETES_PORT=tcp://10.0.0.1:443
HOSTNAME=mark-super-simple-test-pod
SHLVL=1
HOME=/root
KUBERNETES_PORT_443_TCP_ADDR=10.0.0.1
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
KUBERNETES_PORT_443_TCP_PORT=443
KUBERNETES_PORT_443_TCP_PROTO=tcp
KUBERNETES_SERVICE_PORT_HTTPS=443
KUBERNETES_PORT_443_TCP=tcp://10.0.0.1:443
PWD=/
KUBERNETES_SERVICE_HOST=10.0.0.1
~~~

<p>The information we need is in <cite>$HOSTNAME</cite> so the next thing we need to do is created a pod template which puts that into a file.</p>


<p>
<cite>hostname_simple.yaml</cite>
</p>



~~~text

apiVersion: v1
kind: Pod
metadata:
  name: mark-test-pod
spec:
  containers:
    - name: test-container
      image: gcr.io/google_containers/busybox:1.24
      command: [ "/bin/sh", "-c", "echo $HOSTNAME > /tmp/bar; cat /tmp/bar" ]
  dnsPolicy: Default
  restartPolicy: Never
~~~

<p>We can create a pod using this template by running the following command:</p>



~~~bash

$ kubectl create -f hostname_simple.yaml
pod "mark-test-pod" created
~~~

<p>Now let's check the logs of the instance to see whether our script worked:</p>



~~~bash

$ kubectl logs mark-test-pod
mark-test-pod
~~~

<p>
Indeed it did, good times!
</p>

