+++
draft = false
date="2012-09-07 15:45:16"
title="Apt-Cacher-Server: Extra junk at end of file"
tag=['software-development']
category=['Software Development']
+++

We've been installing <a href="https://help.ubuntu.com/community/Apt-Cacher-Server">Apt-Cache-Server</a> so that we can cache some of the packages that we're installing using apt-get on our own network.

(Almost) Following the instructions from the home page we added the following to <cite>/etc/apt/apt.conf.d/01proxy</cite>:


~~~text

Acquire::http::Proxy "http://apt-cache-server:3142"
~~~

And when we ran 'apt-get update' we were getting the following error:


~~~text

E: Syntax error /etc/apt/apt.conf.d/01proxy:2: Extra junk at end of file
~~~

We initially thought it must be a problem with having an extra space or line ending but it turns out we had just left off the semi colon. D'oh!

The following is what we needed:


~~~text

Acquire::http::Proxy "http://apt-cache-server:3142";
~~~

We also came across <a href="http://askubuntu.com/questions/61540/how-to-update-software-through-proxy">a post on StackOverflow</a> which suggested that sometimes that doesn't work and something more like this is required:


~~~text

Acquire::http { Proxy "http://apt-cache-server:3142"; };
~~~

Either of those seem to work for us but I guess YMMV.
