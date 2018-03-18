+++
draft = false
date="2009-01-24 09:36:32"
title="jQuery: Approaches to testing"
tag=['jquery']
category=['jQuery']
+++

We've been doing a bit of work with <a href="http://jquery.com/">jQuery</a> and true to our TDD roots we've been trying to work out the best way to test drive our coding in this area.

There seem to be 3 main ways that you can go about doing this, regardless of the testing framework you choose to you. We are using <a href="http://github.com/nkallen/screw-unit/tree/master">screw-unit</a> for our javascript testing.

<h3>Mock everything out</h3>

The idea here is that we mock out all calls made to jQuery functions and then we assert that the expected calls were made in our test.

Taking this approach means we are able to reduce the dependencies in our tests and they run very quickly. 

The problem is that a lot of assertions become assertions checking that certain operations were called on the DOM since jQuery makes a lot of these type of calls in its code. The tests therefore end up being quite long and difficult to understand unless you were the one who initially wrote them.

We also effectively end up testing how the framework interacts with the DOM rather than testing our own code with this approach.

<h3>Don't mock anything</h3>

The opposite approach is to just test directly against jQuery and then do assertions against the part of the DOM affected by the javascript code we are testing.

The problem here is that if you want to test against plugins which make ajax requests or carry out animation effects then the tests become dependent on how long these calls take and we need to find a way to block the test until those calls return which is quite difficult!

<h3>Only stub certain calls</h3>

The happy medium is that we test directly against the jQuery library but stub out ajax requests and animation effects. Our test assertions are against the state of the DOM to check that it was changed in the way that we expected.

This approach allows us to test our javascript code in terms of its behaviour without testing the internals of how jQuery works.

The wiring up of events to different controls on the page is done in our test but the actual logic that happens when these events are fired is in our js file under test.

We currently favour this last approach as it seems to give us the best of both worlds so to speak. It be would be interesting to hear how are other people going about Javascript testing.
