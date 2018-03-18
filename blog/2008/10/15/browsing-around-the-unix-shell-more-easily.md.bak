+++
draft = false
date="2008-10-15 22:31:16"
title="Browsing around the Unix shell more easily"
tag=['shell']
category=['Shell Scripting']
+++

Following on from my post about getting the <a href="http://www.markhneedham.com/blog/2008/09/28/show-pwd-all-the-time/">pwd to display on the bash prompt all the time</a> I have learnt a couple of other tricks to make the shell experience more productive.

<a href="http://en.wikipedia.org/wiki/Unalias#Removing_aliases_.28unalias.29">Aliases</a> are the first new concept I came across and several members of my current team and I now have these setup.

We are primarily using them to provide a shortcut command to get to various locations in the file system. For example I have the following 'work' alias in my ~/.bash_profile file:


~~~text

alias work='cd ~/path/to/my/current/project'
~~~

I can then go to the bash prompt and type 'work' and it navigates straight there. You can put as many different aliases as you want in there, just don't forget to execute the following command after adding new ones to get them reflected in the current shell:


~~~text

. ~/.bash_profile
~~~

A very simple idea but one that helps save so many keystrokes for me every day.

Another couple of cool commands I recently discovered are <strong>pushd</strong> and <strong>popd</strong>

They help provide a stack to store directories on, which I have found particularly useful when browsing between distant directories.

For example suppose I am in the directory '/Users/mneedham/Desktop/Blog/' but I want to go to '/Users/mneedham/Projects/Ruby/path/to/some/code' to take a look at some code.

Before changing to that directory I can execute:


~~~text

pushd .
~~~

This will push the current directory ('/Users/mneedham/Desktop/Blog/') onto the stack. Then once I'm done I just need to run:


~~~text

popd
~~~

I'm back to '/Users/mneedham/Desktop/Blog/' with a lot less typing.

Running the following command shows a list of the directories currently on the stack:


~~~text

dirs
~~~

I love navigating with the shell so if you've get any other useful tips please share them!
