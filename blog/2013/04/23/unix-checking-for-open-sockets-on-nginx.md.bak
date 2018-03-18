+++
draft = false
date="2013-04-23 23:59:49"
title="Unix: Checking for open sockets on nginx"
tag=['unix']
category=['Shell Scripting']
+++

<p><a href="https://twitter.com/timrgoodwin">Tim</a> and I were investigating a weird problem we were having with nginx where it was getting in a state where it had exceeded the number of open files allowed on the system and started rejecting requests.</p>


<p>We can find out the maximum number of open files that we're allowed on a system with the following command:</p>



~~~bash

$ ulimit -n
1024
~~~

<p>Our hypothesis was that some socket connections were never being closed and therefore the number of open files was climbing slowly upwards until it exceeded the limit.</p>


<p>We wanted to check how many sockets nginx had open so to start with we needed to know the process IDs it was running under:</p>



~~~bash

$ ps aux | grep nginx | grep -v grep
root      1089  0.0  0.7 105152  2736 ?        Ss   17:34   0:00 nginx: master process /usr/sbin/nginx
www-data 17474  0.0  0.6 105300  2296 ?        S    21:49   0:04 nginx: worker process
www-data 17475  0.0  0.7 105300  2856 ?        S    21:49   0:04 nginx: worker process
www-data 17476  0.0  0.7 105300  2792 ?        S    21:49   0:03 nginx: worker process
www-data 17477  0.0  0.7 105300  2668 ?        S    21:49   0:04 nginx: worker process
~~~

<p>So the process IDs we're interested in are 1089, 17474, 17475, 17476 and 17477.</p>


<p>We can check which file descriptors they have open with the following command:</p>



~~~bash

$ sudo ls -alh /proc/{1089,17{474,475,476,477}}/fd
/proc/17476/fd:
total 0
dr-x------ 2 www-data www-data  0 Apr 23 23:40 .
...
l-wx------ 1 www-data www-data 64 Apr 23 23:40 6 -> /var/log/nginx/error.log
l-wx------ 1 www-data www-data 64 Apr 23 23:40 7 -> /var/www/thinkingingraphs/shared/log/nginx_access.log
l-wx------ 1 www-data www-data 64 Apr 23 23:40 8 -> /var/www/thinkingingraphs/shared/log/nginx_error.log
lrwx------ 1 www-data www-data 64 Apr 23 23:40 9 -> socket:[8910]

/proc/17477/fd:
total 0
...
lrwx------ 1 www-data www-data 64 Apr 23 23:40 56 -> socket:[52213]
lrwx------ 1 www-data www-data 64 Apr 23 23:40 57 -> anon_inode:[eventpoll]
l-wx------ 1 www-data www-data 64 Apr 23 23:40 6 -> /var/log/nginx/error.log
l-wx------ 1 www-data www-data 64 Apr 23 23:40 7 -> /var/www/thinkingingraphs/shared/log/nginx_access.log
l-wx------ 1 www-data www-data 64 Apr 23 23:40 8 -> /var/www/thinkingingraphs/shared/log/nginx_error.log
lrwx------ 1 www-data www-data 64 Apr 23 23:40 9 -> socket:[8910]
~~~

<p>We can narrow that down to just show us how many sockets are open:</p>



~~~bash

$ sudo ls -alh /proc/{1089,17{474,475,476,477}}/fd | grep socket  | wc -l
189
~~~

<p>We could also use <cite><a href="http://linux.die.net/man/8/lsof">lsof</a></cite> although for some reason that returns a slightly different number:</p>



~~~bash

$ sudo lsof -p 1089,17474,17475,17476,17477 | grep socket | wc -l
184
~~~

<p>If we want to use brace expansion to do that it becomes a bit more tricky:</p>



~~~bash

$ sudo lsof -p `echo {1089,174{74,75,76,77}} | sed 's/ /,/g'` | grep socket | wc -l
184
~~~

<p>Annoyingly we couldn't actually replicate the error but think that it's been solved in nginx 1.2.0 (we were using 1.1.19) by <a href="http://nginx.org/en/CHANGES">this change</a>:</p>



~~~text

Bugfix: a segmentation fault might occur in a worker process if the
       "try_files" directive was used; the bug had appeared in 1.1.19.
~~~
