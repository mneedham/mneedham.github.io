+++
draft = false
date="2012-04-30 21:45:50"
title="Performance: Caching per request"
tag=['coding', 'software-development']
category=['Software Development']
+++

A couple of years ago I wrote a post describing an approach my then colleague <a href="https://twitter.com/#!/christianralph">Christian Blunden</a> used to help improve the performance of an application where you try to <a href="http://www.markhneedham.com/blog/2010/07/10/performance-do-it-less-or-find-another-way/">do expensive things less or find another way to do them</a>.

On the application I'm currently working on we load reference data from an Oracle database into memory based on configurations provided by the user.

There are multiple configurations and then multiple ways that those configurations can be priced so we have two nested for loops in which we load data and then perform calculations on it.

When profiling the application we realised that some of the database calls being made with the same parameters and were therefore loading back the same reference data that we'd already loaded.

The most obvious way to solve this problem would be to move the code out of the loop and make less calls to the database that way but logically the  domain is expressed more clearly when it's inside the loop.

<a href="http://www.linkedin.com/pub/alex-harin/13/40b/716">Alex</a> therefore came up with an alternative approach where we wrap the database calling code in a caching decorator.

The caching decorator is a request scoped object so we're only caching those results for a short amount of time which means that we <a href="http://martinfowler.com/bliki/TwoHardThings.html">don't have to worry about cache invalidation</a> because it's thrown away when the request has been processed.

I've previously seen this problem solving by using a Hibernate second level cache which would cache results across requests. 

In our application there are more likely to be calls to the database with the same parameters within the same request rather than across requests.

The load on the system is likely to come from complex requests where many prices needed to be calculated rather than from a huge frequency of requests 

If that changes then we always have the option of caching at both levels but at the moment our current approach seems to work pretty well.
