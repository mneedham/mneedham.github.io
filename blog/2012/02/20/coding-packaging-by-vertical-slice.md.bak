+++
draft = false
date="2012-02-20 21:54:55"
title="Coding: Packaging by vertical slice"
tag=['coding']
category=['Coding']
+++

On most of the applications I've worked on we've tended to organise/package classes by the function that they have or the layer that they fit in.

A typical package structure might therefore end up looking like this:

<ul>
<li>com.awesome.project
	<ul>
		<li>common
			<ul>
				<li>StringUtils</li>
 			</ul>
		</li>
	</ul>
	<ul>
		<li>controllers
			<ul>
				<li>LocationController</li>
				<li>PricingController</li>
 			</ul>
		</li>
	</ul>
	<ul>
		<li>domain
			<ul>
				<li>Address</li>
				<li>Cost</li>
				<li>CostFactory</li>
				<li>Location</li>
				<li>Price</li>
			</ul>
		</li>
	</ul>
	<ul>
		<li>repositories
			<ul>
				<li>LocationRepository</li>
				<li>PriceRepository</li>
 			</ul>
		</li>
	</ul>
	<ul>
		<li>services
			<ul>
				<li>LocationService</li>
 			</ul>
		</li>
	</ul>
</li>
</ul>

This works reasonably well and allows you to find code which is similar in function but I find that more often than not a lot of the code that lives immediately around where you currently are isn't actually relevant at the time.

On the last couple of applications that I've worked on we've been trying to group code around a domain concept or vertical slice of functionality.

Therefore instead of the above code we'd end up with something more like this:

<ul>
<li>com.awesome.project
	<ul>
		<li>location
			<ul>
				<li>Address</li>
				<li>Location</li>
				<li>LocationController</li>
				<li>LocationRepository</li>
				<li>LocationService</li>
 			</ul>
		</li>
		<li>platform
			<ul>
				<li>StringUtils</li>
 			</ul>
		</li>
		<li>price
			<ul>
				<li>Cost</li>
				<li>CostFactory</li>
				<li>Distance</li>	
				<li>Price</li>
				<li>PriceController</li>
				<li>PriceRepository</li>
 			</ul>
		</li>
	</ul>
</li>
</ul>

We were having a discussion about grouping code like this last week and I was struggling to describe what I prefer about the latter approach.

In the code base that I'm currently working on, which provides an API for other systems to do stuff with, it seems to lead to a design where we have created lots of potential <a href="http://2012.33degree.org/talk/show/67">micro services</a> which could be deployed separately if we wanted.

That possibility wasn't as clear to me until we started grouping code this way.

Another cool thing is that it's made us think about the domain of the code more and whether the grouping of classes actually makes sense. We can also see which classes fall inside an aggregate root.

In the above example under 'pricing' we can tell that <cite>Price</cite> is an aggregate root because it has a repository which allows us to get one and we can also tell that <cite>Cost</cite> is probably contained by <cite>Price</cite> since we don't have a way of directly getting a <cite>Cost</cite>.

We stop thinking about the domain classes as a whole, instead we think about them in their groups and how their aggregate roots might interact with each other if at all.

One disadvantage of grouping code like this is that if we're writing a new repository, for example, we've got further to navigate to find another one to base ours on. 

On the other hand you could argue that if we're doing that then perhaps there's an abstraction we can pull out to remove the problem.

It's an interesting approach to grouping code and one thing we've started noticing is that we end up with some packages which have a lot of classes in them and others which have very few. 

We're not sure whether this is a symptom of us not breaking down those particular packages enough or if there are just some areas of the domain that are bigger than others.

These are just some of my early observations so it'd be interesting to hear other's thoughts on whether this is a good/bad idea.
