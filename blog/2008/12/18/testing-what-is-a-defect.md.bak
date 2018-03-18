+++
draft = false
date="2008-12-18 22:34:48"
title="Testing: What is a defect?"
tag=['testing']
category=['Testing']
+++

One of the key ideas that I have learnt from my readings of <a href="http://www.markhneedham.com/blog/2008/11/19/the-toyota-way-book-review/">The Toyota Way</a> and <a href="http://www.markhneedham.com/blog/2008/12/09/taiichi-ohnos-workplace-management-book-review/">Taaichi Ohno's Workplace Management</a> is that we should <strong>strive not to pass defects through the system to the next process</strong>, which you should consider to be your customer.

As a developer the next process for each story is the testing phase where the testers will (amongst other things) run through the acceptance criteria and then do some exploratory testing for scenarios which weren't explicitly part of the acceptance criteria.

The question is how far should we go down this route and what exactly is a defect using this terminology - if a tester finds a bug which was listed in the acceptance criteria then I think it's reasonable enough to suggest that the developer has moved a defect onto the next stage.

But what about if that bug only appears on one particular browser and that's one that the developer didn't test against but the tester did. Clearly automating tests against different browsers can help solve this problem but there are still some types of tests (particularly ones requiring visual verification) where it's much more grey.

We want developers to write code with as few defects as possible but at the end of the day testers are much better at using software in ways that is likely to expose defects that developers wouldn't even think about and I think this is definitely a good thing.

My current thinking around this area is that a <strong>defect is something which was covered by the acceptance criteria or something which has been previously exposed by exploratory testing and reappears</strong>. 

Anything else is a normal part of the process.

