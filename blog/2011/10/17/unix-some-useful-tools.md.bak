+++
draft = false
date="2011-10-17 22:58:50"
title="Unix: Some useful tools"
tag=['ghex']
category=['Software Development']
+++

On my current project we regularly use a few Unix tools which aren't on the standard installation so I thought I'd collate them here so I don't forget about them in the future.

<h3>ghex</h3>

We suspected we'd ended up with some rogue characters in a file that we weren't able to detect in our normal text editor recently and wanted to view the byte by byte representation of the file to check it out.

We came across <cite><a href="http://live.gnome.org/Ghex">ghex</a></cite> which seems to be a pretty decent tool for allowing us to do this.


~~~text

sudo port install ghex
~~~


~~~text

ghex2 ourFile.jade
~~~

<h3>axel</h3>

<cite><a href="http://axel.alioth.debian.org/">axel</a></cite> is a download accelerator and lets us send multiple <a href="http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.35">partial/range requests</a> to download parts of a file before putting it back together at the end. 

We found this quite useful when I was working in India to download files from the US over VPN. scp was painfully slow so we used to set up a simple HTTP server on the US server and then use axel to grab the file.

Some servers don't support range requests but a reasonable number of them seem to.


~~~text

sudo port install axel
~~~


~~~text

axel -a http://www.cs.cmu.edu/~dga/papers/andersen-phd-thesis.pdf
~~~

<h3>ack</h3>

The man page claims the following:

<blockquote>
Ack is designed as a replacement for 99% of the uses of grep.
</blockquote>

It worked reasonably well for replacing the following grep command:


~~~text

grep -iR "searchTerm" .
~~~

One of the cool things is that by default it doesn't search in binary files whereas grep does. I have noticed that it sometimes doesn't pick up search terms in files which grep would match and I'm not entirely sure why. 


~~~text

sudo port install p5-app-ack
~~~


~~~text

ack "something"
~~~

I'm sure there are plenty of other cool tools about so if you know of any let me know!
