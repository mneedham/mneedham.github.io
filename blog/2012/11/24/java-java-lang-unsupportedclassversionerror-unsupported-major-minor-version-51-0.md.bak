+++
draft = false
date="2012-11-24 08:49:28"
title="Java: java.lang.UnsupportedClassVersionError - Unsupported major.minor version 51.0"
tag=['java']
category=['Java']
+++

On my current project we've spent the last day or so setting up an environment where we can deploy a couple of micro services to.

Although the machines are Windows based we're deploying the application onto a <a href="http://vagrantup.com/">vagrant</a> managed VM since the production environment will be a flavour of Linux. 

Initially I was getting quite confused about whether or not we were in the VM or not and ended up with this error when trying to run the compiled JAR:


~~~text

Exception in thread "main" java.lang.UnsupportedClassVersionError: com/whatever/SomeService : Unsupported major.minor version 51.0
        at java.lang.ClassLoader.defineClass1(Native Method)
        at java.lang.ClassLoader.defineClassCond(Unknown Source)
        at java.lang.ClassLoader.defineClass(Unknown Source)
        at java.security.SecureClassLoader.defineClass(Unknown Source)
        at java.net.URLClassLoader.defineClass(Unknown Source)
        at java.net.URLClassLoader.access$000(Unknown Source)
        at java.net.URLClassLoader$1.run(Unknown Source)
        at java.security.AccessController.doPrivileged(Native Method)
        at java.net.URLClassLoader.findClass(Unknown Source)
        at java.lang.ClassLoader.loadClass(Unknown Source)
        at sun.misc.Launcher$AppClassLoader.loadClass(Unknown Source)
        at java.lang.ClassLoader.loadClass(Unknown Source)
Could not find the main class: com/whatever/SomeService. Program will exit.
~~~

These error means that you <a href="http://stackoverflow.com/questions/11239086/java-lang-unsupportedclassversionerror-unsupported-major-minor-version-51-0">compiled the code with a higher JDK than the one you're now trying to run it against</a>.

Since I was accidentally trying to run the JAR against our Windows environment's 1.6 JDK rather than the VM's 1.7 JDK this is exactly what I was doing!

Muppet!
