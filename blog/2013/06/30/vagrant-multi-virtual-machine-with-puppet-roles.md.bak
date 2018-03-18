+++
draft = false
date="2013-06-30 13:13:14"
title="Vagrant: Multi (virtual) machine with Puppet roles"
tag=['vagrant']
category=['Software Development']
+++

<p>I've been playing around with setting up a <a href="http://docs.neo4j.org/chunked/stable/ha-haproxy.html">neo4j cluster</a> using Vagrant and HAProxy and one thing I wanted to do was define two different roles for the HAProxy and neo4j machines.</p>


<p>When I was working at <a href="http://www.uswitch.com/">uSwitch</a> <a href="http://junctionbox.ca/">Nathan</a> had solved a similar problem, but with AWS VMs, by defining the role in an environment variable in the VM's spin up script.</p>


<p>In retrospect I think I might have been able to do that by using the <a href="http://docs.vagrantup.com/v2/provisioning/shell.html">shell provisioner</a> and calling that before the <a href="http://docs.vagrantup.com/v2/provisioning/puppet_apply.html">puppet provisioner</a> but Nathan, <a href="https://twitter.com/garethr">Gareth Rushgrove</a> and <a href="https://twitter.com/russbuelt">Gregor Russbuelt</a> suggested that using <a href="http://puppetlabs.com/puppet/related-projects/facter/">facter</a> might be better.</p>


<p>When I initially looked at the 'Custom Facts' section of <a href="http://docs.vagrantup.com/v2/provisioning/puppet_apply.html">the docs</a> I thought it was only possible to set facts for the Vagrant file as a whole but you can actually do it on a per VM basis which is neat.</p>


<p>I added a method called 'provision_as_role' to the 'Vagrant::Config::V2::Root' class:</p>



~~~ruby

module Vagrant
  module Config
    module V2
      class Root
        def provision_as_role(role)
          vm.provision :puppet do |puppet|
            puppet.manifests_path = "puppet/manifests"
            puppet.module_path = "puppet/modules"
            puppet.manifest_file  = "base.pp"
            puppet.facter = { "role" => role.to_s }
          end 
        end
      end
    end
  end
end
~~~

<p>and then passed in a role depending on the VM in my Vagrantfile:</p>



~~~ruby

require File.join(File.dirname(__FILE__), 'lib', 'root.rb')

Vagrant.configure("2") do |config|  
  config.vm.box = "precise64"
  config.vm.box_url = "http://files.vagrantup.com/precise64.box"
 
  config.vm.define :neo01 do |neo| 
    neo.vm.hostname = "neo01"
    neo.vm.network :private_network, ip: "192.168.33.101"    
    neo.provision_as_role :neo
  end

  config.vm.define :lb01 do |lb|
    lb.vm.hostname = "lb01"
    lb.vm.network :private_network, ip: "192.168.33.104"    
    lb.provision_as_role :lb
  end
end
~~~

<p>We can now access the variable '$role' in our puppet code which I used like so:</p>


<cite>puppet/base.pp</cite>

~~~puppet

class all_the_things {
  exec { 'apt-get update': command => '/usr/bin/apt-get update'; }
  package { 'curl': ensure => '7.22.0-3ubuntu4', }
  class { 'apt': }
}

node default {
  class { 'all_the_things': }
  class { $role:
    require => Class['all_the_things']
  }
} 
~~~

<p>The 'neo' and 'lb' classes look like this:</p>



~~~puppet

class neo {
  class { 'java': version => '7u25-0~webupd8~1', }
  class { 'neo4j': require     => Class['java'], }
}
~~~


~~~puppet

class lb {
  class { 'haproxy':  }
}
~~~

<p>The full code is on <a href="https://github.com/mneedham/haproxy-neo4j">github</a> but it's behaving a bit weirdly in some scenarios so I'm still trying to get it properly working.</p>

