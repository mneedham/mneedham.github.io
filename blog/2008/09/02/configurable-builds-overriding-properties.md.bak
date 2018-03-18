+++
draft = false
date="2008-09-02 14:49:02"
title="Configurable Builds: Overriding properties"
tag=['build', 'nant', 'configuration']
category=['Build']
+++

Sometimes when configuring our build for flexibility we don't need to spend the time required to create <a href="http://www.markhneedham.com/blog/2008/09/02/configurable-builds-one-configuration-file-per-user/">one build configuration per user</a> or <a href="http://www.markhneedham.com/blog/2008/09/02/configurable-builds-one-configuration-file-per-environment/">one build configuration per environment</a>.

In these cases we can just override properties when we call Nant from the command line. 

One recent example where I made use of this was where we had one configuration file with properties in but wanted to override a couple of them when we ran the continuous integration build.

Since build properties are immutable (i.e. once they are set they can't be changed) if we set them from the command line the build script makes use of these values.

For example we might have the following in our build file:


~~~text

<property name="repository.url" value="http://localhost:3000" />
~~~

But when we're running it on cruise control we have the repository on a different machine. We can override it like so:


~~~text

nant -buildfile:build-file.build target-name -D:repository.url=http://some-remote-url
~~~

If we have more than one property we want to override it might be a bit annoying to have to pass them all via the command line. We can define them in a file to overcome this problem:


~~~text

nant -buildfile:build-file.build target-name @ci.properties.xml
~~~

where ci.properties.xml contains the following:


~~~text

-D:repository.url=http://remote-url:3000
-D:some.other.property=newvalue
~~~

If you start seeing a lot of properties in this file then it is probably an indicator that you need to have a more robust solution but this works for providing simple flexibility.
