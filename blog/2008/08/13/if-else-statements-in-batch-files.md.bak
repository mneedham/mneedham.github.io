+++
draft = false
date="2008-08-13 22:27:40"
title="If Else statements in batch files"
tag=['batch-scripts', 'dos', 'command-line']
category=['Batch Scripting']
+++

I mentioned in a couple of <a href="http://www.markhneedham.com/blog/2008/08/12/getting-the-current-working-directory-from-dos-or-batch-file/">earlier</a> <a href="http://www.markhneedham.com/blog/2008/08/08/spaces-in-batch-scripts/">posts</a> that I've been doing quite a bit of work with batch files and the windows command line, and today I wanted to do an If Else statement in one of my scripts.

I thought it would be relatively simple, but after various searches and having read articles that suggested that there wasn't an ELSE construct in batch land I finally found a <a href="http://www.codeguru.com/forum/showthread.php?t=377124">forum post</a> which explained how to do it.

The script I'm working on takes in a working directory as one of the arguments and what I wanted to do was either set a variable to be the value passed in, or if the value passed in was '.' then to set it to the <a href="2008/08/12/getting-the-current-working-directory-from-dos-or-batch-file/">current working directory</a>.

<table class="CodeRay"><tr>
  <td class="line_numbers" title="click to toggle" onclick="with (this.firstChild.style) { display = (display == '') ? 'none' : '' }"><pre>1<tt>
</tt>2<tt>
</tt>3<tt>
</tt>4<tt>
</tt>5<tt>
</tt>~~~</td>
  <td class="code"><pre ondblclick="with (this.style) { overflow = (overflow == 'auto' || overflow == '') ? 'visible' : 'auto' }">IF &quot;%1&quot;==&quot;.&quot;  (<tt>
</tt>  set WORKING_DIRECTORY=%cd%<tt>
</tt>) ELSE (<tt>
</tt>  set WORKING_DIRECTORY=%1<tt>
</tt>)~~~</td>
</tr></table>

I played around with this a little bit and it does seem that the brackets need to be in that exact format otherwise it doesn't work at all. Even putting brackets around the IF part of the statement will stop the script from working as expected. 

IF statements on their own are much easier to deal with. To check for an empty argument for example either of the following will work:

<table class="CodeRay"><tr>
  <td class="line_numbers" title="click to toggle" onclick="with (this.firstChild.style) { display = (display == '') ? 'none' : '' }"><pre>1<tt>
</tt>2<tt>
</tt>3<tt>
</tt>~~~</td>
  <td class="code"><pre ondblclick="with (this.style) { overflow = (overflow == 'auto' || overflow == '') ? 'visible' : 'auto' }">IF &quot;%1&quot;==&quot;&quot; GOTO usage<tt>
</tt><tt>
</tt>IF [%1]==[] GOTO usage~~~</td>
</tr></table>

It does all seem a bit fiddly and <a href="http://www.microsoft.com/windowsserver2003/technologies/management/powershell/default.mspx">Powershell</a> is probably the way forwards, but for now batch scripts it is!
