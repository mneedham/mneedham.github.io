+++
draft = false
date="2012-08-16 23:31:28"
title="puppetdb: Failed to submit 'replace catalog' command for client to PuppetDB at puppetmaster:8081: [500 Server Error]"
tag=['puppet', 'puppetdb']
category=['Software Development']
+++

I'm still getting used to the idea of <strong>following the logs</strong> when working out what's going wrong with distributed systems but it worked well when trying to work out why our puppet client which was throwing this error when we ran 'puppet agent -tdv':


~~~text

err: Could not retrieve catalog from remote server: Error 400 on SERVER: Failed to submit 'replace catalog' command for client to PuppetDB at puppetmaster:8081: [500 Server Error] 
~~~

We were seeing the same error in <cite>/var/log/syslog</cite> on the puppet master and a quick look at the process list didn't show that the puppet master or puppetdb services were under a particularly heavy load.

<a href="http://serverfault.com/questions/403753/puppet-gives-ssl-error-because-master-is-not-running">Eventually</a> we ended up looking at the puppetdb logs which showed that it was running out of memory:

<cite>/var/log/puppetdb/puppetdb.log</cite>

~~~text

2012-08-15 17:48:38,535 WARN  [qtp814855969-66] [server.AbstractHttpConnection] /commands
java.lang.OutOfMemoryError: Java heap space
~~~

The default <cite>/etc/default/puppetdb</cite> only has 192MB of heap space so we upped that to 1GB and problem solved! (at least for now)

<cite>/etc/default/puppetdb</cite>

~~~text

###########################################
# Init settings for puppetdb
###########################################

# Location of your Java binary (version 6 or higher)
JAVA_BIN="/usr/bin/java"

# Modify this if you'd like to change the memory allocation, enable JMX, etc
JAVA_ARGS="-Xmx1024m"

# These normally shouldn't need to be edited if using OS packages
USER="puppetdb"
INSTALL_DIR="/usr/share/puppetdb"
CONFIG="/etc/puppetdb/conf.d"                          
~~~
