+++
draft = false
date="2011-01-14 14:15:19"
title="Sed: 'sed: 1: invalid command code R' on Mac OS X"
tag=['shell-scripting-2']
category=['Shell Scripting']
+++

A few days ago I wrote about how we'd been <a href="http://www.markhneedham.com/blog/2011/01/11/sed-across-multiple-files/">using Sed to edit multiple files</a> and while those examples were derived from what we'd been using on Ubuntu I realised that they didn't actually work on Mac OS X.

For example, the following command:

~~~text

sed -i 's/require/include/' Rakefile
~~~

Throws this error:


~~~text

sed: 1: "Rakefile": invalid command code R
~~~ 

What I hadn't realised is that on the Mac version of sed the '-i' flag has a mandatory suffix, <a href="http://hintsforums.macworld.com/showpost.php?p=393450&postcount=11">as described in this post</a>.

The appropriate section of the man page for sed on the Mac looks like this:

<blockquote>
  -i extension
            

Edit files in-place, saving backups with the specified extension.  If a zero-length extension is given, no backup will be saved.  

It is not recommended togive a zero-length extension when in-place editing files, as you risk corruption or partial content in situations where disk space is exhausted, etc.
</blockquote>

Whereas on Ubuntu the suffix is optional so we see this:

<blockquote>
-i[SUFFIX], --in-place[=SUFFIX]

edit files in place (makes backup if extension supplied)
</blockquote>

In order to get around this we need to provide a blank suffix when using the '-i' flag on the Mac:


~~~text

sed -i "" 's/require/include/' Rakefile
~~~

I didn't <a href="http://en.wikipedia.org/wiki/RTFM">RTFM</a> closely enough the first time! 
