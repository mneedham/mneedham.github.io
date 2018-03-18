+++
draft = false
date="2008-12-22 21:39:22"
title="Testing First vs Testing Last"
tag=['tdd', 'testing']
category=['Testing']
+++

I recently posted about <a href="http://www.markhneedham.com/blog/2008/11/28/tdd-suffering-from-testing-last/">my experiences of testing last</a> where it became clear to me how important writing the test before the code is.

If we view the tests purely as a way of determining whether or not our code works correctly for a given set of examples then it doesn't make much difference whether we test before or after we have written the code.

If on the other hand we want to <a href="http://www.lostechies.com/blogs/jimmy_bogard/archive/2008/12/18/getting-value-out-of-your-unit-tests.aspx">get more value out of our tests</a> such as having them  the tests act as documentation, drive the design of our APIs and generally prove useful reading to ourself and others in future then a <strong>test first approach is the way to go</strong>.

Testing last means we've applied <a href="http://www.code-magazine.com/article.aspx?quickid=0805061&page=2">assumption driven development</a> when we wrote the code and now we're trying to work out how to use the API rather than driving out the API with some examples.

In a way writing tests first is applying the <a href="http://c2.com/xp/YouArentGonnaNeedIt.html">YAGNI</a> concept to this area of development. Since we are only writing code to satisfy the examples/tests that we have written it is likely to include much less 'just in case' code and therefore lead to a simpler solution. Incrementally improving the code with small steps works particularly well for keeping the code simple.

As <a href="http://blog.scottbellware.com/2008/12/testing-and-reverse-engineering.html">Scott Bellware points out</a>, the costs of testing after the code has been written is much higher than we would imagine and we probably won't cover as many scenarios as we would have done had we taken a test first approach.

I think we also spend less time thinking about exactly where the best place to test a bit of functionality is and therefore don't end up writing the most useful tests.

Obviously sometimes we want to just try out a piece of code to see whether or not an approach is going to work but when we have gained this knowledge it makes sense to go back and test drive the code again.

As has been said many times, TDD isn't about the testing, it's much more.
