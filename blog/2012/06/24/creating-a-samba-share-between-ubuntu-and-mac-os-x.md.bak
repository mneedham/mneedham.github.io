+++
draft = false
date="2012-06-24 00:40:35"
title="Creating a Samba share between Ubuntu and Mac OS X"
tag=['software-development']
category=['Software Development']
+++

On the project I'm currently working on we have our development environment setup on a bare bones Ubuntu instance which we run via VmWare. 

We wanted to be able to edit files on the VM from the host O/S so my colleague <a href="http://twitter.com/philandstuff">Phil</a> suggested that we set up a Samba server on the VM and then connect to it from the Mac.

We first needed to install a couple of packages on the VM:

<ul>
<li>apt-get install samba</li>
<li>apt-get install libpam-smbpass</li>
</ul>

The first package is self explanatory and the second allows us to keep the samba username/password in sync with the unix user on the VM.

Installing the samba package will automatically start up the Samba daemon 'smbd'. 


~~~text

$ ps aux | grep smbd
mneedham 10915  0.0  0.0   7624   928 pts/14   S+   17:37   0:00 grep --color=auto smbd
root     32610  0.0  0.1  95372  5408 ?        S    Jun22   0:50 smbd -F
~~~

We then need to edit <cite>/etc/samba/smb.conf</cite>:

First we uncomment this line:


~~~text

security = user
~~~

Then add a share, probably at the bottom of the file but anywhere is fine:


~~~text

[mneedham]
comment = Mark's vm
read only = no
path = /home/mneedham
guest ok = no
browseable = yes
create mask = 0644
~~~

From the Mac we need to mount the share:

<ul>
<li>Go to finder</li>
<li>Connect to server (Cmd - K)</li>
<li>Type in 'smb://ip.of-vm</li>
<li>Select the name of the share</li>
</ul>

The share should now be accessible from the host O/S at <cite>/Volumes/name.of.share</cite>

Looking back I'm sure there's a way to configure VmWare to share files from the guest O/S but at least I now know another way to do it as well!
