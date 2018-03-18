+++
draft = false
date="2008-08-14 19:54:03"
title="msbuild - Use OutputPath instead of OutDir"
tag=['build', 'msbuild']
category=['Build']
+++

We've been using msbuild to build our project files on my current project and <a href="http://www.floydprice.com/">a colleague</a> and I noticed some strange behaviour when trying to set the directory that the output should be built to.

The problem was whenever we tried to set the output directory (using OutDir) to somewhere where there was a space in the directory name it would just fail catastrophically. We spent ages searching for the command line documentation before finding it <a href="http://msdn.microsoft.com/en-us/library/bb629394.aspx">here</a>.

According to this though:

"OutputPath: This property is typically specified in the project file and resembles OutDir. OutputPath has been deprecated and OutDir should be used instead whenever possible. "

We decided to try changing OutDir to OutputPath and it started working again! The code is simple, but for those wondering:
<table class="CodeRay" border="0">
<tbody>
<tr>
<td class="line_numbers" title="click to toggle" onclick="with (this.firstChild.style) { display = (display == '') ? 'none' : '' }">
<pre>1<tt>
</tt>2<tt>
</tt>3<tt>
</tt>4<tt>
</tt>~~~
</td>
<td class="code">
<pre ondblclick="with (this.style) { overflow = (overflow == 'auto' || overflow == '') ? 'visible' : 'auto' }"><exec program="\path\to\msbuild35"><tt>
</tt>  <arg value="${projectfile}" /><tt>
</tt>  <arg value="/p:OutputPath=${build.dir}\${project.name}\" /><tt>
</tt></exec>~~~
</td>
</tr>
</tbody></table>
I can't decide whether the documentation is just wrong or if it's now a convention that you can't have spaces in your build output path. Surely the former?
