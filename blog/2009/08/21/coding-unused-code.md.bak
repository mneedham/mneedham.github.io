+++
draft = false
date="2009-08-21 08:56:02"
title="Coding: Unused code"
tag=['coding']
category=['Coding']
+++

An interesting problem that we have come across a few times over the past 6 months is the dilemma about what to do when start work on a feature and get part way through it before it gets descoped from the current iteration, maybe to be picked up later on but maybe not.

The easiest, and there most common, approach is to just leave the code in the code base half complete and then hopefully return to it at some later stage. 

In theory perhaps this doesn't seem like such a bad idea.

The problem is that this code is clutter and create confusion since other people in the team come across it and they're not really sure what to do.

In a way it is comparable to <a href="http://www.markhneedham.com/blog/2009/01/17/the-danger-of-commenting-out-code/">commenting code</a> in that it creates doubt in people's minds about whether or not the code is actually important or whether they can delete it.

One of the annoying side effects of testing this type of code is that as a result of those tests it will still have usages in the code base which means that the IDE won't be able to identify it as unused code. If it did then you would probably feel more confident about deleting it. 

On top of the problems that we get from leaving commented code in the code base it is also quite likely that the complexity of the code base has been increased from adding this code and since it's not currently being used it is now unnecessary complexity.

We noticed this in our code base when our original plan for release was to have three different customer work flows through our application.

Two of the work flows were descoped quite close to the release but were needed in the second release so we didn't go through the code base and delete everything, we just left it in there.

The thinking behind this decision was that we would be needing that code quite soon anyway since we would start working on the next release which had those features in straight after we did the first release.

As it turned out the first release ended up being a little later than planned and when we got back to implementing those features the details of how the business now wanted them to work had changed to such an extent that what we had done previously was actually more of a hindrance than help. 

We ended up having to rewrite a lot of the functionality.

In lean terms this was therefore the worst kind of <a href="http://www.learnleanblog.com/2008/01/lean-manufacturing-inventory-and-work.html">work in progress</a> since we know that it is half finished, currently adding no value and we're not sure exactly when or even if it will eventually add some value to the end user.

We actually have a similar situation with a feature which we started work on but which was pushed out of the current iteration.

The approach this time was to go through the code base and get rid of all the code and then just re-implement it when we need it - the original code is in source control if we need to refer to it so it's not gone forever.

Another approach which <a href="http://intwoplacesatonce.com/">Dave</a> suggested which we considered but decided not to do this time was to keep a copy of the unused code on a branch so that if/when that code is needed we could just switch to the branch to continue working on that functionality.

I guess this approach might work quite well if it really is a short delay until we are actually going to implement the feature.

Perhaps surprisingly given that things change quite quickly with the agile approach to software development I can't actually remember coming across this problem before but I'm sure it's quite common so I'd be interested to hear what others are doing.
