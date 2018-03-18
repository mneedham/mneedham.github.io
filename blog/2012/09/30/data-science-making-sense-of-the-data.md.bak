+++
draft = false
date="2012-09-30 14:58:11"
title="Data Science: Making sense of the data"
tag=['data-science-2']
category=['Data Science']
+++

Over the past month or so <a href="https://twitter.com/a5hok">Ashok</a> and I have been helping one of our clients explore and visualise some of their data and one of the first things we needed to do was make sense of the data that was available. 

<h3>Start small</h3>

Ashok suggested that we <strong>work with a subset of our eventual data set</strong> so that we could get a feel for the data and quickly see whether what we were planning to do made sense.

Although our data set isn't at 'big data' levels - we're working with hundreds of thousands/millions of data points rather than the terabytes of data I often read about - I think this worked out well for us.

The data we're working with was initially stored in a SQL Server database so the quickest way to get moving was to export it as CSV files and then work with those.

One problem we had with that approach was that we hadn't realised that some product names could have commas in them and since we were using a comma as our field separator this led to products being imported with some quite strange properties!

Since we only had a few thousand records we were able to see that quickly even when running queries which returned all records.

We've been <a href="http://www.markhneedham.com/blog/2012/05/05/neo4j-what-question-do-you-want-to-answer/">asking questions of the data</a> and with the small data set we were able to very quickly get an answer to these questions for a few records and decide whether it would be interesting to find the answer for the whole data set. 

<h3>Visual verification of the data</h3>

Another useful, and in hindsight obvious, technique is to spend a little bit of time <strong>skimming over the data and look for any patterns which stand out when visualising scanning the file</strong>.

For example, one import that we did had several columns with NULL values in and we initially tried to parse the file and load it into neo4j.

After going back and skimming the file we realised that we hadn't understood how one of the domain concepts worked and those NULL values did actually make sense and we'd need to change our import script.

On another occasion skimming the data made it clear that we'd made a mistake with the way we'd exported the data and we had to go back and try again.

I'm sure there are other useful techniques we can use when first playing around with a new data set so feel free to point those out in the comments!
