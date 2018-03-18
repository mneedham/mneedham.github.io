+++
draft = false
date="2013-06-26 15:23:14"
title="Unix/awk: Extracting substring using a regular expression with capture groups"
tag=['awk']
category=['Shell Scripting']
+++

<p>A couple of years ago I <a href="http://www.markhneedham.com/blog/2011/09/12/gawk-getting-story-numbers-from-git-commit-messages/">wrote a blog post</a> explaining how I'd used <a href="http://www.gnu.org/software/gawk/">GNU awk</a> to extract story numbers from git commit messages and I wanted to do a similar thing today to extract some node ids from a file.</p>


<p>My eventual solution looked like this:</p>



~~~bash

$ echo "mark #1000" | gawk '{ match($0, /#([0-9]+)/, arr); if(arr[1] != "") print arr[1] }'
1000
~~~

<p>But in the comments an alternative approach was suggested which used the Mac version of awk and the RSTART and RLENGTH global variables which get set when a match is found:</p>



~~~bash

$ echo "mark #1000" | awk 'match($0, /#[0-9]+/) { print substr( $0, RSTART, RLENGTH )}'
#1000
~~~

<p>Unfortunately <a href="http://stackoverflow.com/questions/2957684/awk-access-captured-group-from-line-pattern">Mac awk doesn't seem to capture groups</a> so as you can see it includes the # character which we don't actually want.</p>


<p>In this instance it wasn't such a big deal but it was more annoying for the node id extraction that I was trying to do:</p>



~~~bash

$ head -n 5 log.txt
Command[27716, Node[7825340,used=true,rel=14547348,prop=31734662]]
Command[27716, Node[7825341,used=true,rel=14547349,prop=31734665]]
Command[27716, Node[7825342,used=true,rel=14547350,prop=31734668]]
Command[27716, Node[7825343,used=true,rel=14547351,prop=31734671]]
~~~


~~~bash

$ head -n 5 log.txt | awk 'match($0, /Node\[([^,]+)/) { print substr( $0, RSTART, RLENGTH )}'
Node[7825340
Node[7825341
Node[7825342
Node[7825343
Node[7825336
~~~

<p>I ended up having to <cite>brew install gawk</cite> and using a variation of the <cite>gawk</cite> command I mentioned at the beginning of this post:</p>



~~~bash

$ head -n 5 log.txt | gawk 'match($0, /Node\[([^,]+)/, arr) { print arr[1]}'
7825340
7825341
7825342
7825343
7825336
~~~
