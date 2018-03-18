+++
draft = false
date="2016-12-21 07:11:50"
title="Docker: Unknown - Unable to query docker version: x509: certificate is valid for"
tag=['docker']
category=['Docker']
+++

<p>I was playing around with Docker locally and somehow ended up with this error when I tried to list my <a href="https://docs.docker.com/machine/overview/">docker machines</a>:
</p>



~~~bash

$ docker-machine ls
NAME      ACTIVE   DRIVER       STATE     URL                         SWARM   DOCKER    ERRORS
default   -        virtualbox   Running   tcp://192.168.99.101:2376           Unknown   Unable to query docker version: Get https://192.168.99.101:2376/v1.15/version: x509: certificate is valid for 192.168.99.100, not 192.168.99.101

~~~

<p>
My Google Fu was weak I couldn't find any suggestions for what this might mean so I tried shutting it down and starting it again!
</>

<p>
On the restart I actually got some helpful advice:
</p>



~~~bash

$ docker-machine stop
Stopping "default"...
Machine "default" was stopped.
~~~


~~~bash

$ docker-machine start
Starting "default"...
(default) Check network to re-create if needed...
(default) Waiting for an IP...
Machine "default" was started.
Waiting for SSH to be available...
Detecting the provisioner...
Started machines may have new IP addresses. You may need to re-run the `docker-machine env` command.
~~~

<p>So I tried that:</p>



~~~bash

$ docker-machine env
Error checking TLS connection: Error checking and/or regenerating the certs: There was an error validating certificates for host "192.168.99.101:2376": x509: certificate is valid for 192.168.99.100, not 192.168.99.101
You can attempt to regenerate them using 'docker-machine regenerate-certs [name]'.
Be advised that this will trigger a Docker daemon restart which will stop running containers.
~~~

<p>
And then regenerates my certificates:
</p>



~~~bash

$ docker-machine regenerate-certs
Regenerate TLS machine certs?  Warning: this is irreversible. (y/n): y
Regenerating TLS certificates
Waiting for SSH to be available...
Detecting the provisioner...
Copying certs to the local machine directory...
Copying certs to the remote machine...
Setting Docker configuration on the remote daemon...
~~~

<p>And now everything is happy again!</p>



~~~bash

$ docker-machine ls
NAME      ACTIVE   DRIVER       STATE     URL                         SWARM   DOCKER   ERRORS
default   -        virtualbox   Running   tcp://192.168.99.101:2376           v1.9.0
~~~
