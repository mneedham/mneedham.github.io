+++
draft = false
date="2013-09-19 06:55:19"
title="Data Science: Don't build a crawler (if you can avoid it!)"
tag=['data-science-2']
category=['Data Science']
+++

<p>On Tuesday I spoke at the <a href="http://www.meetup.com/Data-Science-London/events/139205302/">Data Science London meetup</a> about <a href="http://bit.ly/rankings-dsldn">football data</a> and I started out by covering some lessons I've learnt about building data sets for personal use when open data isn't available.</p>


<p>When that's the case you often end up scraping HTML pages to extract the data that you're interested in and then storing that in files or in a database if you want to be more fancy.</p>


<p>Ideally we want to spend our time playing with the data rather than gathering it so we we want to keep this stage to a minimum which we can do by following these rules.</p>


<h3>Don't build a crawler</h3>

<p>One of the most tempting things to do is build a crawler which starts on the home page and then follows some/all the links it comes across, downloading those pages as it goes.</p>


<p>This is incredibly time consuming and yet this was the approach I took when scraping an internal staffing application to <a href="http://skillsmatter.com/podcast/home/what-do-you-want-to-know">model ThoughtWorks consultants/projects in neo4j</a> about 18 months ago.</p>


<p><a href="https://twitter.com/a5hok">Ashok</a> wanted to get the same data a few months later and instead of building a crawler, spent a bit of time understanding the URI structure of the pages he wanted and then built up a list of pages to download.</p>


<p>It took him in the order of minutes to build a script that would get the data whereas I spent many hours using the crawler based approach.</p>


<p>If there is no discernible URI structure or if you want to get every single page then the crawler approach might make sense but I try to avoid it as a first port of call.</p>


<h3>Download the files</h3>

<p>The second thing I learnt is that running <a href="http://docs.seleniumhq.org/projects/webdriver/">Web Driver</a> or <a href="http://nokogiri.org/">nokogiri</a> or <a href="https://github.com/cgrand/enlive">enlive</a> against live web pages and then only storing the parts of the page we're interested in is sub optimal.</p>


<p>We pay the network cost every time we run the script and at the beginning of a data gathering exercise we won't know exactly what data we need so we're bound to have to run it multiple times until we get it right.</p>


<p>It's much quicker to download the files to disk and work on them locally.</p>


<h3>Use wget</h3>

<p>Having spent a lot of time writing different tools to download the ThoughtWorks data set <a href="http://linux.about.com/od/commands/l/blcmdl1_wget.htm">Ashok</a> asked me why I wasn't using wget instead.</p>


<p>I couldn't think of a good reason so now I favour building up a list of URIs and then letting wget take care of downloading them for us. e.g.</p>



~~~bash

$ head -n 5 uris.txt
https://www.some-made-up-place.com/page1.html
https://www.some-made-up-place.com/page2.html
https://www.some-made-up-place.com/page3.html
https://www.some-made-up-place.com/page4.html
https://www.some-made-up-place.com/page5.html

$ cat uris.txt | time xargs wget
...
Total wall clock time: 3.7s
Downloaded: 60 files, 625K in 0.7s (870 KB/s)
        3.73 real         0.03 user         0.09 sys
~~~

<p>If we need to speed things up we can always use the '-P' flag of xargs to do so:</p>



~~~bash

cat uris.txt | time xargs -n1 -P10 wget
        1.65 real         0.20 user         0.21 sys
~~~

<p>It pays to be reasonably sensible when using tools like this and of course read the terms and conditions of the site to check what they have to say about downloading copies of pages for personal use.</p>
 

<p>Given that you can get the pages using a web browser anyway it's generally fine but it makes sense not to bombard their site with requests for every single page and instead just focus on the data you're interested in.</p>

