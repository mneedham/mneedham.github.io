+++
draft = false
date="2008-08-16 00:10:51"
title="Getting latest tagged revision in SVN from DOS/Batch script"
tag=['batch-scripts', 'dos', 'command-line', 'svn']
category=['Batch Scripting', 'Version Control']
+++

The way we have setup the build on our continuous integration server, <a href="http://www.jetbrains.com/teamcity/">Team City</a> is configured to create a new tag every time the functional tests past successful on that machine.

We then have a QA and Showcase build that we can run to deploy all the artifacts necessary to launch the application on that machine.

Originally I had just written the batch script to take in the tag of the build which the user could find by looking through <a href="http://tortoisesvn.tigris.org/">repo-browser</a> for the last tag created. This quickly became very tedious so I started looking for a way to get the latest tagged revision from the command line.

We thought it would be possible to get this information using svn info but it turned out that the information returned by svn info about revisions doesn't necessarily refer  to the latest created tag. We ended up using svn log and then parsing through that data. It's a bit messy but it does the job (I name each tagged version of the code as 'build-{TeamCity-Build-Number}):
<table class="CodeRay" border="0">
<tbody>
<tr>
<td class="line_numbers" title="click to toggle" onclick="with (this.firstChild.style) { display = (display == '') ? 'none' : '' }">
<pre>1<tt>
</tt>2<tt>
</tt>~~~
</td>
<td class="code">
<pre ondblclick="with (this.style) { overflow = (overflow == 'auto' || overflow == '') ? 'visible' : 'auto' }">FOR /F "Tokens=2" %%i in ('svn log /tags/path --limit=1 -v ^| find "build"') do set TMP=%%i<tt>
</tt>FOR /F "Tokens=2 delims=/" %%i in ('echo %TMP%') do SET TAG=%%i~~~
</td>
</tr>
</tbody></table>
The for loop uses a space as its default delimiter so that's what the 'delims=/' is doing on the second line, the 'Tokens=2' allows us to get the second token after the string is split and the '^' in the first command is being used to escape the pipe.
