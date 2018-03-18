+++
draft = false
date="2011-01-15 18:31:07"
title="mount_smbfs: mount error..File exists"
tag=['shell-scripting-2']
category=['Shell Scripting']
+++

I've been playing around with mounting a Windows file share onto my machine via the terminal because I'm getting bored of constantly having to go to Finder and manually mounting it each time!

After a couple of times of mounting and unmounting the drive I ended up with this error:


~~~text

> mount_smbfs //mneedham@punedc02/shared punedc02_shared/
mount_smbfs: mount error: /Volumes/punedc02_shared: File exists
~~~

I originally thought the 'file exists' part of the message was suggesting that I'd already mounted a share on 'punedc02_shared' but calling the 'umount' command led to the following error:


~~~text

> umount punedc02_shared
umount: punedc02_shared: not currently mounted
~~~

I had actually absent mindedly gone and mounted the drive elsewhere through Finder which I only realised after reading <a href="http://www.cmsimike.com/blog/2009/06/30/os-x-failure-mounting-via-shell/comment-page-1/#comment-7714">Victor's comments on this post</a>.

<blockquote>
Make sure that you already do not have the same share mounted on your Mac.

I had //host/share already mounted in /Volumes/share, so when I tried to mount //host/share to /Volumes/newshare it gave me the “file exists” error.
</blockquote>

I learnt, thanks to the <a href="http://www.unix.com/71392-post2.html">unix.com forums</a>, that you can see which devices are mounted by using 'df'.

This is where Finder had mounted the drive for me: 


~~~text

> df
Filesystem                 512-blocks      Used  Available Capacity  Mounted on
...
//mneedham@punedc02/shared  209696376 199773696    9922680    96%    /Volumes/shared
~~~

Since the shared drive gets unmounted when I disconnect from the network I decided to write a shell script that would set it up for me again.


~~~text

#!/bin/sh
function mount_drive {
  mkdir -p $2
  mount_smbfs $1 $2 
}

drives_to_unmount=`df | awk '/mneedham@punedc02/ { print $6 }'`

if [ "$drives_to_unmount" != "" ]; then
  echo "Unmounting existing drives on punedc02: \n$drives_to_unmount"
  umount $drives_to_unmount
fi

mount_drive //mneedham@punedc02/media /Volumes/punedc02_media 
mount_drive //mneedham@punedc02/shared /Volumes/punedc02_shared
~~~

At the moment I've just put that in '/usr/bin' so that it's available on the path.

If there's a better way to do this or a way to simplify the code please let me know.

I did come across a few ways to do the mounting using Apple Script in <a href="http://hints.macworld.com/article.php?story=20020610225855377">this post</a> but that's not half as fun as using the shell!

