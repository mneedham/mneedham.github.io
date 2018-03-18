+++
draft = false
date="2009-08-29 09:54:39"
title="Book Club: Unshackle your domain (Greg Young)"
tag=['domain-driven-design', 'book-club']
category=['Book Club']
+++

In this week's book club we continued with the idea of discussing videos, this week's selection being Greg Young's '<a href="http://www.infoq.com/presentations/greg-young-unshackle-qcon08">Unshackle your Domain</a>' presentation from QCon San Francisco in November 2008. He also did a version of this talk in the <a href="http://vimeo.com/3171910">February European Alt.NET meeting</a>.

In this presentation Greg talks about <a href="http://codebetter.com/blogs/gregyoung/archive/2009/08/13/command-query-separation.aspx">Command Query Separation</a> at the architecture level and explicit state transitions amongst other things.

Jonathan Oliver has created a <a href="http://jonathan-oliver.blogspot.com/2009/03/dddd-and-cqs-getting-started.html">useful resource page</a> of the material that's been written about some of these ideas as well.

These are some of my thoughts from our discussion:

<ul>
<li>I think the idea of <strong>eventual consistency</strong> is quite interesting and I can see how taking this approach instead of trying to create the impression that everything the user does is in real time we can make life much easier for ourselves.

I'm not sure how this type of idea works when users have the expectation that when they change information on a page that it is updated straight away though. 

For example on a form I might decide to change my address and I would expect that if I reload the page with my address on that it would now display my new address instead of the old one. If that address was eventually consistent after 5 minutes for example the user might become quite confused and send in another update to try and change their address again. 

<a href="http://lizdouglass.wordpress.com/">Liz</a> pointed out that with bank transactions it is often explicitly described to users that money transfers are 'pending' so perhaps the expectation that things aren't done in real time has already been set in some domains.

Werner Vogels has a nice article about <a href="http://www.allthingsdistributed.com/2007/12/eventually_consistent.html">eventual consistency in distributed systems</a> in which he references <a href="http://lpd.epfl.ch/sgilbert/pubs/BrewersConjecture-SigAct.pdf">a paper by Seth Gilbert and Nancy Lynch</a> which talks about the idea that "of three properties of shared-data systems; data consistency, system availability and tolerance to network partition one can only achieve two at any given time."</li>
<li><a href="http://intwoplacesatonce.com/">Dave</a> pointed out that the idea of '<a href="http://en.wikipedia.org/wiki/Post/Redirect/Get">POST redirect GET</a>' often used when processing web form submissions seems to adhere quite nicely to the idea of <strong>Command Query Separation</strong> as described in the video. 

I find it quite interesting that CQS at the method level in our code is usually quite closely adhered too but so often we'll just <a href="http://www.markhneedham.com/blog/2009/08/17/law-of-demeter-some-thoughts/">bolt on getters onto domain objects</a> so that we can access some data to display on the view. 

The idea of not doing this and having a write only domain seems very interesting and seemed to make sense in the system that Greg described.

It would be interesting to know whether one would follow such an extreme approach at the architecture level if there weren't such high performance requirements or the need to have all the operations performed on the system available for an audit.</li>
<li>Greg's idea of <strong>state transitions</strong> sounds quite similar although perhaps not exactly the same as Eric Evans' 'domain events' which he discussed in <a href="http://www.markhneedham.com/blog/2009/08/24/book-club-what-ive-learned-about-ddd-since-the-book-eric-evans/">last week's book club</a>.

It would be interesting to see what the code to process form submissions by the user would look like with this approach.

As Silvio pointed out, the complexity of this code would probably be much higher than in  a more typical approach where we might just build our domain objects straight from the data the user entered. 

Using Greg's approach we would need to work out which state transitions had actually happened based on the user input which would presumably involve keeping a copy of the previous state of the domain objects in order to work out what had changed.

I like the idea of making concepts more explicit though and the idea of keeping all state transitions is something that is built into databases by way of their log by default so it's not a completely new concept.

Pat Helland has a cool post titled '<a href="http://blogs.msdn.com/pathelland/archive/2007/06/14/accountants-don-t-use-erasers.aspx">Accountants don't use erasers</a>' where he describes it in more detail. </li>
</ul>
