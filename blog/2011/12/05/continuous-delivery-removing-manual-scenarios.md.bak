+++
draft = false
date="2011-12-05 23:13:34"
title="Continuous Delivery: Removing manual scenarios"
tag=['continuous-delivery']
category=['Software Development']
+++

On the project that I'm currently working on we're trying to move to the stage where we'd be able to deploy multiple times a week while still having a reasonable degree of confidence that the application still works.

One of the (perhaps obvious) things that we've had to do as a result of wanting to do this is <strong>reduce the number of manual scenarios</strong> that our QAs need to run through.

At the moment it takes a few hours of manual testing time on top of all our automated scenarios before we can put the application in production which is fine if you release infrequently but doesn't really scale.

Following the ideas of <a href="http://www.markhneedham.com/blog/2011/08/21/pain-driven-development/">pain driven development</a> we delayed automating any bits of the application if we couldn't work out how to automate them easily.

For example we have quite a few Javascript driven light boxes which pop up on various users actions and we weren't able to test using the HTML Unit Driver in <a href="http://code.google.com/p/selenium/">Web Driver</a> so we created automated tests only for the non Javascript version of those features.

We've started work on automating these scenarios recently and although we're having to invest some time in fiddling around with the Firefox Driver to do so, it will save us time on each deployment so it should be worth it.

My colleague <a href="http://www.linkedin.com/pub/harinee-muralinath/13/157/531">Harinee</a> showed me an interesting post by Anand Bagmar in which he describes <a href="http://essenceoftesting.blogspot.com/2011/08/to-test-or-not-to-test-do-you-ask.html">a cost/value matrix which can help us decide whether or not to automate something</a>.

In this case the lightbox feature was initially only used in a couple of places and we realised it would be quite difficult to test it compared to our current approach so it fitted in the 'Naaaah' section (Low value, High cost).

Over time it has been introduced in more and more places so it's become more important that we find a way to automatically test it since the application can fail in many more places if it doesn't work.

It's therefore moved into section #2 (High value, High cost) and become a candidate for automation.

Although not directly related to manual scenarios, one thing we haven't quite worked out yet is what the balance should be between getting something into production and ensuring that it isn't full of bugs.

This is also something which James Birchler addresses in <a href="http://engineering.imvu.com/2010/04/09/imvus-approach-to-integrating-quality-assurance-with-continuous-deployment/">his post about IMVU's approach to continuous deployment</a>:

<blockquote>
We’re definitely not perfect: with constrained QA resources and a persistent drive by the team to deliver value to customers quickly, we do often ship bugs into production or deliver features that are imperfect. The great thing is that we know right away what our customers want us to do about it, and we keep on iterating.
</blockquote>

At the moment the application is only being beta tested by a small number of users so we're veering towards pushing something even if it's not perfect but as we open it up to more people I imagine it'll become a bit more stringent.

At times it's quite painful working out what you need to change in your approach to make it possible to release frequently but it's cool to see the progress we're making as we get better at doing so.
