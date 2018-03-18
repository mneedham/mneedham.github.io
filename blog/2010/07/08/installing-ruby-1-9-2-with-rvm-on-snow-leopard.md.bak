+++
draft = false
date="2010-07-08 13:10:32"
title="Installing Ruby 1.9.2 with RVM on Snow Leopard"
tag=['ruby']
category=['Ruby']
+++

Yesterday evening I decided to try and upgrade the Ruby installation on my Mac from 1.8.7 to 1.9.2 and went on the yak shaving mission which is doing just that.

<div align="center">
<a href="http://www.flickr.com/photos/revcyborg/22883042/in/photostream/"><img src="http://farm1.static.flickr.com/17/22883042_01f3a1a3d2.jpg" border="0" width="300"   /></a>
</div>

<a href="http://rvm.beginrescueend.com/rvm/install/">RVM</a> seems to be the way to install Ruby these days so I started off by installing that with the following command from the terminal:


~~~text

bash < <( curl http://rvm.beginrescueend.com/releases/rvm-install-head )
~~~

That bit worked fine for me but there are further instructions on the RVM website if that doesn't work.

My colleague <a href="http://www.ilovemartinfowler.com">David Santoro</a> pointed me to <a href="http://asciicasts.com/episodes/200-rails-3-beta-and-rvm">a post on ASCIIcasts detailing the various steps to follow to get Ruby installed</a>.

Unfortunately my first attempt...


~~~text

rvm install 1.9.2
~~~

...resulted in the following error in the log file:


~~~text

yaml.h is missing. Please install libyaml.
readline.c: In function ‘username_completion_proc_call’:
readline.c:1292: error: ‘username_completion_function’ undeclared (first use in this function)
readline.c:1292: error: (Each undeclared identifier is reported only once
readline.c:1292: error: for each function it appears in.)
make[1]: *** [readline.o] Error 1
make: *** [mkmain.sh] Error 1
~~~

I thought that perhaps 'libyaml' was the problem but <a href="http://michaelguterl.com/">Michael Guterl</a> pointed me to <a href="http://groups.google.com/group/rubyversionmanager/browse_thread/thread/364c2366f67c3d55">a post on the RVM mailing list</a> which suggests this was a red herring and that the real problem was 'readline'.

That led me back to <a href="http://rvm.beginrescueend.com/packages/readline/">a post on the RVM website which explains how to install 'readline' and then tell RVM to use that version of readline when installing Ruby</a>.

I tried that and then ran the following command as suggested on Mark Turner's <a href="http://amerine.net/2010/02/24/rvm-rails3-ruby-1-9-2-setup.html">blog post</a>:


~~~text

rvm install 1.9.2-head -C --enable-shared,--with-readline-dir=/opt/local,--build=x86_64-apple-darwin10
~~~

That resulted in this error:


~~~text

ld: in /usr/local/lib/libxml2.2.dylib, file was built for i386 which is not the architecture being linked (x86_64)
collect2: ld returned 1 exit status
make[1]: *** [../../.ext/x86_64-darwin10/tcltklib.bundle] Error 1
make: *** [mkmain.sh] Error 1
~~~

Michael pointed out that I needed to <a href="https://gist.github.com/dbaee0a06702f6441e0f">recompile 'libxml2.2' to run on a 64 bit O/S</a> as I'm running Snow Leopard.

I hadn't previously used the 'file' function which allows you to see which architecture a file has been compiled for.

e.g.


~~~text

file /usr/local/lib/libxml2.2.dylib

/usr/local/lib/libxml2.2.dylib: Mach-O dynamically linked shared library i386
~~~

I had to recompile 'libxml2.2' to run on a 64 bit O/S which I did by downloading the distribution from the <a href="ftp://xmlsoft.org/libxml2/">xmlsoft website</a> and then running the following commands:


~~~text

tar xzvf libxml2-2.7.3.tar.gz 
cd libxml2-2.7.3
./configure --with-python=/System/Library/Frameworks/Python.framework/Versions/2.3/
make
sudo make install
~~~

Re-running RVM Ruby installation command I then had this error instead:


~~~text

tcltklib.c:9539: warning: implicit conversion shortens 64-bit value into a 32-bit value
ld: in /usr/local/lib/libsqlite3.dylib, file was built for i386 which is not the architecture being linked (x86_64)
collect2: ld returned 1 exit status
make[1]: *** [../../.ext/x86_64-darwin10/tcltklib.bundle] Error 1
make: *** [mkmain.sh] Error 1
~~~


I downloaded the <a href="http://www.sqlite.org/sqlite-amalgamation-3.6.23.1.tar.gz">sqlite3 distribution</a> and having untarred the file ran the following commands <a href="http://osdir.com/ml/sqlite-users/2010-05/msg00477.html">as detailed on this post</a>:


~~~text

CFLAGS='-arch i686 -arch x86_64' LDFLAGS='-arch i686 -arch x86_64' 
./configure --disable-dependency-tracking
make
sudo make install
~~~

Next I needed to recompiled 'libxslt' which I downloaded from the <a href="ftp://xmlsoft.org/libxslt/">xmlsoft website</a> as well before untarring it and running the following:


~~~text

./configure
make
sudo make install
~~~

Having done that I re-ran the RVM Ruby installation command:


~~~text

rvm install 1.9.2-head -C --enable-shared,--with-readline-dir=/opt/local,--build=x86_64-apple-darwin10
~~~

And it finally worked!

<em>The magnificent yak is borrowed under the Creative Commons Licence from <a href="http://www.flickr.com/photos/revcyborg/22883042/in/photostream/">LiminalMike's Flickr Stream</a>.</em>
