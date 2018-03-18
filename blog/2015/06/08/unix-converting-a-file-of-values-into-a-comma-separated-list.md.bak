+++
draft = false
date="2015-06-08 22:23:32"
title="Unix: Converting a file of values into a comma separated list"
tag=['unix']
category=['Shell Scripting']
+++

<p>
I recently had a bunch of values in a file that I wanted to paste into a Java program which required a comma separated list of strings.
</p>


<p>
This is what the file looked like:
</p>



~~~bash

$ cat foo2.txt | head -n 5
1.0
1.0
1.0
1.0
1.0
~~~

<p>
And the idea is that we would end up with something like this:
</p>



~~~text

"1.0","1.0","1.0","1.0","1.0"
~~~

<P>
The first thing we need to do is quote each of the values. I found a <a href="http://www.unix.com/unix-for-dummies-questions-and-answers/138445-unix-command-insert-double-quotes-delimited-file.html">nice way to do this using sed</a>:
</p>




~~~bash

$ sed 's/.*/"&"/g' foo2.txt | head -n 5
"1.0"
"1.0"
"1.0"
"1.0"
"1.0"
~~~

<p>
Now that we've got all the values quoted we need to get rid of the new lines and replace them with commas. The way I'd normally do this is using 'tr' and then just not copy the final comma...
</p>



~~~bash

$ sed 's/.*/"&"/g' foo2.txt | tr '\n' ','
"1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0",
~~~

<p>...but I learnt that we can actually do one better than this using 'paste' which allows you to <a href="http://unix.stackexchange.com/questions/114244/replace-all-newlines-to-space-except-the-last">replace new lines excluding the last one</a>.
<p>

<p>
The only annoying thing about paste is that you can't pipe to it so we need to use process substitution instead:
</p>



~~~bash

$ paste -s -d ',' <(sed 's/.*/"&"/g' foo2.txt)
"1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0","1.0"
~~~

<p>If we're only a Mac we could even automate the copy/paste step too by piping to 'pbcopy':</p>



~~~bash

$ paste -s -d ',' <(sed 's/.*/"&"/g' foo2.txt) | pbcopy
~~~
