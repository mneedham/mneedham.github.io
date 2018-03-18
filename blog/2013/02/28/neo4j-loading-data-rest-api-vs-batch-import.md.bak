+++
draft = false
date="2013-02-28 23:36:13"
title="neo4j: Loading data - REST API vs Batch Import"
tag=['neo4j']
category=['neo4j']
+++

<p>A couple of weeks ago when I first started playing around with my football data set I was loading all the data into neo4j using the REST API via <a href="https://github.com/maxdemarzi/neography">neography</a> which was taking around 4 minutes to load.</p>


<p>The data set consisted of just over 250 matches which translated into 8,000 nodes & 30,000 relationships so it's very small by all means.</p>


<p><a href="https://twitter.com/a5hok">Ashok</a> and I were discussing how that could be quicker and the first thing we tried was to store inserted nodes in an in memory hash map and look them up from there rather than doing an index lookup each time.</p>


<p>These were the timings for different numbers of matches when I did that:</p>



~~~text

--------------------------------------------------------------------
| Matches | Cache-Hits | Cache-Misses | Lucene        | In memory  |
--------------------------------------------------------------------
| 25      | 501        | 325          | 26.692s       | 22.877s    |
| 50      | 1275       | 373          | 50.491s       | 38.304s    |
| 263     | 8016       | 480          | 4m 11.031s    | 2m 49.951s |
--------------------------------------------------------------------
~~~

<p>For the full data set it was about 30% faster which was a nice improvement but still left me waiting around for a bit longer than I wanted to!</p>


<p>I've <a href="http://www.markhneedham.com/blog/2012/09/23/neo4j-the-batch-inserter-and-the-sunk-cost-fallacy/">previously used the batch inserter</a> and I was planning to use that again to get a significant improvement in loading time until Ashok pointed out Michael Hunger's <a href="https://github.com/jexp/batch-import">batch-import</a> which seemed worth a try.</p>


<p>I had to add an extra step to the <a href="http://www.markhneedham.com/blog/2013/02/18/micro-services-style-data-work-flow/">pipeline</a> to put all the nodes and relationships into CSV files and then pass those files to the batch-import JAR.</p>


<p>There was a massive improvement in the load time using it. These were the timings:</p>



~~~text

-------------------------------------------------------------------
| Matches | Lucene        | In memory  | Batch Import             |
-------------------------------------------------------------------
| 25      | 26.692s       | 22.877s    | 0.378s + 0.921s = 1.299s |
| 50      | 50.491s       | 38.304s    | 0.392s + 1.025s = 1.417s |
| 263     | 4m 11.031s    | 2m 49.951s | 0.524s + 1.239s = 1.763s |
-------------------------------------------------------------------
~~~

<p><em>(the two numbers represent the time taken to generate the CSV files and then the time to import them)</em></p>


<p>From my brief skimming of the code it seems to take in the files and then route them through the batch importer API so I imagine similar results would be had by calling that directly.</p>


<p>I know this is not a very fair comparison given that you probably shouldn't be using the REST API to insert data but since I've done it a couple of times I thought it'd be interesting to measure anyway!</p>

