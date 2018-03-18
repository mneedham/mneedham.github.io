+++
draft = false
date="2012-12-24 09:09:44"
title="The Tracer Bullet Approach: An example"
tag=['devops-2']
category=['DevOps']
+++

<p>A few weeks ago my former colleague <a href="https://twitter.com/kief">Kief Morris</a> wrote a blog post describing <a href="http://kief.com/tracer-bullet.html">the tracer bullet approach</a> he's used to setup a continuous delivery pipeline on his current project.</p>


<blockquote>
The idea is to get the simplest implementation of a pipeline in place, prioritizing a fully working skeleton that stretches across the full path to production over a fully featured, final-design functionality for each stage of the pipeline.
</blockquote>

<p>Kief goes on to explain in detail how we can go about executing this and it reminded of a project I worked on almost 3 years ago where we took a similar approach.</p>


<p>We were building an internal application for an insurance company and didn't have any idea how difficult it was going to be to put something into production so we decided to find out on the first day of the project.</p>


<p>We started small - our initial goal was to work out what the process would be to get a 'Hello world' text file onto production hardware.</p>


<p>Although we were only putting a text file into production we wanted to try and make the pipeline as similar as possible to how it would actually be so we set up a script to package the text file into a ZIP file. We then wired up a continuous integration server to generate this artifact on each run of the build.</p>


<p>What we learnt from this initial process was how far we'd be able to automate things. We were working closely with one of the guys in the operations team and he showed us where we should deploy the artifact so that he could pick it up and put it into production.</p>


<p>Our next step after this was to do the same thing but this time with a web application just serving a 'Hello world' response from one of the end points.</p>


<p>This was relatively painless but we learnt some other intricacies of the process when we wanted to deploy a script that would make changes to a database.</p>


<p>Since these changes had to be verified by a different person they preferred it if we put the SQL scripts in a different artifact which they could pick up.</p>


<p>We found all these things out within the first couple of weeks which made our life much easier when we put the application live a couple of months down the line.</p>


<p>Although there were a few manual steps in the process I've described <strong>we still found the idea of driving out the path to production early a useful exercise</strong>.</p>


<p>Read <a href="http://kief.com/tracer-bullet.html">Kief's post</a> for ideas about how to handle some of the problems you'll come across when it's all a bit more automated!</p>

