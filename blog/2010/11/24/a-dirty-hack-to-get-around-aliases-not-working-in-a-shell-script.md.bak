+++
draft = false
date="2010-11-24 18:48:25"
title="A dirty hack to get around aliases not working in a shell script"
tag=['shell-scripting-2']
category=['Shell Scripting']
+++

In another script I've been working on lately I wanted to call 'mysql' but unfortunately on my machine it's 'mysql5' rather than 'mysql'.

I have an alias defined in '~/.bash_profile' so I can call 'mysql' from the terminal whenever I want to.


~~~text

alias mysql=mysql5
~~~

Unfortunately shell scripts don't seem to have access to this alias and the <a href="http://unix.ittoolbox.com/groups/technical-functional/shellscript-l/how-to-use-an-alias-in-shell-script-2076287">only suggestion</a> I've come across while googling this is to source '~/.bash_profile' inside the script.

Since others are going to use the script and might have '~/.bashrc' instead of '~/.bash_profile' I didn't really want to go down that route.

At this stage a colleague of mine came up with the idea of creating a soft link from mysql to mysql5 inside a folder which is already added to the path.

We located mysql5...


~~~text

> which mysql5
/opt/local/bin/mysql5
~~~

...and then created a soft link like so:


~~~text

cd /opt/local/bin/mysql5
ln -s mysql5 mysql
~~~

And it works!

Of course t'is pure hackery so I'd be interested if anyone knows a better way of getting around this.

