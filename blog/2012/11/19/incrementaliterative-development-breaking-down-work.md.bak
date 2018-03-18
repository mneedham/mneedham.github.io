+++
draft = false
date="2012-11-19 08:50:07"
title="Incremental/iterative development: Breaking down work"
tag=['software-development']
category=['Software Development']
+++

Over the past couple of years I've worked on several different applications and one thing they had in common was that they had a huge feature which would take a few months to complete and initially seemed difficult to break down.

Since we favoured an incremental/iterative approach to building these features and wanted to add value in short feedback cycles we needed to find a way to break them down.

I thought I'd record the ways that we came up with for doing that.

<h4>Complexity of markup</h4>

On one of the projects that I worked we were building a publishing platform and needed to publish some documents which had varying degrees of complexity in their XML markup.

Trying to get all the combinations of markup working at once was a non starter - there were way too many different ways that a document could be marked up just from a quick glance. We would later also find other ways that we didn't know about at the start.

Instead we decided to start with the simplest markup and then as part of our data ingestion process we excluded any documents which had too much complexity through a sequence of rules.

We slowly relaxed those rules as we played the stories to introduce the more complex markup until eventually we'd imported and were showing all of the documents.

<h4>Simplicity of rules</h4>

On another project we were writing a pricing engine which needed to come up with prices for connecting a network between various locations that a customer could specify.

The end goal was that you'd be able to price a network regardless of which locations the customer suggested but we realised early on that there were some very different rules for pricing the USA compared to the rest of the world.

Since the rules for the USA were a bit more complicated and we didn't understand them as well as the other rules we were able to first get our algorithm working for the rest of the world and then move onto the USA.

On another project we needed to work out the shipping costs and the calculation differed in complexity depending on where you were in the country so we started with the simple areas first and built on that!

<h4>Dependency Chain</h4>
On my most recent project we needed to do the initial release of all our applications into the production environment but there were quite a few moving parts involved in doing that.

To break this problem down we wrote each application on a card, stuck them all up on the wall and worked out the dependencies between them. 

We first focused on deploying the ones which had no dependencies and then worked out from there.

<h4>Workflow</h4>
A couple of years ago I worked on an insurance application where we were building an application which would be used by sales representatives when renewing a customer's home insurance.

It was based around a workflow that the client wanted the sales representatives to follow whereby they could over the customer varying incentives to renew which increased in actual value as you went down the work flow.

There were various calculations at each stage which were somewhat inter-mingled but the approach that made most sense here was to drive out the solution starting with the early parts of the workflow and continuing from there.

We had to do a little bit of rework of existing calculations as we added a new step to the application but in general it seemed to work reasonably well.

I'm sure there are other ways of breaking down work but this is how we did it - I'd be interested in learning any other tricks/techniques people have for figuring out how to do this.
