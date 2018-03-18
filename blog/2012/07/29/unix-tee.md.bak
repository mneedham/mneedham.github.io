+++
draft = false
date="2012-07-29 19:11:24"
title="Unix: tee"
tag=['unix', 'tee']
category=['Shell Scripting']
+++

I've read about the Unix '<a href="http://en.wikipedia.org/wiki/Tee_(command)">tee</a>' command before but never found a reason to use it until the last few weeks.

One of the things I repeatedly do by mistake is open <cite>/etc/hosts</cite> without sudo and then try to make changes to it:


~~~text

$ vi /etc/hosts
# Editing it leads to the dreaded 'W10: Changing a readonly file'
~~~

I always used to close the file and then re-open it with sudo but I recently came across <a href="http://www.commandlinefu.com/commands/view/1204/save-a-file-you-edited-in-vim-without-the-needed-permissions">an approach which allows us to use 'tee' to get around the problem</a>.

Once we've made our change we can run the following command:


~~~text

:w !sudo tee %
~~~


The ':w' is usually used to write the buffer to the current file but here we're substituting a shell command to receive the buffer instead. 

In this case we're sending the buffer to the 'sudo tee %' command where '%' refers to the current file name.

tee is defined like so:

<blockquote>
The tee utility copies standard input to standard output, making a copy in zero or more files.  The output is unbuffered.
</blockquote>

So we're sending the buffer for the current file to tee which then saves it to the current file. Since we've run tee with sudo it will give us the appropriate permissions to write to the file that we didn't initially have.

This <a href="http://stackoverflow.com/questions/2600783/how-does-the-vim-write-with-sudo-trick-work">Stack Overflow post explains what's going on in more detail</a>.

Another thing we've been working on is hooking up the logs of our various services to <a href="http://logstash.net/">logstash</a> and to test it out we needed to write to files in the <cite>/var/log</cite> directory.

We started out trying to echo a message to the end of the apache log file like this:


~~~text

$ echo "random message" >> /var/log/apache2/access_log 
zsh: permission denied: /var/log/apache2/access_log
~~~

As you can see that doesn't work since we don't have permissions to write to files in <cite>/var/log</cite> so we need to find another way to do that and <a href="https://twitter.com/nickstenning">Nick</a> pointed out that tee would do the job here as well.


~~~text

$ echo "random message" | sudo tee -a /var/log/apache2/access_log
random message
~~~

Passing the '-a' flag to tee means that it appends standard input to the file instead of replacing the whole file like before. If we don't want standard in to be directed to standard out we can redirect that to <cite>/dev/null</cite> like so:


~~~text

$ echo "random message" | sudo tee > /dev/null -a /var/log/apache2/access_log
~~~
