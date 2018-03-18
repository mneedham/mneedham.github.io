+++
draft = false
date="2008-11-28 00:34:24"
title="TDD: Suffering from testing last"
tag=['tdd', 'testing']
category=['Testing']
+++

I've always been a big proponent of writing tests before writing code, and I roll off the standard reasons to people who question this approach:

<ul>
<li>They help to drive the design</li>
<li>They provide a safety net when making future changes</li>
<li>They provide a way of communicating the intent of the code to the rest of the team</li>
</ul>

And so on. Despite knowing all this I recently took a non test driven approach to writing some bits of code - we were keen to get the system working end to end so it seemed a trade off worth making to prove that it was doable.

I knew that I would <strong>suffer when it came to testing this code after I had already written it</strong> and indeed it did!

I've tested around legacy code before and although <a href="http://www.amazon.co.uk/Working-Effectively-Legacy-Robert-Martin/dp/0131177052/ref=sr_1_1?ie=UTF8&s=books&qid=1227794213&sr=8-1">Michael Feather's book</a> makes it much easier, it's still not a great experience. The saving grace has always been that I didn't write the code whereas in this case it was quite definitely my fault that I ended up with this problem.

The original pain came from not knowing where I should start. Since we didn't have any tests I wasn't sure exactly what the code was doing despite the fact that I had written most of it fairly recently.

In particular I ran into the problem whereby I wrote a test which passed so all seemed good. Suspicious as to whether this was the case I decided to comment out some of the code which was apparently making the code pass. I expected the test to fail and give me the red bar but in actual fact the test still passed!

It turned out that I had written the expectations for my mocks slightly wrong in the test - a mistake that I would have definitely caught if I had written the test first but could have easily missed by testing last.

After this I decided that because there wasn't too much complex logic in this particular piece it would be much better to <strong>comment out the code and then test first</strong> before fitting it back together again. Eventually I got all the code covered but it took much longer than if I had just tested it properly the first time around.

For me software development is all about creating quick feedback loops and I find it very frustrating when I'm unable to do this. Testing first is one very good way of achieving this as it provides a clear way forward and gives feedback on our progress.

I will certainly be very reluctant to test last again.
