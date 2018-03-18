+++
draft = false
date="2011-07-27 23:02:33"
title="Unix: Summing the total time from a log file"
tag=['shell', 'unix']
category=['Shell Scripting']
+++

As I <a href="http://www.markhneedham.com/blog/2011/07/27/a-crude-way-of-telling-if-a-remote-machine-is-a-vm/">mentioned in my last post</a> we've been doing some profiling of a data ingestion job and as a result have been putting some logging into our code to try and work out where we need to work on.

We end up with a log file peppered with different statements which looks a bit like the following:


~~~text

18:50:08.086 [akka:event-driven:dispatcher:global-5] DEBUG - Imported document. /Users/mneedham/foo.xml in: 1298
18:50:09.064 [akka:event-driven:dispatcher:global-1] DEBUG - Imported document. /Users/mneedham/foo2.xml in: 798
18:50:09.712 [akka:event-driven:dispatcher:global-4] DEBUG - Imported document. /Users/mneedham/foo3.xml in: 298
18:50:10.336 [akka:event-driven:dispatcher:global-3] DEBUG - Imported document. /Users/mneedham/foo4.xml in: 898
18:50:10.982 [akka:event-driven:dispatcher:global-1] DEBUG - Imported document. /Users/mneedham/foo5.xml in: 12298
~~~

I can never quite tell which column I need to get so end up doing some exploration with awk like this to find out:


~~~text

$ cat foo.log | awk ' { print $9 }'
1298
798
298
898
12298
~~~

Once we've worked out the column then we can add them together like this:


~~~text

$ cat foo.log | awk ' { total+=$9 } END { print total }'
15590
~~~

I think that's much better than trying to determine the total run time in the application and printing it out to the log file.

We can also calculate other stats if we record a log entry for each record:


~~~text

$ cat foo.log | awk ' { total+=$9; number+=1 } END { print total/number }'
3118
~~~


~~~text

$ cat foo.log | awk 'min=="" || $9 < min {min=$9; minline=$0}; END{ print min}' 
298
~~~
