+++
draft = false
date="2013-02-17 20:02:31"
title="Data Science: Don't filter data prematurely"
tag=['neo4j', 'cypher']
category=['Data Science']
+++

<p>Last year I wrote a post describing how I'd <a href="http://www.markhneedham.com/blog/2012/09/30/data-science-scrapping-the-data-together/">gone about getting data for my ThoughtWorks graph</a> and one mistake about my approach in retrospect is that I filtered the data too early.</p>


<p>My workflow looked like this:</p>


<ul>
<li>Scrape internal application using web driver and save useful data to JSON files</li>
<li>Parse JSON files and load nodes/relationships into neo4j</li>
</ul>

<p>The problem with the first step is that I was trying to determine up front what data was useful and as a result I ended up running the scrapping application multiple times when I realised I didn't have all the data I wanted.</p>


<p>Since it took a couple of hours to run each time it was tremendously frustrating but it took me a while to realise how flawed my approach was.</p>


<p>For some reason I kept tweaking the scrapper just to get a little bit more data each time!</p>
 

<p>It wasn't until <a href="https://twitter.com/a5hok">Ashok</a> and I were doing some similar work and had to extract data from an existing database that I realised the filtering didn't need to be done so early in the process.</p>


<p>We weren't sure exactly what data we needed but on this occasion we got everything around the area we were working in and looked at how we could actually use it at a later stage.</p>


<p>Given that it's relatively cheap to store the data I think this approach makes sense more often than not - <strong>we can always delete the data if we realise it's not useful to us at a later stage</strong>.</p>
 

<p>It especially makes sense if it's difficult to get more data either because it's time consuming or we need someone else to give us access to it and they are time constrained.</p>


<p>If I could rework that work flow it'd now be split into three steps:</p>


<ul>
<li>Scrape internal application using web driver and save pages as HTML documents</li>
<li>Parse HTML documents and save useful data to JSON files</li>
<li>Parse JSON files and load nodes/relationships into neo4j</li>
</ul>

<p>I think my experiences tie in reasonably closely with those I heard about at <a href="http://www.markhneedham.com/blog/2012/10/02/strata-conf-london-day-1-wrap-up/">Strata Conf London</a> but of course I may well be wrong so if anyone has other points of view I'd love to hear them.</p>

