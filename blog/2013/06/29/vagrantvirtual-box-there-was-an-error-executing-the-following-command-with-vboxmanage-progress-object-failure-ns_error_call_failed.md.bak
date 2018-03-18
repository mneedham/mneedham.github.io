+++
draft = false
date="2013-06-29 07:38:35"
title="Vagrant/Virtual Box: There was an error executing the following command with VBoxManage - Progress object failure: NS_ERROR_CALL_FAILED"
tag=['vagrant', 'virtualbox']
category=['Software Development']
+++

<p>I've been playing around with <a href="http://www.vagrantup.com/">Vagrant</a> a bit again lately and having installed it on a new machine was running into the following exception when I tried to run 'vagrant up' on a new virtual machine:</p>



~~~text

ERROR vagrant: /Applications/Vagrant/embedded/gems/gems/vagrant-1.1.2/plugins/providers/virtualbox/driver/base.rb:292:in `block in execute'
/Applications/Vagrant/embedded/gems/gems/vagrant-1.1.2/lib/vagrant/util/retryable.rb:17:in `retryable'
/Applications/Vagrant/embedded/gems/gems/vagrant-1.1.2/plugins/providers/virtualbox/driver/base.rb:282:in `execute'
/Applications/Vagrant/embedded/gems/gems/vagrant-1.1.2/plugins/providers/virtualbox/driver/version_4_2.rb:165:in `import'
/Applications/Vagrant/embedded/gems/gems/vagrant-1.1.2/plugins/providers/virtualbox/action/import.rb:15:in `call'
/Applications/Vagrant/embedded/gems/gems/vagrant-1.1.2/lib/vagrant/action/warden.rb:34:in `call'
/Applications/Vagrant/embedded/gems/gems/vagrant-1.1.2/lib/vagrant/action/builtin/handle_box_url.rb:38:in `call'
/Applications/Vagrant/embedded/gems/gems/vagrant-1.1.2/lib/vagrant/action/warden.rb:34:in `call'
/Applications/Vagrant/embedded/gems/gems/vagrant-1.1.2/plugins/providers/virtualbox/action/check_accessible.rb:18:in `call'
/Applications/Vagrant/embedded/gems/gems/vagrant-1.1.2/lib/vagrant/action/warden.rb:34:in `call'
/Applications/Vagrant/embedded/gems/gems/vagrant-1.1.2/lib/vagrant/action/runner.rb:61:in `block in run'
/Applications/Vagrant/embedded/gems/gems/vagrant-1.1.2/lib/vagrant/util/busy.rb:19:in `busy'
/Applications/Vagrant/embedded/gems/gems/vagrant-1.1.2/lib/vagrant/action/runner.rb:61:in `run'
/Applications/Vagrant/embedded/gems/gems/vagrant-1.1.2/lib/vagrant/action/builtin/call.rb:51:in `call'
/Applications/Vagrant/embedded/gems/gems/vagrant-1.1.2/lib/vagrant/action/warden.rb:34:in `call'
/Applications/Vagrant/embedded/gems/gems/vagrant-1.1.2/lib/vagrant/action/builtin/config_validate.rb:25:in `call'
/Applications/Vagrant/embedded/gems/gems/vagrant-1.1.2/lib/vagrant/action/warden.rb:34:in `call'
/Applications/Vagrant/embedded/gems/gems/vagrant-1.1.2/plugins/providers/virtualbox/action/check_virtualbox.rb:17:in `call'
/Applications/Vagrant/embedded/gems/gems/vagrant-1.1.2/lib/vagrant/action/warden.rb:34:in `call'
/Applications/Vagrant/embedded/gems/gems/vagrant-1.1.2/lib/vagrant/action/builder.rb:109:in `call'
/Applications/Vagrant/embedded/gems/gems/vagrant-1.1.2/lib/vagrant/action/runner.rb:61:in `block in run'
/Applications/Vagrant/embedded/gems/gems/vagrant-1.1.2/lib/vagrant/util/busy.rb:19:in `busy'
/Applications/Vagrant/embedded/gems/gems/vagrant-1.1.2/lib/vagrant/action/runner.rb:61:in `run'
/Applications/Vagrant/embedded/gems/gems/vagrant-1.1.2/lib/vagrant/machine.rb:129:in `action'
/Applications/Vagrant/embedded/gems/gems/vagrant-1.1.2/plugins/commands/up/command.rb:37:in `block in execute'
/Applications/Vagrant/embedded/gems/gems/vagrant-1.1.2/lib/vagrant/plugin/v2/command.rb:182:in `block in with_target_vms'
/Applications/Vagrant/embedded/gems/gems/vagrant-1.1.2/lib/vagrant/plugin/v2/command.rb:180:in `each'
/Applications/Vagrant/embedded/gems/gems/vagrant-1.1.2/lib/vagrant/plugin/v2/command.rb:180:in `with_target_vms'
/Applications/Vagrant/embedded/gems/gems/vagrant-1.1.2/plugins/commands/up/command.rb:32:in `execute'
/Applications/Vagrant/embedded/gems/gems/vagrant-1.1.2/lib/vagrant/cli.rb:46:in `execute'
/Applications/Vagrant/embedded/gems/gems/vagrant-1.1.2/lib/vagrant/environment.rb:406:in `cli'
/Applications/Vagrant/embedded/gems/gems/vagrant-1.1.2/bin/vagrant:60:in `<top (required)>'
/Applications/Vagrant/bin/../embedded/gems/bin/vagrant:23:in `load'
/Applications/Vagrant/bin/../embedded/gems/bin/vagrant:23:in `<main>'
 INFO interface: error: There was an error executing the following command with VBoxManage:

