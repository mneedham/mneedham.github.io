+++
draft = false
date="2008-10-06 20:12:49"
title="Calling shell script from ruby script"
tag=['ruby', 'shell', 'ruby-ldap']
category=['Ruby']
+++

Damana and I <a href="http://geekdamana.blogspot.com/2008/10/ruby-ldap.html">previously</a> <a href="http://www.markhneedham.com/blog/2008/10/05/ruby-ldap-options/">posted</a> about our experiences with different Ruby LDAP solutions.

Having settled on <a href="http://sourceforge.net/projects/ruby-ldap/">Ruby-LDAP</a> (although having read Ola and Steven's comments we will now look at <a href="http://rubyforge.org/projects/net-ldap/">ruby-net-ldap</a>) we then needed to put together the setup, installation and teardown into a ruby script file.

A quick bit of Googling revealed that we could use the <a href="http://ruby-doc.org/core/classes/Kernel.html#M005979">Kernel.exec</a> method to do this.

For example, you could put the following in a ruby script file and it would execute and show you the current directory listing:


~~~ruby

exec "ls"
~~~

The problem with using Kernel.exec, which we became aware of after reading <a href="http://blog.jayfields.com/2006/06/ruby-kernel-system-exec-and-x.html">Jay's post</a>, is that we lose control of the current process - i.e. the script will exit after running 'exec' and won't process any other commands that follow it in the file.

Luckily for us there is another method called <a href="http://ruby-doc.org/core/classes/Kernel.html#M005982">Kernel.system</a> which allows us to execute a command in a sub shell, and therefore continue processing other commands that follow it.

We were able to use this method for making calls to the make script to install Ruby-LDAP:


~~~ruby

@extconf = "ruby extconf.rb"
system @extconf
system "make"
system "make install"
~~~

There is one more option we can use if we need to collect the results  called %x[...]. We didn't need to collect the results so we have gone with 'Kernel.system' for the time being. 

Jay <a href="http://blog.jayfields.com/2006/06/ruby-kernel-system-exec-and-x.html">covers the options in more detail on his post</a> for those that need more information than I have presented.
