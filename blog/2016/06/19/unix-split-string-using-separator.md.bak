+++
draft = false
date="2016-06-19 07:22:57"
title="Unix: Split string using separator"
tag=['unix']
category=['Shell Scripting']
+++

<p>
I recently found myself needing to iterate over a bunch of '/' separated strings on the command line and extract just the text after the last '/'.
</p>


<p>
e.g. an example of one of the strings
</p>



~~~text

A/B/C
~~~

<p>I wanted to write some code that could split on '/' and then pick the 3rd item in the resulting collection. </p>


<p>One way of doing this is to echo the string and then pipe it through cut:</p>



~~~bash

$ string="A/B/C"
$ echo ${string} | cut -d"/" -f3
C
~~~

<p>or awk:</p>



~~~bash

$ echo ${string} | awk -F"/" '{ print $3}'
C
~~~

<p>I don't like having to echo the string - it feels a bit odd so I wanted to see if there was a way to do the parsing more 'inline'.</p>


<p>I came across <a href="http://stackoverflow.com/questions/918886/how-do-i-split-a-string-on-a-delimiter-in-bash">this post</a> which explains how to change the internal field separator (IFS) on the shell and then parse the string into an array using <a href="http://ss64.com/bash/read.html">read</a>. I gave it a try:</p>



~~~bash

$ IFS="/" read -ra ADDR <<< "${string}"; echo ${ADDR[2]}
C
~~~

<p>Works! We can even refer to the last item in the array using -1 instead of it's absolute position:</p>



~~~bash

$ IFS="/" read -ra ADDR <<< "${string}"; echo ${ADDR[-1]}
C
~~~

<p>I'd not come across this use of the 'read' function before. The key is the '-a' parameter. From the man page:</p>


<blockquote>
  -a aname 
    The words are assigned to sequential indices of the array variable aname, 
    starting at 0. All elements are removed from aname before the assignment. 
    Other name arguments are ignored.
</blockquote>

<p>
So we're resetting the internal field separator and then reading the string into another variable as an array split on the '/' character.
</p>


<p>Pretty neat although now it's longer than the original command and I'm sure I'll forget the syntax.</p>


<p>Further down the page is another suggestion which seems even harder to remember but is much shorter:</p>



~~~bash

$ echo ${string##*/} 
C
~~~

<p>This drops from the beginning of the string up until the last occurrence of '/' which is exactly what we want.</p>


<p>
This way is the nicest and doesn't require any echoing if we just want to assign the result to a variable. The echo is only used here to see the output.
</p>

