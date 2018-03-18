+++
draft = false
date="2008-08-08 20:10:49"
title="Spaces in batch scripts"
tag=['batch-scripts']
category=['Build']
+++

Since reading <a href="http://www.amazon.co.uk/Pragmatic-Programmer-Andrew-Hunt/dp/020161622X/ref=sr_1_1?ie=UTF8&s=books&qid=1218153128&sr=8-1">The Pragmatic Programmer</a> I've become a bit of an automation junkie and writing batch scripts falls right under that category.

Unfortunately, nearly every single time I write one I forget that Windows really hates it when you have spaces in variable assignments, and I forget how to print out a usage message if the right number of parameters are not passed in.

So as much for me as for everyone else, this is how you do it:
<table class="CodeRay" border="0">
<tbody>
<tr>
<td class="line_numbers" title="click to toggle" onclick="with (this.firstChild.style) { display = (display == '') ? 'none' : '' }">
<pre>1<tt>
</tt>2<tt>
</tt>3<tt>
</tt>4<tt>
</tt>5<tt>
</tt>6<tt>
</tt>7<tt>
</tt>8<tt>
</tt>9<tt>
</tt><strong>10</strong><tt>
</tt>11<tt>
</tt>12<tt>
</tt>13<tt>
</tt>14<tt>
</tt>15<tt>
</tt>16<tt>
</tt>~~~
</td>
<td class="code">
<pre ondblclick="with (this.style) { overflow = (overflow == 'auto' || overflow == '') ? 'visible' : 'auto' }">@ECHO off<tt>
</tt>IF [%1]==[] GOTO usage<tt>
</tt>IF [%2]==[] GOTO usage<tt>
</tt><tt>
</tt>set VAR1=%1<tt>
</tt>set VAR2=%2<tt>
</tt><tt>
</tt>rem important client stuff<tt>
</tt><tt>
</tt>goto end<tt>
</tt><tt>
</tt>:usage<tt>
</tt>echo Usage: script.bat var1 var2<tt>
</tt><tt>
</tt>:end<tt>
</tt>echo Script finished~~~
</td>
</tr>
</tbody></table>
