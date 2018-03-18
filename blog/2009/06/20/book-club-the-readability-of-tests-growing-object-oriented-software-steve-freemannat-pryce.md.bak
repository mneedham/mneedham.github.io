+++
draft = false
date="2009-06-20 11:26:51"
title="Book Club: The Readability of Tests - Growing Object Oriented Software (Steve Freeman/Nat Pryce)"
tag=['testing', 'tests']
category=['Book Club']
+++

Our technical book club this week focused on '<a href="http://www.mockobjects.com/book/readability.html">The Readability of Tests</a>' chapter from Steve Freeman & Nat Pryce's upcoming book '<a href="http://www.mockobjects.com/book/index.html">Growing Object Oriented Software, guide by tests</a>'.

I've been reading through some of the other chapters online and I thought this would be an interesting chapter to talk about as people seem to have different opinions on how DRY tests should be, how we build test data, how we name tests and so on.

These were some of my thoughts and our discussion on the chapter:

<ul>
<li>I found it interesting that there wasn't any mention of the <a href="http://www.markhneedham.com/blog/2008/09/04/bdd-style-unit-test-names/">BDD style of test naming</a> whereby the name of the test begins with 'should...'. I've been using these style of naming for about 2 years now as I find it useful for allowing us to <strong>question whether or not the test is valid</strong>. There are equally arguments against using the word 'should' as it's not particularly assertive and perhaps we ought to be more certain about what our tests are asserting. 

Recently I have started to move more towards Jay Fields idea that <a href="http://blog.jayfields.com/2008/05/testing-value-of-test-names.html">test names are just comments</a> and if we write tests to be really clear and readable then the test name becomes redundant.</li>
<li>The chapter talks about the order in which the authors write their tests, the approach being to try and <strong>start with the assertion first</strong> and then write the execution and setup steps. My current approach is to write the execution step first and then build up the setup and expectations almost simultaneously. I've never been able to quite get the hang of writing the test bottom up but it's something I might experiment with again.</li>
<li>Refactoring tests is something I've <a href="http://www.markhneedham.com/blog/2009/01/30/tdd-test-dryness/">written about previously</a> and my current thinking is that our aim shouldn't be to remove absolutely all duplication in tests but instead remove it to a stage where we can still easily understand the test when it fails. This seems to fit in with the authors' idea of 'refactoring but not too hard'.

I am currently following the idea of having <a href="http://www.markhneedham.com/blog/2009/04/13/tdd-balancing-dryness-and-readability/">three distinct areas in my tests</a> (Given, When, Then)  with each section separated by an empty line. I find writing them in this style makes it easier for me to quickly work out why a test is failing.

I was recently watching <a href="http://blog.jayfields.com/2009/06/developer-testing-welcome-to-beta-test.html">Jay Fields' presentation from SpeakerConf</a> and Michael Feathers makes an interesting comment that we need to keep in mind that the reason for removing duplication in code is so that when we need to make changes we know where to do that. In test code the test failing will tell us where we need to make changes so the need to remove duplication to do this is less.

I'm still heavily in favour of <strong>trading duplication for better readability when it comes to writing tests</strong>.
</li>
<li>The idea of keeping <a href="http://blog.jayfields.com/2008/11/ubiquitous-assertion-syntax.html">consistency in tests</a> is an important one although I think it's <strong>difficult to keep this consistency across the whole suite of tests</strong>. Certainly within a single test fixture it should be possible though.

One example of something which doesn't follow this approach is the 'ExpectedException' annotation in JUnit/NUnit which goes against the style of pretty much all other tests.</li>
<li>When it comes to setting up tests data I think it's pretty much given that test data builders are a really good way to help remove noise and duplication from our tests. Other patterns such as object mother can be useful but it doesn't seem to work as well when you have multiple different was that you want to setup your data for tests.</li>
<li>There's no specific mention of <strong>'Setup' and 'Teardown' methods</strong> in the chapter but this is another area which I think has an important impact on readability.

I'm not yet completely against tear down methods for integration style tests but I've seen a lot of pain causes by putting <a href="http://www.markhneedham.com/blog/2008/12/19/tdd-mock-expectations-in-setup/">mocks in setup methods</a> and even just having the setup method means that you have to go up and down the test fixture just to work out what's going on. I prefer to try and <a href="http://fragmental.tw/2008/07/02/domain-driven-tests/">keep all the context needed for a test in one place</a> .
</li>
<li>I found the section about the way that we name literals/variables in tests to be particularly interesting as this is a discussion I've been having with a couple of colleagues recently.

I find it useful to state <strong>why that variable is important or not important for this particular test</strong> (i.e. give it context) so that someone can easily understand what's going on when they look at the test. For example if we have a variable in a test that doesn't affect the outcome then it might be useful to name it 'stubFoo' or 'irrelevantFoo' or something similar.

I've previously been against the idea of naming dependencies we're mocking/stubbing as 'mockRepository' or 'stubRepository' but I've been trying this out a bit this week and it exposed some mistakes I'd made which I don't think I would have seen otherwise.</li>
<li>Another idea which I quite liked is the idea of <strong>only testing one feature set per test</strong>.

I've certainly written a lot of tests which break this rule and you really suffer when you need to make a change later on. 

Jay Fields also applies this rule to mocks whereby you can only have one expectation per test but as many stubs as you want.

I've been trying that out both these approaches this week and although there's probably more code overall as a result of writing more tests, each of the tests feels much more succinct and understandable.</li>
</ul>
