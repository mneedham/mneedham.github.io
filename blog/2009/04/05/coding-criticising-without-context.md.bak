+++
draft = false
date="2009-04-05 19:45:56"
title="Coding: It's all about the context"
tag=['coding']
category=['Coding']
+++

I think one of the easiest things to do as a developer is to look at some code that you didn't write and then start trashing it for all the supposed mistakes that the author has made that you wouldn't have.

It's certainly something I've been guilty of doing and probably will be again in the future.

Sometimes it's justified but most of the time we lack the context for <a href="http://www.markhneedham.com/blog/2008/08/08/if-they-were-that-rubbish/">understanding why the code was written the way it was</a> and therefore our criticism is not very useful to anyone.

I think the more projects that I work on the more I realise that there's no single set of rules that we can apply in all contexts.

I think rules or principles do still have value but <a href="http://www.markhneedham.com/blog/2009/02/13/ferengi-programmer-and-the-dreyfus-model/">we shouldn't rigidly stick to them</a>, but be aware when there is more value in not following the rule and then go for it.

To give a simple example, one of the forms of good practice when using the NUnit testing framework is to minimise our use of the TestFixtureSetUp attribute and instead use SetUp so that the common bit of code is repeated before each test is run rather than one time before all the tests are run.

One time when we found it useful to break this rule is when writing tests for mapping code when there are a lot of different things to assert and only one method call to make.

Using our normal approach of keeping each test as it's own little specification resulted in tests that were really difficult so we broke the rule and using an approach which <a href="http://www.markhneedham.com/blog/2009/03/01/nunit-tests-with-contextspec-style-assertions/">resembles the context/spec approach to driving code</a>.

Looking at that code without the context of what I've just described you would probably think that it's terrible code and that we don't know how to use the framework but in this case it actually made our lives easier so I think it's fine to break the rule in this case.

Another example is passing booleans into methods - in general I think this is really bad practice but it actually helps to significantly simplify code when we pass them into HtmlHelpers so that it knows whether to render the read only version of a control or not.

I'm not sure who said that 'if you rewrite a system that you didn't write the first time you'll probably make the same mistakes as the original team did' but it's certainly becoming more clear to me how this would be the case.

The conclusion I'm pretty much coming to is that <strong>it's great to follow a set of practices</strong>, and doing so helps ensure that we are doing the right thing most of the time, but <strong>having the flexibility of thought to step away from that and try something different is very important</strong>.
