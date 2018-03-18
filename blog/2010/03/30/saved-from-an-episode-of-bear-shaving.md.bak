+++
draft = false
date="2010-03-30 06:57:43"
title="Saved from an episode of bear shaving"
tag=['software-development']
category=['Software Development']
+++

As part of our continuous integration build we have a step in the build which tears down a Windows service, uninstalls it and then reinstalls it later on from the latest files checked into the repository.

One problem we've been having recently is that despite the fact it should already have been uninstalled a lock has been kept on the log4net dll in our build directory, a directory that we tear down as one of the next steps.

It was a bit of a sporadic failure and whenever we went on the build machine and checked for file handles with <a href="http://technet.microsoft.com/en-us/sysinternals/bb896653.aspx">Process Explorer</a> the log4net dll never showed up on the list.

I wrongly assumed that it couldn't be getting locked by the Windows service because the Windows service would already be gone by that stage.

We therefore started on a <a href="http://www.markhneedham.com/blog/2009/08/06/bear-shaving/">bear shaving</a> expedition which involved trying to make use of <a href="http://www.emptyloop.com/unlocker/">Unlocker</a> and <a href="http://download.cnet.com/FileAssassin/3000-2094_4-10639988.html">File Assassin</a> to release the file handle so that we'd be able to delete the directory.

We weren't able to get either of those tools to do the job from the command line and luckily at this stage another colleague had the idea to check whether or not the Windows service was actually immediately removed in Task Manager when we tore it down.

After realising that it wasn't we were able to address this problem and put a step in the build to look for that process and kill it as part of the build.

I guess the real solution to this problem would be for the uninstall to block until it was properly uninstalled but this seems to be the closest we can get to addressing the cause rather than the effect.
