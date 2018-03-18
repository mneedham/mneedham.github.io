+++
draft = false
date="2012-07-04 19:34:45"
title="sudo, sudo -i & sudo su"
tag=['software-development']
category=['Software Development']
+++

On the project I'm currently working on we're doing quite a bit of puppet and although we're using the puppet master approach in production & test environments it's still useful to be able to run puppet headless to test changes locally.

Since several of the commands require having write access to 'root' folders we need to run 'puppet apply' as a super user using sudo. We also need to run it in the context of some environment variables which the root user has. 

One way to do this would be to run the following command:


~~~text

sudo su 
~~~

That runs the 'su' command as root which means that we can <a href="https://twitter.com/rjhunter/status/220347921915314176">run root's shell as the root user</a> without needing to know the root password.

The cool thing about using 'su' like this is that it leaves us in the same directory that we were in before we ran the command.


~~~text

mneedham@ubuntu:/home/mneedham/puppet$ sudo su
root@ubuntu:/home/mneedham/puppet# 
~~~

If instead we want to be positioned in the root home directory we could use the following:


~~~text

mneedham@ubuntu:/home/mneedham/puppet$ sudo su -
root@ubuntu:~# pwd
/root
~~~

We can achieve a similar outcome using 'sudo -i', a flag I didn't know about until my colleague <a href="https://twitter.com/#!/philandstuff">Phil Potter</a> showed me:


~~~text

mneedham@ubuntu:/home/mneedham/puppet$ sudo -i
root@ubuntu:~# pwd
/root
~~~ 

<blockquote>
-i [command]
<p>
The -i (simulate initial login) option runs the shell specified in the passwd(5) entry of the target user as a login shell.  This means that
login-specific resource files such as .profile or .login will be read by the shell.  
</p>

<p>
If a command is specified, it is passed to the shell for execution. Otherwise, an interactive shell is executed.  
</p>

<p>
sudo attempts to change to that user's home directory before running the shell.  It also initializes the environment, leaving DISPLAY and TERM unchanged, setting HOME, SHELL, USER, LOGNAME, and PATH, as well as the contents of /etc/environment on Linux and AIX systems.  All other environment variables are removed.
</p>

</blockquote>

Interestingly with 'sudo -i' we can pass a command which will be executed in the root context which would be useful in this situation as we wouldn't need to keep switching to the root shell to run puppet.

One of the things that changes if we're in the root shell is the value of $HOME so I started with that to check I was passing the command correctly:


~~~text

mneedham@ubuntu:/home/mneedham/puppet$ sudo -i echo $HOME
/home/mneedham
~~~

Unfortunately the echo statement is getting evaluated in the context of the current user's shell rather than the root shell and <a href="https://twitter.com/rjhunter/status/220286792346243072">my colleague Rob Hunter showed me the 'set -x' tool/flag</a> so that I could figure out what was going on with the escaping in the shell:


~~~text

mneedham@ubuntu:/home/mneedham/puppet$ sudo -i echo $HOME
+ sudo -i echo /home/mneedham
/home/mneedham
~~~ 

As we can see, the $HOME value is expanded too early so we need to escape it like so:


~~~text

mneedham@ubuntu:/home/mneedham/puppet$ sudo -i echo \$HOME
+ sudo -i echo '$HOME'
/root
~~~

If we disable that flag:


~~~text

mneedham@ubuntu:/home/mneedham/puppet$ set +x
+ set +x
mneedham@ubuntu:/home/mneedham/puppet$ sudo -i echo \$HOME
/root
~~~

We can see that $HOME is being evaluated in the root shell context and we can also call our 'puppet apply' script in a similar vein.
