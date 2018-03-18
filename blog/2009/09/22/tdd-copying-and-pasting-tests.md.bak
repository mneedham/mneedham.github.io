+++
draft = false
date="2009-09-22 23:39:56"
title="TDD: Copying and pasting tests"
tag=['tdd']
category=['Testing']
+++

I've been re-reading <a href="http://iancartwright.com/blog/2009/04/test-code-is-just-code.html">a post my colleague Ian Cartwright wrote earlier this year about treating test code the same way as production code</a> and one thing which stands out as something which I'm certainly guilty off is copying and pasting tests.

Ian lists the following problems with doing this:

<blockquote>
The first one is cut & paste, for some reason when it comes to unit tests people suddenly start cutting and pasting all over the place. Suddenly you find a file with 20 tests each of which repeats exactly the same few lines of code. I don't think I need to describe why this is bad and I expect we've all seen the outcome: at some point later those tests all start breaking at the same time, if we are unlucky a few tweaks have happened to the cut & pasted code in each so we spend a lot of effort figuring out how to make each one pass again. There is no rule that says we can't have methods in test fixtures so ExtractMethod still applies, and using SetUp sensibly often helps. The same rational for avoiding cut & paste and the same solutions we know from production code apply to test code.
</blockquote>

Despite this I've often felt that at some stage we should have factored tests down to a stage where removing any more of the 'duplication' would actually harm the <a href="http://www.markhneedham.com/blog/2009/04/13/tdd-balancing-dryness-and-readability/">readability of the test</a> and that at this stage perhaps it's ok to copy the skeleton of a test and reuse it for your next test.

Since I first read Ian's post I've been playing around with the idea of never copying/pasting tests when I've been working on my own on my project and with stuff I play around with outside work and I like the approach but hadn't really fully appreciated the benefits that we could get from doing so.

Over the last week or so my colleague Matt Dunn and I have been writing tests around pre-existing code and we decided that we would try wherever possible to not copy tests but instead write them out from scratch each time. 

I found it quite difficult to start with as <strong>the temptation is always there to just grab a similar test and tweak it slightly</strong> to test the new bit of functionality but an interesting early observation was that we were far less accepting of duplication in tests when we had to type out that duplication each time than if we had just copied and pasted it.

I tend to extract method quite frequently when I see test code which is similar but <strong>we were seeing potential areas for extracting out common test code which I would never have spotted</strong>.

There's a chapter in Steve Freeman and Nat Pryce's book '<a href="http://www.growing-object-oriented-software.com/">Growing Object Oriented Software, guided by tests</a>' titled '<a href="http://mockobjects.com/book/listening-to-the-tests.html">Listening to the tests</a>' which I quite like and I think <strong>we become much more aware of the tests if we have to write them out each time</strong>.

An example of this which Matt spotted was that in one bit of test code we were working on there was a method called 'StubOutSomeRepository' which was called by every single test and I instinctively made the call to that method as the first line in our new test.

Matt questioned whether it was actually even needed so we removed it from every single test in that test fixture and they all still worked!

I'm pretty sure that we wouldn't have spotted that problem if we'd just copy/pasted and I'm also fairly sure that all the other tests in that test fixture were copy/pasted from the first test written in the test fixture when there may actually have been a need to stub out the dependency.

Apart from enabling us to simplify our tests I think that writing out our tests each time <a href="http://www.markhneedham.com/blog/2009/08/05/think-a-little-code-a-little/">keeps us thinking</a> - it's really easy to turn off and work on auto pilot if you're just copy/pasting because it's essentially mindless and doesn't engage the mind that much.

Keeping in the thinking mindset allows us to see whether we're actually testing properly and I think it also makes the pairing process a bit more interesting since you now have to talk through what you're doing with your pair.

One of the other reasons I thought copy/pasting might be useful sometimes is that it can save time if we're typing out similar types of tests repeatedly and I often feel that it would be quite annoying for my pair to watch me do this.

Now I'm not so convinced by my own argument and I think that the time that we save by writing more readable tests probably easily outweighs any short term time gains. 

Our conversations have become more about working out ways that we can 

On a related note I recently watched a <a href="http://charlesmaxwood.com/8-lessons-from-corey-haines-performance-kata/">video of a performance kata by Corey Haines</a> where he works through a problem guided by tests and as far as I remember doesn't ever copy and paste a test but instead looks for ways to reduce the duplication he has in his test code so that he doesn't have to do too much typing for each test.
