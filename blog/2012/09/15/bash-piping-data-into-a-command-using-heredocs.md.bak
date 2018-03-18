+++
draft = false
date="2012-09-15 07:54:04"
title="Bash: Piping data into a command using heredocs"
tag=['shell']
category=['Shell Scripting']
+++

I've been playing around with some data modelled in neo4j recently and one thing I wanted to do is run an adhoc query in the <a href="http://docs.neo4j.org/chunked/stable/shell-starting.html">neo4j-shell</a> and grab the results and do some text manipulation on them.

For example I wrote a query which outputted the following to the screen and I wanted to sum together all the values in the 3rd column:


~~~text

| ["1","2","3"]         | "3"                             | 1234567    |   
| ["4","5","6"]         | "6"                             | 8910112    |   
~~~

Initially I was pasting the output into a text file and then running the following sequence of commands to work it out:


~~~text

$ cat blah2.txt| cut -d"|" -f 4  | awk '{s+=$0} END {print s}'  
10144679
~~~

One way to avoid having to create <cite>blah2.txt</cite> would be to echo the output into standard out like so:


~~~text

$ echo "| ["1","2","3"]         | "3"                             | 1234567    |   
| ["4","5","6"]         | "6"                             | 8910112    | " | cut -d"|" -f 4  | awk '{s+=$0} END {print s}'   
10144679
~~~

But it gets a bit confusing as the number of lines of results increases and you have to keep copy/pasting the cut and awk parts of the chain around which was annoying.

One of the things I read on the bus this week was a blog post going through a bunch of <a href="http://www.catonmat.net/blog/bash-one-liners-explained-part-three/">bash one liners</a> and half way through it covers piping data into commands using heredocs which I'd completely forgotten about!

A simple example could be to send a simple message to <cite>cat</cite> which will output the message to standard out:


~~~text

$ cat <<EOL
heredoc> hello i am mark
heredoc> EOL
hello i am mark
~~~

That works if we want to pipe data into a single command but I didn't know how we'd be able to pipe the output of that command to another command.

In fact it's actually reasonably simple:


~~~text

$ cat <<EOL | cut -d"|" -f 4  | awk '{s+=$0} END {print s}' 
pipe pipe heredoc> | ["1","2","3"]         | "3"                             | 1234567    |   
pipe pipe heredoc> | ["4","5","6"]         | "6"                             | 8910112    | 
pipe pipe heredoc> EOL
10144679
~~~

And now I have no need to create random text files all over my machine!
