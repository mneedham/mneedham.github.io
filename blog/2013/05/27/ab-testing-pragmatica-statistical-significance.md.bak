+++
draft = false
date="2013-05-27 13:13:49"
title="A/B Testing: Being pragmatic with statistical significance"
tag=['absplittesting']
category=['Software Development']
+++

<p>One of the first things that we did before starting any of the <a href="http://www.markhneedham.com/blog/tag/absplittesting/">A/B tests</a> that I've previously written about was to work out how many users we needed to go through before we could be sure that the results we saw were statistically significant.</p>


<p>We used the <a href="http://www.r-tutor.com/elementary-statistics/hypothesis-testing/two-tailed-test-population-proportion">prop.test</a> function from R to do this and based on our traffic at the time worked out that we'd need to run a test for 6 weeks to achieve statistical significance.</p>


<p>That means that we could manage a maximum of 8 tests a year i.e. 8 changes a year which isn't really feasible for a website which needs to evolve quickly to remain competitive.</p>


<p>We therefore had two ways that we could use A/B tests and make changes more frequently:</p>


<ol>
<li>Don't A/B test everything</li>
<li>Speed up the cycle by:
	<ul>
	  <li>iterating within a test i.e. making tweaks/fixing bugs</li>
      <li>ending the test early if control or experiment was consistently better.</li>
	</ul>
</li>
</ol>

<h3>Don't A/B test everything</h3>

<p>When we were looking through our product backlog it was interesting to see that there were some features that we agreed would be definite improvements while there were others that we weren't really sure about.</p>


<p>As Nate Silver points out in '<a href="http://www.markhneedham.com/blog/2013/05/14/book-review-the-signal-and-the-noise-nate-silver/">The Signal and the Noise</a>' whenever we rely on intuition we introduce bias but in this case the people making the call were experts of the domain so it seemed like a reasonable approach.</p>


<p>If we felt that a feature made the user experience more delightful or if it was an integral part of the way we were driving the product then we'd just make the change without running an A/B test.</p>


<p>We still had daily metrics which would highlight if things had been made significantly worse but we didn't track the performance of those features with the same vigour as you would with an A/B test.</p>


<h3>Speed up the cycle</h3>

<p>Although it would take 6 weeks to be completely confident in an A/B test we were able to get feedback much more quickly as to which branch (master/experiment) was performing better.</p>


<p>If we noticed a drop off in conversion for a specific browser then we'd <a href="http://www.markhneedham.com/blog/2013/04/28/ab-testing-reporting/">make the appropriate bug fixes</a> while the test was still running.<p>

<p>In an ideal world I suppose we should have started the test from scratch but we didn't do this unless there was something seriously wrong and we had to make major changes.</p>


<p>Instead we started <strong>tracking the daily conversion rate</strong> which allowed us to see whether our bug fixes had made an impact.</p>


<p>Tracking the daily conversion rate also allowed us to see whether one branch was consistently better or not - if we saw that one branch was consistently better over a week or two then we'd be confident that we should end the test.</p>


<p>On the other hand early on in the test cycle we'd see the control converting better on the first day, then the experiment converting better the next day before the control converted better for the next two.</p>


<p>When we observed that behaviour we assumed that random variation was at play and waited a few more days to see if it would settle down before we made a decision.</p>


<p>We were effectively trading off statistical significance against the number of tests that we could run which in this context was a reasonable trade off to make.</p>


<h3>In summary</h3>

<p>I'd not done A/B testing before I worked at <a href="http://www.uswitch.com/">uSwitch</a> and I think the approach we took seems reasonable for most web based products.</p>


<p>We want to use data to help us make decisions but we need to leverage our intuition/domain expertise rather than relying completely on the data.</p>


<p>In other words we're more <a href="http://blog.iic.uam.es/2010/04/pick-a-number-maybe-data-driven-should-be-data-assisted/">data assisted rather than data driven</a>.</p>

