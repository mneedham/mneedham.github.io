+++
draft = false
date="2016-06-19 08:36:46"
title="Unix: Find all text below string in a file"
tag=['unix']
category=['Shell Scripting']
+++

<p>I recently wanted to parse some text out of a bunch of files so that I could do some sentiment analysis on it. Luckily the text I want is at the end of the file and doesn't have anything after it but there is text before it that I want to get rid. 
</p>


<p>The files look like this:</p>



~~~text

# text I don't care about

= Heading of the bit I care about

# text I care about
~~~

<p>In other words I want to find the line that contains the Heading and then get all the text after that point.</p>


<p>
I figured sed was the tool for the job but my knowledge of the syntax was a bit rusty. Luckily <a href="http://stackoverflow.com/questions/7103531/how-to-get-the-part-of-file-after-the-line-that-matches-grep-expression-first">this post</a> served as a refresher.
</p>


<p>
Effectively what we want to do is delete from the beginning of the file up until the line after the heading. We can do this with the following command:
</p>



~~~bash

$ cat /tmp/foo.txt 
# text I don't care about

= Heading of the bit I care about

# text I care about
~~~


~~~bash

$ cat /tmp/foo.txt | sed '1,/Heading of the bit I care about/d'

# text I care about
~~~

<p>That still leaves an extra empty line after the heading which is a bit annoying but easy enough to get rid of by passing another command to sed that strips empty lines:</p>



~~~bash

$ cat /tmp/foo.txt | sed -e '1,/Heading of the bit I care about/d' -e '/^\s*$/d'
# text I care about
~~~

<p>
The only difference here is that we're now passing the '-e' flag to allow us to specify multiple commands. If we just pass them sequentially then the 2nd one will be interpreted as the name of a file. 
</p>

