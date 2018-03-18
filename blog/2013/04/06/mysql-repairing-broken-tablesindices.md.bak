+++
draft = false
date="2013-04-06 17:26:20"
title="MySQL: Repairing broken tables/indices"
tag=['mysql']
category=['Software Development']
+++

<p>I part time administrate <a href="http://www.soccer24-7.com/forum/index.php">a football forum</a> that I used to run when I was at university and one problem we had recently was that some of the tables/indices had got corrupted when MySQL crashed due to a lack of disc space.</p>


<p>We weren't seeing any visible sign of a problem in any of the logs but whenever you tried to query one of the topics it wasn't returning any posts.</p>


<p>I eventually came across a useful article which explained <a href="http://www.softwareprojects.com/resources/programming/t-how-to-fix-mysql-database-myisam-innodb-1634.html">how to check whether some of the tables in a MySQL database had been corrupted and how to fix them</a>.</p>


<p>I first shutdown the database using the following command:</p>



~~~text

mysqladmin shutdown
~~~

<p>And then I ran this command to check on the status of each of the tables:</p>



~~~text

for path in `ls /var/lib/mysql/forum/*.MYI`; do echo $path; myisamchk $path; done
~~~

<p>This gave an output like the following for each table:</p>



~~~text

Checking MyISAM file: /var/lib/mysql/forum/forum.MYI
Data records:     217   Deleted blocks:       4
myisamchk: warning: 1 client is using or hasn't closed the table properly
- check file-size
- check record delete-chain
- check key delete-chain
- check index reference
- check data record references index: 1
- check record links
MyISAM-table '/var/lib/mysql/forum/forum.MYI' is usable but should be fixed
~~~

<p>If you pass the '--recover' flag to <cite>myisamchk</cite> it will attempt to fix any problems it finds. I therefore ran the following command:</p>



~~~text

for path in `ls /var/lib/mysql/forum/*.MYI`; do echo $path; myisamchk --recover $path; done
~~~

<p>After I'd run that it seemed to fix most of the problems we'd been experiencing. There are still a couple of edge cases left but at least the majority of the forum is now in a usable state.</p>


<p>I think we could just as easily run <cite>myisamchk</cite> by passing a wildcard selection of files for it to run against but I didn't realise that until afterwards!</p>


<p>The following would therefore work just as well:~~~


~~~text

myisamchk --recover /var/lib/mysql/forum/*.MYI
~~~
