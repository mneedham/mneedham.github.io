+++
draft = false
date="2013-04-07 11:41:34"
title="Treating servers as cattle, not as pets"
tag=['devops-2']
category=['DevOps']
+++

<p>Although I didn't go to <a href="http://www.devopsdays.org/events/2013-london/">Dev Ops Days London</a> earlier in the year I was following the hash tag on twitter and one of my favourites things that I read <a href="https://twitter.com/pikesley/statuses/312614061818904576">was the following</a>:</p>


<blockquote>
“Treating servers as cattle, not as pets” #DevOpsDays
</blockquote>

<p>I think this is particularly applicable now that a lot of the time we're using virtualised production environments via <a href="http://aws.amazon.com/">AWS</a>, <a href="http://www.rackspace.co.uk/cloud-servers/">Rackspace</a> or <insert-cloud-provider-here>.</p>


<p>At <a href="http://www.uswitch.com/">uSwitch</a> we use AWS and over the last week <a href="https://twitter.com/siddharthdawara">Sid</a> and I spent some time investigating a memory leak by running our applications against two different versions of Ruby.</p>


<p>One of them was from the <a href="https://launchpad.net/~brightbox/+archive/ppa">Brightbox repository</a> and the other was custom built but they had annoyingly different puppet configurations so we decided to treat them as separate machine types.</p>


<p>We spun up one of the custom built Ruby nodes and put it in the load balancer alongside 11 of the other node types and left it for the day serving traffic.</p>


<p>The next day we had look at the <a href="http://newrelic.com/">New Relic</a> memory consumption for both node types and it was clear that the custom built one's memory usage was climbing much more slowly than the other one.</p>


<p>Instead of trying to work out how to change the Ruby version of the 11 existing nodes we realised it would probably be quicker to just spin up 11 new ones with the custom built Ruby and swap them with the existing ones.</p>


<p>This was pretty much as easy as removing the existing nodes from the load balancer and putting the new ones in although we do have one 'special' machine which runs some background jobs.</p>


<p>We needed to make sure there weren't any jobs on its queue that hadn't been processed and then make sure that we tagged one of the new machines so that they could take over that role.</p>


<p>One thing that made it particularly easy for us to do this is that spin up of new VMs is extremely quick and completely automated including the installation and start up of applications.</p>


<p>The only manual step we have is to put the new nodes into the load balancer which I think works ok as a manual step because it gives us a chance to quickly scan the box and check everything spun up correctly.</p>


<p>We install all packages/configuration on nodes using <a href="http://docs.puppetlabs.com/man/apply.html">puppet headless</a> which makes spin up easier than if you use server/client mode where you have to coordinate node registration with the master on spin up.</p>


<p>I do like this philosophy to machines and although I'm sure it doesn't apply to all situations we're almost at the point where if something breaks on a node we might as well spin up a new one while we're investigating and see which finishes first!</p>

