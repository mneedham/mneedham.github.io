+++
draft = false
date="2013-04-16 20:57:53"
title="Puppet Debt"
tag=['devops-2', 'puppet']
category=['DevOps']
+++

<p>I've been playing around with a puppet configuration to run a neo4j server on an Ubuntu VM and one thing that has been quite tricky is getting the Sun/Oracle Java JDK to install repeatably.</p>


<p>I adapted Julian's <a href="https://github.com/neo4j-contrib/neo4j-puppet/blob/master/manifests/java.pp">Java module</a> which uses <a href="https://github.com/flexiondotorg/oab-java6">OAB-Java</a> and although it was certainly working cleanly at one stage I somehow ended up with it not working because of failed dependencies:</p>



~~~text

[2013-04-12 07:03:10] Notice: /Stage[main]/Java/Exec[install OAB repo]/returns:  [x] Installing Java build requirements Ofailed
[2013-04-12 07:03:10] Notice: /Stage[main]/Java/Exec[install OAB repo]/returns: ^[[m^O [i] Showing the last 5 lines from the logfile (/root/oab-java.sh.log)...
[2013-04-12 07:03:10] Notice: /Stage[main]/Java/Exec[install OAB repo]/returns:  nginx-common
[2013-04-12 07:03:10] Notice: /Stage[main]/Java/Exec[install OAB repo]/returns:  nginx-extras
[2013-04-12 07:03:10] Notice: /Stage[main]/Java/Exec[install OAB repo]/returns: E: Sub-process /usr/bin/dpkg returned an error code (1)
...
[2013-04-12 07:03:10] Warning: /Stage[main]/Java/Package[sun-java6-jdk]: Skipping because of failed dependencies
[2013-04-12 07:03:10] Notice: /Stage[main]/Java/Exec[default JVM]: Dependency Exec[install OAB repo] has failures: true
[2013-04-12 07:03:10] Warning: /Stage[main]/Java/Exec[default JVM]: Skipping because of failed dependencies
~~~

<p>I spent a few hours looking at this problem but couldn't quite figure out how to sort out the dependency problem and ended up running part one command manually after which applying puppet again worked.</p>


<p>Obviously this is a bit of a cop out because ideally I'd like it to be possible to spin up the VM in one puppet run without manual intervention.</p>


<p>A couple of days ago I was discussing the problem with <a href="https://twitter.com/a5hok">Ashok</a> and he suggested that it was probably good to know when I could defer fixing the problem to a later stage since having a completely automated spin up isn't my highest priority.</p>


<p>i.e. when I could take on what he referred to as '<strong>Puppet debt</strong>'</p>


<p>I think this is a reasonable way of looking at things and I have worked on projects where we've been  baffled by puppet's dependency graph and have setup scripts which run puppet twice until we have time to sort it out.</p>


<p>If we're <a href="http://www.markhneedham.com/blog/2013/04/07/treating-servers-as-cattle-not-as-pets/">spinning up new instances frequently</a> then we have less ability to take on this type of debt because it's going to hurt us much more but if not then I think it is reasonable to defer the problem.</p>


<p>This feels like another type of <a href="http://martinfowler.com/bliki/TechnicalDebt.html">technical debt</a> to me but I'd be interested in others' thoughts and whether I'm just a complete cop out!</p>

