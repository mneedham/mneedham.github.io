+++
draft = false
date="2008-12-09 22:07:37"
title="TDD: One test at a time"
tag=['tdd', 'testing']
category=['Testing']
+++

My colleague Sarah Taraporewalla has written a series of posts recently about her <a href="http://sarahtaraporewalla.com/thoughts/testing/what-is-a-good-test/">experiences</a> with <a href="http://sarahtaraporewalla.com/thoughts/testing/tdd-does-not-mean-test-first/">TDD</a> and <a href="http://sarahtaraporewalla.com/thoughts/testing/a-conversation-with-a-tdder/">introducing it at her current client</a>.

While I agreed with the majority of the posts, one thing I found interesting was that in the <a href="http://sarahtaraporewalla.com/thoughts/testing/a-conversation-with-a-tdder/">conversation with a TDDer</a> there were two tests being worked on at the same time (at least as far as I understand from the example).

This means that there will be two tests failing if we run our test suite, something which I try to avoid wherever possible.

I like to keep my focus just on the test that I am currently working on, so my approach if I had another test that I knew needed to be written would either be to write it down on a piece of paper or to write the skeleton and then just not put anything inside the test body. 

This could be seen as being a touch risky in case I then forget to actually write the test and the build remains green, but I prefer this trade off than the distraction that I feel when having more than one test red.

When driving out the design of classes I am now veering towards the approach of <strong>severe simplicity</strong> such that we literally only do enough to make the test green even if that involves returning a hard coded value for example.

The next test after that would probably be the one that drives out the implementation since it becomes easier to write the code to handle the general case rather than hard coding specific implementations for the individual tests.

I started becoming convinced of this approach after trying the <a href="http://codekata.pragprog.com/2007/01/kata_two_karate.html">Karate Chop Code Kata </a>a couple of months ago where I set up all the tests initially and therefore had 20 tests failing all at once.

It felt quite overwhelming having that many tests failing, and the sense of progress from making a test pass wasn't there for me.

It seems a bit ridiculous but <strong>keeping the steps as small as possible</strong> is certainly the approach I am seeing the most success with at the moment.
