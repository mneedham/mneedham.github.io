+++
draft = false
date="2008-12-25 09:41:50"
title="TDD: Does it make you slower?"
tag=['agile', 'tdd', 'test-driven-development']
category=['Testing']
+++

There have been several times where we have been writing code in a test driven way and it has been suggested that we would be able to go much quicker if we stopped writing the tests and just wrote the code.

I feel this is a very short term way of looking at the problem and it does eventually come back to haunt you. 

One of the problems seems to be that in many organisations <strong>only the first release of a piece of software is considered</strong>, and in this case then yes maybe it would be quicker to develop code in a non TDD fashion. 

The issue you have is that the majority of the overall cost of software does not come in that first release - if we assume a total life time for a piece of software to be 3 years and the first release takes 6 months (being generous here!) then if we go at full speed in those first 6 months and don't write a good suite of tests, we leave ourselves with 2 1/2 years of maintenance hell.

This is where the real cost in software lies. The end of development on a piece of software is very rarely after that first release - bugs need to be fixed, new requirements come in and changes have to be made. Without the tests in the former we are left fixing something and hoping it works - I have broken stuff in production by making changes in non test driven code unaware that it would break elsewhere.

Even if we look at the development cycle of a single release, at some stage we are going to have to test the code we've written to ensure it actually works.

The TDD approach to doing this encourages early testing whereas the traditional approach is to do a lot of the testing at the end. The problem with the latter approach is that any <strong>bugs are being discovered quite a long time after the code was written</strong> which means it will take much longer to try and identify where they came from. <a href="http://blog.m.artins.net/">Alex</a> has a nice post showing <a href="http://blog.m.artins.net/measuring-test-effort/">the risks we assume when deciding to cut back on testing effort</a>.

In terms of whether or not actual development time takes longer with TDD, Microsoft <a href="http://www.m3p.co.uk/blog/2008/12/08/tdd-fewer-bugs-to-production-longer-to-write/">recently released a paper</a> which suggested that code written using a TDD approach takes longer to write originally but puts less bugs in production.

Since the goal of software development is to get code into production I think perhaps we need to consider the <a href="http://blog.scottbellware.com/2008/12/does-test-driven-development-speed-up.html">whole period of time</a> from when a feature was worked on until it is in production as being development time.

Clearly there are times when time is the biggest driver for when something needs to be released but the majority of the time having software with less bugs is probably preferable and TDD is helpful for achieving this.
