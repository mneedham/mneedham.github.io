+++
draft = false
date="2013-04-27 14:22:10"
title="Treat servers as cattle: Spin them up, tear them down"
tag=['devops-2']
category=['DevOps']
+++

<p>A few agos I wrote a post about <a href="http://www.markhneedham.com/blog/2013/04/07/treating-servers-as-cattle-not-as-pets/">treating servers as cattle, not as pets</a> in which I described an approach to managing virtual machines at uSwitch whereby we frequently spin up new ones and delete the existing ones.</p>


<p>I've worked on teams previously where we've also talked about this mentality but ended up not doing it because it was difficult, usually for one of two reasons:</p>


<ul>
<li><strong>Slow spin up</strong> - this might be due to the cloud providers infrastructure, doing too much on spin up or I'm sure a variety of other reasons.</li>
<li><strong>Manual steps involved in spin up</strong> - the process isn't 100% automated so we have to do some manual tweaks. Once the machine is finally working we don't want to have to go through that again.</li>
</ul>

<p>Martin Fowler <a href="http://martinfowler.com/bliki/FrequencyReducesDifficulty.html">wrote a post a couple of years ago</a> where he said the following:</p>


<blockquote>
One of my favorite soundbites is: <strong>if it hurts, do it more often</strong>. It has the happy property of seeming nonsensical on the surface, but yielding some valuable meaning when you dig deeper
</blockquote>

<p>I think it applies in this context too and I have noticed that the more frequently we tear down and spin up new nodes the easier it becomes to do so.</p>


<p>Part of this is because there's been less time for <a href="http://www.markhneedham.com/blog/2013/04/27/puppet-package-versions-to-pin-or-not-to-pin/">changes to have happened in package repositories</a> but we are also <strong>more inclined to optimise things that we have to do frequently</strong> so the whole process is faster as well.</p>


<p>For example in one of our sets of machines we need to give one machine a specific tag so that when the application is deployed it sets up a bunch of cron jobs to run each evening.</p>


<p>Initially this was done manually and we were quite reluctant to ever tear down that machine but we've now got it all automated and it's not a big deal anymore - it can be cattle just like the rest of them!</p>


<p>One neat rule of thumb <a href="https://twitter.com/philandstuff">Phil</a> taught me is that if we make major changes to our infrastructure we should spin up some new machines to check that it still actually works.</p>
 

<p>If we don't do this then when we actually need to spin up a new node because of a traffic spike or machine corruption problem it's not going to work and we're going to have to fix things in a much more stressful context.</p>


<p>For example we recently moved some repositories around in github and although it's a fairly simple change spinning up new nodes helped us see all the places where we'd failed to make the appropriate change.</p>


<p>While I appreciate taking this approach is more time consuming in the short term I'd argue that if we automate as much of the pain as possible in the long run it will probably be beneficial.</p>

