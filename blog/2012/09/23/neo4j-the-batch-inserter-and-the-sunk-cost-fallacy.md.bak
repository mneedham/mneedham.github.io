+++
draft = false
date="2012-09-23 10:29:10"
title="neo4j: The Batch Inserter and the sunk cost fallacy"
tag=['neo4j']
category=['neo4j']
+++

About a year and a half ago <a href="http://www.markhneedham.com/blog/2011/04/17/the-sunk-cost-fallacy/">I wrote about the sunk cost fallacy</a> which is defined like so:

<blockquote>
<strong>The Misconception</strong>: You make rational decisions based on the future value of objects, investments and experiences.

<strong>The Truth</strong>: Your decisions are tainted by the emotional investments you accumulate, and the more you invest in something the harder it becomes to abandon it.
</blockquote>

Over the past few weeks <a href="https://twitter.com/A5HOK">Ashok</a> and I have been doing some exploration of one of our client's data by modelling it in a neo4j graph and seeing what interesting things the traversals reveal.

We needed to import around 800,000 nodes with ~ 2 million relationships and because I find that the feedback loop in Ruby is much quicker than Java I suggested that we write the data loading code using the <a href="https://github.com/andreasronge/neo4j">neo4j.rb</a> gem. 

Initially we just loaded a small subset of the data so that we could get a rough feel for it and check that we were creating relationships between nodes that actually made sense. 

It took a couple of minutes to load everything but that was quick enough.

Eventually, however, we wanted to load the full data set and realised that this approach wasn't really going to scale very well. 

The first version created every node/relationship within its own transaction and took around an hour to load everything. 

To speed that up we batched up the nodes and only committed a transaction every 10,000 nodes which took the time down to around 20 minutes which was not bad but not amazing.

At one stage Ashok suggested we should try out the <a href="http://docs.neo4j.org/chunked/stable/batchinsert.html">batch inserter API</a> but having spent quite a few hours getting the Ruby version into shape <strong>I really didn't want to let it go</strong> - the sunk cost fallacy in full flow!

A couple of days later we got some new data to load on top of the initial graph and Ashok suggested we use the batch inserter just for that bit of data. 

Since that didn't involve deleting any of the code we'd already written I was more keen to try that out. 

This time we were adding around 200 nodes but another 1 million relationships to the existing nodes and the end to end time for this bit of code to run was 24 seconds.

Having finally been convinced that the batcher inserter was way better than anything else I spent a couple of hours earlier this week moving all our Ruby code over and it now takes just under 2 minutes to load the whole graph.

To learn how to write code for the batcher inserter we followed the examples from <a href="https://github.com/neo4j/community/blob/1.7.2/kernel/src/test/java/examples/BatchInsertExampleTest.java">BatchInsertExampleTest</a> which covered everything that we wanted to do.

Hopefully the next time I come across such a situation I'll be better able to judge when I'm holding onto something even when I should just let go!
