+++
draft = false
date="2012-10-03 06:46:13"
title="Strata Conf London: Day 2 Wrap Up"
tag=['data-science-2', 'strataconf', 'bigdata']
category=['Data Science']
+++

Yesterday I attended the second day of <a href="http://strataconf.com/strataeu/public/schedule/grid/public-grid/2012-10-02">Strata Conf London</a> and these are the some of the things I learned from the talks I attended:

<ul>
<li><a href="http://twitter.com/jgrahamc">John Graham Cunningham</a> opened the series of keynotes with a talk describing the problems British Rail had in 1955 when trying to calculate the distances between all train stations and comparing them to the problems we have today. 

British Rail were trying to solve a graph problem when people didn't know about graphs and <strong>Dijkstra's algorithm hadn't been invented</strong> and it was effectively invented on this project but never publicised. John's suggestion here was that we need to <strong>share the stuff that we're doing so that people don't re-invent the wheel</strong>.

He then covered the ways they simplified the problem by dumping partial results to punch cards, partitioning the data & writing really tight code - all things we do today when working with data that's too big to fit in memory. Our one advantage is that we have lots of computers that we can get to do our work - something that wasn't the case in 1955.

There is a book titled '<a href="http://www.amazon.co.uk/Computer-Called-LEO-worlds-computer/dp/1841151866/ref=sr_1_1?ie=UTF8&qid=1349167393&sr=8-1">A Computer called LEO: Lyons Tea Shops and the world's first office computer</a>' which was recommended by one of the attendees and covers some of the things from the talk.

The <a href="http://blog.jgc.org/2012/10/the-great-railway-caper-big-data-in-1955.html">talk is online</a> and worth a watch, he's pretty entertaining as well as informative!
</li>
<li>Next up was <a href="https://twitter.com/aallan">Alasdair Allan</a> who gave a talk showing some of the applications of different data sources that he's managed to hack together.

For example he showed an application which keeps track of where his credit card is being used via his bank's transaction record and it sends those details to his phone and compares it to his current GPS coordinates. 

If they differ then the card is being used by someone else, and he was actually able to <strong>detect fraudulent use of his card more quickly than his bank</strong> on one occasion!   

He also got access to the data on an RFID chip of his hotel room swipe card and was able to chart the times at which people went into/came out of the room and make inferences about why some times were more popular than others.

The final topic covered was how we leak our location too easily on social media platforms - he referenced a paper by some guys at the University of Rochester titled '<a href="http://www.cs.rochester.edu/~sadilek/publications/Sadilek-Kautz-Bigham_Finding-Your-Friends-and-Following-Them-to-Where-You-Are_WSDM-12.pdf">Following your friends and following them to where you are</a>' in which the authors showed that it's quite easy to work out your location just by looking at where your friends currently are.</li>
<li><a href="http://www.badscience.net/">Ben Goldacre</a> did the last keynote in which he <a href="http://www.ted.com/talks/ben_goldacre_what_doctors_don_t_know_about_the_drugs_they_prescribe.html">covered similar ground as in his TED talk</a> about pharmaceuticals not releasing the results of failed trials.

I didn't write down anything from the talk because it takes all your concentration to keep up with him but he's well worth watching if you get the chance!
<li>I attended a panel about how journalists use data and an interesting point was made about <strong>being sceptical about data</strong> and finding out how the data was actually collected rather than just trusting it.

Another topic discussed was whether the open data movement might be harmed if people come up with misleading data visualisations - something which is very easy to do. 

If the data is released and people cause harm by making cause/effect claims that don't actually exist then people might be less inclined to make their data open in the first place.

We were encouraged to think about where the gaps are in what's being reported. What isn't being reported but perhaps should be?</li>
<li>The coolest thing I saw at Strata was the stuff that <a href="http://www.narrativescience.com/">Narrative Science</a> are doing - they have developed some software which is able to <strong>take in a load of data and convert it into an article describing the data.</strong>

We were showing examples of this being done for football matches, company reports and even giving feedback on your performance in an exam and suggesting areas in which you need to focus your future study.

<a href="http://www.wired.com/gadgetlab/2012/04/can-an-algorithm-write-a-better-news-story-than-a-human-reporter/all/">Wired had an article a few months ago where they interviewed Kristian Hammond</a>, one of the co founders and the guy who gave this talk.

