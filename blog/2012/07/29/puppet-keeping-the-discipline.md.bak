+++
draft = false
date="2012-07-29 21:53:03"
title="Puppet: Keeping the discipline"
tag=['software-development', 'puppet']
category=['Software Development']
+++

For the last 5 weeks or so I've been working with <a href="http://puppetlabs.com/">puppet</a> every day to automate the configuration of various nodes in our stack and my most interesting observation so far is that you really need to keep your discipline when doing this type of work.

We can keep that discipline in three main ways when developing modules.

<h4>Running from scratch</h4>
Configuring various bits of software seems to follow the <a href="http://en.wikipedia.org/wiki/Pareto_principle">80/20 rule</a> and we get very close to having each thing working quite quickly but then end up spending a disproportionate amount of time tweaking the last little bits.

When it's 'just little bits' there is a massive temptation to <strong>make changes manually and then retrospectively put it into a puppet module and assume that it will work</strong> if we run from scratch.

From doing that a few times and seeing a module fail when run at a later stage we've realised it isn't a very good approach and we're started to get into the discipline of starting from scratch each time.

Ideally that would mean creating snapshots of a Virtual Machine instance and rolling back after each run but that ends up taking quite a bit of time so more often we're removing everything that a module installs and then running that module again.

<h4>Running as part of environment</h4>
We tend to run the modules individually when we start writing them but it's also important to run them as part of an environment definition as well to make sure modules play nicely with each other.

This is particularly useful if there are dependencies between our module and another one - perhaps our module will be notified if there's a configuration file change in another module for example.

<h4>Running on different machines</h4>
Even if we do the above two things we've still found that we catch problems with our modules when we try them out on other machines.

Machines which have been in use for a longer period of time will have earlier versions of a module which aren't easy to upgrade and we'll need to remove the old version and install the new one.

We've also come across occasions where other machines have left over files from modules that have since been removed and although the files seem harmless they can interfere with new modules that we're writing.
