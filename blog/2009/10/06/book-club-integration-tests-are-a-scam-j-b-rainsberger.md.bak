+++
draft = false
date="2009-10-06 23:37:52"
title="Book Club: Integration tests are a scam (J.B. Rainsberger)"
tag=['book-club', 'integration-tests']
category=['Book Club']
+++

In our latest book club we discussed J.B. Rainsberger's presentation from Agile 2009 titled '<a href="http://www.infoq.com/presentations/integration-tests-scam">Integration tests are a scam</a>'.

These are some of my thoughts and our discussion of the video:

<ul>
<li>While talking about how to write interaction tests he suggests that <strong>we should only be looking to create interfaces for Domain Driven Design services</strong>. If we find ourselves wanting to create interfaces for entities or value objects then we probably have a service wanting to get out. We should try to extract that responsibility out into a service. 

I'm intrigued as to how repositories and factories would fit into this picture as I'm not sure whether they count as services, entities or value types. I've worked on code bases where we've created interfaces for them but I don't know if that means they would be services or that we did something wrong.

There also seem to be varying schools of thought on whether or not we should tests these types of things directly or whether we should just make use of them in our code and judge their correctness that way.</li>
<li>Rainsberger's main gripe seems to be with<strong> tests which cover more than one interesting  behaviour</strong> and he identifies the slow feedback and complexity of test setup as being undesired consequences of this approach. 

My feeling is that he was mainly referring to tests written directly from the UI although several colleagues suggested that tests where we call the code directly while using several real objects had the characteristics of the integration tests that Rainsberger dislikes. Ayende is having some success with what he coins '<a href="http://ayende.com/Blog/archive/2009/09/28/even-tests-has-got-to-justify-themselves.aspx">system oriented tests</a>' which sound similar to the latter so there might be something in this approach.</li>
<li>Rainsberger's solution for testing our systems thoroughly is to make use of <strong>contract and interaction tests</strong> - the former testing the real implementation of services and the latter the way that our objects work together with each other. Essentially making use of <a href="http://martinfowler.com/articles/mocksArentStubs.html">mocking</a> as far as I understand.   

He also suggests the need for a tool which would be able to indicate that every interaction test we write has a corresponding contract test which sounds quite similar to the <a href="http://code.google.com/p/nsynthesis/">NSynthesis</a> tool that a couple of my colleagues have worked on. This tool only tests that we do have a contract test for each mock rather than testing with the exact parameters used in our interaction tests as Rainsberger describes. If I understand this correctly then that would seem to result in a lot of tests!

I think we still need some integration tests that go through the user interface particularly if we are writing javascript heavy front ends - from my experience only using unit tests doesn't take us the whole way to having confidence that this type of code works. 

It is perhaps useful as a rule of thumb to test the happy path of pieces of functionality through integration tests and try and test the edge cases from tests that sit further down.</li>
<li>I like the idea that <strong>acceptance tests are supposed to be clarifying requirements and not testing correctness</strong> although it seems to be really easy to cross the line where they do end up verifying the correctness of our application. </li>
</ul>

Rainsberger has an interesting post on his blog where he <a href="http://www.jbrains.ca/permalink/284">goes through the feedback he received</a> from the talk.

I'm not sure if I totally understand contract tests at the moment - there is <a href="http://jbrains.ca/permalink/281">a post on Rainsberger's blog</a> which explains it a bit more and my colleague Danilo Sato wrote <a href="http://www.markhneedham.com/blog/2009/09/18/tdd-testing-with-generic-abstract-classes/#comment-22678">a comment on a post I wrote</a> about using generic abstract classes for testing suggesting that this approach is similar to the one Rainsberger is advocating.
