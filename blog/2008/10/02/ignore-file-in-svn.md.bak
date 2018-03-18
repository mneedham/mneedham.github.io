+++
draft = false
date="2008-10-02 21:10:27"
title="Ignore file in Svn"
tag=['svn', 'svnignore']
category=['Version Control']
+++

I spent a bit of time this afternoon marveling at the non intuitiveness of working out how to ignore files in Svn.

Normally I'd just use <a href="http://tortoisesvn.tigris.org/">Tortoise SVN</a> as it makes it so easy for you but I really wanted to know how to do it from the shell!

After a bit of Googling and conversation with a <a href="http://pilchardfriendly.wordpress.com/">colleague</a> I think I have it figured out to some extent.

<h3>Ignoring just one file or pattern</h3>

If you only have one pattern or file that you want to ignore then the following command should do the trick.


~~~text

svn propset svn:ignore <file_or_pattern_to_ignore> <dir_in_which_to_create_ignore_file>
~~~

For example:


~~~text

svn propset svn:ignore build .
~~~

This means my 'build' directory will now be ignored and the svn ignore file will be placed in the current directory.

<h3>Ignoring multiple files or patterns</h3>

The problem with the above approach comes when you want to ignore more than one pattern/file. If you just run the propset command again it overrides the current svn ignore file with the current value - clearly not what we want!

Luckily propedit comes to the rescue.

Running the following command will open up your chosen editor and allow you to edit the svn ignore file.


~~~text

svn propedit svn:ignore <dir_where_ignore_file_resides>
~~~

When I initially did this I received the following error:


~~~text

svn: None of the environment variables SVN_EDITOR, VISUAL or EDITOR is set, and no 'editor-cmd' run-time configuration option was found
~~~

I wanted my default editor to be <a href="http://macromates.com/">Textmate</a> so I entered the following: 


~~~text

export SVN_EDITOR=mate
~~~

This didn't seem to work for me - the svn tmp file being opened up in Textmate was always empty for some reason. Changing my editor to vi seemed to fix the problem.


~~~text

export SVN_EDITOR=vi
~~~

Running the command now opens up vi and allowed me to add the pattern '*.log' to my ignore list. If it is added successfully the following message will show up on exiting vi:


~~~text

Set new value for property 'svn:ignore' on '.'
~~~

<h3>Seeing which files or patterns are currently ignored</h3>
While having my Textmate problems detailed above my colleague pointed out the propget command which shows you which files/patterns are currently being ignored.


~~~text

svn propget svn:ignore .
~~~

Running this command shows me the following:


~~~text

build
*.log
~~~

<a href="http://svnbook.red-bean.com/en/1.4/svn-book.html#svn.advanced.props.special.ignore">svnbook</a> has even more goodness on ignoring files for those that are interested.
