+++
draft = false
date="2009-03-24 22:55:41"
title="ASP.NET MVC: Pre-compiling views when using SafeEncodingCSharpCodeProvider"
tag=['aspnet-mvc']
category=['.NET']
+++

We've been doing some work to get our views in ASP.NET MVC to be pre-compiled which allows us to see any errors in them at compilation rather than at run time.

It's relatively simple to do. You just need to add the following code into your .csproj file anywhere below the <Project> element:


~~~text

<Target Name="AfterBuild">
    <AspNetCompiler VirtualPath="/" PhysicalPath="$(ProjectDir)\..\$(ProjectName)"/>
</Target>
~~~

where VirtualPath refers to the virtual path defined inside your project file and PhysicalPath is the path to the folder which contains the project with the views in.

As I <a href="http://www.markhneedham.com/blog/2009/02/12/aspnet-mvc-preventing-xss-attacks/">previously mentioned</a> we're using <a href="http://blog.codeville.net/2007/12/19/aspnet-mvc-prevent-xss-with-automatic-html-encoding/">Steve Sanderson's SafeEncodingHelper</a> to protect our website from cross scripting attacks.

A problem we ran into when trying to pre-compile these views is that when the AfterBuild target gets run it tries to compile our views using the SafeEncodingCSharpCodeProvider, leading to this error:


~~~text

 [msbuild] /global.asax(1): error ASPPARSE: The CodeDom provider type "SafeEncodingHelper.SafeEncodingCSharpCodeProvider, SafeEncodingHelper" could not belocated. (\path\to\web.config line 143)
~~~

From what we could tell it looked like the AspNetCompiler was expecting the dll containing SafeEncodingCSharpCodeProvider to be within the directory we specified for the PhysicalPath but we were actually compiling it to another directory instead.


~~~text

	<target name="compile">
		<msbuild project="solutionFile.sln">
			<property name="OutputPath" value="/some/output/path" />
		</msbuild>
	</target>
~~~

We only noticed this on our build machine because when Visual Studio builds the solution it builds each project into ProjectName/bin which meant that locally we always had the dll available since we rarely do 'Project Clean' from the IDE.

The solution/hack to our problem was to build just that project in Nant without specifying an OutputPath - by default msbuild builds into the /bin directory of the project which is exactly what we need! Our compile target now looks like this:


~~~text

	<target name="compile">
		<msbuild project="projectWithViewsIn.csproj">
		</msbuild>
		<msbuild project="solutionFile.sln">
			<property name="OutputPath" value="/some/output/path" />
		</msbuild>
	</target>
~~~

It's not the greatest solution ever but it's an easier one than changing how we use the compilation path throughout the build file.
