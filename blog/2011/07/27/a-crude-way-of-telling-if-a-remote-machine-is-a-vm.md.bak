+++
draft = false
date="2011-07-27 22:31:20"
title="A crude way of telling if a remote machine is a VM"
tag=['software-development']
category=['Software Development']
+++

We were doing a bit of profiling of a data importing process we've been running across various environments and wanted to check whether or not one of the environments was a physical machine or a VM.

A bit of googling first led me to <a href="http://www.coffer.com/mac_find/">the following site</a> where you can fill a MAC address and it will tell you which vendor it belongs to.

<a href="http://www.macvendorlookup.com">macvendorlookup.com</a> is even better though because it's more easily scriptable!

If I wanted to find the vendor of my MAC address on the ethernet port I could try the following:


~~~text

ifconfig | grep -A1 en1 | grep ether | cut -d" " -f2 | xargs -I {} curl -s http://www.macvendorlookup.com/getoui.php?mac={} -o - | sed -e :a -e 's/<[^>]*>//g;/</N;//ba'
~~~

Which gives:


~~~text

Vendor: Apple Inc
~~~

Sed magic was shamelessly stolen from <a href="http://www.eng.cam.ac.uk/help/tpl/unix/sed.html">sed one liners</a>. 

As it turns out the machine we wanted to learn about was a VM hosted on VMWare!
