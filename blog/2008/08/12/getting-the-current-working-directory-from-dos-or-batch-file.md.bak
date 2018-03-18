+++
draft = false
date="2008-08-12 22:37:27"
title="Getting the current working directory from DOS or Batch file"
tag=['batch-scripts', 'dos']
category=['Build', 'Batch Scripting']
+++

In the world of batch files I've been trying for ages to work out how to get the current/present working directory to make the batch script I'm working on a bit more flexible.

In Unix it's easy, just call 'pwd' and you have it. I wasn't expecting something that simple in Windows but it is! A call to 'cd' is all that's needed. If you need to set it in a batch script the following line does the trick:
<table class="CodeRay" border="0">
<tbody>
<tr>
<td class="line_numbers" title="click to toggle" onclick="with (this.firstChild.style) { display = (display == '') ? 'none' : '' }">
<pre><tt>
</tt>~~~
</td>
<td class="code">
<pre ondblclick="with (this.style) { overflow = (overflow == 'auto' || overflow == '') ? 'visible' : 'auto' }">set WORKING_DIRECTORY=%cd%~~~
</td>
</tr>
</tbody></table>
I was surprised that something so simple (I do now feel like an idiot) wasn't easier to find on Google. I ended up going via Experts Exchange (how they end up with such high search results when you have to pay to see the information is beyond me) and several other <a href="http://www.codeguru.com/forum/archive/index.php/t-96124.html">verbose ways</a> of solving the problem before finally coming across <a href="http://blogs.msdn.com/oldnewthing/archive/2005/01/28/362565.aspx">this article</a> which explained it.
