+++
draft = false
date="2012-07-05 23:42:35"
title="Bash Shell: Reusing parts of previous commands"
tag=['shell']
category=['Shell Scripting']
+++

I've paired a few times with my colleague <a href="https://twitter.com/#!/philandstuff">Phil Potter</a> over the last couple of weeks and since he's a bit of a ninja with bash shortcuts/commands I wanted to record some of the things he's shown me so I won't forget them!

Let's say we're in the '/tmp' directory and want to create a folder a few levels down but forget to pass the '-p' option to 'mkdir':


~~~text

$ mkdir blah/de/blah
mkdir: cannot create directory `blah/de/blah': No such file or directory
~~~

One way of fixing that would be to press the up arrow and navigate along the previous command and put in the '-p' flag but it's a bit fiddly so instead we can do the following:


~~~text

$ ^mkdir^mkdir -p
mkdir -p blah/de/blah
~~~

The '^' allows us to replace any parts of the previous command and then run it again, so we could actually make that more concise if we wanted to:


~~~text

$ ^r^r -p
mkdir -p blah/de/blah
~~~

Reasonably frequently after we've created a folder like this we'll want to create a file inside it. '!$' comes in handy here as it allows us to refer to the last argument passed to the last command:


~~~text

$ touch !$/blah.xml
touch blah/de/blah/blah.xml
~~~

If we decide to remove that file and want to check it's been deleted we can run the following:


~~~text

$ touch blah/de/blah/blah.xml
$ rm blah/de/blah/blah.xml
$ ls -alh !$:h
ls -alh blah/de/blah
total 8.0K
drwxr-xr-x 2 mneedham mneedham 4.0K 2012-07-05 16:26 .
drwxr-xr-x 3 mneedham mneedham 4.0K 2012-07-05 16:16 ..
~~~

The ':h' <a href="http://www.gnu.org/software/bash/manual/html_node/Modifiers.html#Modifiers">modifier</a> removes the file name and leaves the rest of the file path alone. 

We can expand the value of '!$' or any other command by typing 'Esc' followed by '^' (Shift 6):


~~~text

mneedham@ubuntu:/tmp$ mkdir -p blah/de/blah
mneedham@ubuntu:/tmp$ touch !$
~~~

Esc + ^


~~~text

$ mkdir -p blah/de/blah
$ touch blah/de/blah
~~~

If we get carried away with modifiers we could also fix that first 'mkdir' command by making use of the 'substitution' modifier:


~~~text

$ mkdir blah/de/blah
mkdir: cannot create directory `blah/de/blah': No such file or directory

$ !!:s/r/r -p
mkdir -p blah/de/blah
~~~

There's not really any reason I can think of why you'd want to use that when you can use the initial '^' approach though!

I came across <a href="http://samrowe.com/wordpress/advancing-in-the-bash-shell/">this blog post which explains how to do this type of thing and much more in the bash shell</a> - worth a read!
