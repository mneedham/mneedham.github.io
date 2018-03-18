+++
draft = false
date="2013-04-28 22:32:38"
title="A/B Testing: Reporting"
tag=['absplittesting']
category=['Software Development']
+++

<p>A few months ago I wrote about <a href="http://www.markhneedham.com/blog/2013/01/27/ab-testing-thoughts-so-far/">my initial experiences with A/B testing</a> and since then we've been working on another one and learnt some things around reporting on these types of tests that I thought was interesting.</p>


<h4>Reporting as a first class concern</h4>

<p>One thing we changed from our previous test after a suggestion by <a href="https://twitter.com/michael_jones">Mike</a> was to start treating the reporting of data related to the test as a first class citizen.</p>


<p>To do this we created an end point which the main application could send POST requests to in order to record page views and various other information about users.</p>


<p>On our previous test we'd derived the various conversion rates from our main transactional data store but it was really slow and painful because the way we structure data in there is optimised for a completely different use case.</p>


<p>Having just the data we want to report on in a separate data store has massively reduced the time spent generating reports.</p>


<p>However, one thing that we learnt about this approach is that you need to spend some time thinking about what data is going to be needed up front.

<p>If you don't then it will have to be added later on and the reporting on that metric won't cover the whole test duration.</p>


<h4>Drilling down to get insight</h4>

<p>In the first test we ran we only really looked at conversion at quite a high level which is good for getting an overview but doesn't give much insight into what's going on.</p>


<p>For this test we started off with higher level metrics but a few days in became curious about what was going on between two of the pages and so created a report that segmented users based on an action they'd taken on the first page.</p>


<p>This allowed us to rule out a theory about a change in conversion which we had initially thought was down to a change we'd made but actually proved to be because of a change in an external factor.</p>


<p>The frustrating part of drilling down into the data is that you don't really know what is it you're going to want to zoom in on so you have to write code for the specific scenario each time!</p>


<h4>Detecting bugs</h4>

<p>We generate browser specific metrics on each test that we run and while the conversion rate is generally similar between them there have been some times when there's a big drop in one browser.</p>


<p>More often than not when we've drilled into this we've found that there was actually a Javascript bug that we hadn't detected and we can then go back and sort that out.</p>


<p>An alternative approach would be to have an automated Javascript/Web Driver test suite which ran against each browser. We've effectively traded off the maintenance cost of that for what is usually a small period of inconvenience for some users.</p>

