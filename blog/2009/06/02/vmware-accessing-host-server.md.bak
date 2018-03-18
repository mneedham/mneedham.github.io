+++
draft = false
date="2009-06-02 21:36:46"
title="VMware: Accessing host server"
tag=['vmware']
category=['Software Development']
+++

I've been doing all my spare time .NET development from within VMWare for about the last year or so and now and then it's quite useful to be able to access the host machine either to get some files from there or to access a server that's running on the host.

The former problem is solved by going to 'Virtual Machines -> Shared Folders' and clicking on the + button on the bottom left of the menu to add a folder that you want to share.

This folder will be accessible by going to  'My Network Places -> Entire Network -> VMWare Shared Folders -> .host -> Shared Folders' from Windows Explorer or by typing '\\.host\Shared Folders' into the Windows Explorer address bar.

The latter is something I'd not wanted to do until today when I wanted to access a CouchDB server I had running via <a href="http://janl.github.com/couchdbx/">CouchDBX</a> (thanks to <a href="http://twitter.com/jchris/statuses/1996608145">J Chris Anderson for the recommendation</a>) from a .NET application that I was running inside VMWare.

From the host environment I can view all the databases in CouchDB by going to 'http://127.0.0.1:5984/_utils' but from VMWare I need to make use of the Gateway IP address which can be found by typing 'ipconfig' at the command prompt inside the VM.

The database listing is now available at 'http://the.gateway.ip:5984/_utils'.
 
