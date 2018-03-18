+++
draft = false
date="2013-01-31 22:36:34"
title="Levels of automation"
tag=['software-development']
category=['Software Development']
+++

<p>Over the last 18 months or so I've worked on a variety of different projects in different organisations and seen some patterns around the way that automation was done which I thought would be interesting to document.</p>


<p>The approaches tend to fall into roughly three categories:</p>


<h4>Predominantly Manual</h4>

<p>This tends to be less frequent these days as most developers have at some stage flicked through <a href="http://pragprog.com/the-pragmatic-programmer">The Pragmatic Programmer</a> and been persuaded that automating away boring and repetitive tasks is probably a good idea.</p>


<p>It is still possible to drift into this mode when time pressured and addressing a problem for the first time.</p>
 

<p>The general approach I've seen is to first address the crisis with a manual solution and then automate it so they don't have to handle it manually the next time.</p>


<p>There can be a tendency to think that someone is a one off and that the effort it would take to automate it isn't worthwhile. In my experience <strong>if something goes wrong once it's probably going to happen again</strong> at some stage when you least want it to!</p>


<h4>Partial Automation</h4>

<p>This is the stage where you have a few automation scripts for common tasks but there's still some human involvement.</p>
 

<p>It might be that a developer needs to remember which machine to run the script against or which arguments to pass to the script but we're not quite at the 'click a button' stage.</p>


<p>Interestingly when we have partial automation it can still feel as if we're solving problems manually because there's still a degree of human interaction involved.</p>


<p>An example of this might be that we've fully automated the deployment of a service but manually take a server out of the load balancer, deploy to it, check that it passes a smoke test and then put it back into the load balancer.</p>


<p>The main task is automated but we still need to babysit the deployment rather than being able to fire it off and then leave it running in the background while we focus on something else.</p>


<h4>Full Automation</h4>

<p>At the fully automated stage we've abstracted away the complexity around the tasks we're automating and may now be at the stage where it's <strong>possible for a non developer to use the tools we've written</strong>.</p>


<p><a href="http://junctionbox.ca/nathan-fisher.html">We</a> fully automated the earlier service example by making use of <a href="http://docs.fabfile.org/en/1.4.3/index.html">Fabric</a> and <a href="http://boto.cloudhackers.com/en/latest/index.html">Boto</a> to get a collection of the appropriate AWS instances and then automated the removing/adding of them from the load balancer.</p>


<p>We also wrote a simple smoke test which used curl to check that the main route returned a 200 response code and aborted the deployment if that wasn't the case.</p>


<p>Another example of full automation is creating a dashboard to glue all the different parts together.</p>


<p>For example we recently spent a couple of hours creating an interface on top of a bunch of <a href="https://github.com/defunkt/resque">Resque</a> queues. We had previously got in a situation where we knew there were jobs stuck somewhere but didn't know which node they were on because we have queues spread across 12 machines. This makes it easier.</p>


<p>I have a tendency to want to automate absolutely everything and it can be tricky to tell when you're overdoing it although it's equally hard to know when you're undergoing it!</p>


<p>It's nearly always initially faster manually if you know what you're doing. but in the long run you may just be spending time doing something that a computer can help with.</p>


<p>One suggestion was to keep a tally chart of how often you end up doing something manually and then if it reaches a certain threshold put some automation in place.</p>

