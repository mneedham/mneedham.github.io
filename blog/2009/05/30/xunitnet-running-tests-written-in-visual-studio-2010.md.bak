+++
draft = false
date="2009-05-30 11:51:53"
title="xUnit.NET: Running tests written in Visual Studio 2010"
tag=['xunit']
category=['.NET']
+++

I've been playing around with F# in Visual Studio 2010 after the <a href="http://blogs.msdn.com/dsyme/archive/2009/05/20/visual-studio-2010-beta1-with-f-is-now-available-plus-matching-f-ctp-update-for-vs2008.aspx">Beta 1 release last Wednesday</a> and in particular I've been writing some xUnit.NET tests around the <a href="http://www.markhneedham.com/blog/2009/04/13/f-a-day-of-writing-a-little-twitter-application/">twitter</a> <a href="http://www.markhneedham.com/blog/2009/04/18/f-refactoring-that-little-twitter-application-into-objects/">application</a> I've been working on.

A problem I ran into when attempting to run my tests against 'xunit.console.exe' is that <a href="http://twitter.com/bradwilson/statuses/1955212964">xUnit.NET is linked to run against version 2.0 of the CLR</a> and right now you can't actually change the 'targetframework' for a project compiled in Visual Studio 2010.


~~~text

> xunit.console.exe ..\..\TwitterTests\bin\Debug\TwitterTests.dll

System.BadImageFormatException: Could not load file or assembly 'C:\Playbox\FSharpPlayground\Twitter\TwitterTests\bin\Debug\TwitterTests.dll' or one of its dependencies. This assembly is built by a runtime newer than the currently loaded runtime and cannot be loaded.
File name: 'C:\Playbox\FSharpPlayground\Twitter\TwitterTests\bin\Debug\TwitterTests.dll'
   at System.Reflection.AssemblyName.nGetFileInformation(String s)
   at System.Reflection.AssemblyName.GetAssemblyName(String assemblyFile)
   at Xunit.Sdk.Executor..ctor(String assemblyFilename)
   at Xunit.ExecutorWrapper.RethrowWithNoStackTraceLoss(Exception ex)
   at Xunit.ExecutorWrapper.CreateObject(String typeName, Object[] args)
   at Xunit.ExecutorWrapper..ctor(String assemblyFilename, String configFilename, Boolean shadowCopy)
   at Xunit.ConsoleClient.Program.Main(String[] args)
~~~

I wasn't really sure how to fix this but luckily <a href="http://twitter.com/davcamer/statuses/1955037499">Dave</a> pointed out that the way to do this is to add a <a href="http://msdn.microsoft.com/en-us/library/bbx34a2h(VS.100).aspx">'requiredRunTime' tag in the 'startup' section of the configuration file</a> (xunit.console.exe.config):


~~~text

<configuration>
...
	<startup>
      <requiredRuntime version="v4.0.20506" safemode="true"/>
	</startup>
...
</configuration>
~~~

And all is good:


~~~text

> xunit.console.exe ..\..\TwitterTests\bin\Debug\TwitterTests.dll

xUnit.net console runner (xunit.dll version 1.4.9.1416)
Test assembly: C:\Playbox\FSharpPlayground\Twitter\TwitterTests\bin\Debug\TwitterTests.dll
........
Total tests: 8, Failures: 0, Skipped: 0, Time: 0.231 seconds
~~~

