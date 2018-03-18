+++
draft = false
date="2012-09-30 13:44:18"
title="Data Science: Scrapping the data together"
tag=['data-science-2']
category=['Data Science']
+++

On Friday <a href="http://martinfowler.com/">Martin</a>, <a href="https://twitter.com/drnsmth">Darren</a> and I were discussing the ThoughtWorks graph that I was working on earlier in the year and Martin pointed out that an interesting aspect of this type of work is that <strong>the data you want to work with isn't easily available</strong>.

You therefore need to find a way to scrap the data together to make some headway and then maybe at a later stage once some progress has been made it will become easier to replace that with a cleaner solution.

In this case I became curious about exploring the relationships between people in ThoughtWorks but there aren't any APIs on our internal systems so I had to find another way to get the data that I wanted.

The obvious way to do that was to get a copy of the database used by our internal staffing system but I didn't know anybody who worked on that team and trying to get the data that way <strong>would therefore be slow and lose my initial enthusiasm</strong>.

My only alternative was to go via our staffing application and derive the data that way. 

I ended up writing some Selenium scripts to crawl the application for people, projects and clients and save that data to JSON files which I later parsed to build up the graph.

The other bit of data that I was curious about was the sponsor relationships inside the company which is kept in a Google spreadsheet.

I wasn't allowed access to that spreadsheet until I was able to show what I was going to use the data for so I first needed to put together something using the other data I'd screen scrapped.

Once I did get the spreadsheet I spent around 3 hours cleaning the data so I could integrate it with the other data I had.

This involved fixing misspelt names and updating the spreadsheets where I knew that the data was out of date - it's certainly not very glamorous work but it helped me to <a href="http://www.markhneedham.com/blog/2012/06/21/visualising-a-neo4j-graph-using-gephi/">get to a visualisation which I wrote about in an earlier post</a>.

I haven't done a lot of work in this area but I wouldn't be surprised if it's common that we have to use relatively guerilla tactics like the above to get us up and running.