I have no idea how they're doing what they're doing but it's very very clever!</li>
<li>I'd heard about <a href="http://datasift.com/">DataSift</a> before coming to Strata - they are one of the few companies that has access to the twitter fire hose and have <a href="http://highscalability.com/blog/2011/11/29/datasift-architecture-realtime-datamining-at-120000-tweets-p.html">previously been written up on the High Scalability blog</a> - but I still wanted to see it in action!

The talk was focused around five challenges DataSift have had: 

<ul>
<li>Digging through unstructured data volumes - they take tweets and convert them into 94 different files using some <a href="http://en.wikipedia.org/wiki/Natural_language_processing">NLP</a> wizardry. They use <a href="http://www.lexalytics.com/technical-info/salience-engine">Lexalytics Salience Engine</a> to help them do this.</li>
<li>Filtering - separating the signal from the noise. <a href="http://blog.ouseful.info/2012/10/01/strataconf-dreamcatcher/">Popular hash tags end up getting massively spammed</a> so those tweets need to be excluded.</li>
<li>Analysing - real time filtering and tagging of data. They use the <a href="http://www.cloudera.com/company/press-center/releases/cloudera-and-datasift-partner-to-deliver-big-data-insights-from-social-data/">cloudera Hadoop distribution</a>.</li>
<li>Variety - integrating data from different sources. e.g. showing the <a href="http://mashable.com/2012/05/19/facebook-ipo-twitter-prediction/">Facebook stock price vs the twitter sentiment analysis</a> of the company.</li>
<li>Make it work 24/7</li>
</ul>

There was a very meta demo where the presenter showed DataSift's analysis of the <cite>strataconf</cite> hash tag which suggested that 60% of tweets showed no emotion but 15% were extremely enthusiastic -'that must be the Americans'.</li>
<li>I then went to watch another talk by Alasdair Allan - this time pairing with a colleague of his, <a href="http://twitter.com/zenamwood">Zena Wood</a>, talking about the work they're doing at the University of Exeter.

It mostly focused on tracking movement around the campus based on which wifi mast your mobile phone was currently closest to and allowed them to make some fascinating observations.

e.g. Alasdair often took a different route out of the campus which was apparently because that route was more scenic. However, he would only take it if it was sunny!

They discussed  some of the questions they want to answer with the work they're doing such as:

<ul>
<li>Do people go to lectures if they're on the other side of the campus?</li>
<li>How does the campus develop? Are new buildings helping build the social network of students?</li>
<li>Is there a way to stop freshers' flu from spreading?</li>
</li>
</ul>
</li>
<li>The last talk I went to was by <a href="http://twitter.com/thomaslevine">Thomas Levine</a> of <a href="https://scraperwiki.com/">ScraperWiki</a> talking about different tools he uses to clean up the data he's working with.

There were references to 'head', 'tail', 'tr' and a few other Unix tools and a Python library called <a href="http://pypi.python.org/pypi/Unidecode">unidecode</a> which is able to convert Unicode data into ASCII.

He then moved onto tools for converting PDFs into something more digestible and mentioned <a href="http://pdftohtml.sourceforge.net/">pdftohtml</a>, <a href="http://en.wikipedia.org/wiki/Pdftotext">pdftotext</a> and <a href="http://inkscape.org/">inkscape</a>.

He suggested saving any data you're working with into a database rather than working with raw files - <a href="http://couchdb.apache.org/">CouchDB</a> was his preference and he's also written a document like interface over SQLite called <a href="http://linux.softpedia.com/get/Database/Administrative-frontents/DumpTruck-84416.shtml">DumpTruck</a>.

In the discussion afterwards someone mentioned <a href="http://tika.apache.org/">Apache Tika</a> which is a tool for extracting meta data using parser libraries. It looks neat as well.</li>
<li>A general trend at this conference was that some of the talks ended up feeling quite salesy and <strong>some presenters would only describe what they were doing up to a certain point</strong> at which the rest effectively became 'magic'. 

I found this quite strange because in software conferences that I've attended people are happy to explain everything to you but I think here the 'magic' is actually how people are making money so it doesn't make sense to expose it.
</ul>

Overall it was an enjoyable couple of days and it was especially fascinating to see the different ways that people have come up with for exploring and visualising data and creating useful applications on top of that.
