+++
draft = false
date="2008-08-20 18:50:18"
title="Building in release mode with no pdbs with msbuild"
tag=['build', 'msbuild', 'net', 'microsoft', 'release']
category=['.NET', 'Build']
+++

I've been having trouble trying to work out how to build our projects in msbuild in release mode without creating the customary <a href="http://msdn.microsoft.com/en-us/library/yd4f8bd1(VS.71).aspx">pdb</a> files that seem to be created by default.

I tried calling msbuild.exe with the 'Release' configuration:

~~~text

'C:\WINDOWS\Microsoft.NET\Framework\v3.5\MSBuild.Exe ( Proj.csproj /p:OutputPath=\output\path\ 	/p:Configuration=Release)'
~~~
To no avail. It still created the pdb file. Next I tried setting the 'DebugSymbols' property to false:

~~~text

'C:\WINDOWS\Microsoft.NET\Framework\v3.5\MSBuild.Exe ( Proj.csproj /p:OutputPath=\output\path\ 	/p:Configuration=Release /p:DebugSymbols=false)'
~~~
Still it created the file. Finally I found <a href="http://forums.msdn.microsoft.com/en-US/msbuild/thread/59d636b2-0cf3-4434-b7b9-c20f2e38fb18/">this post</a> which suggested that you actually needed to make the change in the Proj.csproj file itself.

I changed this part of the file so that DebugType is now 'none'. It had a value of 'pdbonly'  when I opened the file.

~~~text

  none
  true
  bin\Release\
  TRACE
  prompt
  4
~~~
The pdb is no longer created.

*Update*
This can also be done by passing /p:DebugType=none as a command line argument as <a href="2008/08/20/building-in-release-mode-with-no-pdbs-with-msbuild/#comment-67">Tim points out</a> in the comments.
