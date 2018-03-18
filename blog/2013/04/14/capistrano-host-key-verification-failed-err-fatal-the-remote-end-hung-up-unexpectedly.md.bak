+++
draft = false
date="2013-04-14 18:18:32"
title="Capistrano: Host key verification failed. ** [err] fatal: The remote end hung up unexpectedly"
tag=['capistrano']
category=['DevOps']
+++

<p>As I mentioned in <a href="http://www.markhneedham.com/blog/2013/04/13/capistrano-deploying-to-a-vagrant-vm/">my previous post</a> I've been deploying a web application to a vagrant VM using Capistrano and my initial configuration was like so:</p>



~~~text

require 'capistrano/ext/multistage'

set :application, "thinkingingraphs"
set :scm, :git
set :repository,  "git@bitbucket.org:markhneedham/thinkingingraphs.git"
set :scm_passphrase, ""

set :ssh_options, {:forward_agent => true, :paranoid => false, keys: ['~/.vagrant.d/insecure_private_key']}
set :stages, ["vagrant"]
set :default_stage, "vagrant"

set :user, "vagrant"
server "192.168.33.101", :app, :web, :db, :primary => true
set :deploy_to, "/var/www/thinkingingraphs"
~~~

<p>When I ran 'cap deploy' I ended up with the following error:</p>



~~~text

  * executing "git clone -q git@bitbucket.org:markhneedham/thinkingingraphs.git /var/www/thinkingingraphs/releases/20130414171523 && cd /var/www/thinkingingraphs/releases/20130414171523 && git checkout -q -b deploy 6dcbf945ef5b8a5d5d39784800f4a6b7731c7d8a && (echo 6dcbf945ef5b8a5d5d39784800f4a6b7731c7d8a > /var/www/thinkingingraphs/releases/20130414171523/REVISION)"
    servers: ["192.168.33.101"]
    [192.168.33.101] executing command
 ** [192.168.33.101 :: err] Host key verification failed.
 ** [192.168.33.101 :: err] fatal: The remote end hung up unexpectedly
~~~

<p>As far as I can tell the reason for this is that bitbucket hasn't been verified as a host by the VM and therefore the equivalent of the following happens when it tries to clone the repository:</p>



~~~text

$ ssh git@bitbucket.org
The authenticity of host 'bitbucket.org (207.223.240.182)' can't be established.
RSA key fingerprint is 97:8c:1b:f2:6f:14:6b:5c:3b:ec:aa:46:46:74:7c:40.
Are you sure you want to continue connecting (yes/no)?
~~~

<p>Since we aren't answering 'yes' to that question and bitbucket isn't in our <cite>~/.ssh/known_hosts</cite> file it's not able to continue.</p>


<p>One solution to this problem is to run the ssh command above and then answer 'yes' to the question which will add bitbucket to our known_hosts file and we can then run 'cap deploy' again.</p>


<p>It's a bit annoying to have that manual step though so another way is to set cap to use pty by putting the following line in our config file:</p>



~~~text

set :default_run_options, {:pty => true}
~~~

<p>Now when we run 'cap deploy' we can see that bitbucket automatically gets added to the known_hosts file:</p>



~~~text

    servers: ["192.168.33.101"]
    [192.168.33.101] executing command
 ** [192.168.33.101 :: out] The authenticity of host 'bitbucket.org (207.223.240.181)' can't be established.
 ** RSA key fingerprint is 97:8c:1b:f2:6f:14:6b:5c:3b:ec:aa:46:46:74:7c:40.
 ** Are you sure you want to continue connecting (yes/no)?
 ** [192.168.33.101 :: out] yes
 ** [192.168.33.101 :: out] Warning: Permanently added 'bitbucket.org,207.223.240.181' (RSA) to the list of known hosts.
~~~

<p>As far as I can tell this runs the command using a pseudo terminal and then automatically adds bitbucket into the known_hosts file but I'm not entirely sure how that works. My google skillz have also failed me so if anyone can explain it to me that'd be cool</p>

