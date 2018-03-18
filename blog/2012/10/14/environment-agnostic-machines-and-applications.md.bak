+++
draft = false
date="2012-10-14 18:49:02"
title="Environment agnostic machines and applications"
tag=['devops-2']
category=['Software Development', 'DevOps']
+++

On my current project we've been setting up production and staging environments and <a href="http://in.linkedin.com/pub/shodhan-sheth/2/277/287">Shodhan</a> came up with the idea of making staging and production identical to the point that a machine wouldn't even know what environment it was in.

Identical in this sense means:

<ul>
<li>Puppet doesn't know which environment the machine is in. Our factor variables suggest the environment is production.</li>
<li>We set the RACK_ENV variable to production so applications don't know what environment they're in.</li>
<li>The IPs and host names of equivalent machines in production/staging are identical</li>
</ul>

The only thing that differs is that the external IPs to access machines differ and therefore the NATed address that they display to the world when making any outgoing requests is also different.

The only place where we do something different based on an environment is when deploying applications from <a href="http://jenkins-ci.org/">Jenkins</a>.

At that stage if there needs to be a different configuration file or initializer depending on the environment we'll have it placed in the correct location.

<h3>Why are we doing this?</h4>

The benefit of doing this is that we can have a much higher degree of confidence that something which works in staging is also going to work in production. 

Previously we'd noticed that we were inclined to write switch or if/else statements in puppet code based on the environment which meant that the machines were being configured differently depending on the environment. 

There have been a few problems with this approach, most of which we've come up with a solution for.

<h3>Problems</h4>

<h4>Applications that rely on knowing their environment</h4>

One problem we had while doing this was that some applications did internally rely on knowing which environment they were deployed on.

For example, we have an email processing job which relies on the RACK_ENV variable and we would end up processing production emails on staging if we deployed the job there with RACK_ENV set to 'production'.

Our temporary fix for this was to change the application's deployment mechanism so that this job wouldn't run in staging but the long term fix is to make it environment agnostic. 

<h4>Addressing machines from outside the network</h4>

We sometimes need to <a href="http://www.markhneedham.com/blog/2012/08/10/sshing-onto-machines-via-a-jumpbox/">SSH into machines via a jumpbox</a> and this becomes more difficult now that machines in production and staging have identical IPs and host names.

We got around this with some cleverness to rewrite the hostname if it ended in staging. The <cite>~/.ssh/config</cite> file reads like this:


~~~text

Host *.staging
  IdentityFile ~/.ssh/id_rsa 
  ProxyCommand sh -c "/usr/bin/ssh_staging %h %p"
~~~

And in <cite>/usr/bin/ssh_staging</cite> we have the following:


~~~text

 HOSTNAME=`echo $1 | sed s/staging/production/`
 ssh staging-jumpbox1 nc $HOSTNAME $2
~~~

If we were to run the following command:


~~~text

ssh some-box.staging
~~~

That would SSH us onto the staging jumpbox and then proxy an SSH connection onto <cite>some-box.production</cite> using netcat.

Since web facing applications in both staging and production are referred to by the same fully qualified domain name (FQDN) we need to update our <cite>/etc/hosts</cite> file to access the staging version.


~~~text

staging.ip     some-app.production.whatever.else
~~~

<h4>When SSHing you can't tell which environment a machine is</h4>
One problem with having the machines not know their environment is that we couldn't tell whether or not we'd SSH'd into a staging or production machine by looking at our command prompt since they have identical host names.

We ended up defining PS1 based on the public IP address of the machine which we found out by calling <a href="http://icanhazip.com/">icanhazip.com</a>

Overall despite the fact that it was initially painful - and Shodhan game-fully took most of that pain - to do this I think it makes sense as an idea and I'd probably want to have it baked in from the beginning on anything I work on in future.
