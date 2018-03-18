+++
draft = false
date="2008-09-20 17:32:01"
title="Where are we now? Where do we want to be?"
tag=['nlp', 'build', 'continous-improvement', 'improvement', 'deployment']
category=['Build', 'Software Development']
+++

Listening to <a href="http://dannorth.net/">Dan North</a> speaking last week I was reminded of one of my favourite <a href="http://en.wikipedia.org/wiki/Neuro-linguistic_programming">NLP</a><a href="#nlp">[*]</a> techniques for making improvements on projects.

The technique is the <a href="http://en.wikipedia.org/wiki/T.O.T.E.">TOTE</a> (Test, Operate, Test, Exit) and it is a technique designed to help us get from where we are now to where we want to be via short feedback loops.

On my previous project we had a situation where we needed to build and deploy our application in order to show it to the client in a show case. 

The first time we did this we did most of the process manually - it took three hours and even then still didn't work properly. It was clear that we needed to do something about this. We needed the process to be automated.

Before we did this I mentally worked out what the difference was between where we were now and what the process would look like when we were at our desired state.

A full description of the technique can be found in the <a href="http://www.amazon.co.uk/NLP-Practical-Achieving-Results-Workbook/dp/0007100035/ref=sr_1_1?ie=UTF8&s=books&qid=1221926782&sr=8-1">NLP Workbook</a> but in summary, these are the steps for using the TOTE technique.

<ol>
<li>What is our present state?</li>
<li>What is our desired state?</li>
<li>What specific steps and stages do we need to go through to get there?</li>
</ol>

We then execute an action and then re-compare the current state to the desired state until they are the same. Then we exit.

In our situation:

<ol>
<li>To deploy our application we need to manually build it then copy the files to the show case machine.</li>
<li>We want this process to happen automatically each time a change is made to the application</li></ol>

For step 3 to make sense more context is needed. 

For our application to be ready to use we needed to build it and deploy it to the user's desktop and build and deploy several other services to an application repository so that our application could stream them onto the desktop.

The small steps for achieving step 3 were:
<ul>
<li>Write a build for building the application and making the artifacts available</li>
<li>Write a script to deploy the application to the user's desktop</li>
<li>Edit the build for building the services to make artifacts available</li>
<li>Write a script to deploy these services to the repository</li>
</ul>

This evolved slightly so that we could get Team City to simulate the process for our functional testing and then run a script to deploy it on the show case machine but the idea is the same.

There's nothing mind blowing about this approach. It's just a way of helping us to clarify what exactly it is we want to do and providing an easy way of getting there as quickly as possible.
--
<a name="nlp"></a>
* Sometimes when I mention NLP people get a bit defensive as it has been fed to them previously as a tool kit for solving all problems. 

We need to remember that NLP is a set of communication techniques gathered from observing effective communicators and then recorded so that others could learn from this.

When used properly ideas from NLP can help us to clarify what we want to do and improve our ability to communicate with each other.
