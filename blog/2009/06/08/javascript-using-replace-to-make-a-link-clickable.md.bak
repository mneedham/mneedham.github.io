+++
draft = false
date="2009-06-08 11:57:39"
title="Javascript: Using 'replace' to make a link clickable"
tag=['javascript']
category=['Javascript']
+++

I've been doing a bit more work on my <a href="http://www.markhneedham.com/blog/2009/04/13/f-a-day-of-writing-a-little-twitter-application/">twitter application</a> over the weekend - this time taking the tweets that I've stored in CouchDB and displaying them on a web page.

One of the problems I had is that the text of the tweets is just plain text so if there is a link in a tweet then when I display it on a web page it isn't clickable since it isn't enclosed by the '&#60;a href"..."&#62;&#60;/a&#62;' tag.

Javascript has a 'replace' function which you can call to allow you to replace some characters in a string with some other characters.

What I actually wanted to do was surround some characters with the link tag but most of the examples I came across didn't explain how to do this.

Luckily I came across a <a href="http://www.webmasterworld.com/forum91/562.htm">forum post from a few years ago</a> which explained how to do it.

In this case then we would make use of a matching group on links to create a clickable link:


~~~javascript

"Interesting post... Kanban & estimates http://tinyurl.com/p58o3r".replace(/(http:\/\/\S+)/g, "<a href='$1'>$1</a>");
~~~

Which results in a tweet with a nice clickable link:


~~~text

"Interesting post... Kanban & estimates <a href='http://tinyurl.com/p58o3r'>http://tinyurl.com/p58o3r</a>"
~~~

