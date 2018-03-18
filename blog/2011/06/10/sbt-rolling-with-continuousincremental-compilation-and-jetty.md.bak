+++
draft = false
date="2011-06-10 00:16:05"
title="Sbt: Rolling with continuous/incremental compilation and Jetty"
tag=['sbt']
category=['Build', 'Scala']
+++

As I mentioned <a href="http://www.markhneedham.com/blog/2011/06/04/sbt-zipping-files-without-their-directory-structure/">in an earlier post</a> we're using SBT on our project and one of it's cool features is that it will listen to the source directory and then automatically recompile the code when it detects file changes.

We've also installed the <a href="https://github.com/glenford/sbt-jetty-embed">sbt-jetty-embed</a> plugin which allows us to create a war which has Jetty embedded so that we can <a href="http://patforna.blogspot.com/2011/04/containerless.html?utm_source=feedburner&utm_medium=feed&utm_campaign=Feed%3A+patforna+%28Patric+Fornasier%27s+Blog%29">keep our application containerless</a>.

That plugin adds an action called 'jetty' to sbt so we (foolishly in hindsight) thought that we would be able to launch the application in triggered execution mode by making use of a ~ in front of that:


~~~text

$ ./sbt
> ~jetty
~~~

Unfortunately that doesn't do any continuous compilation which left us quite confused until we realised that <a href="http://code.google.com/p/simple-build-tool/wiki/TriggeredExecution">RTFM</a> might be a good idea...

What we actually needed to launch the application locally and edit code/see changes as if it's written in a dynamic language was the following:


~~~text

$ ./sbt
> jetty-run
> ~ prepare-webapp
~~~
