+++
draft = false
date="2008-11-23 23:21:46"
title="Testing Test Code"
tag=['tdd', 'testing']
category=['Testing']
+++

One of the interesting discussions that has come up on several projects I've worked on is whether or not we should test code that was written purely to help us test production code.

One of the main arguments used against testing test utility code is that it is not production code and therefore perhaps doesn't need to be held to the same standards because it lacks the complexity of production code.

Even ignoring this assumption, which I don't agree with, I think we are still missing the point as to why we actually test in the first place.

Although a lot of the value of the test driven approach is that it helps us to <a href="http://www.markhneedham.com/blog/2008/10/01/tdd-without-the-design/">drive design</a>, the other side of the story, which we perhaps only fully appreciate after working with legacy code, is the safety net that having a suite of tests around our code provides.

From my experience the <strong>complexity of the test utility code is what determines whether it is valuable to test</strong> it or not. If it's just builders to help create test data then I would agree there is little value in testing it, but if there's actual logic and/or complexity then having a safety net is a good thing. Even if the tests are very simple they help protect us to ensure our code is still working when we make future changes.

The thing to watch for is that test utility code often starts off being very simple but slowly complexity creeps in making it more difficult to verify whether it actually does what we want it to.

As a rough marker, when you end up debugging through your test utility code to work out why it isn't working as you expected it's probably time to consider putting some tests around it.
