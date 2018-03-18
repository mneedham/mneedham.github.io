+++
draft = false
date="2012-10-02 23:42:58"
title="Strata Conf London: Day 1 Wrap Up"
tag=['data-science-2']
category=['Data Science']
+++

For the past couple of days I attended the <a href="http://strataconf.com/strataeu">first Strata Conf to be held in London</a> - a conference which seems to <strong>bring together people from the data science and big data worlds</strong> to talk about the stuff they're doing.

Since I've been playing around with a couple of different things in this area over the last 4/5 months I thought it'd be interesting to come along and see what people much more experienced in this area had to say!

<ul>
<li>My favourite talk of the morning was by <a href="http://jakeporway.com/">Jake Porway</a> talking about his company <a href="http://datakind.org/">DataKind</a> - "an organisation that matches data from non-profit and government organisations with data scientists". 

In particular he focused on <strong>data dive</strong> - weekend events DataKind run where they bring together NGOs who have data they want to explore and data scientists/data hackers/statisticians who can help them find some insight in the data.

There was <a href="http://datakind.org/events/londondatadive/">an event in London last weekend</a> and there's <a href="http://www.shareable.net/blog/datakinds-vision-of-a-data-driven-social-change-movement">an extensive write up on one that was held in Chicago</a> earlier in the year.

Jake also had some good tips for working with data which he shared:
<ul>
<li>Start with a question not with the data</li>  
<li>Team up with someone who knows the story of the data</li>
<li>Visualisation is a process not an end - need tools that allow you to explore the data</li>
<li>You don't need big data to have big insights</li>
</ul>

Most of those tie up with what <a href="https://twitter.com/a5hok">Ashok</a> and I have been learning in the stuff we've been working on but Jake put it much better than I could!
</li>
<li>
<a href="https://twitter.com/jenit">Jeni Tennison</a> gave an interesting talk about the <a href="http://www.theodi.org/about">Open Data Institute</a> - an organisation that I hadn't heard about until the talk. Their goal is to help people find value from the Open Government Data that's now being made available.

There's an <a href="http://www.theodi.org/events/open-data-hack-days">Open Data Hack Day</a> in London on October 25th/26th being run by these guys which sounds like it could be pretty cool.

Jeni had another talk on the second day where I believe she went into more detail about how they are going about making government data publicly available, including the data of <a href="http://data.gov.uk/blog/legislationgovuk-api">legislation.gov.uk</a>.
</li>
<li><a href="https://twitter.com/smfrogers">Simon Rogers</a> of the Guardian and Kathryn Hurley of Google gave a talk about the <a href="http://www.guardian.co.uk/data">Guardian Data blog</a> where Kathyrn had recently spent a week working.

Simon started out by talking about the importance of knowing what stories matter to you and your audience before Kathryn rattled through a bunch of useful tools for doing this type of work.

Some of the ones I hadn't heard of were <a href="http://code.google.com/p/google-refine/">Google Refine</a> and <a href="http://vis.stanford.edu/wrangler/">Data Wrangler</a> for cleaning up data, <a href="http://www.google.com/publicdata/directory">Google Data Explorer</a> for finding interesting data sets to work with and finally <a href="http://cartodb.com/">CartoDB</a>, <a href="http://datawrapper.de/">DataWrapper</a> and <a href="http://www.tableausoftware.com/">Tableau</a> for creating data visualisations.</li>
<li>In the afternoon I saw a very cool presentation demonstrating <a href="http://www.emoto2012.org/#home//2012-07-27/">Emoto 2012</a> - a bunch of visualisations done using London 2012 Olympics data.

It particularly focused around sentiment analysis - working out the positive/negative sentiment of tweets - which the guys used <a href="http://www.lexalytics.com/technical-info/salience-engine-for-text-analysis">Lexalytics Salience Engine</a> to do.

One of the more amusing examples showed the emotion of tweets about Ryan Lochte suddenly going very negative when he admitted to <a href="http://www.usmagazine.com/celebrity-news/news/ryan-lochte-admits-to-peeing-in-pool-at-olympics-201258">peeing in the pool</a>.
</li>
<li><a href="https://twitter.com/noelwelsh">Noel Welsh</a> gave a talk titled 'Making Big Data Small' in which he ran through different streaming/online algorithms which we can use to work out things like the most frequent items or to learn classifiers/recommendation systems.

It moved pretty quickly so I didn't follow everything but he did talk about Hash functions, referencing the <a href="https://sites.google.com/site/murmurhash/">Murmur Hash 3 algorithm</a> and also talked about the <a href="https://github.com/clearspring/stream-lib">stream-lib</a> library which has some of the other algorithms mentioned.

<a href="http://alex.smola.org/">Alex Smola's blog</a> was suggested as a good resource for learning more about this topic as well.

<li><a href="https://twitter.com/edmundjackson">Edmund Jackson</a> then gave an interesting talk about using <strong>clojure to do everything you'd want to do in the data science arena</strong> from quickly hacking something to building a production ready piece of machine learning code.

He spent a bit of time at the start of the talk explaining the <strong>mathematical and platform problems</strong> that we face when working in this area and suggested that clojure sits nicely on the intersection. 

If we need to do anything statistics related we can use <a href="http://incanter.org/">incanter</a>, <a href="http://www.cs.waikato.ac.nz/ml/weka/">weka</a> and <a href="http://mahout.apache.org/">Mahout</a> give us machine learning algorithms, we can use <a href="http://jblas.org/">JBLAS</a> to do linear algebra and <a href="https://github.com/nathanmarz/cascalog/wiki">cascalog</a> is available to run queries on top of Hadoop.

On top of that if we want to try some code out on a bit of data we have an easily accessible REPL and if we later need to make our code run in parallel it should be reasonably easy to do.</li>
<li>Jason McFall gave a talk about <a href="http://strataconf.com/strataeu/public/schedule/detail/25895">establishing cause and effect from data</a> which was a good refresher in statistics for me and covered similar ground to some of the <a href="https://www.coursera.org/course/stats1">Statistics One</a> course on coursera.

In particular he talked about the <strong>danger of going on a fishing expedition</strong> where we decide what it is we want to conclude from our data and then go in search of things to support that conclusion. 

We also need to make sure we connect all the data sets - sometimes we can make wrong conclusions about something but when we have all the data that conclusion no longer makes sense.

<a href="http://www.greenteapress.com/thinkstats/">Think Stats</a> was suggested as a good book for learning more in this area.
<li>The last talk I saw was by <a href="http://www.maxgadney.com/">Max Gadney</a> talking about the work he's done for the Government Digital Service (GDS) building a dashboard for departmental data & for uefa providing insight to users about what's happening in a match.

I'd seen some of the GDS stuff before but <a href="http://aftertheflood.co/government-digital-service-dashboard-tool/">Max has written it up pretty extensively on his blog as well</a> so it was the uefa stuff that intrigued me more!

In particular he developed <a href="http://aftertheflood.co/uefa-com-pitch-view-application/">an 'attacking algorithm'</a> which filtered through the masses of data they had and was able to determine which team had the attacking momentum - it was especially interesting to see how much Real Madrid dominated against Manchester City when they played each other a couple of weeks ago.</li>
</ul>
