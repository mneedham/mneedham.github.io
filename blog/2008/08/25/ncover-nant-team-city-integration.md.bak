+++
draft = false
date="2008-08-25 21:29:03"
title="NCover Nant Team City Integration"
tag=['team-city', 'nant', 'ncover', 'tutorial']
category=['Build']
+++

I've been spending quite a bit of time setting up <a href="http://www.ncover.com/">NCover</a> and then integrating it into <a href="http://www.jetbrains.com/teamcity/">Team City</a>. 

I've read some posts which cover parts of this process but nothing which covers the end to end process so hopefully my experience can help to fill that void.

<h3>Step 1</h3>
Download NCover 1.5.8, NCover Explorer 1.4.0.7, NCover Explorer Extras 1.4.0.5 from <a href="http://www.kiwidude.com/dotnet/DownloadPage.html">Kiwidude's website</a> and the <a href="http://www.ncover.com/download/discontinued">NCover website</a> .

<h3>Step 2</h3>
Put the following into your Nant build file:


~~~text

	<loadtasks assembly="..\lib\NCoverExplorer.Extras\NCoverExplorer.NAntTasks.dll"/>
   	<exec program="regsvr32" workingdir="..\lib\NCover-1.5.8" commandline="/s coverlib.dll"/>
~~~

I put this right at the top of the build but I expect it doesn't matter where it goes as long as it's called at some stage before NCover and NCover Explorer are called.


~~~text

<macrodef name="cover.tests">
	<attributes>
		<attribute name="in.assemblies" />
	</attributes>
	<sequential>	
		<ncover
		    program="..\lib\NCover-1.5.8\NCover.Console.exe"
		    commandLineExe="..\lib\nunit-2.4\nunit-console.exe"
		    commandLineArgs="${build.dir}\UnitTests\UnitTests.dll"
		    coverageFile="${report.dir}\Unit.Test.Coverage.xml"
			assemblyList="${in.assemblies}"
		  />	
		  
	  <ncoverexplorer
		program="..\lib\NCoverExplorer\NCoverExplorer.Console.exe"
		projectName="Project"
		reportType="ModuleClassSummary" 
		outputDir="${report.dir}"
		xmlReportName="TestCoverage.xml"
		htmlReportName="TestCoverage.html"
		showExcluded="True"
		satisfactoryCoverage="80" >
		<fileset>
		  <include name="${report.dir}\Unit.Test.Coverage.xml" />
		</fileset>
		<exclusions>
		  <exclusion type="Assembly" pattern="*.Tests" />
		  <exclusion type="Namespace" pattern="*.Tests*" />
		</exclusions>
	  </ncoverexplorer>			  		  
	</sequential>
</macrodef>
~~~

This <a href="http://peelmeagrape.net/projects/nant_macrodef">macro</a> can then be called as follows:


~~~text

<target name="cover.unit.tests"	
	<cover.tests in.assemblies="Project1;Project1" />
</target>
~~~

N.B. The projects passed in as the 'in.assemblies' argument should be semi colon separated.

<h3>Step 3</h3>

The next step is to setup the artifacts for your project. From the Team City admin panel navigate to the project configuration settings and select artifacts.

Add the following to the 'Artifact paths':


~~~text

TestCoverage.html
~~~

It should now show up as a viewable artifact from the project listing page.

<h3>Step 4</h3>

To get the coverage report to show up on a tab on the build summary page we need to edit the <b>main-config.xml</b> file

The location of this file can be found by browsing to 'Administration > Server Configuration' from the Team City admin panel

Add the following line after the other 'report-tab' entries in this file:


~~~text

<report-tab title="Code Coverage Summary" basePath="" startPage="TestCoverage.html" /> 
~~~

<h3>Potential Problems</h3>

I encountered some problems in getting this up and running. They were as follows:

<blockquote>
NCover: Profiled process terminated. Profiler connection not established
</blockquote>

After some Googling I found <a href="http://weblogs.asp.net/rchartier/archive/2006/01/30/436897.aspx">this post</a> which explains how to solve the problem. 

To summarise this problem occurs when trying to run NCover without Administrative privileges. The coverlib.dll shipped with NCover needs to be registered. This can be done two ways:

1) Put the following code into your build file right at the top

~~~text

<exec program="regsvr32" workingdir="\path\to\ncover" commandline="/s coverlib.dll"/>
~~~

2) Run the same command from the command line


~~~text

C:\path\to\NCover-1.5.8>regsvr32 CoverLib.dll
~~~

<blockquote>
NCover - Requested value '/r' was not found
</blockquote>

This error occurred when I was using version 1.0.1 of NCover and to cut a long story short, you need to <a href="http://www.ncover.com/download/discontinued">upgrade</a> to get rid of the problem.

More details are on <a href="http://www.markhneedham.com/blog/2008/08/19/ncover-requested-value-r-was-not-found/">this post</a>.


The information here has been accumulated from my experiences, <a href="http://weblogs.asp.net/lkempe/archive/2008/03/30/integration-of-ncover-into-team-city-for-tech-head-brothers.aspx">this post</a> on NCover integration and the <a href="http://www.jetbrains.net/confluence/display/TCD3/TeamCity+Data+Directory">official documentation</a>.


