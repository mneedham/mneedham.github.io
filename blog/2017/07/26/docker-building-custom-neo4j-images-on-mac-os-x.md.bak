+++
draft = false
date="2017-07-26 22:20:23"
title="Docker: Building custom Neo4j images on Mac OS X"
tag=['neo4j', 'docker']
category=['neo4j']
description="In this post we look at how to build a custom Neo4j Docker image on Mac OS X."
+++

I sometimes needs to create custom Neo4j Docker images to try things out and wanted to share my work flow, mostly for future Mark but also in case it's useful to someone else. 

There's already a docker-neo4j repository so we'll just tweak the files in there to achieve what we want.


~~~bash

$ git clone git@github.com:neo4j/docker-neo4j.git
$ cd docker-neo4j
~~~

If we want to build a Docker image for Neo4j Enterprise Edition we can run the following build target:


~~~bash

$ make clean build-enterprise
Makefile:9: *** This Make does not support .RECIPEPREFIX. Please use GNU Make 4.0 or later.  Stop.
~~~

<p>
Denied at the first hurdle! What version of make have we got on this machine?
</p>



~~~bash

$ make --version
GNU Make 3.81
Copyright (C) 2006  Free Software Foundation, Inc.
This is free software; see the source for copying conditions.
There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE.

This program built for i386-apple-darwin11.3.0
~~~

<p>We can sort that out by <a href="https://stackoverflow.com/questions/40871732/using-gnu-make-4-x-on-osx">installing a newer version using brew</a>:
</p>



~~~bash

$ brew install make
$ gmake --version
GNU Make 4.2.1
Built for x86_64-apple-darwin15.6.0
Copyright (C) 1988-2016 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.
~~~

<p>
That's more like it! brew installs make with the 'g' prefix and since I'm not sure if anything else on my system relies on the older version of make I won't bother changing the symlink.
</p>


<p>
Let's retry our original command:
</p>



~~~bash

$ gmake clean build-enterprise
Makefile:14: *** NEO4J_VERSION is not set.  Stop.
~~~

<p>
It's still not happy with us! Let's set that environment variable to the latest released version as of writing:
</p>



~~~bash

$ export NEO4J_VERSION="3.2.2"
$ gmake clean build-enterprise
...
Successfully built c16b6f2738de
Successfully tagged test/18334:latest
Neo4j 3.2.2-enterprise available as: test/18334
~~~

<p>We can see that image in Docker land by running the following command:</p>



~~~bash

$ docker images | head -n2
REPOSITORY                                     TAG                          IMAGE ID            CREATED             SIZE
test/18334                                     latest                       c16b6f2738de        4 minutes ago       303MB
~~~

<p>
If I wanted to deploy that image to my own Docker Hub I could run the following commands:
</p>



~~~bash

$ docker login --username=markhneedham
$ docker tag c16b6f2738de markhneedham/neo4j:3.2.2
$ docker push markhneedham/neo4j
~~~

<p>
Putting Neo4j Enterprise 3.2.2 on my Docker Hub isn't very interesting though - that version is already on the official Neo4j Docker Hub. 
</p>


<p>
I've actually been building versions of Neo4j against the HEAD of the Neo4j 3.2 branch (i.e. 3.2.3-SNAPSHOT), deploying those to S3, and then building a Docker image based on those archives.
</p>


<p>
To change the destination of the Neo4j artifact we need to tweak <a href="https://github.com/neo4j/docker-neo4j/blob/master/Makefile#L18">this line in the Makefile</a>:
</p>



~~~bash

$ git diff Makefile
diff --git a/Makefile b/Makefile
index c77ed1f..98e05ca 100644
--- a/Makefile
+++ b/Makefile
@@ -15,7 +15,7 @@ ifndef NEO4J_VERSION
 endif
 
 tarball = neo4j-$(1)-$(2)-unix.tar.gz
-dist_site := http://dist.neo4j.org
+dist_site := https://s3-eu-west-1.amazonaws.com/core-edge.neotechnology.com/20170726
 series := $(shell echo "$(NEO4J_VERSION)" | sed -E 's/^([0-9]+\.[0-9]+)\..*/\1/')
 
 all: out/enterprise/.sentinel out/community/.sentinel
~~~

<p>
We can then update the Neo4j version environment variable:
</p>



~~~bash

$ export NEO4J_VERSION="3.2.3-SNAPSHOT"
~~~

<p>
And then repeat the Docker commands above. You'll need to sub in your own Docker Hub user and repository names. 
</p>


<p>
I'm using these custom images as part of Kubernetes deployments but you can use them anywhere that accepts a Docker container. 
</p>


<p>
If anything on the post didn't make sense or you want more clarification let me know <a href="https://twitter.com/markhneedham">@markhneedham</a>.
</p>

