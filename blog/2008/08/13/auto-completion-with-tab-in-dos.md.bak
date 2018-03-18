+++
draft = false
date="2008-08-13 23:55:38"
title="Auto complete with tab in DOS"
tag=['dos', 'windows-command-prompt', 'auto-completion']
category=['Batch Scripting']
+++

It's becoming quite a couple of weeks of learning for me around DOS and I have another tip that I just learnt today.

I always found it really frustrating when using the windows command prompt that I couldn't get Unix style tab auto completion. To navigate my way to a directory I would do the following:
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
</tt>~~~
</td>
<td class="code">
<pre ondblclick="with (this.style) { overflow = (overflow == 'auto' || overflow == '') ? 'visible' : 'auto' }">C:\>cd Downloads<tt>
</tt><tt>
</tt>C:\Downloads>cd nant-0.85<tt>
</tt><tt>
</tt>C:\Downloads\nant-0.85>cd bin<tt>
</tt><tt>
</tt>C:\Downloads\nant-0.85\bin>~~~
</td>
</tr>
</tbody></table>
It is very tedious as you might imagine. I would try placing a forward slash after each directory in the hope that it would allow me to scroll through the next directory down but to no avail.

Little did I know that in fact I needed to be using the backslash. The above can now be done in one line using Unix style tabbing auto completion:
<table class="CodeRay" border="0">
<tbody>
<tr>
<td class="line_numbers" title="click to toggle" onclick="with (this.firstChild.style) { display = (display == '') ? 'none' : '' }">
<pre>1<tt>
</tt>2<tt>
</tt>3<tt>
</tt>~~~
</td>
<td class="code">
<pre ondblclick="with (this.style) { overflow = (overflow == 'auto' || overflow == '') ? 'visible' : 'auto' }">C:\>cd Downloads\nant-0.85\bin<tt>
</tt><tt>
</tt>C:\Downloads\nant-0.85\bin>~~~
</td>
</tr>
</tbody></table>
