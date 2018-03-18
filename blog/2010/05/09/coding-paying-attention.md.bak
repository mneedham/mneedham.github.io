+++
draft = false
date="2010-05-09 13:04:48"
title="Coding: Paying attention"
tag=['coding']
category=['Coding']
+++

<a href="http://twitter.com/jeremydmiller">Jeremy Miller</a> tweeted earlier in the week about <a href="http://twitter.com/jeremydmiller/status/13310240804">the dangers of using an auto mocking container</a> and how it can encourage sloppy design:

<blockquote>
That whole "Auto Mocking Containers encourage sloppy design" meme that I blew off last week? Seeing an example in our code.
</blockquote>

I haven't used an auto mocking container but it seems to me that although that type of tool might be useful for reducing the amount of code we have to write in our tests it also hides the actual problem that we have - an object has too many dependencies.

By hiding the creation of stubs/mocks for those dependencies in our test we are addressing the effect and not the cause i.e. we are <a href="http://www.markhneedham.com/blog/2009/08/06/bear-shaving/">bear shaving</a>.

Jeremy followed this up with <a href="http://twitter.com/jeremydmiller/status/13310461017">a couple of</a> <a href="http://twitter.com/jeremydmiller/status/13310483817">quite insightful comments</a>:

<blockquote>
You know though, I still think it comes down to <strong>you being responsible for paying attention.
</strong></blockquote>

<blockquote>
It's no different than still having to worry about DB optimization even though the ORM is shielding you from the details
</blockquote>

Another somewhat related situation where I've noticed a similar problem is when we have several tests which require a certain method to be stubbed out and in the interests of reducing duplication we <a href="http://www.markhneedham.com/blog/2008/12/19/tdd-mock-expectations-in-setup/">pull that up into a setup method</a>. 

While this achieves that goal it also means that there is information that is hidden away from us when we read each of our tests.

One approach that I've seen encouraged is that we should never use a setup method so that we have to create everything we need for our test in the test body.

I quite like this approach because it encourages us to see any problems that we're creating with respect to writing difficult to test code but quite often what ends up happening is we'll <a href="http://www.markhneedham.com/blog/2009/09/22/tdd-copying-and-pasting-tests/">copy and paste tests</a> because there's more code to write for each test.

I'm coming to the conclusion that there's no one approach that will stop us making design mistakes and that as Jeremy says, we need to make sure that we pay attention to what we're doing.