["import", "/Users/markneedham/.vagrant.d/boxes/precise32/virtualbox/box.ovf"]
~~~

<p>I tried running the command directly against Virtual Box to see if that would tell me anything else but it didn't shed much light:</p>



~~~text

$ VBoxManage import "/Users/markneedham/.vagrant.d/boxes/precise32/virtualbox/box.ovf"
0%...10%...20%...30%...40%...50%...60%...70%...80%...90%...100%
Interpreting /Users/markneedham/.vagrant.d/boxes/precise32/virtualbox/box.ovf...
OK.
Disks:  vmdisk1	85899345920	-1	http://www.vmware.com/interfaces/specifications/vmdk.html#streamOptimized	box-disk1.vmdk	-1	-1
Virtual system 0:
 0: Suggested OS type: "Ubuntu_64"
    (change with "--vsys 0 --ostype <type>"; use "list ostypes" to list all possible values)
 1: Suggested VM name "precise64"
    (change with "--vsys 0 --vmname <name>")
 2: Number of CPUs: 2
    (change with "--vsys 0 --cpus <n>")
 3: Guest memory: 384 MB
    (change with "--vsys 0 --memory <MB>")
 4: Network adapter: orig NAT, config 3, extra slot=0;type=NAT
 5: CD-ROM
    (disable with "--vsys 0 --unit 5 --ignore")
 6: IDE controller, type PIIX4
    (disable with "--vsys 0 --unit 6 --ignore")
 7: IDE controller, type PIIX4
    (disable with "--vsys 0 --unit 7 --ignore")
 8: SATA controller, type AHCI
    (disable with "--vsys 0 --unit 8 --ignore")
 9: Hard disk image: source image=box-disk1.vmdk, target path=/Users/markneedham/VirtualBox VMs/precise64/box-disk1.vmdk, controller=8;channel=0
    (change target path with "--vsys 0 --unit 9 --disk path";
    disable with "--vsys 0 --unit 9 --ignore")
0%...
Progress object failure: NS_ERROR_CALL_FAILED
~~~

<p>That gave me enough information to Google my way to <a href="https://github.com/mitchellh/vagrant/issues/1847">an issue on github</a> where it was suggested that this was a problem with VirtualBox 4.2.14 and that downgrading with 4.2.10 would more profitable.</p>


<p>As I'd downloaded the latest VirtualBox the version I had was indeed 4.2.14:</p>



~~~bash

$ VBoxManage --version
4.2.14r86644
~~~

</p>
I grabbed <a href="https://www.virtualbox.org/wiki/Download_Old_Builds_4_2">an older copy</a> of Virtual Box and that seemed to do the trick although I later ran into a problem which I foolishly haven't kept the stack trace of and found that upgrading my vagrant version solved that.<p>

<p>So to summarise, my current versions of vagrant and Virtual Box which work splendidly:</p>



~~~bash

$ vagrant -v
Vagrant version 1.2.2

$ VBoxManage -version
4.2.10r84104
~~~ 

<p>YMMV and all that!</p>

