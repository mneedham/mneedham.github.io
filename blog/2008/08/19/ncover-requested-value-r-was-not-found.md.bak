+++
draft = false
date="2008-08-19 21:18:44"
title="NCover - Requested value '/r' was not found"
tag=['build', 'nant', 'ncover', 'net']
category=['Build']
+++

I've been trying to integrate <a href="http://www.ncover.com/">NCover</a> into our build and probably making life harder for myself than it needs to be.

The title refers to the error message that I was getting when trying to run  the <a href="http://www.kiwidude.com/dotnet/doc/NCoverExplorer.NAntTasks/tasks/ncover.html">ncover nant task</a> on version 1.0.1 of NCover earlier today.


~~~text

[ncover] Starting 'C:\Program Files\NCover\ncover-console.exe 
(//r "\long\path\to\tmp392.tmp.ncoversettings" )' in 'C:\my-project\trunk\src'
[ncover] Unhandled Exception: System.ArgumentException: Requested value '/r' was not found.
[ncover]    at System.Enum.Parse(Type enumType, String value, Boolean ignoreCase)
[ncover]    at NCover.Utilities.Arguments.ParseArgument(String arg, 
CommandLineArgument& key, String& value) in C:\tools\eclipse3M6\workspace\ncover\src\NCover\Utilities\Arguments.cs:line 192
~~~


After some inspired Googling <a href="http://markthomas.info/blog">my colleague</a> managed to work out that the problem was that you can't pass a settings file path which has spaces in to the ncover executable, hence the error message. It's the same problem in handling spaces that I mentioned in an <a href="2008/08/14/msbuild-use-outputpath-instead-of-outdir/">earlier post on msbuild</a>.

The advice on the forum was to upgrade to one of the more recent versions where the bug has been fixed. Downloads of the free version of NCover (it becomes paid for at version 2.0) are available <a href="http://www.ncover.com/download/discontinued">here</a>.
