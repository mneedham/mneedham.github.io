+++
draft = false
date="2013-06-29 08:44:00"
title="Vagrant 1.2.2: `[]': can't convert Symbol into Integer (TypeError)/The following settings don't exist"
tag=['vagrant']
category=['Software Development']
+++

<p>As I mentioned in my previous post I've been playing around with Vagrant for the past couple of days and I was trying to adapt a <a href="https://gist.github.com/nfisher/4982076">Vagrantfile that Nathan created</a> a few months ago to do what I wanted.</p>


<p>I'm using Vagrant 1.2.2 and I started out with the following Vagrantfile:</p>



~~~ruby

Vagrant.configure("2") do |config|   
  config.vm.box = "precise64"
  config.vm.box_url = "http://files.vagrantup.com/precise64.box"

  config.vm.define :neo01 do |neo|    
    neo.vm.network :hostonly, "192.168.33.101"
    neo.vm.forward_port 8080, 4569
  end
end
~~~

<p>Unfortunately a 'vagrant up' doesn't quite work as expected:</p>



~~~bash

$ vagrant up
/Applications/Vagrant/embedded/gems/gems/vagrant-1.2.2/plugins/kernel_v2/config/vm.rb:146:in `[]': can't convert Symbol into Integer (TypeError)
	from /Applications/Vagrant/embedded/gems/gems/vagrant-1.2.2/plugins/kernel_v2/config/vm.rb:146:in `network'
	from /Users/markneedham/projects/support/haproxy/Vagrantfile:19:in `block (2 levels) in <top (required)>'
	from /Applications/Vagrant/embedded/gems/gems/vagrant-1.2.2/lib/vagrant/config/v2/loader.rb:37:in `call'
	from /Applications/Vagrant/embedded/gems/gems/vagrant-1.2.2/lib/vagrant/config/v2/loader.rb:37:in `load'
	from /Applications/Vagrant/embedded/gems/gems/vagrant-1.2.2/lib/vagrant/config/loader.rb:104:in `block (2 levels) in load'
	from /Applications/Vagrant/embedded/gems/gems/vagrant-1.2.2/lib/vagrant/config/loader.rb:98:in `each'
	from /Applications/Vagrant/embedded/gems/gems/vagrant-1.2.2/lib/vagrant/config/loader.rb:98:in `block in load'
	from /Applications/Vagrant/embedded/gems/gems/vagrant-1.2.2/lib/vagrant/config/loader.rb:95:in `each'
	from /Applications/Vagrant/embedded/gems/gems/vagrant-1.2.2/lib/vagrant/config/loader.rb:95:in `load'
	from /Applications/Vagrant/embedded/gems/gems/vagrant-1.2.2/lib/vagrant/environment.rb:329:in `machine'
	from /Applications/Vagrant/embedded/gems/gems/vagrant-1.2.2/lib/vagrant/plugin/v2/command.rb:131:in `block in with_target_vms'
	from /Applications/Vagrant/embedded/gems/gems/vagrant-1.2.2/lib/vagrant/plugin/v2/command.rb:164:in `call'
	from /Applications/Vagrant/embedded/gems/gems/vagrant-1.2.2/lib/vagrant/plugin/v2/command.rb:164:in `block in with_target_vms'
	from /Applications/Vagrant/embedded/gems/gems/vagrant-1.2.2/lib/vagrant/plugin/v2/command.rb:163:in `map'
	from /Applications/Vagrant/embedded/gems/gems/vagrant-1.2.2/lib/vagrant/plugin/v2/command.rb:163:in `with_target_vms'
	from /Applications/Vagrant/embedded/gems/gems/vagrant-1.2.2/plugins/commands/up/command.rb:42:in `block in execute'
	from /Applications/Vagrant/embedded/gems/gems/vagrant-1.2.2/lib/vagrant/environment.rb:206:in `block (2 levels) in batch'
	from /Applications/Vagrant/embedded/gems/gems/vagrant-1.2.2/lib/vagrant/environment.rb:204:in `tap'
	from /Applications/Vagrant/embedded/gems/gems/vagrant-1.2.2/lib/vagrant/environment.rb:204:in `block in batch'
	from <internal:prelude>:10:in `synchronize'
	from /Applications/Vagrant/embedded/gems/gems/vagrant-1.2.2/lib/vagrant/environment.rb:203:in `batch'
	from /Applications/Vagrant/embedded/gems/gems/vagrant-1.2.2/plugins/commands/up/command.rb:41:in `execute'
	from /Applications/Vagrant/embedded/gems/gems/vagrant-1.2.2/lib/vagrant/cli.rb:46:in `execute'
	from /Applications/Vagrant/embedded/gems/gems/vagrant-1.2.2/lib/vagrant/environment.rb:467:in `cli'
	from /Applications/Vagrant/embedded/gems/gems/vagrant-1.2.2/bin/vagrant:84:in `<top (required)>'
	from /Applications/Vagrant/bin/../embedded/gems/bin/vagrant:23:in `load'
	from /Applications/Vagrant/bin/../embedded/gems/bin/vagrant:23:in `<main>'
~~~

<p>The problem line is 'neo.vm.network :hostonly, "192.168.33.101"' which I learnt is because <a href="https://github.com/mitchellh/vagrant/issues/1628">the way you setup networking has changed slightly between the versions</a>.</p>


<p>We now need something like this:</p>



~~~ruby

Vagrant.configure("2") do |config|   
  config.vm.box = "precise64"
  config.vm.box_url = "http://files.vagrantup.com/precise64.box"

  config.vm.define :neo01 do |neo|    
    neo.vm.network :private_network, ip: "192.168.33.101"
    neo.vm.forward_port 8080, 4569
  end
end
~~~

<p>If we run 'vagrant up' again we'll see that error has been removed and we have a new one!</p>



~~~bash

$ vagrant up
Bringing machine 'neo01' up with 'virtualbox' provider...
There are errors in the configuration of this machine. Please fix
the following errors and try again:

vm:
* The following settings don't exist: forward_port
~~~

<p>It turns out the way that we do port forwarding has also changed. Annoyingly if you google 'vagrant port forwarding' it still points you to the <a href="http://docs-v1.vagrantup.com/v1/docs/getting-started/ports.html">old documentation</a> rather than the <a href="http://docs.vagrantup.com/v2/getting-started/networking.html">newer one</a>.</p>


<p>We need to change our code to the following:</p>



~~~ruby

Vagrant.configure("2") do |config|   
  config.vm.box = "precise64"
  config.vm.box_url = "http://files.vagrantup.com/precise64.box"

  config.vm.define :neo01 do |neo|    
    neo.vm.network :private_network, ip: "192.168.33.101"
    neo.vm.network :forwarded_port, host: 4569, guest: 8080
  end
end
~~~

<p>If we run 'vagrant up' now it's much happier:</p>



~~~bash

$ vagrant up
Bringing machine 'neo01' up with 'virtualbox' provider...
[neo01] Setting the name of the VM...
[neo01] Clearing any previously set forwarded ports...
...
~~~
