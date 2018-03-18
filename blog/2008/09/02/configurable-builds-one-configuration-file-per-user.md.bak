+++
draft = false
date="2008-09-02 13:53:53"
title="Configurable Builds: One configuration file per user"
tag=['build', 'nant', 'configuration']
category=['Build']
+++

Following on from <a href="http://www.markhneedham.com/blog/2008/09/02/configurable-builds-one-configuration-file-per-environment/">my first post</a> about making builds configurable, the second way of doing this that I have seen is to have one configuration build file per user.

This approach is more useful where there are different configurations needed on each developer machine. For example, if the databases being used for development are on a remote server then each developer machine would be assigned a database with a different name.

The setup is fairly similar to configuring by environment - the main difference is that we don't have to pass the user in as a parameter. The following would go near the top of the build file:


~~~text

<property name="user" value="${environment::get-user-name()}" />
<include buildfile="${trunk.dir}\config\${user}.properties.xml" />
~~~

We can then have different configurations for two developer machines like so:

developer1.properties.xml

~~~xml

<?xml version="1.0" ?>
<properties>
	<property name="property1" value="onevalue" />
</properties>
~~~

developer2.properties.xml

~~~xml

<?xml version="1.0" ?>
<properties>
	<property name="property1" value="anothervalue" />
</properties>
~~~

We can then run the build file like this:


~~~text

nant -buildfile:build-file.build target-name
~~~

The disadvantage of this approach is that every time a new developer joins the team they need to create a new configuration file with their settings in. We also need to ensure that the continuous integration build is running using an independent user account. It provides more flexibility and is easier to setup on the plus side.

My colleague <a href="http://jimbarritt.com/non-random/">Jim Barritt</a> points out a similar technique his team is using <a href="http://www.markhneedham.com/blog/2008/09/02/configurable-builds-one-configuration-file-per-environment/#comment-161">here</a>.
