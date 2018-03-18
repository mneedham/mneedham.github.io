+++
draft = false
date="2008-08-30 16:30:41"
title="scp Nant Task - 'scp' failed to start. The system cannot find the file specified"
tag=['build', 'nant', 'scp']
category=['Build']
+++

I was trying to make use of the <a href="http://nantcontrib.sourceforge.net/">Nant Contrib</a> <a href="http://nantcontrib.sourceforge.net/release/latest/help/tasks/scp.html">scp task</a> earlier and was getting an error message which at the time seemed a bit strange (now of course having solve the problem it is obvious!)

This was the task I was running:


~~~text

<scp file="someFile.txt" server="some.secure-server.com" />
~~~

This was the error:


~~~text

'scp' failed to start. 
     The system cannot find the file specified
~~~

I ran it in debug mode to try and see what was going on and got this stack trace:


~~~text

NAnt.Core.BuildException: C:\projects\project1\default.build(18,4):
'scp' failed to start. ---> System.ComponentModel.Win32Exception: The system cannot find the file specified
   at System.Diagnostics.Process.StartWithCreateProcess(ProcessStartInfo startInfo)
   at System.Diagnostics.Process.Start()
   at NAnt.Core.Tasks.ExternalProgramBase.StartProcess()
   --- End of inner exception stack trace ---
   at NAnt.Core.Tasks.ExternalProgramBase.StartProcess()
   at NAnt.Core.Tasks.ExternalProgramBase.ExecuteTask()
   at NAnt.Contrib.Tasks.ScpTask.ExecuteTask()
   at NAnt.Core.Task.Execute()
   at NAnt.Core.Target.Execute()
   at NAnt.Core.Project.Execute(String targetName, Boolean forceDependencies)
   at NAnt.Core.Project.Execute()
   at NAnt.Core.Project.Run()
~~~

Eventually a colleague and I realised that the scp task was <strong>assuming</strong> that there was an executable called 'scp' on the path.

This can be overriden by setting the 'program' attribute to whatever you want. In this case since we were running from Windows we downloaded <a href="http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html">Putty's</a> <a href="http://the.earth.li/~sgtatham/putty/latest/x86/pscp.exe">pscp executable</a> and put that on the Windows path. The code to call the scp task now looks like this:


~~~text

<scp file="someFile.txt" server="some.secure-server.com" program="pscp" />
~~~

If you don't want to put it on the path then the following works just as well:


~~~text

<scp file="someFile.txt" server="some.secure-server.com" program="c:\path\to\pscp.exe" />
~~~
