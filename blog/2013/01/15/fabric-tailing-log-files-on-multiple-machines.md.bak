+++
draft = false
date="2013-01-15 00:20:49"
title="Fabric: Tailing log files on multiple machines"
tag=['devops-2', 'python', 'fabric']
category=['DevOps']
+++

<p>We wanted to tail one of the log files simultaneously on 12 servers this afternoon to try and see if a particular event was being logged and rather than opening 12 SSH sessions decided to get <a href="http://docs.fabfile.org/en/1.5/">Fabric</a> to help us out.</p>


<p>My initial attempt to do this was the following:</p>



~~~text

fab -H host1,host2,host3 -- tail -f /var/www/awesome/current/log/production.log
~~~

<p>It works but the problem is that by default Fabric runs the specified command <a href="http://docs.fabfile.org/en/1.4.4/usage/execution.html#execution-strategy">one machine after the other</a> so we've actually managed to block Fabric with the tail command on 'host1'.</p>
 

<p>The output of host1's log file will be printed to the terminal but nothing from the other two hosts.</p>


<p><a href="http://junctionbox.ca/">Nathan</a> showed me how to get around this problem by making use of Fabric's parallel execution which we can enable with the '-P' option:</p>



~~~text

fab -P --linewise -H host1,host2,host3 -- tail -f /var/www/awesome/current/log/production.log
~~~

<p>We also used the 'likewise' flag to ensure that data between the different tail processes didn't get mixed up although this wasn't necessary because Fabric <a href="http://docs.fabfile.org/en/1.4.4/usage/parallel.html">defaults to likewise if you're using parallel execution</a> mode anyway.</p>


<p>On a side-note, <a href="http://oobaloo.co.uk/kafka-for-uswitchs-event-pipeline">Paul Ingles wrote up the approach taken to make data from log files more accessible</a> using a Kafka driven event pipeline but in this case we haven't got round to wiring this data up yet so Fabric it is for now.</p>

