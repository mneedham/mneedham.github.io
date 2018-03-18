+++
draft = false
date="2011-11-10 23:37:36"
title="fgrep: Searching for a list of identifiers"
tag=['fgrep']
category=['Software Development']
+++

We had a problem to solve earlier in the week where we wanted to try and find out which files we had ingested into our database based on a unique identifier.

We had a few hundred thousand files to search through to try and find the ones where around 50,000 identifiers were mentioned so that we could re-ingest them.

Running a normal grep for each identifier individually took a ridiculously long time so we needed to find a way to search for all of the identifiers at the same time to speed up the process.

Luckily my colleague knew about <cite><a href="http://ss64.com/bash/fgrep.html">fgrep</a></cite> which allowed us to do this.

<blockquote>
fgrep is essentially grep (or egrep) with no special characters. If you want to search for a simple string without wild cards, use fgrep. The fgrep version of grep is optimized to search for strings as they appear on the command line, so it doesn't treat any characters as special. 
</blockquote>

We created a file containing all the identifiers:

identifiers.txt

~~~text

identifier1
identifier2
identifier3
~~~

And then created the following command to identify which files those identifiers existed in:


~~~text

fgrep -Rl -f identifiers.txt .
~~~

We passed the '-l' flag because we don't care where in the file the identifier matches, we just care that it exists in the file.

If we only have a few different things to search for then we could supply those directly to 'fgrep' without the file:


~~~text

fgrep -Rl -e "identifier1" -e "identifier2" -e "identifier3" .
~~~

I haven't used 'fgrep' before but it came in quite useful for us here. I also came across <a href="http://www.kingcomputerservices.com/unix_101/grep_this.htm">this article</a> which explains the different variants of grep in more details.
