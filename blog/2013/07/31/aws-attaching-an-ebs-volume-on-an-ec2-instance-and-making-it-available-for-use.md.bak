+++
draft = false
date="2013-07-31 06:21:42"
title="AWS: Attaching an EBS volume on an EC2 instance and making it available for use"
tag=['software-development']
category=['Software Development']
+++

<p>I recently wanted to attach an EBS volume to an existing EC2 instance that I had running and since it was for a one off tasks (famous last words) I decided to configure it manually.</p>


<p>I created the EBS volume through the AWS console and one thing that initially caught me out is that the EC2 instance and EBS volume need to be in the <strong>same region and zone</strong>.</p>


<p>Therefore if I create my EC2 instance in 'eu-west-1b' then I need to create my EBS volume in 'eu-west-1b' as well otherwise I won't be able to attach it to that instance.</p>


<p>I attached the device as <cite>/dev/sdf</cite> although the UI gives the following warning:</p>


<blockquote>	
Linux Devices: /dev/sdf through /dev/sdp
Note: Newer linux kernels may rename your devices to /dev/xvdf through /dev/xvdp internally, even when the device name entered here (and shown in the details) is /dev/sdf through /dev/sdp.
</blockquote>

<p>After attaching the EBS volume to the EC2 instance my next step was to SSH onto my EC2 instance and <a href="http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-using-volumes.html">make the EBS volume available</a>.</p>


<p>The first step is to create a file system on the volume:</p>



~~~bash

$ sudo mkfs -t ext3 /dev/sdf
mke2fs 1.42 (29-Nov-2011)
Could not stat /dev/sdf --- No such file or directory

The device apparently does not exist; did you specify it correctly?
~~~

<p>It turns out that warning was handy and the device has in fact been renamed. We can confirm this by calling <cite>fdisk</cite>:</p>



~~~bash

$ sudo fdisk -l

Disk /dev/xvda1: 8589 MB, 8589934592 bytes
255 heads, 63 sectors/track, 1044 cylinders, total 16777216 sectors
Units = sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disk identifier: 0x00000000

Disk /dev/xvda1 doesn't contain a valid partition table

Disk /dev/xvdf: 53.7 GB, 53687091200 bytes
255 heads, 63 sectors/track, 6527 cylinders, total 104857600 sectors
Units = sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disk identifier: 0x00000000

Disk /dev/xvdf doesn't contain a valid partition table
~~~

<p><cite>/dev/xvdf</cite> is the one we're interested in so I re-ran the previous command:</p>



~~~bash

$ sudo mkfs -t ext3 /dev/xvdf
mke2fs 1.42 (29-Nov-2011)
Filesystem label=
OS type: Linux
Block size=4096 (log=2)
Fragment size=4096 (log=2)
Stride=0 blocks, Stripe width=0 blocks
3276800 inodes, 13107200 blocks
655360 blocks (5.00%) reserved for the super user
First data block=0
Maximum filesystem blocks=4294967296
400 block groups
32768 blocks per group, 32768 fragments per group
8192 inodes per group
Superblock backups stored on blocks:
	32768, 98304, 163840, 229376, 294912, 819200, 884736, 1605632, 2654208,
	4096000, 7962624, 11239424

Allocating group tables: done
Writing inode tables: done
Creating journal (32768 blocks): done
Writing superblocks and filesystem accounting information: done
~~~

<p>Once I'd done that I needed to create a mount point for the volume and I thought the best place was probably a directory under <cite>/mnt</cite>:</p>



~~~bash

$ sudo mkdir /mnt/ebs
~~~

<p>The final step is to mount the volume:</p>



~~~bash

$ sudo mount /dev/xvdf /mnt/ebs
~~~

<p>And if we run <cite>df</cite> we can see that it's ready to go:</p>



~~~bash

$ df -h
Filesystem      Size  Used Avail Use% Mounted on
/dev/xvda1      7.9G  883M  6.7G  12% /
udev            288M  8.0K  288M   1% /dev
tmpfs           119M  164K  118M   1% /run
none            5.0M     0  5.0M   0% /run/lock
none            296M     0  296M   0% /run/shm
/dev/xvdf        50G  180M   47G   1% /mnt/ebs
~~~
