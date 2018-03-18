+++
draft = false
date="2008-08-18 22:39:49"
title="From Prototype to Delivery"
tag=['software-development', 'prototype', 'spikes', 'delivery']
category=['Software Development']
+++

Projects often reach the interesting point where the prototyping and development phases intersect and there are some interesting decisions to make.

From a development point of view the biggest decision is what to do with the code that has been developed.

When developing <a href="http://en.wikipedia.org/wiki/Software_prototyping">prototypes</a> the focus tends to be on getting something to work quick and dirty. Not a lot of time is put into considering edge cases or error conditions or any of the other niceties that are needed for software to be usable in an enterprise environment.

There are generally three choices with regards to what to do with the code:
<h3>Throw the code away</h3>
This would be the favoured choice all things considered as it means that the team can get the dual benefit of writing good quality production code TDD style while also taking on the lessons learnt during prototyping.

If this approach is to actually happen then expectations of the client need to have been set extremely well. It needs to be made clear to them during the prototyping phase that what's being written is throwaway code and is not production quality.

It is very easy for the client to see the output of prototyping and believe that functionality has been implemented and can now be rolled out.

From their point of view what they would see (from a UI level for example) from code written as a prototype or as production quality code may be no different, and they may think that you are just wasting their money by writing the same thing twice unless this is well handled.
<h3>Keep the code and retrospectively refactor it</h3>
This option is the middle ground between the two extremes. We keep the prototyping code but add some tests and refactor the code in retrospect.

The code produced probably won't be as clean as if it had been written with a TDD approach, but it will allow the project to be delivered more quickly in the short term at least.

Edge cases probably won't be investigated as thoroughly as if the code is written from scratch with complete analysis, but more cases will be considered than if it was not tested at all.
<h3>Keep the code as it is</h3>
The final option is to keep the code written during prototyping and add edge cases and error conditions around it.

This is the most risky approach because although we have working prototype code we lose the set of regression tests that we would have if it had been developed in a <a href="http://en.wikipedia.org/wiki/Test-driven_development">test first</a> approach.

Our mind set will now also be more inclined to think that a piece of functionality is complete and we may end up missing important edge cases which only rear their ugly head when the code is in production.

In a perfect world every  prototyping session would result in the code being thrown away and then rewritten using the lessons learned in the initial attempt.

As it is not, it does make me wonder whether it would be best to sacrifice some of the speed in the prototyping phase to write better code and remove some of the pain that will otherwise be felt later on.
