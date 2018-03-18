+++
draft = false
date="2008-08-14 21:49:04"
title="Macros in nant"
tag=['nant', 'macrodef', 'ant']
category=['Build']
+++

One of my favourite features of <a href="http://ant.apache.org/">ant</a> is the ability to create macros where you can define common behaviour and then call it from the rest of your build script.

Unfortunately that task doesn't come with <a href="http://nant.sourceforge.net/">nant</a> and it's not available on <a href="http://nantcontrib.sourceforge.net/">nant-contrib</a> either. 

We were using a very roundabout way to build the various projects in our solution.


 <table class="CodeRay"><tr>
  <td class="line_numbers" title="click to toggle" onclick="with (this.firstChild.style) { display = (display == '') ? 'none' : '' }"><pre>1<tt>
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
</tt>17<tt>
</tt>18<tt>
</tt>19<tt>
</tt>~~~</td>
  <td class="code"><pre ondblclick="with (this.style) { overflow = (overflow == 'auto' || overflow == '') ? 'visible' : 'auto' }"><target name=&quot;compile&quot;>  <tt>
</tt>  <foreach item=&quot;Folder&quot; property=&quot;folderName&quot;><tt>
</tt>    <in><tt>
</tt>      <items><tt>
</tt>        <include name=&quot;${project::get-base-directory()}\Project1&quot; /><tt>
</tt>        <include name=&quot;${project::get-base-directory()}\Project2&quot; />                <tt>
</tt>      </items><tt>
</tt>    </in><tt>
</tt>    <do><tt>
</tt>      <property name=&quot;project.name&quot; value=&quot;${path::get-file-name(folderName)}&quot; /><tt>
</tt>      <property name=&quot;project.file&quot; value=&quot;${project.name}.csproj&quot; /><tt>
</tt>                <tt>
</tt>      <exec program=&quot;/path/to/msbuild3.5/&quot;><tt>
</tt>        <arg value=&quot;${folderName}\${project.file}&quot; /><tt>
</tt>        <arg value=&quot;/p:OutputPath=${build.dir}\${project.name}\&quot; /><tt>
</tt>      </exec>                                <tt>
</tt>    </do>                <tt>
</tt>  </foreach>        <tt>
</tt></target>~~~</td>
</tr></table>


Horrendous! Luckily I happened to be emailing back and forth with <a href="http://manicprogrammer.com/cs/blogs/heynemann/default.aspx">Bernardo</a> about <a href="http://www.stormwindproject.org/">Stormwind</a> at the time and he mentioned that there <a href="http://peelmeagrape.net/projects/nant_macrodef">was in fact</a> a task. 

I added the Macros dll to the build file and voila:

<table class="CodeRay"><tr>
  <td class="line_numbers" title="click to toggle" onclick="with (this.firstChild.style) { display = (display == '') ? 'none' : '' }"><pre>1<tt>
</tt>2<tt>
</tt>3<tt>
</tt>4<tt>
</tt>~~~</td>
  <td class="code"><pre ondblclick="with (this.style) { overflow = (overflow == 'auto' || overflow == '') ? 'visible' : 'auto' }"><target name=&quot;compile&quot;><tt>
</tt>  <compile-project projectfile=&quot;\path\to\Project1\Project1.csproj&quot; /><tt>
</tt>  <compile-project projectfile=&quot;\path\to\Project2\Project2.csproj&quot; /><tt>
</tt></target>~~~</td>
</tr></table>
<br />
<table class="CodeRay"><tr>
  <td class="line_numbers" title="click to toggle" onclick="with (this.firstChild.style) { display = (display == '') ? 'none' : '' }"><pre>1<tt>
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
</tt>~~~</td>
  <td class="code"><pre ondblclick="with (this.style) { overflow = (overflow == 'auto' || overflow == '') ? 'visible' : 'auto' }"><macrodef name=&quot;compile-project&quot;><tt>
</tt>  <attributes><tt>
</tt>          <attribute name=&quot;projectfile&quot;/><tt>
</tt>  </attributes><tt>
</tt><tt>
</tt>  <sequential><tt>
</tt>    <property name=&quot;project.name&quot; value=&quot;${path::get-file-name-without-extension(projectfile)}&quot; /><tt>
</tt>                <tt>
</tt>    <exec program=&quot;${msbuild}&quot;><tt>
</tt>      <arg value=&quot;${projectfile}&quot; /><tt>
</tt>      <arg value=&quot;/p:OutputPath=${build.dir}\${project.name}\&quot; /><tt>
</tt>    </exec>        <tt>
</tt>  </sequential><tt>
</tt></macrodef>~~~</td>
</tr></table>

Further instructions on using the macrodef task are <a href="https://please.peelmeagrape.net/svn/public/nant/macrodef/build/doc/tasks/macrodef.html">here</a>.
