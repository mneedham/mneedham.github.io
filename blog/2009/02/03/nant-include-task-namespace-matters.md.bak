+++
draft = false
date="2009-02-03 10:43:56"
title="Nant include task - namespace matters"
tag=['build', 'nant']
category=['Build']
+++

We've been trying to include some properties into our build file from a properties file today but no matter what we tried the properties were not being set.

We eventually realised that the build file has an XML Namespace set on the project element.


~~~text

<project name="..." xmlns="http://nant.sf.net/schemas/nant.xsd">
~~~

It turns out that if you want to include a properties file in your build file, like so:


~~~text

<include buildfile="properties.xml" />
~~~

...you need to put the namespace on the project attribute of that file as well, otherwise its properties don't get picked up.

Our properties file therefore needs to look like this, assuming that we have a namespace set on the build file.


~~~text

<project name="properties" xmlns="http://nant.sf.net/schemas/nant.xsd">
	<property name="foo" value="bar" />
</project>
~~~

What's a bit confusing is that on the NAnt documentation page for the <a href="http://nant.sourceforge.net/release/latest/help/tasks/include.html">include task</a> it says that project element attributes are ignored! That's not what we found!
