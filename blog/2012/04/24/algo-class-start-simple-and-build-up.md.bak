+++
draft = false
date="2012-04-24 07:17:24"
title="Algo Class: Start simple and build up"
tag=['algo-class']
category=['Software Development', 'Algorithms']
+++

Over the last six weeks I've been working through Stanford's <a href="https://www.coursera.org/course/algo">Design and Analysis of Algorithms I</a> class and each week there's been a programming assignment on a specific algorithm for which a huge data set is provided.

For the first couple of assignments I tried writing the code for the algorithm and then running it directly against the provided data set. 

As you might imagine it never worked first time and this approach led to me becoming very frustrated because there's no way of telling what went wrong.

By the third week I'd adapted and instead tested my code against a much smaller data set to check that the design of the algorithm was roughly correct.

I thought that I would be able to jump straight from the small data set to the huge one but realised that this sometimes didn't work for the following reasons:  

<ol>
<li>An inefficient algorithm will work fine on a small data set but grind to a halt on a larger data set. e.g. my implementation of the <a href="http://en.wikipedia.org/wiki/Strongly_connected_component">strongly connected components (SCC)</a> graph algorithm did a scan of a 5 million element list millions of times.</li>
<li>An incorrect algorithm may still work on a small data set. e.g. my implementation of SCC didn't consider that some vertices wouldn't have forward edges and excluded them.</li>
</ol>

My colleague Seema showed me a better approach where we still use a small data set but think through all the intricacies of the algorithm and make sure our data set covers all of them. 

For the SCC algorithm this meant creating a graph with 15 vertices where some vertices weren't strongly connected while others were connected to many others. 

In my initial data set all of the vertices were strongly connected which meant I had missed some edge cases in the design of the algorithm.

Taking this approach was very effective for ensuring the correctness of the algorithm but it could still be inefficient.

I used <a href="http://visualvm.java.net/">Visual VM</a> to identify where the performance problems were.

In one case I ended up running out of memory because I had 3 different representations of the graph and was inadvertently using all of them.

I made the stupid mistake of not writing any automated tests for the smaller data sets. They would have been very helpful for ensuring I didn't break the algorithm when performance tuning it.

I should really have learnt that lesson by now given that I've been writing code in a test driven style for nearly six years but apparently I'd turned off that part of my brain.

Looking forward to Design and Analysis of Algorithms II!
