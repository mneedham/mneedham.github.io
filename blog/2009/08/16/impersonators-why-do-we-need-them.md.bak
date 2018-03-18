+++
draft = false
date="2009-08-16 22:11:25"
title="Impersonators: Why do we need them?"
tag=['impersonators']
category=['Testing']
+++

I wrote previously about <a href="http://www.markhneedham.com/blog/2009/06/21/seams-some-thoughts/">an impersonator we are using on my project</a> which Martin Fowler has dubbed the '<a href="http://martinfowler.com/bliki/SelfInitializingFake.html">self initializing fake</a>' and although I thought this was the only type of situation where we might use this approach, from discussing this with my colleague <a href="http://blog.rufiao.com/">Julio Maia</a> and from experiences on the project I'm working on I realise there are other advantages to this approach as well.

<h3>To deal with unstable/slow integration points</h3>
This is the main reason that we use the self initializing fake and provides perhaps the most obvious reason why we might create an impersonator because we will remain in pain if we don't create one.

Before we used it all our acceptance tests went from the UI all the way through to the back end via a service layer which often led to tests failing due to timeouts (the service took longer than expected to respond) or problems somewhere in the back end. 

These '<a href="http://www.markhneedham.com/blog/2009/07/25/cruise-agents-reducing-random-build-failures/">random build failures</a>'  were amazingly frustrating since it meant that maybe more than 50% of the time that our continuous integration build light was red it wasn't actually related to anything that the person who checked in had done.

The confidence in the build light had drained and 'red builds' were pretty much being ignored.

<h3>To speed up the feedback cycle</h3>

A nice side effect that we got from putting in an impersonator is that our tests run about 5x more quickly than they did previously due to the fact that the impersonator is on a machine in Sydney whereas the actual end point is on a machine in Melbourne and because the impersonator just returns the same response for a given request each time instead of having to recalculate each time.

It is quite common on projects to use an in memory database instead of the real database for integration tests to allow these tests to run more quickly and I think this logic works well when applied to other systems we need to integrate against as well.

In general if we can have as much of the system as possible under our control in the early parts of our build pipeline then we can have a continuous integration build which gives us very quick feedback and only fails due to problems we created.

<h3>To handle not yet ready integration points early</h3>
Although we would rather do integration early on in a project so that we can discover any problems  and then fix them, sometimes the way the project has been planned means that a system that we need to integrate won't actually be ready until much later on.

An example of this which I've seen a couple of times is integrating applications with single sign on systems. 

Even though we don't know exactly how we will integrate against the real system we might be able to take a reasonably good guess of how it might work e.g. our application is able to detect whether a user is logged in based on some information set in the headers of each request by an <a href="http://msdn.microsoft.com/en-us/library/ms524610.aspx">ISAPI filter</a> which each request passes through before reaching our application.

On this occasion we didn't developer an impersonator for this integration point until after we already had the real end point but I think it would probably have made life easier if we had.

<h3>Impersonators and Continuous Integration</h3>
I'm sure there are more reasons why impersonators make sense but these are the ones that we've noticed so far.

The key with all these ways of impersonating an integration point is that they should only form part of our continuous integration pipeline -we do <strong>still need to test that our code works in a proper end to end test as well</strong>.

In our case we have another stage of our <a href="http://studios.thoughtworks.com/cruise-continuous-integration/deployment-pipelines">Cruise pipeline</a> which runs all the tests against the real end points.

I'm curious as to what our pipeline should look like when we have built multiple impersonators for different end points - my current thinking is that we can have an early stage of the pipeline where we make use of all of the impersonators and then another stage straight after that where we use all the real end points.

However, it does seem like a bit of a jump to go from all impersonators to no impersonators and it increases the likelihood that the build is going to fail since we are going straight from minimal integration to having everything integrated. 

I guess another approach would be to gradually introduce a real integration point on each part of the pipeline until we have everything integrated on the last one although this might actually result in our feedback being slower if its the last integration point which gives us problem.

Julio has <a href="http://blog.rufiao.com/2009/08/impersonator-pattern/">written more about the impersonator pattern</a> on his blog.
