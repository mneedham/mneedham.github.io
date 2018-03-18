+++
draft = false
date="2009-05-21 18:02:27"
title="Build: Using virtual machines to run it in parallel"
tag=['build', 'selenium', 'parallel-builds']
category=['Build']
+++

One of the things that we've been working on lately to improve the overall time that our full build takes to run is to split the acceptance tests into several small groups of tests so that we can run them in parallel.

We are using <a href="http://studios.thoughtworks.com/cruise-continuous-integration">Cruise</a> as our build server so the ability to have multiple agents running against different parts of the build at the same time comes built it.

We then had to work out what the best environment to run more agents would be.

I guess the traditional approach to the problem would be to get some extra machines to use to run the build but this wasn't possible so our initial solution was to use our developer virtual machines as build agents.

This worked in principle but the environment became way too slow to work on when the build was running and the selenium windows that popped up when each test was running became amazingly annoying. We could only really use this approach to set up agents on developer machines that weren't being used that day.

We therefore came across the idea of having 2 virtual machines running on each developer machine, splitting the resources of the machine across the two virtual machines.

From experimenting it seems like the agent used to run a build with selenium tests in it needs to have around 1.2 GB of RAM assigned to it to run at a reasonable rate. Our developer machines have a total of 3 GB of RAM so the majority of the rest is being used by the development virtual machine.

Our development virtual machine environments run marginally slower when there is a build running on that machine but we've reduced that problem by ensuring we have the build running across as many developer machines as possible so that it runs less frequently on each machine

I think it serves as a worthwhile trade off for helping to reduce our total build time significantly - running sequentially it would take over an hour to run all our tests but in parallel we've managed to get a 10-15 minute turn around time at worst.

While trying to see if we could make that any faster we toyed with the idea of having two build virtual machines on the same box but that didn't seem to provide the improvement that we expected due to I/O restraints - our build has quite a bit of writing and reading from disc and having two builds doing this at the same time seemed to slow down both of them.

Overall though it's working out pretty well for us in terms of providing us a quick feedback mechanism of whether or not our system is working correctly end to end.
