+++
draft = false
date="2012-11-24 09:04:17"
title="Windows line endings: Exception in thread 'main' java.io.FileNotFoundException /opt/app/config.yml^M (no such file or directory)"
tag=['software-development']
category=['Software Development']
+++

As I <a href="http://www.markhneedham.com/blog/2012/11/24/java-java-lang-unsupportedclassversionerror-unsupported-major-minor-version-51-0/">mentioned in my previous post</a> we've been making it possible to deploy our application to a new environment and as part of this we defined an <a href="http://upstart.ubuntu.com/">upstart</a> script which would run the JAR.

We tend to edit code on Windows and then test it out on the vagrant VM afterwards. 

The end of our upstart script looked a bit like this:


~~~text

script     
    cd /opt/app 
    java -jar /opt/app/app.jar /opt/app/config.yml
end script  
~~~

Unfortunately when we tried to launch the application using 'start app' we got this error:


~~~text

Exception in thread "main" java.io.FileNotFoundException /opt/app/config.yml^M (no such file or directory)
~~~

We were trying to load the configuration file in the program which was failing because of the Windows line ending just after the file name. That was being read in as part of our config file name argument.

I tried change the upstart script to have the name in quotes (which in hindsight makes no sense) but that made no difference but eventually I realised we could <a href="http://sourceforge.net/p/notepad-plus/discussion/331754/thread/ac70ed25">make the file have UNIX line endings</a> and solve our problem.

Using notepad++:


~~~text

Edit > EOL Conversions > Unix Format
~~~

And all was well with the world.
