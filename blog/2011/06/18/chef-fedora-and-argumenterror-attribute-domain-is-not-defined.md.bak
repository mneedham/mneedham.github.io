+++
draft = false
date="2011-06-18 18:45:29"
title="Chef, Fedora and 'ArgumentError: Attribute domain is not defined!'"
tag=['chef', 'fedora']
category=['DevOps']
+++

I've been playing around with <a href="http://wiki.opscode.com/display/chef/Chef+Solo">Chef Solo</a> on Fedora and executing the following:


~~~text

sudo chef-solo -c config/solo.rb -j config/node.json
~~~

(where <cite>node.json</cite> just contains the example code from the <a href="http://wiki.opscode.com/display/chef/Chef+Solo">resolver example on the Chef documentation page</a> and the cookbooks folder contains <a href="https://github.com/opscode/cookbooks/tree/master">all the opscode cookbooks</a>.)

leads to the following error:


~~~text

...
ERROR: Running exception handlers
ERROR: Exception handlers complete
FATAL: Stacktrace dumped to /home/mark/chef-solo/chef-stacktrace.out
FATAL: ArgumentError: Attribute domain is not defined!
~~~

A bit of googling led me to believe that this error is happening because <a href="http://lists.opscode.com/sympa/arc/chef/2010-03/msg00075.html">the machine doesn't have a fully qualified domain name (fqdn) defined</a> which can be seen by calling the following command:


~~~text

$ hostname -f
> hostname: Name of service not known
~~~ 

One way to fix it is to add the following entry to <cite>/etc/hosts</etc>


~~~text

127.0.0.1	mark-fedora
~~~

Which results in the script running fine with no errors.


~~~text

...
INFO: Running report handlers
INFO: Report handlers complete
~~~

A suggestion I read while googling about fqdn was to add the hostname of the machine into a file called <cite>/etc/HOSTNAME</cite> but that didn't seem to have any impact for me.

On the Mac <cite>hostname -f</cite> works fine even without an entry like the above in <cite>/etc/hosts</cite> so I'm not entirely sure how it all works!

If anyone could explain it to me that'd be awesome.
