+++
draft = false
date="2011-01-18 18:58:35"
title="MySQL: The used command is not allowed with this MySQL version"
tag=['mysql']
category=['Software Development']
+++

For my own reference more than anything else, on my version of MySQL on Mac OS X, which is:

<blockquote>
mysql5  Ver 14.14 Distrib 5.1.48, for apple-darwin10.4.0 (i386) using readline 6.1
</blockquote>

When I try to use the 'LOAD DATA LOCAL' option to load data into tables I get the following error message:


~~~text

ERROR 1148 (42000) at line 4: The used command is not allowed with this MySQL version
~~~

Which we can get around by using the following flag as described in the <a href="http://dev.mysql.com/doc/refman/5.0/en/loading-tables.html">comments of the documentation</a>:


~~~text

mysql --local-infile -uroot -pandsoon
~~~

Or by putting the following entry in a config file (in my case ~/.my.cnf):


~~~text

[mysql]
local-infile
~~~

I tried a bit of googling to see if I could work out why it happens but I'm still none the wiser.
