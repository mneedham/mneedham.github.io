+++
draft = false
date="2013-05-19 21:44:03"
title="Unix: Working with parts of large files"
tag=['unix']
category=['Shell Scripting']
+++

<p><a href="https://twitter.com/digitalstain">Chris</a> and I were looking at the neo4j log files of a client earlier in the week and wanted to do some processing of the file so we could ask the client to send us some further information.</p>


<p>The log file was over 10,000 lines long but the bit of the file we were interesting in was only a few hundred lines.</p>


<p>I usually use Vim and the ':set number' when I want to refer to line numbers in a file but Chris showed me that we can achieve the same thing with e.g. 'less -N data/log/neo4j.0.0.log'.</p>


<p>We can then operate on say lines 10-100 by passing the '-n' flag to sed:</p>


<blockquote>
-n      By default, each line of input is echoed to the standard output after all of the commands have been applied to it.  The -n option suppresses this behavior.
</blockquote>


~~~bash

$ sed -n '10,15p' data/log/neo4j.0.0.log
INFO: Enabling HTTPS on port [7473]
May 19, 2013 11:11:52 AM org.neo4j.server.logging.Logger log
INFO: No SSL certificate found, generating a self-signed certificate..
May 19, 2013 11:11:53 AM org.neo4j.server.logging.Logger log
INFO: Mounted discovery module at [/]
May 19, 2013 11:11:53 AM org.neo4j.server.logging.Logger log
~~~

<p>We then used a combination of grep, awk and sort to work out which log files we needed.</p>

