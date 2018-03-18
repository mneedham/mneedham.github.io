+++
draft = false
date="2013-01-27 13:27:32"
title="A/B Testing: Thoughts so far"
tag=['software-development', 'absplittesting']
category=['Software Development']
+++

<p>I've been working at <a href="http://www.uswitch.com/">uSwitch</a> for about two months now and for the majority of that time have been working on an A/B test we were running to try and make it easier for users to go through the energy comparison process.</p>


<p>I found the '<a href="http://www.exp-platform.com/Documents/GuideControlledExperiments.pdf">Practical Guide to Controlled Experiments on the Web</a>' paper useful for explaining how to go about doing an A/B test and there's also <a href="http://mcfunley.com/design-for-continuous-experimentation">an interesting presentation by Dan McKinley</a> about how <a href="http://www.etsy.com/">etsy</a> do A/B testing.</p>


<p>I've previously read about A/B tests which changed the page for users on the client side using tools like <a href="http://analytics.blogspot.co.uk/2012/06/helping-to-create-better-websites.html">Google Website Optimiser</a> but since we had made significant changes to the journey we split users on the server side.</p>


<h4>Reporting</h4>
<p>Before we started running our test we needed to work out how we were measuring conversion and how we would get the data to allow us to calculate that.</p>


<p>We decided to measure the number of people who started a comparison against the number of those who reached the thank you page and only included those who had an active session from the time we started the experiment.</p>


<p>We were already recording the pages users were hitting so it wasn't difficult to write a query to derive the conversion rate.</p>
 

<p>Unfortunately it was taking us a couple of hours to run other queries about the experiment because we had mixed together data about users' sessions and the experiment. The data therefore wasn't optimised for the types of queries we wanted to run.</p>


<p>One of our next tasks is to <strong>split these concerns </strong>to make our lives a bit easier.</p>


<h4>Conversion rate and time</h4>
<p>I learnt that <strong>people don't necessarily finish a transaction in one sitting</strong> so the conversion rate at the beginning of the experiment isn't representative.</p>


<p>We saw it level out after a couple of weeks once we'd gone through a full 'season'. A season is a time period which cover all the days of the week and take into account the average amount of time that people take to go end to end in the process.</p>


<p>We've worked out the amount of time that we need to run the test to unequivocally say that the control or experiment has fared better but there is a tendency to kill off the experiment if it's doing significantly worse. I still need to learn when you should stick with it and when it's best to kill it off.</p>


<h4>Cognitive biases</h4>

<p>Although we were <a href="http://www.r-tutor.com/elementary-statistics/hypothesis-testing/two-tailed-test-population-proportion">using a hypothesis test</a> to determine whether the control or experiment was doing better some <a href="http://en.wikipedia.org/wiki/Cognitive_bias">cognitive biases</a> tried to creep in.</p>


<p>When we started the experiment most people were fairly convinced that the experiment was going to fare better and so we <a href="http://en.wikipedia.org/wiki/Confirmation_bias">really wanted that to happen</a> and would look for the positives in how it was doing.</p>


<p>As with the first example in the etsy talk there was quite a big difference between the two versions and as a result we'd spent a few weeks coding up the experiment and <a href="http://en.wikipedia.org/wiki/Sunk_costs#Loss_aversion_and_the_sunk_cost_fallacy">didn't want that work to feel wasted</a>.</p>


<h4>What but not why</h4>
<p>From the data we could easily see what the users behaviour was but it was much more difficult to understand why that was the case even after drilling down into the data.</p>


<p>I hadn't realised that <a href="http://en.wikipedia.org/wiki/Usability_testing">user testing</a> fills this gap quite well because people vocalise what they're thinking when going through the journey and you get an explanation about what other users might be doing as well.</p>


<p>One of the suggestions from the etsy talk is to try and make your hypotheses smaller so that you can run <strong>smaller tests with less variables</strong> and therefore have more chance of explaining what's going on.</p>


<p>I find this type of stuff fascinating so if anyone has some good papers/articles/blogs where others have written about their experiences I'd love to hear about them.</p>


<p>These are some other posts that I've come across:</p>


<ul>
<li><a href="http://www.cennydd.co.uk/2009/statistical-significance-other-ab-test-pitfalls/">Statistical significance & other A/B test pitfalls</a></li>
<li><a href="http://37signals.com/svn/posts/1525-writing-decisions-headline-tests-on-the-highrise-signup-page">Writing Decisions: Headline tests on the Highrise signup page</a></li>
<li><a href="http://kylerush.net/blog/optimization-at-the-obama-campaign-ab-testing/">Optimization at the Obama campaign: a/b testing</a></li>
</ul>
