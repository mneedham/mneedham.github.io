+++
draft = false
date="2013-04-13 11:17:37"
title="Capistrano: Deploying to a Vagrant VM"
tag=['devops-2']
category=['DevOps']
+++

<p>I've been working on a tutorial around thinking through problems in graphs using my football graph and I wanted to deploy it on a local <a href="http://www.vagrantup.com/">vagrant</a> VM as a stepping stone to deploying it in a live environment.</p>


<p>My Vagrant file for the VM looks like this:</p>



~~~text

# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant::Config.run do |config|
  config.vm.box = "precise64"

  config.vm.define :neo01 do |neo|
    neo.vm.network :hostonly, "192.168.33.101"
    neo.vm.host_name = 'neo01.local'
    neo.vm.forward_port 7474, 57474
    neo.vm.forward_port 80, 50080
  end

  config.vm.box_url = "http://files.vagrantup.com/precise64.box"

  config.vm.provision :puppet do |puppet|
    puppet.manifests_path = "puppet/manifests"
    puppet.manifest_file  = "site.pp"
    puppet.module_path = "puppet/modules"
  end
end
~~~

<p>I'm port forwarding ports 80 and 7474 to 50080 and 57474 respectively so that I can access the web app and neo4j console from my browser.</p>


<p>There is a bunch of puppet code to configure the machine in the location specified.</p>


<p>Since the web app is written in Ruby/Sinatra the easiest deployment tool to use is probably capistrano and I found the <a href="http://guides.beanstalkapp.com/deployments/deploy-with-capistrano.html">tutorial on the beanstalk website</a> really helpful for getting me setup.</p>


<p>My <cite>config/deploy.rb</cite> file which I've got Capistrano setup to read looks like this:</p>



~~~text

require 'capistrano/ext/multistage'

set :application, "thinkingingraphs"
set :scm, :git
set :repository,  "git@bitbucket.org:markhneedham/thinkingingraphs.git"
set :scm_passphrase, ""

set :ssh_options, {:forward_agent => true}
set :default_run_options, {:pty => true}
set :stages, ["vagrant"]
set :default_stage, "vagrant"
~~~

<p>In my <cite>config/deploy/vagrant.rb</cite> file I have the following:</p>



~~~text

set :user, "vagrant"
server "192.168.33.101", :app, :web, :db, :primary => true
set :deploy_to, "/var/www/thinkingingraphs"
~~~

<p>So that IP there is the same one that I assigned in Vagrantfile. If you didn't do that then you'd need to use 'vagrant ssh' to go onto the VM and then 'ifconfig' to grab the IP instead.</p>


<p>I figured there was probably another step required to tell Capistrano where it should get the vagrant public key from but I thought I'd try and deploy anyway just to see what would happen.</p>



~~~text

$ bundle exec cap deploy
~~~

<p>It asked me to enter the vagrant user's password which is 'vagrant' by default and I eventually found <a href="http://stackoverflow.com/questions/10353530/is-there-a-way-to-deploy-into-a-vagrant-vm-using-capistrano">a post on StackOverflow</a> which suggested changing the 'ssh_options' to the following:</p>



~~~text

set :ssh_options, {:forward_agent => true, keys: ['~/.vagrant.d/insecure_private_key']}
~~~

<p>And with that the deployment worked flawlessly! Happy days.</p>

