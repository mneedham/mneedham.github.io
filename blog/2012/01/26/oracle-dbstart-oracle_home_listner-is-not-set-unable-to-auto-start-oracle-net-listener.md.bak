+++
draft = false
date="2012-01-26 21:58:27"
title="Oracle: dbstart - ORACLE_HOME_LISTNER is not SET, unable to auto-start Oracle Net Listener"
tag=['oracle']
category=['Software Development']
+++

We ran into an interesting problem when trying to start up an Oracle instance using <cite>dbstart</cite> whereby we were getting the following error:


~~~text

-bash-3.2$ dbstart

ORACLE_HOME_LISTNER is not SET, unable to auto-start Oracle Net Listener
Usage: /u01/app/oracle/product/11.2.0/dbhome_1/bin/dbstart ORACLE_HOME
Processing Database instance "orcl": log file /u01/app/oracle/product/11.2.0/dbhome_1/startup.log
~~~

Ignoring the usage message we thought that setting the environment variable was what we needed to do, but...


~~~text

-bash-3.2$ export ORACLE_HOME_LISTNER=$ORACLE_HOME
-bash-3.2$ dbstart
ORACLE_HOME_LISTNER is not SET, unable to auto-start Oracle Net Listener
Usage: /u01/app/oracle/product/11.2.0/dbhome_1/bin/dbstart ORACLE_HOME
Processing Database instance "orcl": log file /u01/app/oracle/product/11.2.0/dbhome_1/startup.log
~~~

We ended up looking at the source of <cite>dbstart</cite> to see what was going on:


~~~text

# First argument is used to bring up Oracle Net Listener
ORACLE_HOME_LISTNER=$1
if [ ! $ORACLE_HOME_LISTNER ] ; then
  echo "ORACLE_HOME_LISTNER is not SET, unable to auto-start Oracle Net Listener"
  echo "Usage: $0 ORACLE_HOME"
~~~

The usage message does explain that you're supposed to call it like this:


~~~text

-bash-3.2$ dbstart $ORACLE_HOME
~~~

But it still seems a bit weird/misleading to me that you'd override the value of a global variable from inside a script which doesn't suggest that it's going to do that!

Such is life in Oracle land..
