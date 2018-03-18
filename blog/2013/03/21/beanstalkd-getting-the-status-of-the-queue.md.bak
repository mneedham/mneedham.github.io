+++
draft = false
date="2013-03-21 23:25:09"
title="beanstalkd: Getting the status of the queue"
tag=['beanstalkd']
category=['Software Development']
+++

<p>For the last few days <a href="https://twitter.com/jasonneylon">Jason</a> and I have been porting a few of our applications across to a new puppet setup and one thing we needed to do was check that messages were passing through <a href="http://kr.github.com/beanstalkd/">beanstalkd</a> correctly.</p>


<p>We initially had the idea that it wasn't configured correctly so <a href="https://twitter.com/pingles">Paul</a> showed us a way of checking whether that was the case by connecting to the port it runs on like so:</p>



~~~text

$ telnet localhost 11300
stats

current-jobs-urgent: 0
current-jobs-ready: 0
current-jobs-reserved: 0
current-jobs-delayed: 0
current-jobs-buried: 0
cmd-put: 66
...
current-connections: 6
current-producers: 1
current-workers: 1
current-waiting: 1
total-connections: 58
pid: 15622
version: 1.4.6
rusage-utime: 0.000000
rusage-stime: 0.040002
uptime: 22740
binlog-oldest-index: 0
binlog-current-index: 0
binlog-max-size: 10485760
~~~

<p>The way we'd setup our beanstalks consumer, if it wasn't able to process a message correctly we put the message back on the queue in a 'buried' state so we'd see a number greater than 0 for the 'current-jobs-buried' property.</p>


<p>I was already curious how we'd go about writing a one liner to get those stats using <a href="http://netcat.sourceforge.net/">netcat</a> and after a bit of fiddling to force the new line character to be sent properly I ended up with the following:</p>



~~~text

$ echo -e "stats\r\n" | nc localhost 11300
~~~

<p>The key is the <a href="http://linux.about.com/library/cmd/blcmdl1_echo.htm">'-e'</a> flag which I may well have written about before but had forgotten all about:</p>



~~~text

-e
enable interpretation of the backslash-escaped characters listed below

...

\NNN
the character whose ASCII code is NNN (octal)
\\
backslash
\a
alert (BEL)
\b
backspace
\c
suppress trailing newline
\f
form feed
\n
new line
\r
carriage return
\t
horizontal tab
\v
vertical tab
~~~

<p>We can see how that works with the following example:</p>



~~~text

$ echo -e "mark\nmark"
mark
mark
~~~


~~~text

$ echo  "mark\nmark"
mark\nmark
~~~

<p>Alternatively we can pass either the '-c' or '-C' flag depending on our version of netcat and a <a href="http://en.wikipedia.org/wiki/Newline">CRLF/newline</a> will be sent as the line ending:</p>



~~~text

# netcat-openbsd version
$ echo "stats" | nc -C localhost 11300
~~~

<p>or</p>



~~~text

# one on Mac OS X by default
$ echo "stats" | nc -c localhost 11300
~~~



<p>Going back to beanstalkd - there is actually a <a href="https://github.com/kr/beanstalkd/blob/master/doc/protocol.txt">pretty good document</a> explaining all the different commands that you can send to it, most of which I haven't tried yet!</p>


<p>I have come across some useful ones though:</p>



~~~text

$ telnet localhost 11300
~~~

<h4>To see the names of the tubes (queues) where messages get put</h4>

~~~text

list-tubes
OK 14
---
- default
~~~

<h4>To use that tube</h4>

~~~text

use default
USING DEFAULT
~~~

<h4>To see if there are any ready jobs</h4>

~~~text

peek-ready
NOT_FOUND
~~~

<h4>To get the stats for that tube</h4>

~~~text

stats-tube default
OK 253
---
name: default
current-jobs-urgent: 0
current-jobs-ready: 0
current-jobs-reserved: 0
current-jobs-delayed: 0
current-jobs-buried: 0
total-jobs: 155
current-using: 9
current-watching: 9
current-waiting: 1
cmd-pause-tube: 0
pause: 0
pause-time-left: 0
~~~

<p>I came across <a href="https://github.com/dustin/beanstalk-tools">beanstalk-tools</a> which contains a bunch of tools for working with beanstalks but since our use is sporadic sending the commands over TCP every now and then will probably do! </p>

