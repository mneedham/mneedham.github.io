+++
draft = false
date="2008-11-19 21:30:19"
title="Debugging ASP.NET MVC source code"
tag=['aspnet', 'mvc']
category=['.NET']
+++

We've been doing some work with the ASP.NET MVC framework this week and one of the things we wanted to be able to do is to debug through the source code to see how it works.

Our initial idea was to <a href="http://haacked.com/archive/2008/11/03/bin-deploy-aspnetmvc.aspx">bin deploy the ASP.NET MVC assemblies</a> with the corresponding pdbs. Unfortunately this didn't work and we got a conflict with the assemblies deployed in the GAC:


~~~text

Compiler Error Message: CS0433: The type 'System.Web.Mvc.FormMethod' exists in both 'c:\WINDOWS\Microsoft.NET\Framework\v2.0.50727\Temporary ASP.NET Files\root\8553427a\c1d1b9c6\assembly\dl3\898a195a\60680eb9_3349c901\System.Web.Mvc.DLL' and 'c:\WINDOWS\assembly\GAC_MSIL\System.Web.Mvc\1.0.0.0__31bf3856ad364e35\System.Web.Mvc.dll'
~~~

We attempted to uninstall the System.Web.Mvc assembly from the GAC but were unable to do so because it has other dependencies. 

The next idea was to uninstall ASP.NET MVC using the MSI uninstaller. This worked in terms of getting rid of the assembly from the GAC but it meant that we no longer had support for ASP.NET MVC in Visual Studio.

Luckily <a href="http://tgould.blogspot.com/">Troy</a> pointed out James Kovac's blog post about <a href="http://codebetter.com/blogs/james.kovacs/archive/2008/01/17/debugging-into-the-net-framework-source.aspx">debugging the .NET framework source</a> and we were able to debug the ASP.NET MVC code by hooking up the <a href="http://www.codeplex.com/aspnet/SourceControl/DirectoryView.aspx?SourcePath=%24%2faspnet%2fMVC%2fSymbols&changeSetId=17272">pdbs</a> that come with the <a href="http://weblogs.asp.net/scottgu/archive/2008/03/21/asp-net-mvc-source-code-now-available.aspx ">source code download</a>. 

Some other approaches were pointed out on the <a href="http://www.nabble.com/Debugging-ASP.NET-MVC-td20554211.html">ALT.NET mailing list</a> although the above is what worked for us.


