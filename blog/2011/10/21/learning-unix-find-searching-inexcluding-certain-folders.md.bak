+++
draft = false
date="2011-10-21 21:25:04"
title="Learning Unix find: Searching in/Excluding certain folders"
tag=['shell-scripting-2', 'unix']
category=['Shell Scripting']
+++

I love playing around with commands on the Unix shell but one of the ones that I've found the most difficult to learn beyond the very basics is <cite><a href="http://unixhelp.ed.ac.uk/CGI/man-cgi?find">find</a></cite>.

I think this is partially because I find the find man page quite difficult to read and partially because it's usually quicker to work out how to solve my problem with a command I already know than to learn another one.

However, I recently came across <a href="http://mywiki.wooledge.org/UsingFind">Greg's wiki</a> which seems to do a pretty good job of explaining it.

Reasonably frequently I want to get a list of files to scan but want to exclude files in the .git directory since the results tend to become overwhelming with those included:


~~~text

$ find . ! -path  "*.git*" -type f -print
~~~

Here we're saying find items which don't have git in their path and which are of type 'f' (file) and then print them out.

If we don't include the <cite>-type</cite> flag then the results will also include directories which isn't what we want in this case. The <cite>-print</cite> is optional in this case since by default what we select will be printed.

Sometimes we want to exclude more than one directory which can be done with the following command:


~~~text

$ find . \( ! -path "*target*" -a ! -path "*tools*" -a ! -path "*.git*" -print \) 
~~~

Here we're excluding the 'target', 'tools' and 'git' directories from the listing of files that we return.

The <cite>-a</cite> flag stands for 'and' so the above command reads 'find all files/directories which do not have target in their path and do not have tools in their path and do not have .git in their path'. 

We can always make that command a bit more specific if any of those words legitimately appear in a path.

As well as the <cite>-print</cite> flag there is also a <cite>-prune</cite> flag which we can use to stop find from descending into a folder.

The first command could therefore be written like this:


~~~text

$ find . -path "*.git*" -prune -o -type f -print
~~~

This reads 'don't go any further into a folder which has git in the path but print any other files which don't have git in their path'.

I'm still finding <cite>-prune</cite> a bit confusing to understand and as the wiki points out:

<blockquote>
The most confusing property of -prune is that it is an ACTION, and thus no further filters are processed after it.

To use it, you have to combine it with -o to actually process the non-skipped files, like so:
</blockquote>

A couple of months ago I was playing around with our git repository trying to get a list of all the scala files in the 'src/main' directory and I went with this command:


~~~text

$ find . -type f -regex ".*src/main.*\.scala$"
~~~

Using the above flags it could instead be written like this:


~~~text

$ find . -path "*src/main*" -type f -iname "*\.scala*"
~~~

or


~~~text

$ find . -type f -path "*src/main/*\.scala" 
~~~

Interestingly those latter two versions seem to be a bit slower than the one that uses the <cite>-regex</cite> flag.

I'm not entirely sure why that is - presumably by supplying two flags on the latter two solutions <cite>find</cite> has to do more operations per line than it does with the <cite>-regex</cite> option or something like that?
