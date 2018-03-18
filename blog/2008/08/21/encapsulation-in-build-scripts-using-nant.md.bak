+++
draft = false
date="2008-08-21 00:40:45"
title="Encapsulation in build scripts using nant"
tag=['oop', 'build', 'nant', 'ncover', 'encapsulation']
category=['Build']
+++

When writing build scripts it's very easy for it to descend into complete Xml hell when you're using a tool like <a href="http://nant.sourceforge.net/">nant</a>.

I <a href="http://www.markhneedham.com/blog/2008/08/12/dependency-tasks/#comment-20">wondered previously</a> whether it was possible to TDD build files and while this is difficult given the dependency model most build tools follow. That doesn't mean we can't apply other good design principles from the coding world however.

<a href="http://en.wikipedia.org/wiki/Encapsulation_(classes_-_computers)">Encapsulation</a> is one of the key principles of OOP and it can be applied in build files too. <a href="http://www.stephenchu.com/">Stephen Chu</a> talks about this in his post on <a href="http://www.stephenchu.com/2006/03/pragmatic-nant-scripting.html">Pragmatic Nant Scripting</a> where he recommends having 3 different levels of targets to help create this encapsulation.

I've been trying to follow this advice with our build scripts and today <a href="http://manicprogrammer.com/cs/blogs/heynemann/default.aspx">Bernardo</a> made the suggestion of using macros in an English readable way. He calls it OO Scripting - it's effectively a <a href="http://www.martinfowler.com/bliki/DomainSpecificLanguage.html">DSL</a> inside a DSL if you like.

I was having problems with the ncover nant task - the following error message was being thrown every time I called it:
<blockquote>could not find ncover folder in your path  in NCoverExplorer.NAntTasks.NCoverUtilities</blockquote>
I managed to find the source code for that class and had a look at it but I couldn't figure out what was going wrong without debugging through it. The strange thing was that it worked fine from the command line which suggested to me that I was getting something simple wrong.

I created a cover.tests <a href="2008/08/14/macros-in-nant/">macro</a> to encapsulate the details of how I was executing the coverage.

The plan was to get it working using an exec call to the ncover executable and then phase the ncover nant task back in when I'd figured out what I was doing wrong.

This is what I started out with:


~~~text

<macrodef name="cover.tests">
        <attributes>
                <attribute name="in.assemblies" />
        </attributes>
       <sequential>
                <copy file="\path\to\Coverage.xsl" tofile="${report.dir}\Coverage.xsl" />
        
                <exec program="..\lib\NCover-1.5.8\NCover.Console.exe">
                        <arg value="..\lib\nunit-2.4\nunit-console.exe" />
                        <arg value="${build.dir}\UnitTests\UnitTests.dll" />
                        <arg value="//a" />
                        <arg value="${in.assemblies}" />
                        <arg value="//x" />
                        <arg value="${report.dir}\Unit.Test.Coverage.xml" />
                </exec>
        </sequential>
</macrodef>
~~~

//a is the assemblies to include in the report

//x is the name of the report xml file which will be created

The full list is <a href="http://www.ncover.com/documentation/console/programsettings">here</a>.

The macro was called like this:
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
<pre ondblclick="with (this.style) { overflow = (overflow == 'auto' || overflow == '') ? 'visible' : 'auto' }"><target name="coverage"><tt>
</tt>   <cover.tests in.assemblies="Project1;Project2" /><tt>
</tt></target>~~~
</td>
</tr>
</tbody></table>
I substituted the ncover task back in with the same parameters as above and low and behold it worked!
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
<pre ondblclick="with (this.style) { overflow = (overflow == 'auto' || overflow == '') ? 'visible' : 'auto' }"><macrodef name="cover.tests"><tt>
</tt>        <attributes><tt>
</tt>                <attribute name="in.assemblies" /><tt>
</tt>        </attributes><tt>
</tt>        <sequential><tt>
</tt>                <copy file="\path\to\Coverage.xsl" tofile="${report.dir}\Coverage.xsl" /><tt>
</tt>        <tt>
</tt>                <ncover<tt>
</tt>                    program="..\lib\NCover-1.5.8\NCover.Console.exe"<tt>
</tt>                    commandLineExe="..\lib\nunit-2.4\nunit-console.exe"<tt>
</tt>                    commandLineArgs="${build.dir}\UnitTests\UnitTests.dll"<tt>
</tt>                    coverageFile="${report.dir}\Unit.Test.Coverage.xml"<tt>
</tt>                    assemblyList="${in.assemblies}"<tt>
</tt>                  />        <tt>
</tt>        </sequential><tt>
</tt></macrodef>~~~
</td>
</tr>
</tbody></table>
I'm not sure exactly what the problem parameter was but encapsulating this part of the build gave me the option of working that out in a way that impacted very little of the rest of the build file.

*Update*
Fixed the first example to include the opening <sequential> as pointed out by Vikram in the comments. Thanks again Vikram for pointing that out!
