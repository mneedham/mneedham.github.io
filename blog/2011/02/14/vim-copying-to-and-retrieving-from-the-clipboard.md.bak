+++
draft = false
date="2011-02-14 14:13:56"
title="Vim: Copying to and retrieving from the clipboard"
tag=['software-development', 'vim']
category=['Software Development']
+++

My memory when it comes to remembering how to get text to and from Vim via the clipboard is pretty bad so I thought I'd try summarising what I know and see if that works out any better.

We can access the system clipboard via the '+' buffer so the commands revolve around that.

<h4>Copying to the clipboard</h4>

To copy the whole file to the clipboard we can use this command:


~~~text

:%y+
~~~

Or if we want to get the data between lines 4 and 10 then we could do:


~~~text

:4,10y+
~~~

If we want just the current line the following will work:


~~~text

:.y+
~~~

If we want to copy lines via visual mode, we would use 'v' to go into that and select which lines we want to copy followed by:


~~~text

"+y
~~~

<h4>Retrieving from the clipboard</h4>

Retrieving data from the clipboard is a case of accessing the '+' buffer.

Therefore to paste whatever's in the clipboard into a file we'd do this:


~~~text

"+p
~~~

If we wanted to paste it just before the current position of the cursor then we'd do this instead:


~~~text

"+P
~~~


