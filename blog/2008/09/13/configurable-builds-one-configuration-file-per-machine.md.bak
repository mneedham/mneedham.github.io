+++
draft = false
date="2008-09-13 03:54:25"
title="Configurable Builds: One configuration file per machine"
tag=['build', 'nant', 'configuration']
category=['Build']
+++

I've covered some of the ways that I've seen for making builds configurable in previous posts:

<ul>
<li><a href="http://www.markhneedham.com/blog/2008/09/02/configurable-builds-one-configuration-file-per-environment/">One configuration file per environment</a></li>
<li><a href="http://www.markhneedham.com/blog/2008/09/02/configurable-builds-one-configuration-file-per-user/">One configuration file per user</a></li>
<li><a href="http://www.markhneedham.com/blog/2008/09/02/configurable-builds-overriding-properties/">Overriding properties</a></li>
</ul>


One which I haven't covered which my colleagues <a href="http://www.markhneedham.com/blog/2008/09/02/configurable-builds-one-configuration-file-per-user/#comment-263">Gil Peeters</a> and <a href="http://www.markhneedham.com/blog/2008/09/02/configurable-builds-one-configuration-file-per-environment/#comment-161">Jim Barritt</a> have pointed out is having a build with one configuration file for each machine.

Again the setup is fairly similar to one configuration per user or environment. Using Nant we would have the following near the top of the build file:


~~~text

<property name="machine.name" value="${environment::get-machine-name()}" />
<include buildfile="${trunk.dir}\config\${machine.name}.properties.xml" />
~~~

We could then have one configuration for each developer machine:

machine1.properties.xml

~~~xml

<?xml version="1.0" ?>
<properties>
	<property name="property1" value="onevalue" />
</properties>
~~~

machine2.properties.xml

~~~xml

<?xml version="1.0" ?>
<properties>
	<property name="property1" value="anothervalue" />
</properties>
~~~

The build file can be run using the following command:


~~~text

nant -buildfile:build-file.build target-name
~~~

The benefit of this approach can be seen (as Gil points out) in <a href="http://en.wikipedia.org/wiki/Pair_programming">pair programming</a> where the settings on any one machine will always be the same regardless of who is logged in. We also still get the advantage of being able to use remote resources on developer machines.

Having machine specific configuration also allows more flexibility for configurations on continuous integration for example. To quote Gil:

<blockquote>
Each CI build (multiple builds per build server) get's it's own [configuration] based on the build host and build name.</blockquote>

The disadvantage again is we have to add a new configuration file every time we want to run the build on a different machine.
