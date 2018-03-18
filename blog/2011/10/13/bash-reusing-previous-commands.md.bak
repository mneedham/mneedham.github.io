+++
draft = false
date="2011-10-13 19:46:20"
title="Bash: Reusing previous commands"
tag=['unix', 'bash']
category=['Shell Scripting']
+++

A lot of the time when I'm using the bash shell I want to re-use commands that I've previously entered and I've recently learnt some neat ways to do this from my colleagues <a href="http://twitter.com/#!/tomduckering">Tom</a> and <a href="http://twitter.com/kief">Kief</a>.

If we want to list the history of all the commands we've entered in a shell session then the following command does the trick:


~~~text

> history
...
  761  sudo port search pdfinfo
  762  to_ipad andersen-phd-thesis.pdf 
  763  vi ~/.bash_profile
  764  source ~/.bash_profile
  765  to_ipad andersen-phd-thesis.pdf 
  766  to_ipad spotify-p2p10.pdf 
  767  mkdir LinearAlgebra
~~~

If we want to execute any of those commands again then we can do that by entering <cite>![numberOfCommand</cite>. For example, to execute the last command on that list we'd do this:


~~~text

> !767
mkdir LinearAlgebra
mkdir: LinearAlgebra: File exists
~~~	

We can also search the history and execute the last command that matches the search by doing the following:


~~~text

> !mk
mkdir LinearAlgebra
mkdir: LinearAlgebra: File exists
~~~


A safer way to do this would be to suffix that with <cite>:p</cite> so the command gets printed to stdout rather than executed:


~~~text

> !mk:p
mkdir LinearAlgebra
~~~

A fairly common use case that I've come across is to search for a file and then once you've found it open it in a text editor. 

We can do this by using the <cite>!!</cite> command which repeats the previously executed command:


~~~text

> find . -iname "someFile.txt"
> vi `!!`
~~~

We can achieve the same thing by wrapping '!!' inside '$()' as well:


~~~text

> find . -iname "someFile.txt"
> vi $(!!)
~~~

Sam Rowe has a cool post where he <a href="http://samrowe.com/wordpress/advancing-in-the-bash-shell/">goes into this stuff in even more detail</a>.

I'm sure there are more tricks that I haven't learnt yet so please let me know if you know some!
