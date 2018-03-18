+++
draft = false
date="2009-08-19 00:43:18"
title="Impersonators: Finding the enabling point"
tag=['impersonators']
category=['Testing']
+++

One of the other interesting problems that we've come across while making use of different impersonators in our build process, and which <a href="http://blog.typemock.com/2009/08/by-any-other-name.html#comment-14998269">Julio mentions at the end of his comment on Gil Zilberfeld's blog post</a>,  is trying to work out where the correct place for the impersonator is.

Ideally we want to put the impersonator in a place where we can easily turn it on or off depending on whether we want to use the impersonator or the real end point. In fact if we aren't able to do this then it is perhaps the case that we haven't actually created an impersonator at all. 

I like to use the term '<strong>enabling point</strong>', which I learnt from Michael Feathers in his chapter on <a href="http://www.markhneedham.com/blog/2009/06/21/seams-some-thoughts/">seams</a> in <a href="http://www.amazon.co.uk/Working-Effectively-Legacy-Robert-Martin/dp/0131177052/ref=sr_1_1?ie=UTF8&qid=1250602607&sr=8-1">Working Effectively With Legacy Code</a>, to describe <strong>the place where we can make the decision to use the impersonator or the real end point</strong>.

Ideally this will probably be determined by changing a simple setting in a configuration file.

If you choose the wrong enabling point the 'impersonator' may not actually help you that much and it might even become such a hindrance that you stop using it and just accept the problems we can have when we have to integrate against real end points all the way through our build process.

On the way to making use of the <a href="http://martinfowler.com/bliki/SelfInitializingFake.html">self initializing fake</a> on my current project we tried/thought about some other approaches which we thought might be able to ease the pain of integrating directly against the service layer which were quite unstable at the time. 

We were often losing 4 or 5 hours a day due to the website being unusable without this integration point working.

<h3>Stubs</h3>

The first thought was that perhaps we could just integrate against a stub of each of the services in our development environment and then inject either the stub or real service into our code through dependency injection.

Julio points out quite an important flaw with this approach:

<blockquote>
It happens that the results of those tests have very limited value, as they're not actually validating if the system actually integrates correctly with its environment.
</blockquote>

If there was a change to the structure of the xml being returned we wouldn't know about this until we actually ran a test against the real integration point and our <a href="http://www.markhneedham.com/blog/2009/07/20/coding-quick-feedback/">feedback cycle</a> is now fairly slow.

In addition we would be returning a canned set of results from data that we had setup and the maintenance of this canned data just becomes a real pain after a while.

<h3>The internal cache</h3>

The first approach that we tried involved intercepting the requests/responses of each of the service calls from inside the application itself by making use of <a href="http://unity.codeplex.com/Thread/View.aspx?ThreadId=63680">interceptors injected from our DI container</a> around the classes which made the calls.

We eventually managed to get this working to a stage where we could save the requests and responses to disk and then make use of this data when the services weren't working.

The problem with this approach was that we were configuring it by configuring a 'UseCache' property in our configuration file which I think was probably a sign that we were doing something wrong, the problem being that we made use of the 'UseCache' property in our production code.

We only setup the recording part of the process to record the requests and responses from our service tests when run as part of the build and then saved those results onto a remote server.

Another step we needed to do to make use of the 'impersonator' was therefore to copy those files across to the local machine and put them into the 'cache directory' which was another configurable property.

Although it only took maybe 5 minutes to do this it became quite annoying after a while. If we have found a good enabling point then it should be really easy to switch to using it which wasn't the case here.

In addition we know had all this impersonating code inside our main solution and it became more and more complex as we tried to make it more useful - another lesson here was that <strong>if we're going to write an impersonator, that code should be outside of our main application</strong>.

<h3>Self Initializing Fake</h3>
The self initializing fake is our current approach and the nice thing about this approach is that it's really easy to switch back and forth between this and the real end point - all you need to do is change the 'ServiceUrl' value in the configuration file!

The self initializing fake is a recording proxy which sits on our CI server and captures the requests and responses to/from the service and then stores those results in memory. 

If you make the same request again it returns the response from its store instead of sending that request through to the service layer.

The code for the self initializing fake is outside of our main solution - in fact it's actually written in Ruby and the application is in C#.

<h3>In summary</h3>
From my experience it's quite important to make use of impersonators of our integration points if we are to get a stable environment to run against but we can cause ourselves a lot of pain if we pick the wrong enabling point for that impersonator.

The key seems to be that it should be minimal effort to enable an impersonator and we shouldn't need to make any changes to our production code in order to do so. 

From working with some other impersonators I think it is also important that we shouldn't have to make any changes to our test code in order to use an impersonator either.

If we find ourselves having to do something that seems crazy with impersonators it might well be worth considering whether we have the right enabling point.
