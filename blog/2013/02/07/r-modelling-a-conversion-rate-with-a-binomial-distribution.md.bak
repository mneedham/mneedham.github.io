+++
draft = false
date="2013-02-07 01:26:12"
title="R: Modelling a conversion rate with a binomial distribution"
tag=['r-2']
category=['R']
+++

<p>As part of some work <a href="https://twitter.com/siddharthdawara">Sid</a> and I were doing last week we wanted to simulate the conversion rate for an A/B testing we were planning.</p>


<p>We started with the following function which returns the simulated conversion rate for a given conversion rate of 12%:</p>



~~~r

generateConversionRates <- function(sampleSize) {
	sample_a <- rbinom(seq(0, sampleSize), 1, 0.12)
	conversion_a <- length(sample_a[sample_a == 1]) / sampleSize

	sample_b <- rbinom(seq(0, sampleSize), 1, 0.12)
	conversion_b <- length(sample_b[sample_b == 1]) / sampleSize
		
	c(conversion_a, conversion_b)
}
~~~

<p>If we call it:</p>



~~~r

> generateConversionRates(10000)
[1] 0.1230 0.1207
~~~

<p>We have a 12.3% conversion rate on A and a 12.07% conversion rate on B based on 10,000 sample values.</p>


<p>We then wrote the following function to come up with 1000 versions of those conversion rates:</p>



~~~r

generateSample <- function(sampleSize) {
	lapply(seq(1, 1000), function(x) generateConversionRates(sampleSize))
}
~~~

<p>We can call that like this:</p>



~~~r

> getSample(10000)
[[998]]
[1] 0.1179 0.1216

[[999]]
[1] 0.1246 0.1211

[[1000]]
[1] 0.1248 0.1234
~~~

<p>We were then using these conversion rates to try and work out how many samples we needed to include in an A/B test to have reasonable confidence that it represented the population.</p>


<p>We actually ended up abandoning that exercise but I thought I'd record the code because I thought it was pretty interesting. </p>

