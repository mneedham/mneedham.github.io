+++
draft = false
date="2009-07-25 11:28:38"
title="Cruise Agents: Reducing 'random' build failures"
tag=['cruise-agents']
category=['Build']
+++

As I mentioned previously we're making use of <a href="http://www.markhneedham.com/blog/2009/05/21/build-using-virtual-machines-to-run-it-in-parallel/">multiple cruise agents in our build</a> to allow us to run our acceptance tests in parallel, therefore allowing a build which would be nearly 2 hours if run in sequence to be completed in around 10 minutes.

Early on with this approach we were getting a lot of failures in our builds which weren't directly related to the code being changed and were more to do with the various dependencies we were making use of. 

We needed these dependencies but we were only finding out if they were actually setup correctly much later on instead of doing an environment check first.

One example of this was the Shibboleth daemon which needed to be started in order for our tests to be able to login to the single sign on system.

We have it running as a Windows service and despite the fact we had it setup to 'auto start' whenever the operating system was running we often had failures where it had just failed to start with no trace in any of the error logs as to why that was the case.

The way we have currently got around this problem is by writing a <a href="http://blogs.geekdojo.net/rcase/archive/2005/01/06/5971.aspx">custom nant task</a> which checks if the service is running and if not then starts it up by making use of the '<a href="http://msdn.microsoft.com/en-us/library/system.serviceprocess.servicecontroller.servicecontroller.aspx">ServiceController</a>' class.


~~~csharp

[TaskName ("startShibboleth")]
public class StartShibbolethDaemon : Task
{
	protected override void ExecuteTask() 
	{
		var shibbolethDaemon = new ServiceController("shibbolethServiceName");

		if(shibbolethDaemon.Status == ServiceControllerStatus.Running) 
		{
			Project.Log(Level.Info, "Shibboleth already running");
		}
		else 
		{
			shibbolethDaemon.Start();
			Project.Log(Level.Info, "Shibboleth started");
		}
	}
}
~~~

We can then reference that task in our build before we run any tests which rely on it. We decided to write a custom task instead of using the built in <a href="http://nant.sourceforge.net/release/latest/help/tasks/servicecontroller.html">servicecontroller</a> task so that we could record whether or not it was already running and I couldn't see a way to do that with the built in task.

Another quite common trend of build failures came about when our tests tried to connect to selenium server and were unable to do so because it wasn't currently running - we have a batch file to manually start it up on our agents as we are running the build from a Windows service which means we can't  directly start processes from the file system the way we can when we run the build locally.

The original way we got around this problem was to add the selenium server startup script to the 'StartUp' folder of the 'Administrator' user on each of the cruise agents.

While this works fine when a user is actually logged into the virtual machine that hosts the agent we noticed that quite often an agent would register itself with the cruise server but we had forgotten to login on that virtual machine and any builds assigned to it would fail.

My colleague came up with quite a neat way of getting around this problem by automatically logging in the cruise agents which can be done by adding the following registry entry by putting the following in a file with the extension 'reg' and then double clicking it.


~~~text

Windows Registry Editor Version 5.00

[HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon]
"AutoAdminLogon"="1"
"DefaultPassword"="password"
~~~

I think the key for us here was ensuring that the build was pretty much self contained and able to get itself into a working state if its dependencies aren't setup correctly.

We spent a bit of time tracking the 'random' failures and working out which ones were addressable and which ones we needed to gather more information on. We certainly have some work to do in this area but we've managed to sort out some of the persistent offenders!

It's really easy to just ignore the supposedly random failures and just re-run the build but it doesn't really solve the underlying problem. We've found it's quite rare that there are ever actually random failures in the build, just failures that we don't know enough about yet.
