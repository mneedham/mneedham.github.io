+++
draft = false
date="2017-09-30 21:23:11"
title="AWS: Spinning up a Neo4j instance with APOC installed"
tag=['neo4j', 'aws', 'apoc', 'ami']
category=['neo4j']
description="Learn how to spin up an ES2 instance on AWS with Neo4j and the Awesome Procedures on Cypher (APOC) library installed by default."
+++

<p>
One of the first things I do after installing Neo4j is install the <a href="https://github.com/neo4j-contrib/neo4j-apoc-procedures/releases">APOC library</a>, but I find it's a bit of a manual process when spinning up a server on AWS so I wanted to simplify it a bit. 
</p>


<p>
There's already <a href="https://neo4j.com/developer/neo4j-cloud-aws-ec2-ami/">a Neo4j AMI which installs Neo4j 3.2.0</a> and my colleague <a href="https://twitter.com/mesirii">Michael</a> pointed out that we could download APOC into the correct folder by writing a script and sending it as <a href="http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-metadata.html#instancedata-add-user-data">UserData</a>.
</p>


<p>
I've been doing some work in JavaScript over the last two weeks so I thought I'd automate all the steps using the AWS library. You can <a href="https://gist.github.com/mneedham/0246221849ccf3646727d6b80977d85f">find the full script on GitHub</a>.
</p>


<p>The UserData part of the script is actually very simple:</p>


<p>
This script creates a key pair, security group, opens up that security group on ports 22 (SSH), 7474 (HTTP), 7473 (HTTPS), and 7687 (Bolt). The server created is <cite>m3.medium</cite>, but you can <a href="https://gist.github.com/mneedham/0246221849ccf3646727d6b80977d85f#file-neo4j-with-apoc-js-L38">change that</a> to <a href="https://aws.amazon.com/ec2/pricing/on-demand/">something else</a> if you prefer.
</p>



~~~bash

#!/bin/bash
curl -L https://github.com/neo4j-contrib/neo4j-apoc-procedures/releases/download/3.2.0.3/apoc-3.2.0.3-all.jar -O
sudo cp apoc-3.2.0.3-all.jar /var/lib/neo4j/plugins/
~~~

<p>We can run it like this:</p>



~~~bash

$ node neo4j-with-apoc.js 
Creating a Neo4j server
Key pair created. Save this to a file - you'll need to use it if you want to ssh into the Neo4j server
-----BEGIN RSA PRIVATE KEY-----
<Private key details>
-----END RSA PRIVATE KEY-----
Created Group Id:<Group Id>
Opened Neo4j ports
Instance Id: <Instance Id>
Your Neo4j server is now ready!
You'll need to login to the server and change the default password:
https://ec2-ip-address.compute-1.amazonaws.com:7473 or http://ec2-ip-address.compute-1.amazonaws.com:7474
User:neo4j, Password:<Instance Id>
~~~

<p>
We'll need to wait a few seconds for Neo4j to spin up, but it'll be accessible at the URI specified.
</p>


<p>
Once it's accessible we can login with the username <cite>neo4j</cite> and password <cite><AWS Instance Id></cite>. We'll then be instructed to choose a new password.
</p>


<p>
We can then run the following query to check that APOC has been installed:
</p>



~~~cypher

call dbms.procedures() YIELD name
WHERE name starts with "apoc"
RETURN count(*)

╒══════════╕
│"count(*)"│
╞══════════╡
│214       │
└──────────┘
~~~

<p>
Cool, it worked and we can now Neo4j and APOC to our heart's content! If we want to SSH into the server we can do that as well by first saving the private key printed on the command line to a file and then executing the following command:
</p>



~~~bash

$ cat aws-private-key.pem
-----BEGIN RSA PRIVATE KEY-----
<Private key details>
-----END RSA PRIVATE KEY-----

$ chmod 600 aws-private-key.pem

$ ssh -i aws-private-key.pem ubuntu@ec2-ip-address.compute-1.amazonaws.com
Welcome to Ubuntu 16.04.2 LTS (GNU/Linux 4.4.0-1013-aws x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  Get cloud support with Ubuntu Advantage Cloud Guest:
    http://www.ubuntu.com/business/services/cloud

106 packages can be updated.
1 update is a security update.

To run a command as administrator (user "root"), use "sudo <command>".
See "man sudo_root" for details.
~~~

<p>You can start/stop neo4j by running the following command:</p>



~~~bash

$ /etc/init.d/neo4j 
Usage: /etc/init.d/neo4j {start|stop|status|restart|force-reload}
~~~

<p>
The other commands you may be used to finding in the <cite>bin</cite> folder can be found here:
</p>



~~~bash

$ ls -lh /usr/share/neo4j/bin/
total 48K
-rwxr-xr-x 1 neo4j adm   15K May  9 09:22 neo4j
-rwxr-xr-x 1 neo4j adm  5.6K May  9 09:22 neo4j-admin
-rwxr-xr-x 1 root  root  612 May 12 00:03 neo4j-awspasswd
-rwxr-xr-x 1 neo4j adm  5.6K May  9 09:22 neo4j-import
-rwxr-xr-x 1 neo4j adm  5.6K May  9 09:22 neo4j-shell
drwxr-xr-x 2 neo4j adm  4.0K May 11 22:13 tools
~~~

<p>
Let me know if this is helpful and if you have any suggestions/improvements.
</p>

