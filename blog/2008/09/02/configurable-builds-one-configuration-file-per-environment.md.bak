+++
draft = false
date="2008-09-02 01:50:02"
title="Configurable Builds: One configuration file per environment"
tag=['build', 'nant', 'configuration']
category=['Build']
+++

One of the most important things when coding build files is to try and make them as configurable as possible.

At the very least on an agile project there will be a need for two different configurations - one for developer machines and one for <a href="http://www.martinfowler.com/articles/continuousIntegration.html">continuous integration</a>.

On my last two .NET projects we have setup our <a href="http://nant.sourceforge.net/">Nant</a> build to take in a parameter which indicates which build configuration should be used. We then have a configuration file by that name which contains the environment specific data.

The build file would contain the following code before anything else:


~~~xml

<fail unless="${property::exists('environment')}" message="You must provide the environment property to the build script using -D:environment=[dev|ci]" />
<include buildfile="${trunk.dir}\config\${environment}.properties.xml" />
~~~

dev.properties.xml would look like this:


~~~xml

<?xml version="1.0" ?>
<properties>
	<property name="property1" value="value1" />
	<property name="property2" value="value2" />
</properties>
~~~

We would call the build file for the dev environment like so:


~~~text

nant -buildfile:build-file.build target-name -D:environment=dev
~~~

Configuring the build this way assumes that the dev builds all have the same properties. On the projects where I used this approach this was the case.

The disadvantage of it is that you need to remember to pass in the environment variable each time you call the build. This can be countered by wrapping the full nant call in a batch script if it becomes too much of a hassle.
