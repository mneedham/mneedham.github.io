+++
draft = false
date="2008-11-30 18:42:29"
title="TDD: If it's hard to test reflect on your approach"
tag=['tdd', 'testing']
category=['Testing']
+++

Chad Myers gets it spot on in his recent post about <a href="http://www.lostechies.com/blogs/chad_myers/archive/2008/11/21/do-not-test-private-methods.aspx">not testing private methods</a> - private methods are private because they should be inaccessible from outside the class and their functionality should be tested via one of the public methods that calls them.

I've found that when a piece of code seems really difficult to test without exposing a private method then we're probably trying to test that functionality from the wrong place.

I came across just this problem earlier this week when trying to test the functionality of one of our controllers - we are using the <a href="http://www.asp.net/mvc/">ASP.NET MVC</a> framework to build our application.

My first approach was to try and test everything from the controller test but it quickly became apparent that this was going to be very difficult as the only data we had access to was the ActionResult which was insufficient for our testing purposes.

It became clear that if we put the logic into one of the objects being created inside the method (by a WCF web services call) that it would be significantly easier to test the logic - so that's what we did! Suddenly it became much easier to test and we were able to come up with other test scenarios that we hadn't previously considered.

The lesson to learn here is to constantly reflect on whether we are testing from the right place and <strong>if it feels too difficult then it probably is</strong>.

Another testing lesson I learnt recently was not to override protected methods in order to test other logic in the class. This is arguably even worse than exposing private methods because now we are not testing the production code but a variant of it.

The reason I did it was because all the logic for preventing caching of data was encapsulated into a single method and since I wasn't interesting in testing that part of the code I thought it would be fine to just ignore it for those tests.

<a href="http://pilchardfriendly.wordpress.com/">Nick</a> pointed out that the actual problem was that we were missing an abstraction and as a result had ended up creating a dependency that made testing difficult. In this case the object was dependent on HttpResponse.

The lesson here is to ensure that objects <strong>depend on abstractions and not on concrete implementations</strong> wherever possible. 

The underlying lesson in both cases being that we need to be constantly reflecting and questioning our approach to ensure that we write clean code and test that code in a clean way.
