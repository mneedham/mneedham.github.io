+++
draft = false
date="2013-07-31 05:41:12"
title="Getting started with screen"
tag=['screen']
category=['Software Development']
+++

<p>Last week I had a ~10GB file I wanted to download to my machine but Chrome's initial estimate was that it would take 10+ hours to do so which meant I'd have probably shutdown my machine before it had completed.</p>


<p>It seemed to make more sense to spin up an EC2 instance and download it onto there instead but I didn't want to have to keep an SSH session open to that machine either.</p>


<p>I've previously come across <a href="http://www.gnu.org/software/screen/">screen</a> and <a href="http://tmux.sourceforge.net/">tmux</a> which allow you to create a session in which you can do some work even if you aren't currently connected to it which was perfect for my use case.</p>
 

<p>screen was a bit more familiar so I decided to use that and I thought I should make a quick note of some of its basic flags for future me.</p>


<h3>Starting a new session</h3>

<p>Starting a new screen session is as simple as typing the following command:</p>



~~~bash

$ screen
~~~

<p>which leads to the following output:</p>



~~~bash

Screen version 4.00.03jw4 (FAU) 2-May-06

Copyright (c) 1993-2002 Juergen Weigert, Michael Schroeder
Copyright (c) 1987 Oliver Laumann

This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2, or (at your option) any later
version.
...
~~~

<p>We can now start downloading our file using cURL, wget or a download accelerator like <a href="http://freecode.com/projects/axel">axel</a> which is my personal favourite.</p>


<h3>Detaching/Exiting from a session without it dying</h3>

<p>Once I'd got the download running I wanted to close my SSH session to the AWS instance but first I wanted to detach from my screen session without killing it.</p>


<p>My first attempt was to use <cite>Ctrl + D</cite> but that actually results in the session being terminated and our download is therefore stopped as well which isn't quite what we wanted.</p>


<p>Instead what we want to do is <a href="http://www.gnu.org/software/screen/manual/screen.html#Detach">detach</a> from the session which allows us to <a href="http://stackoverflow.com/questions/4847691/how-do-i-get-out-of-a-screen-without-typing-exit">leave it but keep it running</a>. To do that we type <cite>Ctrl + A</cite> followed by <cite>Ctrl + D</cite>.</p>


<h3>Reattaching to a session</h3>

<p>After about an hour I wanted to checkup on my download and I assumed just typing <cite>screen</cite> would take me back to my session but instead it created a new one.</p>


<p><a href="http://www.apcjones.com/blog/">Alistair</a> pointed out that I could get a listing of all the open screen sessions by typing the following command:</p>



~~~bash

$ screen -ls
There are screens on:
	23397.pts-0.ip-10-243-5-102	(07/31/2013 05:25:30 AM)	(Detached)
	3981.pts-0.ip-10-243-5-102	(07/26/2013 07:59:28 AM)	(Detached)
	3910.pts-0.ip-10-243-5-102	(07/26/2013 07:58:42 AM)	(Detached)
	1094.pts-0.ip-10-243-5-102	(07/26/2013 07:49:31 AM)	(Detached)
4 Sockets in /var/run/screen/S-ubuntu.
~~~

<p>As you can see, I'd created a bunch of extra sessions by mistake.</p>


<p>The one I had the download running on was '1094.pts-0.ip-10-243-5-102' and we can reattach to that one like this:</p>



~~~bash

$ screen -x 1094.pts-0.ip-10-243-5-102
~~~

<p>We can also attach using the '-r' flag:</p>



~~~bash

$ screen -r 1094.pts-0.ip-10-243-5-102
~~~

<p>I'm not quite sure what the difference is between '-r' and '-x', they both seem to behave in the same way in this scenario.</p>


<p>The manual suggests that '-x' is for attaching to a 'not detached screen session' which suggests to me that it shouldn't have worked since I wanted to connect to a detached session.</p>


<p>Hopefully someone with more knowledge of how these things work can explain what's going on!</p>


<h3>Attach to an existing session or start a new one if none exists</h3>

<p>I <a href="http://serverfault.com/questions/38417/reattach-or-create-a-named-screen-session-or-persistent-screen-sessions">later learnt</a> that had I not accidentally created all those extra sessions the following command would have been quite useful for finding the first screen session available and connecting to it:</p>



~~~bash

$ screen -x -R
~~~

<p>If there aren't any existing screen sessions available then it will create a new one which means that in my particular situation this would have been a more appropriate command to start with.</p>

