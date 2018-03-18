+++
draft = false
date="2011-01-15 19:05:26"
title="Installing git-svn on Mac OS X"
tag=['software-development']
category=['Software Development']
+++

I somehow managed to uninstall git-svn on my machine and <a href="http://blog.emmanuelbernard.com/2009/01/how-to-install-git-and-git-svn-on-mac.html">Emmanuel Bernard's blog post</a> suggested it could be installed using ports:


~~~text

sudo port install git-core +svn
~~~

I tried that and was ending up with the following error:


~~~text

--->  Computing dependencies for git-core
--->  Dependencies to be installed: p5-svn-simple subversion-perlbindings apr-util db46 cyrus-sasl2 neon serf subversion p5-term-readkey
--->  Verifying checksum(s) for db46
Error: Checksum (md5) mismatch for patch.4.6.21.1
Error: Checksum (md5) mismatch for patch.4.6.21.2
Error: Checksum (md5) mismatch for patch.4.6.21.3
Error: Checksum (md5) mismatch for patch.4.6.21.4
Error: Target org.macports.checksum returned: Unable to verify file checksums
~~~

A bit of googling led me to the <a href="https://trac.macports.org/ticket/26075">macports website</a> where it was pointed out that this problem was happening in that user's case because the link to the patch now redirects to a HTML page:

<blockquote>
It's actually the fact that the links pointing to those patches have become invalid.

 <a href="http://www.oracle.com/technology/products/berkeley-db/db/update/4.6.21/">http://www.oracle.com/technology/products/berkeley-db/db/update/4.6.21/</a>

redirects to the Berkley-DB webpage

 <a href="http://www.oracle.com/technetwork/database/berkeleydb/overview/index.html">http://www.oracle.com/technetwork/database/berkeleydb/overview/index.html</a>

and you get a HTML instead of the real patch.
</blockquote>

I'm not sure if that's the case for me because only the Checksum is failing, nothing is mentioned about downloading from Oracle's website.

By adapting one of the suggestions for downloading the patches manually I arrived at the following combination of commands to fix the db46 dependency:


~~~text

cd /opt/local/var/macports/distfiles/db4/4.6.21_6/
sudo rm -rf patch*
for i in 1 2 3 4; do echo $i && sudo curl http://distfiles.macports.org/db4/4.6.21_6/patch.4.6.21.$i -O; done
~~~

Followed by:


~~~text

sudo port install git-core +svn
~~~

And I'm back in the game!

