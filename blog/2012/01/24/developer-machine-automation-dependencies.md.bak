+++
draft = false
date="2012-01-24 23:16:52"
title="Developer machine automation: Dependencies"
tag=['software-development']
category=['Software Development']
+++

As I <a href="http://www.markhneedham.com/blog/2012/01/18/installing-puppet-on-oracle-linux/">mentioned in a post last week</a> we've been automating the setup of our developer machines with puppet over the last week and one thing that we've learnt is that you need to be careful about how you define dependencies.

The aim is to get your scripts to the point where the outcome is reasonably deterministic so that we can have confidence they're going to work the next we run them.	

We noticed two ways in which we haven't quite achieved determinism yet:

<h4>Accidental Dependencies</h4>

The first few times that we ran the scripts on top of a vanilla image we were doing it on a virtual machine which had VMware tools installed on it.

We'd forgotten that VMware tools had been installed on those VMs and ran into a problem with Oracle dependencies not being satisfied when we ran puppet on some machines which had CentOS installed directly (i.e. not on a virtual machine).

Those dependencies had been satisfied by our VMware tools installation on the VMs so we didn't realise that we hadn't explicitly stated those dependencies, something which we have done now.

<h4>External Dependencies</h4>
We couldn't find the Firefox version that we wanted install on the default yum repositories so we created a puppet task which linked to a Firefox RPM on an external server and then installed it.

It worked originally but at some stage over the last couple of weeks the URI was changed as a minor version had been upgraded, breaking our script. 

We also came across another way that external dependencies can fail today - if a corporate proxy blocks access to the URL!

We're trying to get to the stage where we're only relying on artifacts either coming from a <strong>yum repository or an internal repository</strong> where we can store any libraries which aren't available through yum.

<h4>Don't assume determinism</h4>

While trying to solve these dependency problems in our puppet scripts I made the mistake of assuming that if the script runs through once and works that it's always going to be that way in the future.

Since we had achieved that previously in my mind it was impossible for it to fail in future which stopped me from properly investigating why it had stopped working.
