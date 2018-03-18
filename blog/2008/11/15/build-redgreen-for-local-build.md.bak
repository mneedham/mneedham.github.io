+++
draft = false
date="2008-11-15 08:26:21"
title="Build: Red/Green for local build"
tag=['build']
category=['Build']
+++

One thing I'm learning from reading <a href="http://www.amazon.co.uk/Toyota-Way-Management-Principles-Manufacturer/dp/0071392319/ref=sr_1_1?ie=UTF8&s=books&qid=1226698369&sr=8-1">The Toyota Way</a> is that visual indicators are a very important part of the Toyota Production System, and certainly my experience working in agile software development is that the same is true there.

We have certainly learnt this lesson with regards to <a href="http://martinfowler.com/articles/continuousIntegration.html">continuous integration</a> - the build is either red or green and it's a very obvious visual indicator of the code base at any moment in time.

On my last two projects we have setup build lights which project the build status even more visually without us even having to go to the reporting page.

I have never thought about applying this principle when running the build locally but my colleague <a href="http://jamescrisp.org/">James Crisp</a> has setup our build to light up the whole background of the command prompt window red or green depending on the status code we get back from running <a href="http://nant.sourceforge.net/">Nant</a>.

James has promised to post the code we used from the command prompt to do this on his blog - I've tried to work out how to achieve the same effect in the Unix shell but I haven't figured out how to do it yet. I've worked out how to set the <a href="http://linuxshellaccount.blogspot.com/2008/03/using-color-in-linux-or-unix-shell.html">background colour for the prompt</a> but not for the whole window - if anyone knows how to do it, let me know!

The idea is fairly simple though:

<ul>
<li>Run the build</li>
<li>If the exit status is 1, make the background red</li>
<li>If the exit status is 0, make the background green</li>
</ul>


