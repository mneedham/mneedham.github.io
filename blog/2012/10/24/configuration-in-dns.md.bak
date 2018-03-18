+++
draft = false
date="2012-10-24 17:40:49"
title="Configuration in DNS"
tag=['devops-2']
category=['DevOps']
+++

In the <a href="http://www.thoughtworks.com/radar/#/techniques/9056">latest version of the ThoughtWorks Technology Radar</a> one of the areas covered is 'configuration in DNS', a term which I first came across earlier in the year from a mailing list post by my former colleague <a href="http://dan.bodar.com/">Daniel Worthington-Bodart</a>. 

The radar describes it like so:

<blockquote>
Application deployments often suffer from an excess of environment-specific configuration settings, including the hostnames of dependent services. <strong>Configuration in DNS</strong> is a valuable technique to reduce this complexity by using standard hostnames like ‘mail’ or ‘db’ and have DNS resolve to the correct host for that environment. This can be achieved in multiple ways, including split-horizon DNS or configuring search subdomains. Collaboration between development teams and IT operations is essential to achieve this, but that is unfortunately still difficult in some organizations.
</blockquote>

As I alluded to in <a href="http://www.markhneedham.com/blog/2012/10/14/environment-agnostic-machines-and-applications/">my post about creating environment agnostic machines</a> one of the techniques that we've used to achieve this is configuration in DNS, whereby we use fully qualified domain names (FQDN) for services in our configuration files and have DNS resolve them.

For example for our frontend application we use the service name <cite>frontend.production.domain-name.com</cite> which resolves to a load balancer that routes requests to the appropriate machine. 

<a href="http://in.linkedin.com/pub/shodhan-sheth/2/277/287">Shodhan</a> pointed out that the 'production' in the name is a bit misleading because it suggests the name is environment specific which isn't the case. 

We use the same name in staging as well and since the two environments are on different virtual networks the name will resolve to a different machine.

Now that we're using this approach I was trying to remember what other ways I've seen environment-specific configuration handled and I can think of two other ways:

<h4>IP addresses</h4>
One way is to hard code IP addresses in our configuration files and then either vary those based on the environment or have the environments use separate private networks in which case we could use the same ones.

The disadvantage of this approach is that IPs can be quite difficult to remember and are easy to mistype.

<h4>Machine FQDNs</h4>
An approach which is slightly better than using IPs is to make use of a specific machine's FQDN which would then be resolved by DNS.

If the machine's IP changes then that would be taken care of and we wouldn't need to change our configuration file but it isn't particularly flexible to change.

For example if we wanted to change one of our services to make it load balanced that would be much more difficult to do if we've hard coded machine names into configuration files than if we have something like <cite>db.backend.production</cite> which we can instead route to a load balancer's IP.

Given that we wanted to use service oriented host names we than had to decide how those names would be resolved:

<h4>Host files</h4>
One way to do this, and the way that we're currently using, is to store all the FQDNs in the <cite>/etc/hosts</cite> file on every machine and point those names at the appropriate machines.

In our case we're often pointing them at a hardware load balancer but it could also be an individual machine where that makes more sense e.g. when pointing to the master in a MySQL setup.

This could become quite difficult to manage as the number of FQDNs increases but we're managing it through puppet so the most annoying thing is that it can take up to half an hour for a newly added FQDN to be resolvable across the whole stack.

<h4>Internal DNS server</h4>
An alternative approach is to setup an internal DNS server which would mainly be used to service DNS requests for our own network. 

The disadvantage of this approach is that it would be a single point of failure which is problematic in terms of making it a good thing to try and compromise if you can break into the network as well as being a potential performance bottleneck.

Of course the latter can be solved by making use of caching or making the DNS server redundant but I do like the simplicity of the <cite>/etc/hosts</cite> approach.

I'd be interested in hearing about other/better approaches to solving the configuration problem if people know of any!
