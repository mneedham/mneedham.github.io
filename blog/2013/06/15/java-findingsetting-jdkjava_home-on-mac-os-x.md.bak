+++
draft = false
date="2013-06-15 10:28:28"
title="Java: Finding/Setting JDK/$JAVA_HOME on Mac OS X"
tag=['java']
category=['Java']
+++

<p>As long as I've been using a Mac I always understood that if you needed to set <cite>$JAVA_HOME</cite> for any program, it should be set to <cite>/System/Library/Frameworks/JavaVM.framework/Versions/CurrentJDK</cite>.</p>


<p>On my machine this points to the 1.6 JDK:</p>



~~~bash

$ ls -alh /System/Library/Frameworks/JavaVM.framework/Versions/CurrentJDK
/System/Library/Frameworks/JavaVM.framework/Versions/CurrentJDK -> /System/Library/Java/JavaVirtualMachines/1.6.0.jdk/Contents
~~~

<p>This was a bit surprising to me since I've actually got Java 7 installed on the machine as well so I'd assumed the symlink would have been changed:</p>



~~~bash

$ java -version
java version "1.7.0_09"
Java(TM) SE Runtime Environment (build 1.7.0_09-b05)
Java HotSpot(TM) 64-Bit Server VM (build 23.5-b02, mixed mode)
~~~

<p><a href="https://twitter.com/andres_taylor">Andres</a> and I were looking at something around this yesterday and wanted to set <cite>$JAVA_HOME</cite> to the location of the 1.7 JDK on the system if it had been installed.</p>


<p>We eventually came across <a href="http://developer.apple.com/library/mac/#qa/qa1170/_index.html">the following article</a> which explains that you can use the <cite>/usr/libexec/java_home</cite> command line tool to do this.</p>


<p>For example, if we want to find where the 1.7 JDK is we could run the following:</p>



~~~bash

$ /usr/libexec/java_home -v 1.7
/Library/Java/JavaVirtualMachines/jdk1.7.0_09.jdk/Contents/Home
~~~

<p>And if we want 1.6 the following does the trick:</p>



~~~bash

$ /usr/libexec/java_home -v 1.6
/System/Library/Java/JavaVirtualMachines/1.6.0.jdk/Contents/Home
~~~

<p>We can also list all the JVMs installed on the machine:</p>



~~~bash

$ /usr/libexec/java_home  -V
Matching Java Virtual Machines (3):
    1.7.0_09, x86_64:	"Java SE 7"	/Library/Java/JavaVirtualMachines/jdk1.7.0_09.jdk/Contents/Home
    1.6.0_45-b06-451, x86_64:	"Java SE 6"	/System/Library/Java/JavaVirtualMachines/1.6.0.jdk/Contents/Home
    1.6.0_45-b06-451, i386:	"Java SE 6"	/System/Library/Java/JavaVirtualMachines/1.6.0.jdk/Contents/Home

/Library/Java/JavaVirtualMachines/jdk1.7.0_09.jdk/Contents/Home
~~~

<p>I'm not sure how I've never come across this command before but it seems pretty neat.</p>

