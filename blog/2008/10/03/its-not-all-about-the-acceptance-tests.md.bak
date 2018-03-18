+++
draft = false
date="2008-10-03 01:26:13"
title="It's not all about the acceptance tests"
tag=['tdd', 'testing']
category=['Testing']
+++

A <a href="http://sarahtaraporewalla.com/thoughts/?p=31">few</a> <a href="http://fragmental.tw/2008/09/29/where-do-acceptance-tests-go-to-die/">of</a> <a href="http://www.thekua.com/atwork/2008/09/30/automated-story-based-acceptance-tests-lead-to-unmaintainable-systems/">my colleagues</a> recently posted their opinions about acceptance tests which tied in nicely with a <a href="http://gojko.net/2008/09/17/fitting-agile-acceptance-testing-into-the-development-process/">discussion about acceptance testing</a> that was had at the <a href="http://www.markhneedham.com/blog/2008/09/14/altnet-uk-conference-20/">Alt.NET conference in London</a>.

For the sake of argument I will assume that when we refer to acceptance tests we are talking about tests at the GUI level which are being automatically driven by a tool, usually <a href="http://selenium.openqa.org/">Selenium</a> but maybe something like <a href="http://www.codeplex.com/white">White</a> if it is a client side application. I'm not sure if this definition is 100% accurate but it feels to me that this is what is being referred to when we describe something as an acceptance test.

The discussion at the Alt.NET conference centered around the value of having these acceptance tests when they often take a long time to run therefore dragging out the time that it takes to build our application. These are some of the same problems that <a href="http://sarahtaraporewalla.com/thoughts/?p=31">Sarah points out</a> as well as issues around the maintenance of these tests.

Some of the responses to this pointed out that we should not rely too heavily on acceptance tests to confirm the correctness of our system especially when we can often do this using functional or integration tests which do not have to hit the UI and therefore run much more quickly.

We could still have acceptance tests but maybe they would only be necessary for critical scenarios where the system would become unusable if they did not pass - e.g. for the login screen.

I'm not sure what the solution is - I haven't actually worked on a project which had the problems that Phillip and Sarah have experienced but I've heard the horror stories from speaking to some of my colleagues.

Sarah made one particular comment which I can relate to:

<blockquote>
In fact, when I finish developing my story, the integration/persistence/unit tests already cover all acceptance criteria.
</blockquote>

One of the projects I worked on had the concept of acceptance criteria for every story but we didn't have acceptance tests so to speak. There were certainly unit tests and functional tests covering each story but that was the extent of our automated testing.

There were a couple of regression issues which we may not have had if we had acceptance tests but overall I felt the approach worked really well for us and the team consistently delivered. At one stage we did try to introduce some White driven GUI level tests but they were never introduced into the continuous integration process while I was on the project.

I appreciate that this is just one scenario and that each project is different but the lessons I took from this was that we should just do what works best in a given situation and not be too dogmatic in our approach.

Phillip actually <a href="http://fragmental.tw/2008/10/01/user-stories-are-just-schedulable-change/">has a different view</a> and (to probably quote him out of context) believes that having automated acceptance tests is vital:

<blockquote>
My main concern is that I think people value Acceptance Testing too much. Don’t get me wrong: automated acceptance tests are essential to a healthy agile process, the problem is what we do with them after we deliver a story.
</blockquote>

I do agree that we often place too much emphasis on acceptance testing but I'm not convinced that we need automated acceptance tests to have a 'healthy agile process'.

As I've been writing this the terminology seems a bit strange to me. Is it actually correct to say that an 'acceptance test' always implies an automated test that is run from the GUI? 

Or can an 'acceptance test' be a collection of functional and integration tests which confirm that a piece of business functionality works as expected?


