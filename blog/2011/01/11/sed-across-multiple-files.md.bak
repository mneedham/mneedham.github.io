+++
draft = false
date="2011-01-11 16:43:53"
title="Sed across multiple files"
tag=['shell-scripting-2']
category=['Shell Scripting']
+++

<a href="http://pankhurisa.blogspot.com/">Pankhuri</a> and I needed to rename a method and change all the places where it was used and decided to see if we could work out how to do it using sed.

We needed to change a method call roughly like this:


~~~ruby

home_link(current_user)
~~~

To instead read:


~~~ruby

homepage_path
~~~

For which we need the following sed expression:


~~~text

sed -i 's/home_link([^)]*)/homepage_path/' [file_name]
~~~

Which works pretty well if you know which file you want to change but we wanted to run it over the whole code base.

A bit of googling led us to <a href="http://forums.devshed.com/unix-help-35/how-to-use-sed-to-search-replace-files-throughout-a-184662.html">this thread on devshed</a> which suggested we'd need to get a list of the files and then run sed through the list:


~~~text

for file in `find .  -type f`; do sed -i 's/home_link([^)]*)/homepage_path/' $file; done
~~~

That pretty much works but it doesn't play nicely if the file has a space in the name since sed thinks the file name has ended before it actually has.

I was pretty sure that we should be able to pipe the output of the find into xargs and a bit more googling led us to the following solution:


~~~text

find . -type f -print0 | xargs -0 sed -i 's/home_link([^)]*)/homepage_path/'
~~~

The 'print0' flag is described like so:


~~~text

This primary always evaluates to true.  It prints the pathname of the current file to standard output, followed by an ASCII NUL character (character code 0).
~~~

While '-0' in 'xargs' is described like this:


~~~text

  -0      Change xargs to expect NUL (``\0'') characters as separators, instead of spaces and newlines.  This is expected to be used in concert with the -print0 function in find(1).
~~~

It also runs amazingly fast!

If anyone knows a better way feel free to point it out in the comments.
