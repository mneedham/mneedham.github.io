+++
draft = false
date="2015-11-08 20:58:42"
title="Docker 1.9: Port forwarding on Mac OS X"
tag=['docker']
category=['Software Development']
+++

<p>
Since the <a href="http://www.infoq.com/news/2015/10/neo4j-2.3-release">Neo4j 2.3.0 release</a> there's been an <a href="https://hub.docker.com/r/neo4j/neo4j/">official docker image</a> which I thought I'd give a try this afternoon.
</p>


<p>
The last time I used docker about a year ago I had to install <a href="http://boot2docker.io/">boot2docker</a> which has now been deprecated in place of <a href="http://docs.docker.com/engine/installation/mac/">Docker Machine and the Docker Toolbox</a>.
</p>


<p>
I created a container with the following command:
</p>



~~~bash

docker run --detach --publish=7474:7474 neo4j/neo4j
~~~

<p>
And then tried to access the Neo4j server locally:
</p>



~~~bash

$ curl http://localhost:7474
curl: (7) Failed to connect to localhost port 7474: Connection refused
~~~

<p>I quickly checked that docker had started up Neo4j correctly:</p>



~~~bash

$ docker ps
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                              NAMES
1f7c48e267f0        neo4j/neo4j         "/docker-entrypoint.s"   10 minutes ago      Up 10 minutes       7473/tcp, 0.0.0.0:7474->7474/tcp   kickass_easley
~~~

<p>Looks good. Amusingly I then came across <a href="http://www.markhneedham.com/blog/2014/11/27/dockerneo4j-port-forwarding-on-mac-os-x-not-working/">my own blog post from a year ago</a> where I'd run into the same problem - the problem being that we need to access the Neo4j server via the VM's IP address rather than localhost.
</p>


<p>
Instead of using boot2docker we now need to use docker-machine to find the VM's IP address:
</p>



~~~bash

$ docker-machine ls
NAME      ACTIVE   DRIVER       STATE     URL                         SWARM
default   *        virtualbox   Running   tcp://192.168.99.100:2376
~~~


~~~bash

$ curl http://192.168.99.100:7474
{
  "management" : "http://192.168.99.100:7474/db/manage/",
  "data" : "http://192.168.99.100:7474/db/data/"
}
~~~

<p>And we're back in business.</p>

