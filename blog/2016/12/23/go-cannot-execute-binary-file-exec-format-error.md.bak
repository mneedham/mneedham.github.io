+++
draft = false
date="2016-12-23 18:24:12"
title="Go: cannot execute binary file: Exec format error"
tag=['go', 'golang']
category=['Go']
+++

<p>
In an earlier blog post I mentioned that I'd been <a href="http://www.markhneedham.com/blog/2016/12/23/go-templating-with-the-gin-web-framework/">building an internal application</a> to learn a bit of Go and I wanted to deploy it to AWS.
</p>


<p>Since the application was only going to live for a couple of days I didn't want to spend a long time build up anything fancy so my plan was just to build the executable, SSH it to my AWS instance, and then run it.</p>


<p>
My initial (somewhat naive) approach was to just build the project on my Mac and upload and run it:
</p>



~~~bash

$ go build

$ scp myapp ubuntu@aws...

$ ssh ubuntu@aws...

$ ./myapp
-bash: ./myapp: cannot execute binary file: Exec format error
~~~

<p>
That didn't go so well! By reading <a href="http://askubuntu.com/questions/648555/bash-program-cannot-execute-binary-file-exec-format-error">Ask Ubuntu</a> and <a href="https://dave.cheney.net/2015/03/03/cross-compilation-just-got-a-whole-lot-better-in-go-1-5">Dave Cheney's blog post on cross compilation</a> I realised that I just needed to set the appropriate environment variables before running <cite>go build</cite>.</p>
 

<p>The following did the trick:</p>



~~~bash

env GOOS=linux GOARCH=amd64 GOARM=7 go build
~~~

<p>
And that's it! I'm sure there's more sophisticated ways of doing this that I'll come to learn about but for now this worked for me.
</p>

