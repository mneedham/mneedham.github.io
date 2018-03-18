+++
draft = false
date="2012-09-13 00:17:49"
title="Unix: Caught out by shell significant characters"
tag=['shell']
category=['Shell Scripting']
+++

One of the applications that <a href="https://twitter.com/philandstuff">Phil</a> and I were deploying today needed a MySQL server and part of our puppet code to provision that node type runs a command to setup the privileges for a database user.

The unevaluated puppet code reads like this:


~~~text

/usr/bin/mysql -h ${host} -uroot ${rootpassarg} -e "grant all on ${name}.* to ${user}@'${remote_host}' identified by '$password'; flush privileges;"
~~~

In the application we were deploying that expanded into something like this:


~~~text

/usr/bin/mysql -h localhost -uroot root_pw -e "grant all on db_name.* to db_user@'%' identified by 'awe$ome+password'; flush privileges;"
~~~

Unfortunately when we ran puppet it was executing without any problems but when we tried to connect to MySQL using 'db_user' with a password of 'awe$ome+password' we kept being denied access.

We tried changing the password to 'bob' to see what would happen, expecting that to fail as well, but were actually able to login so we figured there was something wrong with the password.

Phil suggested echoing the command to see what it was being evaluated to in the shell and once we did that we realised that the password was actually being set to 'awe+password' because the <cite>$ome</cite> bit was being evaluated as a shell variable.

This happens because <a href="http://www.howtogeek.com/howto/29980/whats-the-difference-between-single-and-double-quotes-in-the-bash-shell/">shell variables are evaluated</a> if they are enclosed in "" which is the case here as our whole grant statement is enclosed in "". If variables are enclosed in '' then they won't be evaluated:


~~~text

$ mark="foo"; echo "$mark"
foo
~~~


~~~text

$ mark="foo"; echo '$mark'
$mark
~~~

In this case we can therefore switch the '' and "" around to solve the problem:


~~~text

/usr/bin/mysql -h localhost -uroot root_pw -e 'grant all on db_name.* to db_user@"%" identified by awe$ome+password"; flush privileges;'
~~~
