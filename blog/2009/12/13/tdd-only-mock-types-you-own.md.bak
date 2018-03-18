+++
draft = false
date="2009-12-13 21:47:04"
title="TDD: Only mock types you own"
tag=['tdd', 'testing']
category=['Testing']
+++

<a href="http://lizdouglass.wordpress.com/2009/12/12/mock-objects/">Liz recently posted about mock objects</a> and the original '<a href="http://www.jmock.org/oopsla2004.pdf">mock roles, not objects</a>' paper and one thing that stood out for me is the idea that <strong>we should only mock types that we own</strong>.

I think this is quite an important guideline to follow otherwise we can end up in a world of pain.

One area which seems particularly vulnerable to this type of thing is when it comes to <a href="http://www.markhneedham.com/blog/category/hibernate/">testing code which interacts with Hibernate</a>.

A common pattern that I've noticed is to create a mock for the '<a href="http://docs.jboss.org/hibernate/stable/entitymanager/reference/en/html_single/">EntityManager</a>' and then verify that certain methods on it were called when we persist or load an object for example.

There are a couple of reasons why doing this isn't a great idea:

<ol>
<li>We have no idea what the correct method calls are in the first place so we're just guessing based on looking through the Hibernate code and selecting the methods that we think make it work correctly. </li>
<li>If the library code gets changed then our tests break even though functionally the code might still work</li>
</ol>

The suggestion in the paper when confronted with this situation is to put a wrapper around the library and then presumably test that the correct methods were called on the wrapper.

<blockquote>
Programmers should not write mocks for fixed types, such as those defined by the runtime or external libraries. Instead they should write thin wrappers to implement the application abstractions in terms of the underlying infrastructure. Those wrappers will have been defined as part of a need-driven test.
</blockquote>

I've never actually used that approach but I've found that with Hibernate in particular it makes much more sense to write functional tests which <strong>verify the expected behaviour of using the library</strong>.

With other libraries which perhaps don't have side effects like Hibernate does those tests would be closer to unit tests but the goal is still to test the result that we get from using the library rather than being concerned with the way that the library achieves that result.
