+++
draft = false
date="2008-10-19 22:49:14"
title="Build: Checkout and Go "
tag=['build']
category=['Build']
+++

On the previous project I was working on one of the pain points we were having was around setting up developer environments such that you could get the code up and running on a machine as quickly as possible.

I would go to a newly formatted machine ready to set it up for development and run into a cascading list of dependencies I hadn't considered.

SVN wasn't installed, then Ruby, then we had the wrong version of Java and all the while we were wasting time when this process could have been automated.

One of the things we were working on on my previous project was how to get our project into such a state that we could just checkout the code on a machine and get it ready to run on there relatively quickly.

I haven't yet come up with a good solution for automating all dependency checking but an approach that my <a href="http://pilchardfriendly.wordpress.com/">colleague</a> has been advocating on my current project is that of aiming for a '<strong>Checkout and Go</strong>' build.

The idea is fairly simple - when a developer joins the team they should be able to checkout all the code from source control, browse to the root directory and run a script called 'go' which will download and install everything needed to run the build on their machine.

We are using <a href="http://incubator.apache.org/buildr">buildr</a>, so in our case this mainly involves populating our <a href="http://www.rubygems.org/">JRuby</a> and <a href="http://www.rubygems.org/">Ruby gem</a> repositories. buildr takes care of downloading our Java dependencies.

<h3>Potential issues</h3>
The original Checkout and Go build script was only written for use from the Unix shell which obviously restricted its use somewhat! A couple of people on the team were running on Windows so we now have two versions of a very similar script.

There are some parts of our setup process which only need to be run the first time the developer runs the build. There is a trade off to be made with regards to whether it is better to incorporate these into the main script and write the associated logic around ensuring they don't get run every time as opposed to leaving developers to run them once when they first checkout the code.

One interesting thing we have noticed is that although the theory is these scripts only need to be run once, there are actually new dependencies being introduced now and then which requires them to be re-run. If there is frequent change then the benefit of the Checkout and Go approach clearly increases. 

<h3>Alternative approach</h3>
The alternative to the Checkout and Go approach is to have a setup where we only provide a build file which, working on the assumption that the developer will take care of the dependencies themself - these dependencies would then typically be written up on a Wiki page.

The thing I like about this approach is that it is much simpler to setup initially - there is no code to write around automating the download and setup of dependencies. 

The disadvantage is that it is non deterministic - as we are relying on a human to execute a series of instructions the chance of someone doing something just slightly different is higher, therefore leading to the problem of developer machines not being setup in an identical manner.

<h3>In Conclusion</h3>

We don't have this process perfect yet and there is a bit of a trade off with regards to making the go script really complicated to allow a completely automated process as opposed to covering maybe 90% of the setup in an automated script and then having the remaining 10% done manually or in other test scripts which a developer can run when required.

This idea has been the best one that I have seen with regards to getting developer environments setup and running quickly but it would be good to know if anyone has any better ideas around this.
